from django.conf.urls.defaults import *
from piston.resource import Resource
from djblog.api.handlers import BlogHandler, CommentHandler

blog_handler = Resource(BlogHandler)
comment_handler = Resource(CommentHandler)

urlpatterns = patterns('',
    #url(r'^product/(?P<id>[^/]+)/', identifier_handler),
    url(r'^blog/', blog_handler),
    url(r'^comment/', comment_handler),
    )
