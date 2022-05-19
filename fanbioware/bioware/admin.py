from django.contrib import admin
from bioware.models import Game, Studio, Opening, GameSliderImage, StudioSliderImage
from django.utils.html import format_html

class GameSliderImageInline(admin.TabularInline):
    model = GameSliderImage
    extra = 5


class StudioSliderImageInline(admin.TabularInline):
    model = StudioSliderImage
    extra = 4


class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    inlines = [GameSliderImageInline, ]
    list_display = (
        'id', 'title', 'get_html_photo', 'intro',
        'rel_date', 'is_released'
    )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'intro', 'genre')
    list_editable = ('is_released',)
    list_filter = ('genre',)
    fields = (
        'title', 'slug', 'intro', 'description', 'image',
        'get_html_photo', 'rel_date', 'platforms', 'genre',
        'is_online', 'origin_url', 'steam_url', 'ps_url',
        'xbox_url', 'is_released'
    )
    readonly_fields = ('get_html_photo',)
    save_on_top = True

    def get_html_photo(self, object):
        """"Return img html tag with image url"""
        return format_html(f'<img src="{object.image.url}" width=100 height=70>')

    get_html_photo.short_description = 'Cover image'


class StudioAdmin(admin.ModelAdmin):
    inlines = [StudioSliderImageInline, ]
    list_display = (
        'id', 'location', 'address1',
        'get_html_photo', 'phone', 'email',
        'description'
    )
    list_display_links = ('id', 'location')
    readonly_fields = ('get_html_photo',)
    save_on_top = True

    def get_html_photo(self, object):
        return format_html(f'<img src="{object.image.url}" width=100>')

    get_html_photo.short_description = 'Cover image'


class OpeningAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'team', 'studio', 'description', 'is_opened')
    list_display_links = ('id', 'role')
    search_fields = ('role', 'team', 'description', 'studio__location')
    list_editable = ('is_opened',)
    list_filter = ('studio', 'team', 'role')
    save_on_top = True


admin.site.register(Game, GameAdmin)
admin.site.register(Studio, StudioAdmin)
admin.site.register(Opening, OpeningAdmin)
