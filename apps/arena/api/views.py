from rest_framework import viewsets, permissions
from ..models import Arena
from .serializers import ArenaSerializer
from rest_framework.generics import ListAPIView
from datetime import datetime
from account.base_permission import *
from django.db.models import F, Q, Max


class ArenaViewSet(viewsets.ModelViewSet):
    queryset = Arena.objects.all()
    serializer_class = ArenaSerializer
    permission_classes = [IsClientOrOwner, permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


class ArenaListView(ListAPIView):
    serializer_class = ArenaSerializer

    def get_queryset(self):
        latitude = self.request.query_params.get('latitude')
        longitude = self.request.query_params.get('longitude')
        start_time = self.request.query_params.get('start_time')
        end_time = self.request.query_params.get('end_time')
        show_more = self.request.query_params.get('show_more')
        current_time = datetime.now()
        start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M') if start_time else None
        end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M') if end_time else None

        arenas = Arena.objects.filter(mode_start__lte=current_time.time(), mode_end__gte=current_time.time())
        if start_time and end_time:
            arenas = arenas.exclude(
                bron__end_time__gte=start_time, bron__status=True
            )

        if latitude and longitude:
            arenas = arenas.annotate(
                distance=((F('latitude') - float(latitude)) ** 2 + (F('longitude') - float(longitude)) ** 2) ** 0.5
            ).order_by('distance')

        if show_more:
            arenas = Arena.objects.all()

        arenas = arenas.annotate(
            latest_bron_end_time=Max('bron__end_time')
        ).order_by('latest_bron_end_time')

        return arenas

    def get_serializer_context(self):
        return {"request": self.request}
