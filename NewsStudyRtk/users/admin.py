from django.contrib import admin
from .models import *
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user','gender']
    list_filter = ['user','gender']

admin.site.register(Account,AccountAdmin)

from django.contrib.auth.models import Group
def make_author(modeladmin,request,queryset):
    group = Group.objects.get(name='Authors')
    ungroup = Group.objects.get(name='Actions Required')
    for user in queryset:
        user.groups.add(group)
        user.groups.remove(ungroup)

make_author.short_description = "Утвердить автора"

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
class CustomUserAdmin(UserAdmin):
    actions = [make_author]
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class FavoriteArticleAdmin(admin.ModelAdmin):
    list_display = ['article','user','create_at']
admin.site.register(FavoriteArticle, FavoriteArticleAdmin)

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['status','name', 'email']
    list_filter = ['status','name', 'email']
    list_display_links = ['name']
    readonly_fields = ['name', 'email']
    # list_editable = ['status']
    actions = ['set_true']
    @admin.action(description='Пометить исправленными выбранные замечания')
    def set_true(self, request, queryset):
        amount = queryset.update(status=True)
        self.message_user(request, f'Исправлено {amount} проблем')
