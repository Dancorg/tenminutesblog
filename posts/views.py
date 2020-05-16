from django.views.generic.list import ListView
from .models import Post


class PostListsView(ListView):
    template_name = 'posts/posts.html'
    model = Post
    paginate_by = 5