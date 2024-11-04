from django.contrib import admin
from.models import Video, Comment

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_filter = ('pub_date',)
    search_fields = ('title',)
    raw_id_fields = ('author_name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('video', 'author_name', 'text', 'pub_date')
    list_filter = ('video', 'pub_date',)
    search_fields = ('video', 'author_name',)
    raw_id_fields = ('video', 'author_name',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)