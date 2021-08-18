from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, ListView

from .forms import DiaryForm
from .models import Diary

APP_NAME = "personalDiary"
def set_template_name(template_name):
    return f"{APP_NAME}/{template_name}"


class ListDiaryView(ListView):
    model=Diary


    def get_queryset(self):
        user = self.request.user
        return Diary.objects.filter(user=user).all()

class AddDiaryView(FormView):
    form_class=DiaryForm
    # print(reverse('new-diary')) #! here a lesson you have learn from it, use lazy_reverse instead reverse
    template_name='personalDiary/new_diary.html'
    success_url=reverse_lazy('home')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DetailDiaryView(DetailView):
    model=Diary


class UpdateDiaryView(UpdateView):
    model=Diary
    fields='__all__'
    # success_url=reverse_lazy('detail-diary')

class DeleteDairyView(DeleteView):
    model=Diary
    success_url=reverse_lazy('home')
    
