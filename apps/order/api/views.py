from rest_framework import viewsets, permissions
from ..models import Bron
from .serializers import BronSerializer, BronListSerializer
from rest_framework.generics import ListAPIView
from apps.arena.models import Arena
from account.base_permission import *


class BronViewSet(viewsets.ModelViewSet):
    queryset = Bron.objects.all()
    serializer_class = BronSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BronListView(ListAPIView):
    permission_classes = [IsClientOrOwner, permissions.IsAuthenticated]
    serializer_class = BronListSerializer

    def get_queryset(self):
        return Bron.objects.filter(status=True, arena__in=Arena.objects.filter(owner=self.request.user))