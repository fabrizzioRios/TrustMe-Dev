from rest_framework.serializers import ModelSerializer
from trustme_test.models import Opinion, Page, User


class OpinionSerializer(ModelSerializer):
    class Meta:
        model = Opinion
        fields = '__all__'


class PageSerializer(ModelSerializer):
    opinions = OpinionSerializer(many=True, required=False)

    class Meta:
        model = Page
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        opinions = Opinion.objects.filter(user__opinion__page_id=instance.id)
        serialized_opinions = OpinionSerializer(opinions, many=True).data
        data['opinions'] = serialized_opinions
        return data


class UserSerializer(ModelSerializer):
    opinions = OpinionSerializer(many=True, required=False)

    class Meta:
        model = User
        exclude = ('last_login',)


class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class LoginResponseSerializer(ModelSerializer):
    pages = PageSerializer(many=True)

    class Meta:
        model = User
        exclude = ('password', 'last_login')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        pages_query = Page.objects.filter(created_by=instance)
        serialized_pages = PageSerializer(pages_query, many=True).data
        data['pages'] = serialized_pages
        return data
