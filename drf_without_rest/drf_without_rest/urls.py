from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<int:id>', views.EmployeeDataCBV.as_view()),
    path('api/', views.EmployeeListCBV.as_view()),
]
