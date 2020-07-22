from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
	text = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	via = models.URLField(blank=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.text[:50]

	def total_likes(self):
		return self.like_set.count()

	class Meta:
		verbose_name = 'news'
		verbose_name_plural = 'news'	


class Like(models.Model):
	news = models.ForeignKey(News, on_delete=models.CASCADE)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(blank=True)
	blog = models.URLField(blank=True)

