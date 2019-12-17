
from django.contrib import admin
from django.contrib.auth.models import Group
from todo.forms.userForms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from todo.models import Person,Category,List

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'is_admin', 'is_verified','is_active', 'created_at','updated_at')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'person', 'created_at',)

class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'is_done','created_at')

# Now register the new UserAdmin...
admin.site.register(Person, UserAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(List, ListAdmin)
admin.site.unregister(Group)