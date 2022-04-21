from django.contrib import admin
from .models import Game, News, Studio, Opening, GameSliderImage, StudioSliderImage


class GameSliderImageInline(admin.TabularInline):
    model = GameSliderImage
    extra = 5


class StudioSliderImageInline(admin.TabularInline):
    model = StudioSliderImage
    extra = 4


class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    inlines = [GameSliderImageInline, ]


class StudioAdmin(admin.ModelAdmin):
    inlines = [StudioSliderImageInline, ]


admin.site.register(Game, GameAdmin)
admin.site.register(News)
admin.site.register(Studio, StudioAdmin)
admin.site.register(Opening)
