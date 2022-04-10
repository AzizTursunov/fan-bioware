from django.contrib import admin
from .models import Game, News


class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Game, GameAdmin)
admin.site.register(News)
