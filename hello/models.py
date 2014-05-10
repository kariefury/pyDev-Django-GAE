from django.db import models

class Idea(models.Model):
    name = models.CharField(max_length=200,primary_key = True)
    quote = models.CharField()
    stage = models.TextField()
# materials
# title
# image
# description

