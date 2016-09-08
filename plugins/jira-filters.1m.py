#!/usr/bin/python

# <bitbar.title>Alternate Options Tutorial</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Seamus McKenna</bitbar.author>
# <bitbar.author.github>seamymckenna</bitbar.author.github>
# <bitbar.image>http://i.imgur.com/EDYR52G.png</bitbar.image>
# <bitbar.desc>Example of how to include alternate items that replace the one before it when the Option key is pressed.</bitbar.desc>

#Pre-reqisates
# $pip install jira
# $pip install --user --upgrade jira

#Imports
from jira import JIRA
from re import search

#Config
jira_uri='http://tickets.puppetlabs.com'
username='seamus'
password='Ki11adeas'
match_filters='bb' #only display from user filters that match this regexp

#Create JIRA Instance
jira = JIRA('http://tickets.puppetlabs.com', basic_auth=('seamus', 'Ki11adeas'))

#Create a dict of user tickets per user filter
tickets={}
for f in jira.favourite_filters():
    if search(match_filters,f.name):
        tickets[f.name] = jira.search_issues('filter = {}'.format(f.id))

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
        print '-- Status: {}'.format(i.fields.status.name)
        #print dir(i.fields.assignee)
        print '-- Assignee: {}'.format(i.fields.assignee.name)
    print "---"
