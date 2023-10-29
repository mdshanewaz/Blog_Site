from django import forms
from Blog_App.models import BlogModel, CommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('comment',)