from django import forms
from comments.models import Comment



class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget = forms.Textarea(
            attrs = {
            'class': 'textarea',
            'placeholder': 'Write Your Comment Here ...'
        }),
        label = '',
    )
    class Meta:
        model= Comment
        fields= ('comment',)
