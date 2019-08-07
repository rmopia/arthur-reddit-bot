
import praw
import json
import random
import time
import re

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

r = praw.Reddit("ambot") # change according to name of bot in praw.ini
subr = r.subreddit("reddeadredemption") # change accordingly


def ids_to_file(r_list):
    with open("replied_posts.txt", "w") as file:
        for p_id in r_list:
            file.write(p_id + "\n")


for post in subr.hot(limit=10):
    print("Title: " + post.title)
    p_id = r.submission(post.id)
    if p_id not in replied_posts:
        for comment in p_id.comments:
            for reply in comment.replies:
                if re.search("Arthur", comment.body, re.IGNORECASE):
                    print("comment: " + comment.body)
                    arthur_says = random.choice(q_list)
                    print(arthur_says)
                    comment.reply(arthur_says)
                    # time.sleep(3) # prevent harmful spamming
        replied_posts.append(post.id)
        ids_to_file(replied_posts) # puts post id in file after replying to all relevant comments


