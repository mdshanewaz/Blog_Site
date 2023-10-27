from django.urls import path
from Login_App import views

app_name = "Login_App"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.user_change, name='user_change'),
    path('password/', views.pass_change, name='pass_change'),
    path('add-pricture/', views.add_profile_pic, name='add_profile_pic'),
     path('change-pricture/', views.change_profile_pic, name='change_profile_pic'),
]