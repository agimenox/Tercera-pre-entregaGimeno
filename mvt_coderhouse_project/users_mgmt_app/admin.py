from django.contrib import admin

# Register your models here.
from users_mgmt_app.models import Client, Group, User

admin.site.register(Client)
admin.site.register(Group)
admin.site.register(User)