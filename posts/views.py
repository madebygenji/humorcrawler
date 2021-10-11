from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')


class PostDetail(DetailView):
    model = Post