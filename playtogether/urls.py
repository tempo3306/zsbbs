from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from playtogether import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'billiarduser', views.BilliardsUserViewSet)
router.register(r'billiardinvite', views.BilliardsInviteViewSet)
router.register(r'billiardjoin', views.BilliardsJoinViewSet)
router.register(r'playtogether', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.

urlpatterns = [
    url(r'^', include(router.urls)),
]