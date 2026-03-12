from django.contrib import admin
from django import forms
from .models import Assignment, Rewrite

class RewriteAdminForm(forms.ModelForm):
    class Meta:
        model = Rewrite
        fields = '__all__'
        widgets = {
            'body': forms.Textarea(attrs={'class': 'markdown-editor'}),
        }

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('story', 'author', 'status', 'match_score')
    list_filter = ('status', 'author')
    search_fields = ('story__title', 'author__name')

@admin.register(Rewrite)
class RewriteAdmin(admin.ModelAdmin):
    form = RewriteAdminForm
    list_display = ('headline', 'status', 'created_at')
    list_filter = ('status', 'assignment__author')
    search_fields = ('headline', 'body')

    class Media:
        css = {
            'all': ('https://unpkg.com/easymde/dist/easymde.min.css',)
        }
        js = (
            'https://unpkg.com/easymde/dist/easymde.min.js',
            'admin/js/easymde_init.js',
        )
