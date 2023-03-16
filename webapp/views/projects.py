from django.views.generic import ListView
from webapp.models.articles import Project


class ProjectView(ListView):
    template_name = 'projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all().order_by('-created_at')
