from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account.views import UserViewSet
from apps.arena.api.views import ArenaViewSet, ArenaListView
from apps.order.api.views import BronViewSet, BronListView

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('arenas', ArenaViewSet, basename='arena')
router.register('bron', BronViewSet, basename='bron')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/arena-list/', ArenaListView.as_view()),
    path('v1/bron-list/', BronListView.as_view())
]
