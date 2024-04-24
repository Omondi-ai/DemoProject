from . models import Article, Teacher

from django.forms import ModelForm

from welcome.models import CustomUser



class TeacherForm(ModelForm):
    class Meta:

        model = Teacher
        fields = ['name', 'code',]

class ArticleForm(ModelForm):
    class Meta:

        model = Article
        fields = ['title', 'content',]


class UpdateUserForm(ModelForm):
    password = None

    class Meta:

        model = CustomUser
        fields = ['email', 'first_name', 'last_name',]
        exclude = ['password1', 'password2',]

    