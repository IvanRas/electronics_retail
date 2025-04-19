from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from django.views.generic import CreateView
from users.forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(CreateView):
    """Метод для регистраций usera"""

    model = User
    template_name = "register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        response = super().form_valid(form)

        send_mail(
            subject="Добро пожаловать!",
            message='Спасибо за регистрацию на нашем сайте "__"',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[form.cleaned_data.get("email")],
            fail_silently=False,
        )

        return response

