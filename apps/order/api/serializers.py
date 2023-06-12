from rest_framework import serializers
from ..models import Bron
from account.models import User


class BronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bron
        fields = ('arena', 'start_time', 'end_time', 'pre_pay')


class UserInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class BronListSerializer(serializers.ModelSerializer):
    user = UserInfoSerializers(many=False)
    remain_pay = serializers.SerializerMethodField()

    class Meta:
        model = Bron
        fields = ('user', 'arena', 'start_time', 'end_time', 'pre_pay', 'pay', 'remain_pay')

    def get_remain_pay(self, obj):
        if obj.pay:
            return obj.pay - obj.pre_pay
