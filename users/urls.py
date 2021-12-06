from django.urls import path
from users.views import (
    user_signup,
    user_login,
    user_profile,
    add_profile,
    edit_profile,
    user_logout,
    contact,

)

urlpatterns = [
    path('signup/', user_signup, name= "user_signup"),                           # User Register
    path('login/', user_login, name= "user_login"),                              # User Login
    path('user_profile/<int:pk>/', user_profile, name= "user_profile"),          # User Profile
    path('edit_profile/<int:pk>/', edit_profile, name= "edit_profile"),          # Edit Profile
    path('add_profile/', add_profile, name= "add_profile"),                      # Add Profile
    path('logout/', user_logout, name= "logout"),                                # User Logout
    path('contact/', contact, name= "contact"),                                  # Contact Us
]
