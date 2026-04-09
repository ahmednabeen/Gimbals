# myapp/admin.py

from django.contrib import admin
from .models import Post, ContactSubmission, Author, Category

# A more advanced admin view for Posts
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    list_filter = ('author', 'categories', 'publication_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)} # Auto-fills slug from title

class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('first_name', 'last_name', 'email', 'message')
    readonly_fields = ('first_name', 'last_name', 'email', 'phone', 'message', 'submitted_at')

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(ContactSubmission, ContactSubmissionAdmin)
