from rest_framework import serializers

from user.models import User, Page, Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class TagSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Tag
        fields = ('id', 'name')


class PageSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(default=serializers.CurrentUserDefault())
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Page
        fields = ['name', 'uuid', 'description', 'tags', 'owner']
