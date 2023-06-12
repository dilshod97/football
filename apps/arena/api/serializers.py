from rest_framework import serializers
from ..models import Arena, Images
import datetime


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('image',)


class ArenaSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, required=False)
    recommendation_start_time = serializers.SerializerMethodField()
    all_sum = serializers.SerializerMethodField()

    class Meta:
        model = Arena
        fields = ('name', 'phone', 'address', 'mode_start', 'mode_end',
                  'latitude', 'longitude', 'status', 'price_hour', 'min_pre_hour', 'images', 'recommendation', 'all_sum')

    def get_recommendation_start_time(self, obj):
        request = self.context.get("request")
        start_time = request.query_params.get('start_time')
        start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M') if start_time else None

        return '1soat'

    def get_all_sum(self, obj):
        request = self.context.get("request")

        start_time = request.query_params.get('start_time')
        end_time = request.query_params.get('end_time')
        start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M') if start_time else None
        end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M') if end_time else None

        diff_in_hours = (end_time-start_time).total_seconds() / 3600
        return diff_in_hours*obj.price_hour




