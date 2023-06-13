from rest_framework import serializers
from ..models import Arena, Images
from apps.order.models import Bron
import datetime


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('image',)


class ArenaSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, required=False)
    recommendation_start_time = serializers.SerializerMethodField(required=False)
    all_sum = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Arena
        fields = ('name', 'phone', 'address', 'mode_start', 'mode_end',
                  'latitude', 'longitude', 'status', 'price_hour', 'min_pre_hour', 'images', 'recommendation_start_time', 'all_sum')

    def get_recommendation_start_time(self, obj):
        request = self.context.get("request")
        start_time = request.query_params.get('start_time')
        start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M') if start_time else None
        if start_time:
            bron_arena = Bron.objects.filter(arena=obj, start_time__gte=start_time).order_by('start_time').first()
            if bron_arena:
                return f"{bron_arena.end_time.time()} dan boshlashingiz mumkin."
        return f"{start_time.time()} dan boshlashingiz mumkin."

    def get_all_sum(self, obj):
        request = self.context.get("request")
        start_time = request.query_params.get('start_time')
        end_time = request.query_params.get('end_time')
        start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M') if start_time else None
        end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M') if end_time else None
        if start_time:
            diff_in_hours = (end_time-start_time).total_seconds() / 3600
            return diff_in_hours*obj.price_hour




