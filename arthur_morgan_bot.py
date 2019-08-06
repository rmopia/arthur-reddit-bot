
import praw
import json
import random
import time
import re
from pprint import pprint

with open("arthur_quotes.json") as jsfile:
    arthur_quotes = json.load(jsfile)

q_list = []
p_list = []
replied_posts = []

for quote in arthur_quotes['quotes']:
    q_list.append(quote)

with open("replied_posts.txt") as txtfile:
    p_list = txtfile.read()
    p_list = p_list.split("\n")
    for post in p_list:
        if post is not '':
            replied_posts.append(post)

# pprint(replied_posts)

r = praw.Reddit("ambot") # change according to name of bot in praw.ini
subr = r.subreddit("pythonforengineers") # playground subreddit. change accordingly


def ids_to_file(replied_posts):
    with open("replied_posts.txt", "w") as file:
        for p_id in replied_posts:
            file.write(p_id + "\n")


for post in subr.hot(limit=10):
    # print("Title: " + post.title)
    p = r.submission(post.id)
    if post.id not in replied_posts:
        for comment in p.comments:
            if re.search("Arthur", comment.body, re.IGNORECASE):
                print(comment.body)
                arthur_says = random.choice(q_list)
                print(arthur_says)
                comment.reply(arthur_says)
                replied_posts.append(post.id)
                time.sleep(30) # prevent harmful spamming
        ids_to_file(replied_posts) # puts post id in file after replying to all relevant comments
    else:
        pass
    
   
