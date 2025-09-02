from django.contrib import admin
from .models import Blogs, BlogReview

# Register your models here.
class BlogReviewInline(admin.TabularInline):
    model = BlogReview
    extra = 1

class BlogReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog_title', 'blog_upload')
    inlines = [BlogReviewInline]

admin.site.register(Blogs, BlogReviewAdmin)
