from django.db import models
from google.appengine.ext import ndb
from google.appengine.ext import db
class Idea(models.Model):
    name = models.CharField(max_length=200,primary_key = True)
    quote = models.CharField()
    stage = models.TextField()

class story(db.Model):
    name = db.StringProperty()
    quote = db.StringProperty()
    stage = db.StringProperty()
        
class Greeting(ndb.Model):
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)
    content = ndb.DateTimeProperty(auto_now_add=True)
# materials
# title
# image
# description

