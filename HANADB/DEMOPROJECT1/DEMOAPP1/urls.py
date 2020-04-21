from django.urls import path
from . import views


urlpatterns = [
    #path('', views.hi,name='HOMEPAGE'),
    path('details/<int:id>', views.details,name='QUERYRESULT1'),
    path('refresh/<int:id>', views.refresh,name='REFRESH'),
    path('graphs/<int:id>', views.graphs,name='GRAPHS'),
    #path('submit', views.submit,name='QUERYRESULT'),
    path('submit2', views.submit2, name='QUERYRESULT11'),
    path('', views.insi,name='Insight'),

]