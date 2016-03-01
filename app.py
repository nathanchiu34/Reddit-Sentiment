# INPUT: TAKES IN A STRING, SUBREDDIT
# OUPUT: RETURNS A SENTIMENT: TRUE, NEUTRAL, OR NEGATIVE
from flask import Flask 
import praw
from sentiment import word_feats, classifier 
#import nlp classifer 
app = Flask(__name__)


@app.route('/search-and-return/<subreddit>/<string>')
def search_and_return(search_string, subreddit, classifier):

	# I may need to set this as a global
	# For now, I will call one every single time 
	# *NOT SCALABLE*	
	r = praw.Reddit('search application')

	# search 
	search_results = r.search(search_string, 
	 						  subreddit = subreddit,
	 						  sort = True)

	for i in range(0,24):

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
 					sentiment = classifier.classify(word_feats(comment))
 					if sentiment == 'neg':
 						score += -1 * int(comments[i+1])
 					else:
 						score += 1 * int(comments[i+1]) 

 		if score > 10:
 			return "POSITIVE " + str(score)
 		elif score < -10:
 			return "NEGATIVE " + str(score) 
 		else:
 			return "NEUTRAL " + str(score)


NBclassifier = classifier()
print search_and_return('lebron','nba',NBclassifier)
print search_and_return('trump' , 'politics', NBclassifier)
print search_and_return('peyton manning', 'nfl', NBclassifier )
print search_and_return('monty williams', 'nba', NBclassifier)
print search_and_return('frank underwood', 'houseofcards', NBclassifier)