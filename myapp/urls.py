from django.contrib import admin
from django.urls import path
from.import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index,name='index'),
    path('add/', views.add,name='add'),
    path('addrec/', views.addrec,name='addrec'),
    path('delete/<int:id>/', views.delete,name='delete')

]

