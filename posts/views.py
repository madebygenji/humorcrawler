from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag


# Create your views here.
class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()
        
        return context


class PostListByTag(ListView):
    def get_queryset(self):
        tag_slug = self.kwargs['slug']
        tag = Tag.objects.get(slug=tag_slug)

        return tag.post_set.order_by('-created')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListByTag, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()
        
        slug = self.kwargs['slug']
        context['tag'] = Tag.objects.get(slug=slug)
        
        return context


class PostListByCategory(ListView):

    def get_queryset(self):
        slug = self.kwargs['slug']

        if slug == '_none':
            category = None
        else:
            category = Category.objects.get(slug=slug)

        return Post.objects.filter(category=category).order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListByCategory, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()
        
        slug = self.kwargs['slug']

        if slug == '_none':
            context['category'] = '미분류'
        else:
            context['category'] = Category.objects.get(slug=slug)

        return context
