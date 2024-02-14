from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),  # Add this line
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    

]