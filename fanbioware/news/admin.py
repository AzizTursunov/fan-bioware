from django.contrib import admin
from django.utils.html import format_html
from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'get_html_photo', 'intro',
        'pub_date', 'game',
        'is_publicated'
    )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'intro', 'text')
    list_editable = ('is_publicated',)
    list_filter = ('game', )
    readonly_fields = ('get_html_photo',)
    save_on_top = True

    def get_html_photo(self, object):
        """"Return img html tag with image url"""
        return format_html(f'<img src="{object.image.url}" width=100 height=70>')

    get_html_photo.short_description = 'Cover image'


admin.site.register(News, NewsAdmin)
