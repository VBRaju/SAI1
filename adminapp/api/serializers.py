from rest_framework import serializers
from adminapp.models import About_Us, Team_Members

''''''

# About serializer

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Us
        fields =[
            'id',
            'user',
            'title',
            'content',
        ]

    
    def validate(self, data):
        content = data.get('content', None)
        if content == "":
            content = None
        title = data.get('title',None)
        if content is None and title is None:
            raise serializers.ValidationError('Content and title is required')
        return data


# Team serializer
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_Members
        fields =[
            'id',
            'user',
            'name',
            'image',
            'designation',
        ]

    
    def validate(self, data):
        name = data.get('name', None)
        if name == "":
            name = None
        designation = data.get('designation', None)
        if designation == "":
            designation = None
        image = data.get('image',None)
        if name is None and designation is None and image is None:
            raise serializers.ValidationError('Name or image or designation is required')
        return data