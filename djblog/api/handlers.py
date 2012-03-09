from piston.handler import BaseHandler
from djblog.blog.models import Blog, Comment
from django.contrib.auth.models import User

class BlogHandler(BaseHandler):
    """
    This will allow for CRUD operations on blog entries
    """
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    model = Blog
    fields = ('blog_title', 'author', 'blog_summary', 'blog_entry')
    exclude = ('_state', 'is_active', 'email', 'is_superuser', 'is_staff', 'last_login', 'password', 'id')
    
    def read(self, request, blog_title=None):
        base = Blog.objects
        return base.all()

class CommentHandler(BaseHandler):
    """
    This will allow for CRUD operations on blog comments
    """
    allowed_methods = ('GET', 'PUT', 'POST')
    model = Comment
    fields = ('name', 'email', 'comment', 'moderated')

    def read(self, request, comment=None):
        base = Comment.objects
        return base.all()

class BlogAndCommentHandler(BaseHandler):
    """
    This will retrieve a Blog and ALL comments
    """
    allowed_methods = ('GET')
    model = Blog
    fields = ('blog_name', 'author', 'blog_summary', 'blog_entry', ('comment', ()))
    exclude = ('_state', 'is_active', 'email', 'is_superuser', 'is_staff', 'last_login', 'password', 'id')

    def read(self, request, blog_title=None):
        base = Blog.objects
        return base.all()
