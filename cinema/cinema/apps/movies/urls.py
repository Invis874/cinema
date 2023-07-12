from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('reservation/<int:s_id>/<int:m_id>/', views.reservation, name = 'reservation')
]