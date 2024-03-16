from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", views.emp_data_view),
    path("apijson/", views.json_data_view),
    path("apijson02/", views.json_data_view_02),
    path("apijsoncbv/", views.jsonCBV.as_view()),
    
]
