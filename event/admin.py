from django.contrib import admin
from .models import Event, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'status', 'created_on')
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Category)
