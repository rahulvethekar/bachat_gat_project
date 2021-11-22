from django.urls import path
from .views import registrationForm,verifyEmail,otpVerify,login,logout,changePassword
urlpatterns = [
    path('registration/',registrationForm,name = 'register'),
    path('verifyEmail/',verifyEmail,name = 'verifyEmail'),
    path('verifyOtp/',otpVerify,name = 'verifyOtp'),
    path('login/',login,name = 'login'),
    path('logout/',logout,name = 'logout'),
    path('changePassword/',changePassword,name = 'changePassword'),
]