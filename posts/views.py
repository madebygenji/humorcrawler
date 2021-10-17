from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.shortcuts import redirect
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


class PostUpdate(UpdateView):
    model = Post
    fields = [
        'title', 'content', 'head_image', 'category', 'tags'
    ]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostUpdate, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        return context


class PostCreate(CreateView):
    model = Post
    fields = [
        'title', 'content', 'head_image', 'category', 'tags'
    ]
    
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(type(self), self).form_valid(form)
        else:
            return redirect('/posts/')
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostCreate, self).get_context_data(**kwargs)
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
