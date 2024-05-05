# from django.contrib import admin

# from .models import Token, User

# admin.site.register(Token)
# admin.site.register(User)

from django.contrib import admin
from .models import Token, User


class TokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'token_type')
    list_filter = ('user',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')
    list_filter = ('name', 'last_name')


admin.site.register(Token, TokenAdmin)
admin.site.register(User, UserAdmin)
