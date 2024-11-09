from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginater"),
    path('author/detail/<int:id>/', views.author_detail, name='author_detail'),
    path('create-author/', views.create_author, name='create_author'),
    path('add/', views.add_quote, name='add_quote'),
]