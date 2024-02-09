from django import forms
from django.contrib.auth.models import User
from app_users.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    teachers = 'teachers'
    students = 'students'
    parents = 'parents'
    user_types = [
        (teachers, 'Teacher'),
        (students, 'Student'),
        (parents, 'Parent'),
    ]
    user_type = forms.ChoiceField(choices=user_types, widget=forms.Select(attrs={'class': 'form-control'}), required=True)

    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)  # Make password2 not required

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'image', 'user_type')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'password1': 'Password',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user_type = self.cleaned_data.get('user_type')
        if user_type == 'teachers':
            user.is_staff = True  # Set is_staff to True for teachers
        user.save()
        # You may need to create UserProfileInfo object here if you have one and set the user_type accordingly
        return user
