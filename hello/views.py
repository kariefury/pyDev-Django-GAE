from django.views.generic import TemplateView
from django import template
from django import http
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from google.appengine.ext import ndb
from google.appengine.ext import db
import logging
import models
import searchclient
from hello.models import *
#import simplejson

#def json_response(func):
    # """
    # A decorator thats takes a view response and turns it
    # into json. If a callback is added through GET or POST
    # the response is JSONP.
    # """
    # def decorator(request, *args, **kwargs):
    #     objects = func(request, *args, **kwargs)
    #     if isinstance(objects, HttpResponse):
    #         return objects
    #     try:
    #         data = simplejson.dumps(objects)
    #         if 'callback' in request.REQUEST:
    #             # a jsonp response!
    #             data = '%s(%s);' % (request.REQUEST['callback'], data)
    #             return HttpResponse(data, "text/javascript")
    #     except:
    #         data = simplejson.dumps(str(objects))
    #     return HttpResponse(data, "application/json")
    # return decorator


def home(request):
    return http.HttpResponse('Goodbye World!')




#def queryGoodReadAPI( request ):
#    if request.method == 'GET':
#        queryName = request.GET['title']
#        try:
#            cache = QueryCache.objects.get(queryString=myTitle)
#        except Exception:
#            cache = None
#        result = []
#        if not cache:
#            result = searchclient.formatSearch(queryName)
#        cache = QueryCache(queryString=queryName, queryResult=result)cache.save()
#        else:
#            result = cache.queryResult
#            return HttpResponse(str(result))
#    return HttpResponse("Bad Request")


class BaseView(TemplateView):
    template_name = "hello/base.html"

class HeroView(TemplateView):
    template_name = "hello/hero.html"

def ThanksView(request):
    logging.warning(request)
    idea = request.POST
    s = story()
    logging.warning(idea)
    s.name = idea.get("name")
    s.quote = idea.get("quote")
    s.stage = idea.get("stage")
    s.put()
    return render_to_response('hello/thanks.html' , {})

class IdeaForm(forms.Form):
    name = forms.CharField()
    quote = forms.CharField()
    stage = forms.CharField()


def idea_Form(request,argument):
    logging.warning('inside your idea. Being There')
    logging.warning(request)
    form = IdeaForm()
    return render(request, 'hello/idea_form.html', {'form':form, })

def IdeasView(request):
    # This should return all objects of class Idea
    ideas = story.all()
    # ideas = {
	# 'greetings': 'Where is the data?',
	# 'anotherline': 'More to say here?'
    # }
    logging.warning('trying this')
    logging.warning(ideas)
    for i in ideas:
        print i.name
    return render_to_response('hello/ideas.html' , {'ideas':ideas, })
