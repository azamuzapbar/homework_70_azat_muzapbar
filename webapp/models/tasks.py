from django.db import models


class Task(models.Model):
    summary = models.CharField(max_length=300, verbose_name='описание', null=False, blank=False)
    description = models.TextField(max_length=2000, verbose_name='полное_описание')
    status = models.ForeignKey('webapp.Status', related_name='Tasks', on_delete=models.PROTECT, verbose_name='статус')
    type = models.ForeignKey('webapp.Type', related_name='Tasks', on_delete=models.PROTECT, verbose_name='тип')
    project = models.ForeignKey('webapp.Project', related_name='tasks', on_delete=models.CASCADE, verbose_name='проект', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='время_создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='время_обновления', auto_now=True)

    def __str__(self):
        return self.summary