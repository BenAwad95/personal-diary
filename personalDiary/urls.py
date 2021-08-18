from django.urls import path
from .views import DeleteDairyView, ListDiaryView, CreateDiaryView, UpdateDiaryView, DetailDiaryView, DeleteDairyView

app_name='personalDiary'
urlpatterns = [
    path('', ListDiaryView.as_view(), name='home'),
    path('<int:pk>/', DetailDiaryView.as_view(), name='detail-diary'),
    path('new-diary/', CreateDiaryView.as_view(), name='new-diary'),
    path('<int:pk>/update', UpdateDiaryView.as_view(), name='update-diary'),
    path('<int:pk>/delete', DeleteDairyView.as_view(), name='delete-diary')
]
