from django.urls import path

from User import apis

urlpatterns = {
        path('register/', apis.register),
        path('login/', apis.login),
        path('vcode/fetch/',apis.vcode_fetch)
}
