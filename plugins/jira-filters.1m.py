#!/usr/bin/python

# <bitbar.title>JIRA Filter Display</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Seamus McKenna</bitbar.author>
# <bitbar.author.github>seamymckenna</bitbar.author.github>
# <bitbar.desc>Display tickets from your Favourite JIRA filters</bitbar.desc>

#Prerequisates
# Installation of Bitbar (https://getbitbar.com/)
# Installation of python2.7;
# Installation of python-jira
#   $pip install --user --upgrade jira
# Update username and password within your ~/.netrc
#   machine tickets.puppetlabs.com
#   login <your username>
#   password <your password>
# Ensure .netrc privilidges are correct
#   chmod og-rw ~/.netrc

#Imports
from jira import JIRA
from re import search

#Configuration Settings
jira_uri='http://tickets.puppetlabs.com' #enter your jira uri
match_filters='' #only display from user filters that match this regexp

#Create JIRA Instance
jira = JIRA('https://tickets.puppetlabs.com', basic_auth=())

#Create a dict of user tickets per user filter
tickets={}
for f in jira.favourite_filters():
    if search(match_filters,f.name):
        tickets[f.name] = jira.search_issues('filter = {}'.format(f.id))

#Count a total of user tickets
total=0
for t in tickets:
    for i in tickets[t]:
        total+=1
print 'Tickets: {}'.format(total)

#Now display filters
print "---"
for t in tickets:
    print '{} | color=green'.format(t)
    for i in tickets[t]:
        link = '{}/browse/{}'.format(jira_uri,i.key)
        print '{}: {} | href={}'.format(i.key,i.fields.summary,link)
        try:
            print '-- Status: {}'.format(i.fields.status.name)
            print '-- Assignee: {}'.format(i.fields.assignee.name)
        except:
            pass
    print "---"
