#!/usr/bin/python
import twitter
import time
import csv
from settings import *
import datetime
import os
import wget



global now
global api

now = datetime.datetime.now()
message = str(now)
print message


print('establish the twitter object')
# see "Authentication" section below for tokens and keys
api = twitter.Api(consumer_key=CONSUMER_KEY,
                consumer_secret=CONSUMER_SECRET,
                access_token_key=OAUTH_TOKEN,
                access_token_secret=OAUTH_SECRET,
                )


print('twitter object established')


##csv_file = csv.reader(open('/storage/Watergate45/wgatetimeline.csv', 'rb'))
csv_file = csv.reader(open('deregbot.csv', 'rb'))
for row in csv_file:
	print row
	print row[0]
	print row[1]
	
	
	url = row[1]
	wget.download(url, 'image.jpg')  
	#photo = open('image1.jpg', 'rb')
	# response = api.UploadMediaChunked(media=photo)
	# print(response)
	api.PostUpdate(status=row[0], media='image.jpg')
	time.sleep(60)
	os.remove("image.jpg")
	
	
	
