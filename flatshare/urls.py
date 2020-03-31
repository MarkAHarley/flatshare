from django.urls import path
from flatshare import views

app_name = 'flatshare'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('flats/', views.list_flats, name="list_flats"),
    path('flats/<slug:flat_slug>/', views.show_flat, name='show_flat'),
    path('users/<slug:user_slug>', views.view_profile, name='view_profile'),
    path('my_matches/', views.my_matches, name='my_matches'),
    path('add_flat/', views.add_flat, name='add_flat'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
