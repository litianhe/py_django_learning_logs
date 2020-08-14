# define learning_logs url

from django.conf.urls import url

from . import views

urlpatterns = [
  # mainpage
  url('^$', views.index, name='index'),

  # display all topcis
  url('^topic/$', views.topics, name='topics'),

  # display topic
  url('^topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),

  # new topic
  url('^new_topic/$', views.new_topic, name='new_topic'),
  
  # new entry
  url('^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

  # edit entry
  url('^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
