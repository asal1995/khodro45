from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import UpdateModelMixin, ListModelMixin

from khodro45_app.filter import BrandFilterSet
from khodro45_app.models import Auction, Brand
from khodro45_app.serializers import BrandListSerializer, BrandDetailSerializer, BrandUpdateSerializer, \
    AuctionSerializers


class BrandViewSet(UpdateModelMixin, GenericViewSet):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BrandFilterSet
    search_fields = ['title']
    ordering_fields = ['title']

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True,)
        print(type(self.get_serializer))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = BrandDetailSerializer(item)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = BrandUpdateSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        super().update()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuctionView(ListModelMixin, GenericViewSet):
    serializer_class = AuctionSerializers
    queryset = Auction.objects.all()

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        print(type(self.get_serializer))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
