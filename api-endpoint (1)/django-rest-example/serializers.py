from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=1000, required=True)
    
    def validate_message(self, value):
        if not value.strip():
            raise serializers.ValidationError("پیام نمی‌تواند خالی باشد")
        return value

class MessageResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    received_message = serializers.CharField()
    response = serializers.CharField()
    message_length = serializers.IntegerField()
