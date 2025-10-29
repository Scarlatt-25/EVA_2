from django.urls import path
from . import views

app_name = 'contactos'

urlpatterns = [
    path('', views.ContactoListView.as_view(), name='lista'),
    path('crear/', views.ContactoCreateView.as_view(), name='crear'),
    path('editar/<int:pk>/', views.ContactoUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', views.ContactoDeleteView.as_view(), name='eliminar'),
]
