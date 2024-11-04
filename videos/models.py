from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from account.models import Profile
from django.urls import reverse

class Video(models.Model):
    name = models.CharField('Название видео', max_length=255)
    video = models.FileField('video', upload_to='videos/%Y/%m/%d/', null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm', 'ogg', 'avi'])])
    preview = models.ImageField('Превью', upload_to='previews/%Y/%m/%d/', null=True,)
    description = models.TextField('Описание', blank=True)
    author_name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(Profile, related_name='likes', blank=True)
    dislike = models.ManyToManyField(Profile, related_name='dislikes', blank=True)

    def __str__(self):
        return f'Видео: {self.name} от {self.author_name.user.username}'

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def get_absolute_url(self):
        return reverse('videos:detail', args=[self.id])

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    author_name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField('Текст комментария', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Комментарий: {self.text} от {self.author_name.user.username} к видео {self.video.name}'

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        indexes = [
            models.Index(fields=['video', 'pub_date']),
        ]