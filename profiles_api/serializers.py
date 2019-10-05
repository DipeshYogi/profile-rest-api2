from rest_framework import serializers
from .models import UserProfile

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing API View"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id','name','email','password')

        #customize fields
        extra_kwargs = {
            'password':{'write_only':True, #password on write..no display
                        'style':{'input_type':'password'} #to make password as dots while writing
                        }

                        }

        """By default the model serializer allows us to create objects in database using create() fn
           We want to overriide this fn with create_user() so that our passwords are hashed"""

        def create(self,validated_data):
            user = UserProfile.objects.create_user(
                    email = validated_data['email'],
                    name = validated_data['name'],
                    password = validated_date['password']

            )

            return user
