from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView 
from .models import Post

class BlogListView(ListView):
	model = Post #vinculo al modelo
	template_name = 'home.html' #vinculo al template
	context_object_name = 'all_posts_list'


class BlogDetailView(DetailView): #ojo, no es lo mismo ListView que DetailView. Detail View se trae el contexto de un objeto en particular para poder mostrar
	model = Post
	template_name = 'post_detail.html'
	# context_object_name = 'posts_detail'

class BlogCreateView(CreateView):
	model = Post
	template_name = 'post_new.html'
	fields = '__all__'