#!/usr/bin/python
import twitter
import time
import csv
from settings import *
import datetime

# import requests
# import urllib
# import urllib2
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
	
	
	
	
	
	
	
	
	# print("using requests.get")
	# image_url = row[1] ##"https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
  
	# # URL of the image to be downloaded is defined as image_url 
	# r = requests.get(image_url) # create HTTP response object 
  
	# # send a HTTP request to the server and save 
	# # the HTTP response in a response object called r 
	# with open("image2.jpg",'wb') as f: 
  
    # # Saving received content as a png file in 
    # # binary format 
  
    # # write the contents of the response (r.content) 
    # # to a new file in binary mode. 
		# f.write(r.content) 
	

	# ## New version
	# # print('Beginning file download with urllib2...')

	# # url = row[1]
	# # urllib.request.urlretrieve(url, 'image3.jpg') 
	
	
	# ## New version


	# print("using urllib2")
	# filedata = urllib2.urlopen(row[1])  
	# datatowrite = filedata.read()

	# with open('image4.jpg', 'wb') as f:  
		# f.write(datatowrite)
			

	# print('Beginning file download with requests')

	# url = row[1]
	# r = requests.get(url)

	# with open('image5.jpg', 'wb') as f:  
		# f.write(r.content)

	# # Retrieve HTTP meta-data
	# print(r.status_code)  
	# print(r.headers['content-type'])  
	# print(r.encoding)  
	
	
	

	# print('Beginning file download with wget module')

	# ###url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'  
	# wget.download(url, 'image6.jpg')  
	
