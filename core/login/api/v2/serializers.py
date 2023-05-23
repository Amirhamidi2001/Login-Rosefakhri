from rest_framework import serializers

from ...models import LoginMessages


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginMessages
        fields = ["id", "username", "password", "title", "support", "degree", "file_field", "description"]
