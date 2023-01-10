from django.contrib import admin

# Register your models here.
from users_mgmt_app.models import Member, Client, Group

admin.site.register(Member)
admin.site.register(Client)
admin.site.register(Group)