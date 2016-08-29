from selenium import webdriver
import sys
import os


def setup():

	# Create twitterHistories folder if it does not already exist
	if not os.path.isdir('twitterHistories'):
		os.makedirs('twitterHistories')


# Scrapes all available (ie. the 3,200 latest) tweets
def scrapeAllTweets(twitterAccount, outputFile):

	# Create required folders to save tweets
	setup()

	# Open new browser window to Twitter
	page = 'https://twitter.com/' + twitterAccount
	driver = webdriver.Chrome()
	driver.get(page)

	# Scrape tweets and save to file
	index = 0
	setOfIndicies = set()
	endCounter = 0
	text_file = open('twitterHistories/' + outputFile, "a")
	while True:

		try:
			
			# Pull tweet from html
			tweet = driver.find_elements_by_class_name('TweetTextSize')[index].text

			# Turn all whitespace to a normal space
			tweet = ' '.join(tweet.split())

			# Change all encoding to ascii
			tweet = tweet.encode('ascii', 'ignore')
			
			# Save to file
			text_file.write(tweet + '\n')

			# Increment index
			index += 1
			setOfIndicies.add(index)

			# Print tweet and tweet number to output
			print "Tweet #: \t" + str(len(setOfIndicies))
			print str(tweet) + '\n'

		except:
		
			# Scroll down
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		# If the index equals the total number of tweets on the screen, increment endCounter
		if index == len(driver.find_elements_by_class_name('TweetTextSize')):
			endCounter += 1

			# If endCounter reaches 100, end script
			if endCounter == 100:
				break
		
		# If there are unrecorded tweets, then reset endCounter
		else:
			endCounter = 0

	text_file.close()


if __name__ == "__main__":

	# Get command line arguments
	twitterAccount = sys.argv[1]
	outputFile = sys.argv[2]

	# Scrape all tweets from that user
	scrapeAllTweets(twitterAccount, outputFile)


	
	
	
