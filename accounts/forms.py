from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import Egresado


class GraduadoForm(ModelForm):
	class Meta:
		model = Egresado
		fields = '__all__'
		exclude = ['user']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']