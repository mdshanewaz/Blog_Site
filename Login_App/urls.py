from django.urls import path
from Login_App import views


app_name = "Login_App"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout')
]