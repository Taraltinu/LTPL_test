from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from ltpl_accounts.views import UserView

router = DefaultRouter(trailing_slash=False)
router.register(r"user",UserView,basename="user")
urlpatterns = [
   
]+router.urls