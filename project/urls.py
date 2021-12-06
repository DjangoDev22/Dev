from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('users/', include("users.urls")),
    path('users/', include("allauth.urls")),
    path('newsletter/', include("newsletter.urls")),
    path('posts/', include("posts.urls", namespace="posts")),


    # path('comments/api', include("comments.api.urls", namespace="comments_api")),
    # path('posts/api', include("posts.api.urls", namespace="posts_api")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
