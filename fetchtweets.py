#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
		        auth = OAuth('63542770-PYeonIeKKUB52pEHNUmudnSrnl0HLh6nLq0jf2Pnx', 'i9xTQjHKH5TaccH7LhNJfdxy8j9gwgrobKkRL3cXcUdTI', 'deGvJNAbPQZtEHO3IPY4woB33', 'MOUYRi40ueN6g7Ik5SZPZJ7IBuRPlmXpZ8BOffiyFjudd8Yec4'))


#-----------------------------------------------------------------------
# perform a basic search 
# Twitter API docs:
# https://dev.twitter.com/docs/api/1/get/search
#-----------------------------------------------------------------------
query = twitter.search.tweets(q = "lazy dog")

#-----------------------------------------------------------------------
# How long did this query take?
#-----------------------------------------------------------------------
print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])

#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------
for result in query["statuses"]:
	print "(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"])
