from django.contrib.auth.models import User
from django.views.generic import ListView



class UserView(ListView):
    template_name = 'users.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()
