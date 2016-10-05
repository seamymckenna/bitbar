Bitbar Plugins
================

Repo for storing useful bitbar plugins

## Prerequisites
1. Installation of [Bitbar](https://getbitbar.com/)
2. Installation of python2.7;
3. Installation of python-jira
  * $pip install --user --upgrade jira
4. Update username and password within your ~/.netrc:
  * machine tickets.puppetlabs.com
  * login **(your username)**
  * password **(your password)**
5. Ensure .netrc privilidges are correct
  * chmod og-rw ~/.netrc
6. Copy jira-filters.1m.py from this repo into your bitbar plugins folder

## Usage
Update jira_uri within script if required:
* e.g jira_uri='http://tickets.puppetlabs.com'
By default, details from all your Saved Filters will be displayed:
However, a regexp filter can be used to only display the ones you want.
* e.g match_filters='bb'

