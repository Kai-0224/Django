from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/update/<int:grid_id>/', views.update_grid, name='update_grid'),
    path('save/', views.save_grid, name='save_grid'),
    path('api/delete/<int:grid_id>/', views.delete_grid, name='delete_grid'),
]

