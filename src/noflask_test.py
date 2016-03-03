# INPUT: TAKES IN A STRING, SUBREDDIT
# OUPUT: RETURNS A SENTIMENT: TRUE, NEUTRAL, OR NEGATIVE
from sentiment import word_feats, classifier 
import praw
import requests
import datetime

#global r
#global NBclassifier
#r = praw.Reddit('search_application')
#NBclassifier = classifier()

# @app.route('/search-and-return	', methods=['POST'])
# def take_user_input():

# 	projectpath = request.form.projectpath

# 	return search_string, subreddit 
def search_and_return(search_string, subreddit, classifier):

	# I may need to set this as a global
	# For now, I will call one every single time 
	# *NOT SCALABLE*	
	r = praw.Reddit('search application')
	now = datetime.datetime.now()

	# search for string in subreddit
	search_results = r.search(search_string, 
	 						  subreddit = subreddit,
	 						  sort = True)
	# there are 25 posts and then a next option. we can just use the limit
	#for i in xrange(search_results.__sizeof__()):
	for i in range(0,24):
		score = 0
		comments = []
		post = search_results.next() 
		for comment in post.comments:
		    try:
		        comment_str = str(comment.body.encode('utf-8'))
		        comments.append(comment_str)
		        comments.append(comment.score)
		    except AttributeError:
		    	pass

		for i in range(0, len(comments), 2):
			for comment in comments[i].split('\n'):
				if any(i in str(comment) for i in search_string.lower().split(' ')):
 					#print comment
 					sentiment = classifier.classify(word_feats(comment))
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


NBclassifier = classifier()
print search_and_return('lebron','nba',NBclassifier)
print search_and_return('trump' , 'politics', NBclassifier)
print search_and_return('peyton manning', 'nfl', NBclassifier )
print search_and_return('monty williams', 'nba', NBclassifier)
print search_and_return('frank underwood', 'houseofcards', NBclassifier)
print search_and_return('bernie sanders', 'politics', NBclassifier)