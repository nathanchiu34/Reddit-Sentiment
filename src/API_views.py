# INPUT: TAKES IN A STRING, SUBREDDIT
# OUPUT: RETURNS A SENTIMENT: TRUE, NEUTRAL, OR NEGATIVE
from flask import Flask, render_template, request, redirect, url_for 
from sentiment import word_feats, classifier 
import praw
import requests
import datetime


app = Flask(__name__)
global r
global search_string
global subreddit 
#global NBclassifier
r = praw.Reddit('search_application')
#NBclassifier = classifier()

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def get_terms():
	results = []
	if request.method == 'POST':
	 	subreddit = request.form['subreddit']
	 	search_term = request.form['search_term']

	#return search_and_return(search_string, subreddit, classifier)
	search_string = str(subreddit) + '/' + str(search_term)
	search_page = 'search_and_return/'+ search_string
	return redirect(url_for(search_page))

# @app.route('/search-and-return	', methods=['POST'])
# def take_user_input():

# 	projectpath = request.form.projectpath

# 	return search_string, subreddit 

@app.route('/reddit_search')
def reddit_search():
	search = r.search('steph', subreddit='nba',sort=True)
	return 'success'

@app.route('/search_and_return/<subreddit>/<search_string>/')
def search_and_return(subreddit, search_string):

	NBclassifier = classifier()
	# I may need to set this as a global
	# For now, I will call one every single time 
	# *NOT SCALABLE*	
	# r = praw.Reddit('search application')
	now = datetime.datetime.now()

	# search 
	search_results = r.search(search_string, 
	 						  subreddit = subreddit,
	 						  sort = True)

	for i in xrange(search_results.__sizeof__()):

		comments = []

		post = search_results.next()

		for comment in post.comments:
		    try:
		        comment_str = str(comment.body.encode('utf-8'))
		        comments.append(comment_str)
		        comments.append(comment.score)
		    except AttributeError:
		    	pass
		    	
		score = 0    	
		for i in range(0, len(comments), 2):
			for comment in comments[i].split('\n'):
				if any(i in str(comment) for i in search_string.lower().split(' ')):
 					#print comment
 					sentiment = NBclassifier.classify(word_feats(comment))
 					if sentiment == 'neg':
 						score += -1 * int(comments[i+1])
 					else:
 						score += 1 * int(comments[i+1]) 

	 	if score > 10:
	 		result = str(now) + " POSITIVE " + str(score)
	 	elif score < -10:
	 		result = str(now) + " NEGATIVE " + str(score) 
	 	else:
	 		result = str(now) + " NEUTRAL " + str(score)

 	#return result, max_post_comment, pos_score, max_neg_comment, neg_score 
 		return result
 	#return flask.render_template('result.html',result=result)

@app.route('/hello/<first_name>/<last_name>/')
def hello(first_name, last_name):
	print 'test!!!'
	try:
		return firstname
	except:
		return lastname 


if __name__ == '__main__':
	app.debug = True
	app.run()

# NBclassifier = classifier()
# print search_and_return('lebron','nba',NBclassifier)
# print search_and_return('trump' , 'politics', NBclassifier)
# print search_and_return('peyton manning', 'nfl', NBclassifier )
# print search_and_return('monty williams', 'nba', NBclassifier)
# print search_and_return('frank underwood', 'houseofcards', NBclassifier)