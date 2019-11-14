from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeteleView


urlpatterns = [
	path('post/<int:pk>/delete', BlogDeteleView.as_view(), name='post_delete'),
	path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
	path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), #todos los post van a estar en post/ y el resto es la clave primaria que identifica a cada uno
    path('', BlogListView.as_view(), name='home'),
]