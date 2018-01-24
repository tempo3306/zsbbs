from django.conf.urls import include,url
from authapp import views as auth_view
urlpatterns = [
    url('^register$',auth_view.register,name="register"),
    url('^login$',auth_view.login,name="login"),
    url('^logout$',auth_view.logout,name="logout"),
]