from django.conf.urls import patterns, include, url
from hello.views import *

urlpatterns = patterns('',
    url(r'^hello/$', BaseView.as_view()),
    url(r'^hero/$', HeroView.as_view()),
    url(r'^ideas/', 'hello.views.IdeasView'),
    url(r'^action/$', doEmbed),
    #url(r'^ideas/form/(\d*)', 'hello.views.idea_Form'),

)
