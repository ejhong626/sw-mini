from rest_framework import serializers
from barcodes.models import Barcode, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class BarcodeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='barcode-highlight', format='html')

    class Meta:
        model = Barcode
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    barcodes = serializers.HyperlinkedRelatedField(many=True, view_name='barcode-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'barcodes']
