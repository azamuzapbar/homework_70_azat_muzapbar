from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView
from webapp.models import Project


class AddUserView(View):
    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        user_pk = request.POST.get('user')
        user = get_object_or_404(User, pk=user_pk)
        project.users.add(user)
        return redirect('project_detail', pk=pk)


class RemoveUserView(View):
    def get(self, request, project_pk, user_pk):
        project = get_object_or_404(Project, pk=project_pk)
        user = get_object_or_404(User, pk=user_pk)
        project.users.remove(user)
        return redirect('project_detail', pk=project_pk)


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users')

    def get(self, request, *args, **kwargs):
        self.delete(request, *args, **kwargs)
        return redirect(self.success_url)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
