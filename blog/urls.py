from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView


urlpatterns = [
	path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), #todos los post van a estar en post/ y el resto es la clave primaria que identifica a cada uno
    path('', BlogListView.as_view(), name='home'),
]