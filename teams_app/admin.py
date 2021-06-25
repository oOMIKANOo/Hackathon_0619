from django.contrib import admin

from .models import Teams,Lang,Tech

@admin.register(Lang)
class LangAdmin(admin.ModelAdmin):
    pass

@admin.register(Tech)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Teams)
class UserAdmin(admin.ModelAdmin):
    pass