from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'title_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title of the article'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Announcement of the article'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of publication'
            }),
            'title_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'The text of the article'
            })
        }
