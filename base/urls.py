from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints, name='endpoints'),
    path('advocates/', views.advocates_list, name='advocates'),
    path('advocates/<str:username>', views.advocates_detail, name='advocates_detail'),
]
