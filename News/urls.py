from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('businessNews/',views.businessNews,name="businessNews"),
    path('scienceNews/',views.scienceNews,name="scienceNews"),
    path('healthNews/',views.healthNews,name="healthNews"),
    path('technologyNews/',views.technologyNews,name="technologyNews"),
    path('entertainmentNews/',views.entertainmentNews,name="entertainmentNews"),
    path('sportsNews/',views.sportsNews,name="sportsNews"),
]