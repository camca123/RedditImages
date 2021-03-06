import praw
import urllib
import sys

def stringContains(string, checks, breakChar):
    checks = checks.split(breakChar)
    for check in checks:
        if (string.find(check) != -1):
            return True
    return False

sys.stdout = open("log.log", "w")
sys.stderr = open("logerr.log", "w")

subreddits = []
sub = []
configFile = open("subreddits.config", "r")
pictureLocation = configFile.readline().replace("\n", "").strip()

for line in configFile:
    sub = line.replace("\n", "").split(",")
    for i in range(len(sub)):
        sub[i] = sub[i].strip()
    subreddits.append(sub)
configFile.close()

R = praw.Reddit(user_agent="Background Image getter by /u/camca123")
for sub in subreddits:
    if (sub[2] == "hour"):
        submissions = R.get_subreddit(sub[0]).get_top_from_hour(limit = int(sub[1]))
    elif (sub[2] == "day"):
        submissions = R.get_subreddit(sub[0]).get_top_from_day(limit = int(sub[1]))
    elif (sub[2] == "week"):
        submissions = R.get_subreddit(sub[0]).get_top_from_week(limit = int(sub[1]))
    elif (sub[2] == "month"):
        submissions = R.get_subreddit(sub[0]).get_top_from_month(limit = int(sub[1]))
    elif (sub[2] == "year"):
        submissions = R.get_subreddit(sub[0]).get_top_from_year(limit = int(sub[1]))
    elif (sub[2] == "all"):
        submissions = R.get_subreddit(sub[0]).get_top_from_all(limit = int(sub[1]))
    for link in submissions:
        if (link.url.split("/")[-1] == ""): # URL ends in a "/" so it is a text post
            print "Error retrieving " + link.title + " from " + sub[0] + " (Text post??)"
            continue
        if (link.url.split("/")[-1].find(".") == -1 or stringContains(link.url.split("/")[-1], "gifv/gif/html/htm", "/")):
            print "Link is not to an image: " + link.url.split("/")[-1] + " -- " + link.title
            continue
        download = urllib.urlretrieve(link.url, pictureLocation + "\\" + link.url.split("/")[-1])
        try:
            print "Got " + link.url.split("/")[-1] + " (" + link.title + ")" + " from " + sub[0]
        except:
            print "Unicode Error or something"
