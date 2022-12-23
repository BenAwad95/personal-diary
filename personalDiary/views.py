from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView

from .forms import DiaryForm
from .models import Diary
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied


APP_NAME = "personalDiary"
def set_template_name(template_name):
    return f"{APP_NAME}/{template_name}"


class ListDiaryView(ListView):
    context_object_name='diaries'

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            raise PermissionDenied
        user_ins = User.objects.get(username=self.request.user.username)
        return Diary.objects.filter(user=user_ins).all()


class CreateDiaryView(CreateView):
    model=Diary
    fields=['title', 'body', 'mood']
    template_name='personalDiary/new_diary.html'


    #* must user login 
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous:
            raise PermissionDenied
        return super().get(request)

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous:
            raise PermissionDenied
        return super().post(request)

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class DetailDiaryView(DetailView):
    model=Diary

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous:
            raise PermissionDenied
        return super().get(request)

class UpdateDiaryView(UpdateView):
    model=Diary
    fields=['title', 'body']
    # success_url=reverse_lazy('detail-diary')

    #* must user login 
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous:
            raise PermissionDenied

class DeleteDairyView(DeleteView):
    model=Diary
    success_url=reverse_lazy('personalDiary:home')

    #* must user login 
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous:
            raise PermissionDenied
    
