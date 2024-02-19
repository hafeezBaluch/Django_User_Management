from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home_page'),
    path('login/', views.user_login, name='login'),
    path('register/',views.user_registration,name='register'),
    path('logout/',views.user_logout,name='logout'),
    
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
