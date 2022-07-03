from django.urls import path
from . import views

app_name = "board"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('detail/<bpk>', views.detail, name="detail"),
    path('delete/<bpk>', views.delete, name="delete"),
    path('create/', views.create, name="create"),
    path('update/<bpk>', views.update, name="update"),
    path('write/<bpk>', views.write, name="write"),
    path('dreply/<bpk>/<rpk>', views.dreply, name="dreply"),

]