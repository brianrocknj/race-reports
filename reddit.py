import pandas as pd
import praw
import os

fname = 'Reports.csv'
CLIENT_ID = os.environ['RACE_REPORT_CLIENT_ID']
CLIENT_SECRET = os.environ['RACE_REPORT_CLIENT_SECRET']
USER_AGENT = 'Python:RaceReport:v0.1 (by /u/SlowWalkere)'

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)

df = pd.read_csv(fname)

reports = []
subs = ['AdvancedRunning', 'Marathon_Training']
for sub in subs:
    for post in reddit.subreddit(sub).search('Race Report'):
        if post.id in df['id'].values:
            print('Already got this one.')
            continue
         
        report = {
            'id' : post.id,
            'date' : post.created_utc,
            'author' : post.author,
            'author_flair' : post.author_flair_text,
            'subreddit' : sub,
            'permalink' : post.permalink,
            'title' : post.title,
            'text' : post.selftext
        }
    
        reports.append(report)

reports = pd.DataFrame(reports)
reports['date'] = pd.to_datetime(reports['date'], utc=True, unit='s', origin='unix')
reports.to_csv(fname, mode='a', index=False, header=False)
print(reports)