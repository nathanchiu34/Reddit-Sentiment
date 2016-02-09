# the reddit sentiment analyzer should
# analyze the comments for sentiment
# take into fact the upvoted / popularity of the comments 
# return:
# positive, neutral, or negative based on a corpus
# return the comment with the highest weight/most popular comment
# return the comment with the highest weight against the popular

# use the nltk corpus for movie reviews
# will have to use something else eventually
# preferably a reddit comment dataset from kaggle or the subreddit

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews

'''
def word_feats(words):
    return dict([(word, True) for word in words])
 
negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
 
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
negcutoff = len(negfeats)*3/4
poscutoff = len(posfeats)*3/4
 
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
 
classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
classifier.show_most_informative_features()
'''

# build a corpus from reddit comments
def get_redditcomments_corpus():

	corpus = movie_reviews

	return corpus

# build a classifier from reddit corpus
def get_redditcomments_classifier(corpus):

	#train sentiment on classifier

	classifier = NaiveBayesClassifier.train(corpus)
	return classifer  

def get_comment_sentiment(classifier, comments):

	sentiment = nltk.classify.util.predict(classifier,comments)