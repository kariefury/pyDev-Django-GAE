assailed
========

Django install running on google app engine (GAE)

(A) To get started as a developer, install the Google cloud SDK https://developers.google.com/appengine/docs/python/gettingstartedpython27/devenvironment

curl sdk.cloud.google.com | bash

From your terminal, clone the git repo.
git clone https://github.com/kariefury/assailed.git

To login to Assailed each time:
sign into google cloud


<b>gcloud auth login</b>

Project #<b>294320879492</b>

...programming happens...

test it locally...(Note... you have to be outside of assailed directory)

<b>dev_appserver.py assailed</b>

...everything works...

<b>appcfg.py -A swift-door-556 update assailed</b> (Once again, be outside of assailed directory)
