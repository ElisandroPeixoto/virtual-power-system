from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUsuario


class CriarCustomUsuario(UserCreationForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'pais', 'estado', 'cidade')
        labels = {'username': 'Usuario/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()

        return user


class AlterarCustomUsuario(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'pais', 'estado', 'cidade')
