from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    list_display = ("email",)
    ordering = ("email",)

    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name',
                           'last_name', 'name', 'phone', 'gender', 'session_token', 'is_superuser', 'is_staff', 'is_active', 'created_at', 'updated_at', 'is_doctor', 'is_medical_staff', 'hospital', 'department', 'speciality', 'about', 'image')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'first_name', 'last_name', 'is_doctor', 'is_medical_staff', 'hospital', 'department', 'speciality', 'about', 'image', 'is_superuser', 'is_staff', 'is_active')}
         ),
    )

    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
