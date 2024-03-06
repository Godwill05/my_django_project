from django.contrib import admin

from .models import Author, Book
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'quantity')
    list_filter = ['author', 'title', 'quantity']
    search_fields = ['title']

"""
    admin.site.register(Author)
    admin.site.register(Book, BookAdmin)
"""