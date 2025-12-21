from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    message = serializers.CharField(
        max_length=500,
        required=True,
        help_text="متن پیام شما (حداکثر ۵۰۰ کاراکتر)"
    )

    def validate_message(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("پیام نمی‌تواند خالی باشد")
        if len(value.strip()) < 2:
            raise serializers.ValidationError("پیام باید حداقل ۲ کاراکتر باشد")
        return value.strip()


class MessageResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    received_message = serializers.CharField()
    message_length = serializers.IntegerField()
    response = serializers.CharField()
    timestamp = serializers.DateTimeField()