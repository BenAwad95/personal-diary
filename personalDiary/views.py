from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView

from .forms import DiaryForm
from .models import Diary
from django.contrib.auth.models import User


APP_NAME = "personalDiary"
def set_template_name(template_name):
    return f"{APP_NAME}/{template_name}"


class ListDiaryView(ListView):
    context_object_name='diaries'
    def get_queryset(self):
        user = User.objects.get(username=self.request.user.username)
        # print(type(user))
        return Diary.objects.filter(user=user).all()


class CreateDiaryView(CreateView):
    model=Diary
    fields=['title', 'body']
    template_name='personalDiary/new_diary.html'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class DetailDiaryView(DetailView):
    model=Diary


class UpdateDiaryView(UpdateView):
    model=Diary
    fields='__all__'
    # success_url=reverse_lazy('detail-diary')

class DeleteDairyView(DeleteView):
    model=Diary
    success_url=reverse_lazy('personalDiary:home')
    
