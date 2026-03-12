from django.contrib import admin
from .models import Author, EditorialStyleSheet

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active')
    search_fields = ('name', 'slug')
    list_filter = ('is_active',)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(EditorialStyleSheet)
class EditorialStyleSheetAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'updated_at')
    list_filter = ('is_active',)
