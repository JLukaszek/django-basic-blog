from django import forms

from .models import BlogPost


class BlogPostFrom(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Title:', 'text': 'Text:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
