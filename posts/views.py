from django.db.models import Q
from django.urls import reverse_lazy

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from posts.models import (
    Posts,
    Categories,
    Tags,
)

from comments.models import Comment

from posts.forms import (
    PostForm,
    TagForm,
    CategoryForm,
)

from comments.forms import CommentForm

# Create your views here.
class PostListingsView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = "posts/post_listings.html"
    # context_object_name = 'articles'   # by default .. The context name is (object_list)
    paginate_by = 6                    # each page must have 6 items.

    # List The Categories In The Side Bar Of The post listings page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Posts.objects.all()
        context['categories'] = Categories.objects.all()
        return context

@login_required
def PostDetailView(request, slug):
    article = Posts.objects.get(slug=slug)
    comments = Comment.objects.filter(post=article)

    # Related (Similar) Posts By Tags
    tags = article.tags.all()
    related_posts = Posts.objects.filter(tags__in=tags).exclude(slug=slug)[:5]

    # Comments
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.post = article
            myform.save()
            return redirect('posts:post_listings')

    else:
        form = CommentForm()

    context={
        'article': article,
        'form': form,
        'comments': comments,
        'related_posts': related_posts
    }

    return render(request, "posts/post_detail.html", context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    form_class = PostForm
    template_name = "posts/add_post.html"
    success_url = reverse_lazy('posts:post_listings')

    def form_valid(self, form):  # Used to save extra data on the database
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        form.save_m2m()
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    form_class = PostForm
    template_name = "posts/update_post.html"
    success_url = reverse_lazy('posts:post_listings')

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    template_name = "posts/delete_post.html"
    success_url = reverse_lazy('posts:post_listings')

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Categories
    form_class = CategoryForm
    template_name = "posts/add_category.html"
    success_url = reverse_lazy('posts:post_listings')

class CategoryPostListView(LoginRequiredMixin, ListView):
    model = Categories
    template_name = "posts/category_posts.html"
    context_object_name = 'category_articles'
    paginate_by= 6

    # List The Categories In The Side Bar Of The category posts page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        return context

    def get_queryset(self, *args, **kwargs):
        category = get_object_or_404(Categories, slug=self.kwargs['slug'])
        return Posts.objects.filter(category=category).order_by('-created_at')

class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tags
    form_class = TagForm
    template_name = "posts/add_tag.html"
    success_url = reverse_lazy('posts:post_listings')

class TagPostListView(LoginRequiredMixin, ListView):
    model = Tags
    template_name = "posts/tags_posts.html"
    context_object_name = "tags_articles"
    paginate_by= 6

    # List The Categories In The Side Bar Of The tag posts page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        return context

    def get_queryset(self, *args, **kwargs):
        tag = get_object_or_404(Tags, slug=self.kwargs['slug'])
        return Posts.objects.filter(tags=tag)

class SearchPostView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = "posts/search_results.html"
    context_object_name = "search_articles"
    paginate_by= 6

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('q')
        if query:
            return Posts.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()

class LikeView(LoginRequiredMixin, View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Posts, slug=slug)  # Grap The Post U Wanna Like

        # Second Part
        # Check If user disliked the post [The user already clicked dislike button]
        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike == True:  # If the user clicked dislike btn again
            post.dislikes.remove(request.user)  # remove that dislike

        # First Part
        # If user isn't in that field >> add this user to the ManyToMany field [Loop Through The Likes Field]
        is_like = False
        for like in post.likes.all():  # Return The List Of Users
            if like == request.user:  # If user in that list
                is_like = True
                break

        if is_like == False:  # If user didn't make like
            post.likes.add(request.user)  # Add it

        if is_like == True:  # If user made like
            post.likes.remove(request.user)  # Remove it

        return redirect('posts:post_detail', slug=post.slug)

class DisLikeView(LoginRequiredMixin, View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Posts, slug=slug)

        # Second Part
        # Check If user liked the post [The User Clicked Like Button]
        is_like = False
        for like in post.likes.all():  # Return The List Of Users
            if like == request.user:  # If user in that list
                is_like = True
                break

        if is_like == True:
            post.likes.remove(request.user)

        # First Part
        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike == False:
            post.dislikes.add(request.user)

        if is_dislike == True:
            post.dislikes.remove(request.user)

        return redirect('posts:post_detail', slug=post.slug)

@login_required
def favouritePostView(request, slug):
    post = get_object_or_404(Posts, slug=slug)

    is_favourited = False
    for favourite_post in post.favourites.all():
        if favourite_post == request.user:
            is_favourited = True
            break

    if is_favourited == False:
        post.favourites.add(request.user)

    if is_favourited == True:
        post.favourites.remove(request.user)

    return redirect('posts:post_detail', slug=post.slug)
