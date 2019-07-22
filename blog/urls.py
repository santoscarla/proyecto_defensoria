from django.urls import path, include
from django.conf.urls import url
from . import views
from blog.views import prueba, principal, defensoria, quedicelaaudiencia, comunicate, interes, normatividad

#app_name = 'defensoria'

urlpatterns = [
	#$url(r'^', views.principal, name='principal'),
    
    path('principal/', views.principal, name='principal'),
    path('prueba/', views.prueba, name='prueba'),
  	path('defensora/', views.defensora, name='defensora'),
  	path('defensoria/', views.defensoria, name='defensoria'),
    path('derechos/', views.derechos, name='derechos'),
    path('quedicelaaudiencia/', views.quedicelaaudiencia, name='quedicelaaudiencia'),
 	path('comunicate/', views.comunicate, name='comunicate'),
 	path('interes/', views.interes, name='interes'),
 	path('normatividad/', views.normatividad, name='normatividad'),
 	
]