from django.conf.urls import url, include

from. import views 
urlpatterns = [
	url(r'^^pacientes/', views.lista_pacientes, name= "lista_pacientes" ),
]
'''url(r'^^citas/', views.lista_citas, name= "lista_citas" ),'''