from django.urls import path
from . import views
urlpatterns = [
    path('',views.indexvista,name="indexvista"),
    
]