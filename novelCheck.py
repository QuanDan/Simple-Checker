import time
import praw
import smtplib
from pymsgbox import *

def get_subr():
	sub = input("Please enter subreddit to check for:\n")
	return sub;

def get_list(searchWords):
	notdone = True;
	while notdone:
		searchWord = input("Enter string to check for and press enter. If done press enter:\n")
		searchWord.strip()
		if searchWord.isspace() or not searchWord:
			notdone = False
		elif searchWord == "\r\n":
			notdone = False
		else:
			searchWords.append(searchWord.lower())

def sendMessage(message):
	alert(text=message, title='Search Updated', button='ok')
	return

def main():
	user_agent = ("PySubChecker 0.1")
	r = praw.Reddit(user_agent = user_agent)
	sub = get_subr()

	searchWords = []
	get_list(searchWords)
	print (searchWords)

	history = []
	while True:
		subreddit = r.get_subreddit(sub)
		for submission in subreddit.get_hot(limit = 25):
			title = submission.title
			has_word = any(string in title.lower() for string in searchWords)
			if submission.id not in history and has_word:
				print(title)
				sendMessage(title)
				history.append(submission.id)

		print ("waiting 30 mins")
		time.sleep(1800)

if __name__ == '__main__':
	main()