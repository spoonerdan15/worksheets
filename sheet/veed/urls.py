from django.urls import path
from . import views

app_name = 'veed'

urlpatterns = [
    # post views
    # url(r'^$', views.post_list, name='post_list'),
    path('', views.check),
]