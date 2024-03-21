from django.urls import path
from . import views  # we just importd views.py file that is in the myapp(this) folder


urlpatterns=[
    path('',views.index,name='index'),
    ##'' means root url, for e.g. www.nikunj.com
    ## if we have '/download' then it means www.nikunj.com/download

    ##when a user comes to this url, then index function will run that is in views files, name is just an id

    path('counter',views.counter,name='counter'),
    path('register',views.register,name='register'),
    path('login',views.login,name="login")
    ]