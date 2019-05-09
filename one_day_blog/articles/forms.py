from django import forms
from .models import Tag
from .models import Article

class NewArticle(forms.Form):
	title = forms.CharField(max_length=100)
	description = forms.CharField(max_length=500)

	choices = []
	for tag in Tag.objects.all():
		choices.append((tag.id, tag.title))

	tags = forms.MultipleChoiceField(choices=choices)

class RemoveArticle(forms.Form):
	choices = []
	for article in Article.objects.all():
		choices.append((article.id, article.title))

	title = forms.MultipleChoiceField(choices=choices)

class CreateTag(forms.Form):
	title = forms.CharField(max_length=20)

class RemoveTag(forms.Form):
	choices = []
	for tag in Tag.objects.all():
		choices.append((tag.id, tag.title))

	tags = forms.MultipleChoiceField(choices=choices)
