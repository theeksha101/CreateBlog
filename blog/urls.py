from django.urls import path
from . import views  # importing all views from blog

# assigning a view called post_list to the root url
# The last part, name='post_list', is the name of the URL that will be used to identify the view
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
