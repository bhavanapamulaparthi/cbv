from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.CBView.as_view()),
    path('', views.IndexView.as_view())

]