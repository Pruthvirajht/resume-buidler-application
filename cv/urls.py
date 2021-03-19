from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.log_in,name='login'),
    path('signup/',views.signup,name='signup'),
    path('userdetails/',views.userdetail,name='userdetail'),
    path('logout/',views.log_out,name='logout'),
    path('addprofile/',views.add_persnl,name='addpersnl'),
    path('editprofile/',views.edit_prsnl,name='editpersnl'),
    path('addeducation/',views.add_edu,name='addeducation'),
    path('editedu/<int:pk>/',views.edit_edu,name='editeducation'),
    path('addexperience/',views.add_experience,name='addexperience'),
    path('editexperience/<int:pk>/',views.edit_experience,name='editexperience'),
    path('addskill/',views.add_skill,name='addskill'),
    path('edit_skill/<int:pk>/',views.edit_skill,name='editskill'),
    path('selectresume/', views.selectresume, name='selectresume'),
    path('restemp/', views.restemp, name='restemp'),

]
