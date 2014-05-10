from django.conf.urls import patterns, include, url
from hello.views import BaseView
from hello.views import HeroView

urlpatterns = patterns('',
    #url(r'^$', include('hello.urls')),
    url(r'^ideas/form/(\d*)', 'hello.views.idea_Form'),
    url(r'^ideas/', 'hello.views.IdeasView'),
    url(r'^hello/$', BaseView.as_view()),
    url(r'^hero/$', HeroView.as_view()),
    url(r'^thanks/', 'hello.views.ThanksView' ),
)


