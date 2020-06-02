from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('profile_view/', views.profile_view, name='profile_view'),
    path('create/',views.create,name='create'),
    path('delete/<picture_id>',views.delete_picture,name='delete')
]