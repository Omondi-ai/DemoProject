from django.contrib.auth.forms import UserCreationForm

from . models import CustomUser

class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'is_teacher', 'is_student', 'is_parent']
