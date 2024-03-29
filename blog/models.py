from django.db import models
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=50)
	author = models.ForeignKey(
		'auth.User',
		on_delete=models.CASCADE,
		)
	body = models.TextField()

	# Esto me sirve para ver cada objeto por su nombre de titulo
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', args=[str(self.id)])