from django.urls import path

from . import views


app_name = 'home'

urlpatterns = [
    path('', views.title, name='title' ),
    path('qr_code', views.home, name='home'),

    path('att_list/<slug:dr_name>/<slug:att_name>/', views.attendance_list, name='attendance_list'),
    path('att_login/<slug:dr_name>/<slug:att_name>/', views.attendance_login, name='attendance_login'),
    path('att_submit/<int:dr_id>/<int:qrcodeid>/', views.attendance_submit, name='attendance_submit'),
    
    path('leave_list/<slug:dr_name>/<slug:leave_name>/', views.leave_list, name='leave_list'),
    path('leave_login/<slug:dr_name>/<slug:leave_name>/', views.leave_login, name='leave_login'),
    path('leave_submit/<int:leavedr_id>/<int:leaveqrcodeid>/', views.leave_submit_new, name='leave_submit_new'),
]
