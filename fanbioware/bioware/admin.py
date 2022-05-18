from django.contrib import admin
from bioware.models import Game, Studio, Opening, GameSliderImage, StudioSliderImage


class GameSliderImageInline(admin.TabularInline):
    model = GameSliderImage
    extra = 5


class StudioSliderImageInline(admin.TabularInline):
    model = StudioSliderImage
    extra = 4


class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    inlines = [GameSliderImageInline, ]
    list_display = ('id', 'title', 'image', 'description', 'is_released')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description', 'genre')


class StudioAdmin(admin.ModelAdmin):
    inlines = [StudioSliderImageInline, ]
    list_display = (
        'id', 'location', 'address1',
        'phone', 'email', 'description'
    )
    list_display_links = ('id', 'location')


class OpeningAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'team', 'studio', 'is_opened')
    list_display_links = ('id', 'role')
    search_fields = ('role', 'team', 'description', 'studio__location')


admin.site.register(Game, GameAdmin)
admin.site.register(Studio, StudioAdmin)
admin.site.register(Opening, OpeningAdmin)
