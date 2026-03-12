from django.contrib import admin
from .models import EditorialStyleSheet

@admin.register(EditorialStyleSheet)
class EditorialStyleSheetAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)
