from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.HomeListView.as_view(), name='home-list'),

]
