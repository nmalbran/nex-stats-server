from django.conf.urls import patterns, include, url

from views import ParserView

urlpatterns = patterns('',
    url(r'^parse/?$', ParserView.as_view(), name='parse'),

)
