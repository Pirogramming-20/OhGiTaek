from django import forms

from .models import *

class PostForm(forms.ModelForm):
    
    # title = forms.CharField(
    #     label='게시글 제목',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class' : 'signup-input'
    #         }
    #     )
    # )
    # content = forms.Textarea(
    #     label='게시글 내용',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class' : 'signup-input'
    #         }
    #     )
    # )
    
    class Meta:
        model = Post
        fields = ('title','content')