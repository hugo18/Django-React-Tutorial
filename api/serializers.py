from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password':{'write_only':True}} 
    
    def create(self, valideted_data):
        user = User.objects.create_user(**valideted_data)
        return user
    