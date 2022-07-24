from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('signin/',views.signin,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('forgetpassword/',views.forgetpassword,name='forgetpass'),
    path('resetpassword/<token>',views.resetpassword,name="resetpass"),
    path('dashboard/',views.dashboard),
    path('logout/',views.user_logout,name="logout"),
]