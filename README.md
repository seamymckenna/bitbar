Bitbar Plugins
================

Repo for storing useful bitbar plugins

## Prerequisites
* Installation of [Bitbar](https://getbitbar.com/)
* Installation of python2.7;
* Installation of python-jira
**  $pip install --user --upgrade jira
* Update username and password within your ~/.netrc:
    machine tickets.puppetlabs.com
    login <your username>
    password <your password>
* Ensure .netrc privilidges are correct
** chmod og-rw ~/.netrc

## Usage
Update jira_uri within script if required:
* e.g jira_uri='http://tickets.puppetlabs.com'
By default, details from all your Saved Filters will be displayed:
However, a regexp filter can be used to only display the ones you want.
* e.g match_filters='bb'

