from django.db import models
import os
from django.contrib.auth.models import User
from one_day_blog.settings import BASE_DIR

class Tag(models.Model):
	title = models.CharField(max_length=15, unique=True)
	date_created = models.DateTimeField(auto_now_add=True)

class ArticleManager(models.Manager):
	def create_article(self, 
		title, 
		description, 
		tags_,
		):
		content = title.replace(' ', '_') + '/content.html'
		thumbnail = 'articles/' + title.replace(' ', '_') + '/thumbnail.png'

		article = self.create(title=title, 
			description=description, 
			content_template=content,
			thumbnail=thumbnail,
			# author=author,
			)

		for tag in tags_:
			article.tags.add(tag)

		return article


class Article(models.Model):
	title = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=100)
	content_template = models.CharField(max_length=100)
	thumbnail = models.CharField(max_length=100)
	tags = models.ManyToManyField(Tag, related_name='tags')

	date_created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, models.SET_NULL, null=True, related_name='author')

	objects = ArticleManager() 

# Create your models here.
