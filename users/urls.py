from django.urls import path
from users import views
from users import views as user_views
from .views import deleteuser 

urlpatterns = [
    path('profile/', user_views.profile, name='profile'),
    path('/delete/', user_views.deleteuser, name='user-delete'),
]