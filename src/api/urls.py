from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('status/', views.status, name='status'),

    path('users/', views.user_list, name='user-list'),
    path('user-create/', views.user_create, name='user-create'),
    path('user-update/<int:pk>/', views.user_update, name='user-update'),
    path('user-delete/<int:pk>/', views.user_delete, name='user-delete'),

    path('transaction-add/', views.transaction_add, name='transaction-add'),
    path('report/<str:name>', views.get_report, name='report')
]
