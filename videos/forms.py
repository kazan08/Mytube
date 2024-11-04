from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('name', 'description', 'video', 'preview')
        labels = {
            'name': 'Название видео',
            'description': 'Описание',
            'video': 'Видео',
            'preview': 'Превью',
        }
