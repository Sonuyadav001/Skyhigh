# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag, Comment
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Blog Home with List of Posts
from .models import Post, Category, Tag

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['recent_posts'] = Post.objects.order_by('-date_posted')[:5]
        context['tags'] = Tag.objects.all()  # Add all tags to the context
        return context



# Filter Posts by Category
def blog_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category).order_by('-date_posted')
    context = {
        'posts': posts,
        'category': category,
        'tag': None,  # Add tag as None
        'categories': Category.objects.all(),
        'recent_posts': Post.objects.order_by('-date_posted')[:5],
    }
    return render(request, 'blog/blog.html', context)

# Filter Posts by Tag
from django.shortcuts import render, get_object_or_404
from .models import Post, Tag, Category

def blog_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = tag.posts.all().order_by('-date_posted')
    context = {
        'posts': posts,
        'tag': tag,  # Pass the active tag to the template
        'categories': Category.objects.all(),
        'recent_posts': Post.objects.order_by('-date_posted')[:5],
    }
    return render(request, 'blog/blog.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context['categories'] = Category.objects.all()
        context['recent_posts'] = Post.objects.order_by('-date_posted')[:5]
        context['related_posts'] = Post.objects.filter(
            category=post.category
        ).exclude(id=post.id)[:4]
        context['comments'] = post.comments.filter(parent__isnull=True)
        return context



from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        parent_id = request.POST.get('parent_id')
        parent = None

        if parent_id:
            parent = get_object_or_404(Comment, id=parent_id)

        post = get_object_or_404(Post, id=post_id)
        Comment.objects.create(post=post, user=request.user, content=content, parent=parent)
        return redirect('post-detail', pk=post_id)

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(parent=None).prefetch_related('replies__user', 'user')
    return render(request, 'post_detail.html', {'object': post, 'comments': comments})



# Custom View for Blog (if needed)
def blog(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {
        'posts': posts,
        'categories': Category.objects.all(),
        'recent_posts': Post.objects.order_by('-date_posted')[:5],
    }
    return render(request, 'blog/blog.html', context)


from django.shortcuts import render
from .models import Post

def search_posts(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    posts = Post.objects.filter(title__icontains=query) if query else []
    context = {
        'query': query,
        'posts': posts,
    }
    return render(request, 'blog/search_results.html', context)
