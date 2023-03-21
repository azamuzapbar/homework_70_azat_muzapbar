from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import DetailView, CreateView
from webapp.models import Project

class ProjectCreateView(CreateView):
    template_name = 'project_create.html'
    model = Project
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse('projects')


class ProjectDetail(DetailView):
    template_name = 'project_detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context