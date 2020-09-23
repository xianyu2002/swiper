from django.urls import path

from User import views

urlpatterns = {
        path('register/', views.register),
        path('login/', views.login)
}
