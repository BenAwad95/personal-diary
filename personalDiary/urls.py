from django.urls import path
from .views import home, AddDiaryView

urlpatterns = [
    path('', home, name='home'),
    path('new-diary/', AddDiaryView.as_view(), name='new-diary')
]
