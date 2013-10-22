from django.conf.urls import patterns, include, url
from article.views import HelloTemplate

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^articles/', include('article.urls')),

    # url(r'^hello/$', 'article.views.hello', name='hello'),
    # url(r'^hello_template/$', 'article.views.hello_template', name='hello_template'),
    # url(r'^hello_template_simple/$', 'article.views.hello_template_simple', name="hello_template_simple"),
    # url(r'hello_class_view/$', HelloTemplate.as_view()),

    # url(r'^$', 'Blog.views.home', name='home'),
    # url(r'^Blog/', include('Blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # user auth urls
    url(r'^accounts/login/$', 'Blog.views.login'),
    url(r'^accounts/auth/$', 'Blog.views.auth_view'),
    url(r'^accounts/logout/$', 'Blog.views.logout'),
    url(r'^accounts/loggedin/$', 'Blog.views.loggedin'),
    url(r'^accounts/invalid/$', 'Blog.views.invalid_login'),
)
