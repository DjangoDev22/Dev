from django import forms
from posts.models import (
    Posts,
    Categories,
    Tags
)

class PostForm(forms.ModelForm):
    title = forms.CharField(
        widget = forms.TextInput(
            attrs = {
            'class': 'title',
        }),
        label = '',
    )

    content = forms.CharField(
        widget = forms.Textarea(
            attrs = {
            'class': 'body',
        }),
        label = '',
    )

    # image = forms.ClearableFileInput()

    class Meta:
    	model= Posts
    	fields= '__all__'
    	exclude= ['author', 'slug', 'created_at', 'updated_at']



class TagForm(forms.ModelForm):
    tag_name = forms.CharField(
        widget = forms.TextInput(
            attrs = {
            'class': 'tag',
            'placeholder': 'Post Tag'
        }),
        label = '',
    )

    class Meta:
    	model= Tags
    	fields= ('tag_name',)



class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(
        widget = forms.TextInput(
            attrs = {
            'class': 'category',
            'placeholder': 'Post Category'
        }),
        label = '',
    )

    class Meta:
    	model= Categories
    	fields= ('category_name',)
