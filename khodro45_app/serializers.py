from rest_framework import serializers
from User.models import Bider
from khodro45_app.models import Auction, Brand, Bid


class BrandListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='brand-detail', format=None)

    class Meta:
        model = Brand
        fields = ['id', 'title', 'created_time', 'url']

    def to_internal_value(self, data):
        title = data.get('title')
        if len(title) > 10:
            raise serializers.ValidationError({
                'title': 'May not be more than 10 characters.'})
        return {'title': title}


class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


serializer = BrandDetailSerializer()
print(repr(serializer))


class BrandUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['title', 'created_time']
        extra_kwargs = {
            'created_time': {'read_only': True}
        }


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['bider'] = instance.bider.username

        return representation


class AuctionSerializers(serializers.ModelSerializer):
    # bidder = serializers.SerializerMethodField()

    class Meta:
        model = Auction
        fields = '__all__'
        validators = []

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        bidder = Bid.objects.filter(auction=instance.id)
        bid_serilizare = BidSerializer(bidder, many=True)
        representation['bider'] = bid_serilizare.data
        return representation

    def validate(self, data):

        start_price = data.get('start_price')
        if int(start_price) <= 50:
            raise serializers.ValidationError('The price must be more than 50')

        return super().validate(data)



