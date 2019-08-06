
import praw
import json
import random
import time
import re

with open("arthur_quotes.json") as jsfile:
    data = json.load(jsfile)

qlist = []
comments = []
replied_comments = []

for quote in data['quotes']:
    qlist.append(quote)

with open("replied_posts.txt") as txtfile:
    comments = txtfile.read()
    comments = comments.split("\n")
for c in comments:
    if c is not '':
        replied_comments.append(c)

r = praw.Reddit("ambot") # change according to name of bot in praw.ini
subr = r.subreddit("pythonforengineers") # playground subreddit. change accordingly

for post in subr.hot(limit=1):
    if post.id not in replied_comments:
        for comment in subr.comments(limit=1):
            # if re.search("[deleted]", comment.body, re.IGNORECASE):
            print(comment.body)
            arthur_says = random.choice(qlist)
            comment.reply(arthur_says)
            print(arthur_says)
            time.sleep(300)

