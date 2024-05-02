
from django.urls import path
from relativeap import views

app_name = 'relativeap'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login,name='user_login')
]