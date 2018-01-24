from rest_framework import serializers
from playtogether.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from playtogether.models import BilliardsUser,BilliardsInvite,BilliardsJoin

class playtogethererializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')

class BilliardsUserSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = BilliardsUser
        fields = ( 'id', 'email', 'telephone','owner','highlight',
                  'created', 'level', 'location', 'user', 'signature','headshow')

class BilliardsInviteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = BilliardsInvite
        fields = ( 'id','owner','highlight', 'created', 'play_time',
                  'play_loaction', 'play_type', 'description',
                   'total_number', 'currentuser_number',
                   'create_user',)

class BilliardsJoinSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = BilliardsJoin
        fields = ( 'id','owner','highlight','invite','user')

from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    playtogether = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'playtogether')

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
