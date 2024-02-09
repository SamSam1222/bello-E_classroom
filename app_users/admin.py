from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms  # Add this import

class CustomUserCreationForm(UserCreationForm):
    user_types = [
        ('teacher', 'Teacher')
    ]
    user_type = forms.ChoiceField(choices=user_types, initial='teacher', widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'user_type')

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm

    def save_model(self, request, obj, form, change):
        obj.user_type = 'teacher'
        super().save_model(request, obj, form, change)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        # If adding a new user, include 'user_type' field in the form
        if not obj:
            fieldsets += (('User Type', {'fields': ('user_type',)}),)
        return fieldsets

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
