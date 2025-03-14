from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import now


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'blog/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        # Cập nhật trạng thái công việc quá hạn
        Task.objects.filter(
            user=self.request.user,
            finished__lt=now()
        ).exclude(status='C').update(status='O')

        # Lấy danh sách công việc sau khi cập nhật
        return Task.objects.filter(user=self.request.user)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'blog/task_detail.html'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'blog/task_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Công việc được tạo thành công!')
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'blog/task_form.html'
    success_url = '/'


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'blog/task_confirm_delete.html'
    success_url = '/'
