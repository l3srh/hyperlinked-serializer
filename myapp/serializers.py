from rest_framework import serializers
from myapp.models import Person,Color

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    color2 = serializers.HyperlinkedRelatedField(
            queryset = Color.objects.all(), 
            view_name ='color-detail'
        )
    class Meta:
        model = Person
        fields = '__all__'

class ColorSerializer(serializers.HyperlinkedModelSerializer):
    color = serializers.HyperlinkedRelatedField( 
            view_name ='person-detail'
        )
    class Meta:
        model = Color
        fields = '__all__'