from django.contrib import admin

from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    ordering = ('start_date',)
    # search_fields = ('del_flg', False)
admin.site.register(News, NewsAdmin)
