from django.contrib import admin
from bioware.models import Game, Studio, Opening, GameSliderImage, StudioSliderImage
from news.models import News

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
