from django.urls import path
from . import views  # we just importd views.py file that is in the myapp(this) folder


urlpatterns=[
    path('',view.index,name=index)
    ##'' means root url, for e.g. www.nikunj.com
    ## if we have '/download' then it means www.nikunj.com/download
    ]