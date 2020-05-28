from django.urls import path
from accounts.views import loginPage, logoutUser

urlpatterns = [
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('', loginPage),
]
