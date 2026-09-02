from django.urls import path
from .views import home, menu, order, about
urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('order/', order, name='order'),
    path('about/', about, name='about'),
]
