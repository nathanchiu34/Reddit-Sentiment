# the first peice of this project will be if you can get a sentiment analysis on 
# one thing in a subreddit
# we will try this out
#
# There are two parts
#  1. The sentiment analysis (training,testing a corpus for negative positive commments)
#  2. The second is building the system
#  3. First you have to grab the search word, and then put it through reddit

# MY FIRST TWO IDEAS FOR THE REDDIT SCRIPTS
# 1. PREDICT THE TOP RATED COMMENT 
#      PREDICT THE SENTIMENT
#      PREDICT THE WORDS USED IN THE FIRST COMMENT
#      PREDICT THE ACTUAL COMMENT??

import praw
import nltk

#initializes a subreddit ready for analysis
def initialize_reddit(subreddit):

	r = praw.Reddit(user_agent = 'sample_application')

	subreddit = r.get_subreddit(subreddit)

	return subreddit 

#searches r_nba subreddit for the first 10 submissions
def search_nba_subreddit(subreddit, search_word):

	# get top 20 results
	submission = nba.search(search_word)

	# go through all the comments and text
	for submission in submission.next():

		comments = submission.get_comments()

		# analyze comments
		sentiment = nltk.analyze(comments) 

	return sentiment 