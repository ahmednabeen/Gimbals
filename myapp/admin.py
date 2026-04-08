from django.contrib import admin
from .models import Post, ContactSubmission # Add ContactSubmission here

# Register your models here.
admin.site.register(Post)
admin.site.register(ContactSubmission)