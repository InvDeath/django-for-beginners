"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', 'students.views.index', name='index'),
    url(r'^add_student/$', 'students.views.add_student', name='add_student'),
    url(r'^edit_student/(?P<sid>\d+)$', 'students.views.edit_student', name='edit_student'),
    url(r'^delete_student/(?P<sid>\d+)$', 'students.views.delete_student', name='delete_student'),

    url(r'^add_group/$', 'students.views.add_group', name='add_group'),
    url(r'^edit_group/(?P<gid>\d+)$', 'students.views.edit_group', name='edit_group'),
    url(r'^delete_group/(?P<gid>\d+)$', 'students.views.delete_group', name='delete_group'),
]
