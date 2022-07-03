from django.urls import path
from . import views

app_name = "kbm"
urlpatterns = [
    path('info/', views.info, name="info"),
    path('books/', views.books, name="books"),
    path('book1/', views.book1, name="book1"),
    path('book2/', views.book2, name="book2"),
    path('book3/', views.book3, name="book3"),

]