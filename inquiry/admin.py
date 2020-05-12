from django.contrib import admin
from .models import Inquiry
from .models import Category


class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'email', 'categoryname', 'reply')
    ordering = ('-created_at',)
admin.site.register(Inquiry, InquiryAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort', 'created_at', 'updated_at')
    ordering = ('-created_at',)
admin.site.register(Category, CategoryAdmin)