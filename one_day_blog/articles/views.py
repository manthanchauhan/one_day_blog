from django.shortcuts import render
from django.http import HttpResponse
from .models import Tag
from .models import Article

def home(request):
	articles = Article.objects.all()
	return render(request, 'home.html', {'articles': articles})

def article(request, id_):
	article_ = Article.objects.get(id=id_)
	return render(request, str(article_.content_template).replace(' ', '_'), {'article': article_})

def tag(request, id_):
	tag_ = Tag.objects.get(id=id_)
	return render(request, 'tag.html', {'tag':tag_})

# Create your views here.
