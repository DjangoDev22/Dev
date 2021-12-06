from django.urls import path
from posts.views import (
    PostListingsView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CategoryCreateView,
    CategoryPostListView,
    TagCreateView,
    TagPostListView,
    SearchPostView,
    LikeView,
    DisLikeView,
    favouritePostView,
)

# from .feeds import PostFeed

app_name = "posts"
urlpatterns = [
    path('', PostListingsView.as_view(), name="post_listings"),                      # Post Listings
    path('search_results/', SearchPostView.as_view(), name="search_results"),        # Post Search
    path('add_post/', PostCreateView.as_view(), name="add_post"),                    # Add Post
    path('post/<slug:slug>/', PostDetailView, name="post_detail"),                   # Post Detail
    path('<slug:slug>/like/', LikeView.as_view(), name="like"),                      # Post Like
    path('<slug:slug>/dislike/', DisLikeView.as_view(), name="dislike"),             # Post Dislike
    path('<slug:slug>/favourite/', favouritePostView, name="favourite"),             # Favourite Post
    path('update/<int:pk>/', PostUpdateView.as_view(), name="post_update"),          # Update Post
    path('<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),          # Delete Post
    path('add_category/', CategoryCreateView.as_view(), name="add_category"),        # Add Category
    path('category/<slug:slug>/', CategoryPostListView.as_view(), name="category"),  # Category Post Listings
    path('add_tag/', TagCreateView.as_view(), name="add_tag"),                       # Add Tags
    path('tag/<slug:slug>/', TagPostListView.as_view(), name="tags"),                # Tag Post Listings
    # path('feed_rss/', PostFeed(), name='post_feeds'),                              # Post RSS Feeds
]
