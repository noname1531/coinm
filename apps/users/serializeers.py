from rest_framework import serializers

from apps.users.models import Users

class UsersnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username']

class UserSserializer(serializers.ModelSerializer):
    class Meta:
        model = Users   
        fielde = ['id', 'username', 'phone', 'age', 'direction']

class UsersRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=8, write_only=True)
    confirm_password = serializers.CharField(max_length=8, write_only=True)

    class Meta:
        model = Users
        fielde = ['id', 'username', 'phone', 'age', 'direction',  'password', 'confirm_password']


        def validate(self, attrs):
            if attrs['password']!= attrs['confirm_password']:
                raise serializers.ValidationError({'confirm_password': 'Пароли отличаются'})
            elif '+996' not in attrs['phone']:
                raise serializers.ValidationError({'phone': 'Телефон должен начинаться с +996'})
            elif len(attrs['password']) < 8 and len(attrs['confirm_-password']) < 8:
                raise serializers.ValidationError({'password_len': 'Пароль должен содержать не менее 8 символов'})
            return attrs    
        
        def create(self, validated_data):
            user = Users.objects.create(
                username = validated_data['username'],
                phone = validated_data['phone'],
                age = validated_data['age'],
                direction = validated_data['direction'],
                password = validated_data['password'],
            )
            user.set_password(validated_data['password'])
            user.save()
            return user