#!/usr/bin/python
import twitter
#import time
import csv
from settings import *
#import os
import wget
import random

print('establish the twitter object')
# see "Authentication" section below for tokens and keys
api = twitter.Api(consumer_key=CONSUMER_KEY,
                consumer_secret=CONSUMER_SECRET,
                access_token_key=OAUTH_TOKEN,
                access_token_secret=OAUTH_SECRET,
                )


print('twitter object established')


csv_file = csv.reader(open('deregbot.csv', 'rb'))
rows = list(csv_file)
print(rows)
print("row count")
print(csv_file.line_num)
rx = random.randint(0, csv_file.line_num-1)
print rx
print(rows[rx])
print(rows[rx][0])
print(rows[rx][1])
url = rows[rx][1]
wget.download(url, 'image.jpg')  
	####################### photo = open('image1.jpg', 'rb')
	####################### response = api.UploadMediaChunked(media=photo)
	####################### print(response)
api.PostUpdate(status=rows[rx][0], media='image.jpg')
#time.sleep(60)
#os.remove("image.jpg")
	
	
	
