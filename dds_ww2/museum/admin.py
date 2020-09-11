from django.contrib import admin

from .models import ships, battle, outcomes, user

admin.site.register(ships)
admin.site.register(battle)
admin.site.register(outcomes)
admin.site.register(user)

