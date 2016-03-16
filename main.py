import praw

subreddits = []
sub = []
configFile = open("subreddits.config", "r")
for line in configFile:
    sub = line.replace("\n", "").split(",")
    subreddits.append(sub)
configFile.close()

print subreddits
for sub in subreddits:
    R = praw.Reddit(user_agent="Background Image getter by /u/camca123")
    if (sub[2] == "hour"):
        submissions = R.get_subreddit(sub[0]).get_top_from_hour(limit = sub[1])
    elif (sub[2] == "day"):
        submissions = R.get_subreddit(sub[0]).get_top_from_day(limit = sub[1])
    elif (sub[2] == "week"):
        submissions = R.get_subreddit(sub[0]).get_top_from_week(limit = sub[1])
    elif (sub[2] == "month"):
        submissions = R.get_subreddit(sub[0]).get_top_from_month(limit = sub[1])
    elif (sub[2] == "year"):
        submissions = R.get_subreddit(sub[0]).get_top_from_year(limit = sub[1])
    elif (sub[2] == "all"):
        submissions = R.get_subreddit(sub[0]).get_top_from_all(limit = sub[1])
    for link in submissions:
        print link.url