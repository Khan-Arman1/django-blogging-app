from django import forms
from .models import Blogs, BlogReview
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogsForm(forms.ModelForm):
    class Meta:
        model= Blogs
        fields= ['blog_title', 'blog_img', 'blog_text']

        widgets = {
            'blog_title': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Blog Title',
                }
            ),
            'blog_img': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Image',
                }
            ),
            'blog_text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write your blog content...'
                }
            )
        }

        labels = {
            'blog_title': 'Blog Title',
            'blog_text': 'Blog Content',
            'blog_img': 'Related Image',
        }


class BlogReviewForm(forms.ModelForm):
    # reviewer_name=forms.CharField(max_length=40, required=True, label='User Name')
    class Meta:
        model = BlogReview
        fields = ['reviewer_name','rating','comment']

        widgets = {
            'reviewer_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'User Name',
                }
            ),
            'rating': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select Rating',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Write your comment here...',
                }
            ),
        }

        labels = {
            'reviewer_name': 'Your Name',
            'rating': 'Your Rating',
            'comment': 'Your Comment',
        }


class RegisterUser(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Ye tab use hoga jab aap har field me manually Bootstrap class nahi dena chahte
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs.update({'class': 'form-control'})

