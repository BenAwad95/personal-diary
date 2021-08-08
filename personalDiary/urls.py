from django.urls import path
from .views import DeleteDairyView, home, AddDiaryView, UpdateDiaryView, DetailDiaryView, DeleteDairyView

urlpatterns = [
    path('', home, name='home'),
    path('diary/<int:pk>/', DetailDiaryView.as_view(), name='detail-diary'),
    path('new-diary/', AddDiaryView.as_view(), name='new-diary'),
    path('diary/<int:pk>/update', UpdateDiaryView.as_view(), name='update-diary'),
    path('diary/<int:pk>/delete', DeleteDairyView.as_view(), name='delete-diary')
]
