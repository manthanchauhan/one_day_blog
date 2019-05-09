from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tag
from .models import Article
from django.contrib.auth.decorators import login_required
from django.middleware import csrf	
from django.contrib.auth.models import User
from . import forms

def home(request):
	articles = Article.objects.all()
	user = request.user
	return render(request, 'home.html', {'articles': articles, 'user': user})

def admin_profile(request):
	admin = User.objects.filter(is_superuser=True)
	admin = admin[0]
	user = request.user
	return render(request, 'admin_profile.html', 
		{'admin':admin, 
		'user': user,
		})

@login_required(login_url='login_url')
def article(request, id_):
	article_ = Article.objects.get(id=id_)
	return render(request, str(article_.content_template).replace(' ', '_'), {'article': article_})

@login_required(login_url='login_url')
def tag(request, id_):

	if request.method == 'POST':
		print('hi')
		tag_ = Tag.objects.get(id=id_)
		tag_.delete()
		return redirect('home_url')

	if request.method == 'GET':
		tag_ = Tag.objects.get(id=id_)
	return render(request, 'tag.html', {'tag':tag_})

def articles(request):
	if not request.user.is_superuser:
		return redirect('articles_home')

	if request.method == 'POST':
		if 'create' in request.POST.keys():
			print('hey')
			article = forms.NewArticle(request.POST)

			if article.is_valid():
				article = article.cleaned_data	
				
				title = article['title']
				description = article['description']
				tags_ = article['tags']
				tags_ = [Tag.objects.get(id=x) for x in tags_]

				content = title.replace(' ', '_') + '/content.html'
				thumbnail = 'articles/' + title.replace(' ', '_') + '/thumbnail.jpeg'
				article_ = Article.objects.create(title=title, 
					description=description, 
					content_template=content,
					thumbnail=thumbnail,
					author=request.user,
					)
				
				article_ = Article.objects.get(title=title)
				for tag in tags_:
					article_.tags.add(tag)

			return redirect('articles_home')
		else:
			form = forms.RemoveArticle(request.POST)
			
			if form.is_valid():
				form = form.cleaned_data
				titles = form['title']
				titles = [Article.objects.get(id=x) for x in titles]

				for article in titles:
					article.delete()

			return redirect('articles')

	elif request.method == 'GET':
		form_c = forms.NewArticle()
		form_r = forms.RemoveArticle()
		articles = Article.objects.all()

		return render(request, 'articles.html',
			{'create': form_c,
			'remove': form_r,
			'articles': articles,
			})

def tags(request):
	if not request.user.is_superuser:
		return redirect('articles_home')

	if request.method == 'POST':
		if 'create' in request.POST.keys():
			form = forms.CreateTag(request.POST)

			if form.is_valid():
				form = form.cleaned_data
			
				title = form['title']
				tag = Tag.objects.create(title=title)

			return redirect('tags_url')
				# print(tag)
		else:
			form = forms.RemoveTag(request.POST)

			if form.is_valid():
				form = form.cleaned_data
				ids = form['tags']
				for id_ in ids:
					Tag.objects.get(id=id_).delete()

			return redirect('home_url')

	elif request.method == 'GET':
		form_create = forms.CreateTag()
		form_remove = forms.RemoveTag()

		tags = Tag.objects.all()

		return render(request, 'tags.html', 
			{'create': form_create, 
			'remove': form_remove,
			'tags': tags,
			})

