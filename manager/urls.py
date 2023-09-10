from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('student/', views.StudentDashboard, name='student'),
    path('staff-login/', views.StaffLogin, name='staff-login'),
    path('staff/', views.Staff, name='staff'),
    path('student-detail/', views.StudentDetail, name='student-detail'),
    path('project/', views.Projects, name='project')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
