from django.contrib.auth.forms import UserCreationForm

from users.models import User

forbidden = []


class UserRegistrationForm(UserCreationForm):
    """Форма для регестрация usera"""

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "phone_number")
