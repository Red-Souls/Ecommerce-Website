from django import forms
from .models import*

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control'})