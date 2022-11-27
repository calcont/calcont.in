from django.contrib import admin
from .models import Headlines,Contact,Donate
from import_export import resources
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'email')
class UserAdmin(ImportExportModelAdmin):
    list_display = ('id','username','first_name', 'last_name', 'email')
    resource_class = UserResource
    pass


# Register your models here.
admin.site.register(Headlines)
admin.site.register(Contact)
admin.site.register(Donate)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)