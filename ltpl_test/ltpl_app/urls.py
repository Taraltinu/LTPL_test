from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from ltpl_app.views import OrderView,ProductView
from django.urls import path,include

router = DefaultRouter()
router.register("order",OrderView)
router.register(r"product",ProductView,basename="product")

urlpatterns = [
   path('', include(router.urls)),
]