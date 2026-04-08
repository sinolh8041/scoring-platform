from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='scoring_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('setup/', views.setup_event, name='setup_event'),
    path('events/', views.event_list, name='event_list'),
    path('dashboard/<int:event_id>/', views.event_dashboard, name='event_dashboard'),
    path('score/<int:event_id>/', views.enter_passcode, name='enter_passcode'),
    path('scoring/<uuid:token>/', views.scoring_matrix, name='scoring_matrix'),
    path('results/<int:event_id>/', views.event_results, name='event_results'),
    path('results/<int:event_id>/export/', views.export_results_excel, name='export_results_excel'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
]
