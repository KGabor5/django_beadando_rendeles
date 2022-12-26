from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('rendelt_termek', 'lakcim', 'megjegyzes', 'fzetes_modja')
