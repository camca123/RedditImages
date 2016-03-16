import praw

subreddits = []
sub = []
configFile = open("subreddits.config", "r")
pictureLocation = configFile.readline()
print pictureLocation
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
        print link.url