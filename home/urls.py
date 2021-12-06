from django.urls import path
from home.views import home, latest_posts, trending_posts, send_mails


urlpatterns= [
    path('', home, name="home"),
    path('latest/', latest_posts, name="latest_posts"),
    path('trending/', trending_posts, name="trending_posts"),
    path('send_mails/', send_mails, name="send_mails"),
]
