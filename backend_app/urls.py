from django.urls import path
from .views import *

urlpatterns =[
    path('',home_page),
    path('form/',form_page),
    path('view/',view_page),
    path('delete/<int:id>',delete_data,name="student_delete"),
    path('update/<int:id>',update_data,name="student_update"),
    path('http',http)
]
