from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import DiaryForm
from .models import Diary

APP_NAME = "personalDiary"
def set_template_name(template_name):
    return f"{APP_NAME}/{template_name}"

def home(request):
    diaries=Diary.objects.all()
    return render(request, set_template_name('home.html'), {'diaries': diaries})



class AddDiaryView(FormView):
    form_class=DiaryForm
    # print(reverse('new-diary')) #! here a lesson you have learn from it, use lazy_reverse instead reverse
    template_name='personalDiary/new_diary.html'
    success_url=reverse_lazy('home')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)