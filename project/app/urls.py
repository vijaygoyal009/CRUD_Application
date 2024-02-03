from django.urls import path
from app import views
urlpatterns = [
    path('',views.adddata,name='add'),
    path('show/',views.showdata,name='showdata'),
    path('delete/<int:id>/',views.deletedata, name='deletedata'),
    path('<int:id>/',views.updatedata,name='updatedata'),
]
