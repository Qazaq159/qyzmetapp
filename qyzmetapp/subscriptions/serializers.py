from rest_framework import serializers
from .models import Subscription, SubscriptionType

class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = ['id', 'name', 'price', 'duration', 'description', 'features']


class SubscriptionSerializer(serializers.ModelSerializer):
    subscription_type = SubscriptionTypeSerializer()

    class Meta:
        model = Subscription
        fields = ['id', 'subscription_type', 'expires_at', 'is_active']
