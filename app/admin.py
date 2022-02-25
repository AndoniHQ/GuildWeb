from django.contrib import admin
from app.models import Character, Token

# Register your models here.


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Realm', 'Playable_class', 'Playable_race', 'Rank')
    list_filter = ('Playable_class', 'Level', 'Realm')


admin.site.register(Character, CharacterAdmin)
admin.site.register(Token)
