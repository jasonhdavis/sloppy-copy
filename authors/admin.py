from django.contrib import admin
from django import forms
from .models import Author, EditorialStyleSheet

class AuthorAdminForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'markdown-editor'}),
            'beat_description': forms.Textarea(attrs={'class': 'markdown-editor'}),
            'style_guide': forms.Textarea(attrs={'class': 'markdown-editor'}),
            'persona_prompt': forms.Textarea(attrs={'class': 'markdown-editor'}),
        }

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    form = AuthorAdminForm
    list_display = ('name', 'slug', 'is_active')
    search_fields = ('name', 'slug')
    list_filter = ('is_active',)
    prepopulated_fields = {"slug": ("name",)}

    class Media:
        css = {
            'all': ('https://unpkg.com/easymde/dist/easymde.min.css',)
        }
        js = (
            'https://unpkg.com/easymde/dist/easymde.min.js',
            'admin/js/easymde_init.js',
        )

class EditorialStyleSheetAdminForm(forms.ModelForm):
    class Meta:
        model = EditorialStyleSheet
        fields = '__all__'
        widgets = {
            'rules': forms.Textarea(attrs={'class': 'markdown-editor'}),
        }

@admin.register(EditorialStyleSheet)
class EditorialStyleSheetAdmin(admin.ModelAdmin):
    form = EditorialStyleSheetAdminForm
    list_display = ('name', 'is_active', 'updated_at')
    list_filter = ('is_active',)

    class Media:
        css = {
            'all': ('https://unpkg.com/easymde/dist/easymde.min.css',)
        }
        js = (
            'https://unpkg.com/easymde/dist/easymde.min.js',
            'admin/js/easymde_init.js',
        )
