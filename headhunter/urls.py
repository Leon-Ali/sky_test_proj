from django.urls import path

from . import views

urlpatterns = [
    path('resume/', views.ResumeListView.as_view(), name='resume'),
    path('resume/<int:pk>/', views.ResumeUpdateView.as_view(), name='resume_update'),
]
