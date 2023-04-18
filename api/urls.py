from django.urls import path, include

from api.views import TaskDetailView, TaskUpdateView, TaskDeleteView, ProjectDetailView, \
    ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('articles/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('articles/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    path('articles/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete'),
]