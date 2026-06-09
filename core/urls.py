from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('employee/add/', views.employee_add, name='employee_add'),
    path('employee/edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('employee/delete/<int:pk>/', views.employee_delete, name='employee_delete'),
]