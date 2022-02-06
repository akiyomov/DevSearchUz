from django.urls import path 
from . import views
from .views import profiles,userProfile,registerUser,logoutUser,loginUser


urlpatterns = [
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', registerUser, name="register"),
    
    path('',profiles, name="profiles"),
    path('profile/<str:pk>/',userProfile,name="user-profile"),
    path('account/',views.userAccount,name="account"),
    path('edit-account/',views.editAccount,name="edit-account"),
    path('skill_form/',views.createSkill,name="skill_form"),
    path('update-skill/<str:pk>',views.updateSkill,name="update-skill"),
    path('delete-skill/<str:pk>',views.deleteSkill,name="delete-skill"),
    path('inbox/',views.inbox , name="inbox"),
    path('message/<str:pk>',views.viewMessage , name="message"),
    path('send-message/<str:pk>/',views.createMessage , name="create-message"),
]