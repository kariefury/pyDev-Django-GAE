from django.views.generic import TemplateView
from django import template
from django import http
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from google.appengine.ext import ndb
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
    return render_to_response('hello/thanks.html' , {})

class IdeaForm(forms.Form):
    stage = forms.CharField()
    name = forms.CharField()

def idea_Form(request,argument):
    logging.warning('inside your idea. Being There')
    logging.warning(request)
    if request.method == 'POST':
        logging.warning('Post has struck')
        form = IdeaForm(request.POST)
        idea = form.save(commit=True)
        # print "hello carrie"
        # logging.debug("hello")
        # logging.info('should have just saved')
        # idea.put()
        # anIdea = idea.get()
        # logging.debug('Start guestbook signing request')
        # print anIdea
        # logging.getLogger().setLevel(logging.DEBUG)
        return HttpResponseRedirect('/ideas/form/')
    else:
        form = IdeaForm()
        logging.warning('else statement')
    logging.warning('skip all if else?')
    return render(request, 'hello/idea_form.html', {'form':form, })

def IdeasView(request):
    # This should return all objects of class Idea
    #ideas = Idea.get()
    ideas = {
	'greetings': 'Where is the data?',
	'anotherline': 'More to say here?'
    }
    logging.warning('trying this')
    logging.warning(ideas)
    return render_to_response('hello/ideas.html' , {'ideas':ideas, })
