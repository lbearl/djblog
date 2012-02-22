from django.conf.urls.defaults import *
from piston.resource import Resource
from djblog.api.handlers import BlogHandler, CommentHandler

product_handler = Resource(ProductHandler)
registry_handler = Resource(RegistryHandler)

urlpatterns = patterns('',
    #url(r'^product/(?P<id>[^/]+)/', identifier_handler),
    url(r'^blog/', product_handler),
    url(r'^comment/', registry_handler),
    )
