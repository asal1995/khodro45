
from rest_framework import serializers
from khodro45_app.models import Brand

class BrandListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='brand-detail', format=None)

    class Meta:
        model = Brand
        fields = ['id','title','created_time','url']  
    

class BrandDetailtSerializer(serializers.ModelSerializer):
 

    class Meta:
        model = Brand
        fields = "__all__"


class BrandUpadateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = ['title', 'created_time']
        extra_kwargs = {
            'created_time':{ 'read_only' : True}
        }


