from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only = True)
    
    class Meta:
        model = User
        fields = '__all__'
        
    def validate(self,data):
        if data['password'] != data['password_confirm']:
            raise ValueError("Password doesn't match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user