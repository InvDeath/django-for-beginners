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
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'students.views.students_list', name='home'),
    url(r'^journal/', 'students.views.journal', name='journal'),
    url(r'^groups/', 'students.views.groups_list', name='groups'),

    url(r'^students/add$', 'students.views.add_student', name='add_student'),
    url(r'^students/(?P<sid>\d+)/edit$', 'students.views.edit_student', name='edit_student'),
    url(r'^students/(?P<sid>\d+)/delete$', 'students.views.delete_student', name='delete_student'),

    url(r'^admin/', include(admin.site.urls)),
]
