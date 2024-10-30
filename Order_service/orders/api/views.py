from orders.models import Order
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from orders.services import OrderService
from orders.api.serializers import (
    OrderSerializerForCreate,
    OrderSerializer,
)

class OrderViewSet(viewsets.GenericViewSet,
                   viewsets.mixins.ListModelMixin,
                   viewsets.mixins.CreateModelMixin):

    serializer_class = OrderSerializerForCreate
    queryset = Order.objects.all()
    def get_permissions(self):
        return [AllowAny()]

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializerForCreate(data=request.data)
        if not serializer.is_valid():
            return Response(
                {'errors' : serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def list(self, request, *args, **kwargs):
        query_params = request.query_params
        if ('order_id' in query_params):
            queryset = Order.objects.filter(order_id=query_params['order_id'])
            return Response(
                OrderSerializer(queryset, many=True).data,
                status=status.HTTP_200_OK
            )
        if ('user_id' in query_params):
            queryset = Order.objects.filter(user_id=query_params['user_id']).order_by('-order_id')
            return Response(
                OrderSerializer(queryset, many=True).data,
                status=status.HTTP_200_OK
            )
        if ('restaurant_name' in query_params):
            queryset = Order.objects.filter(restaurant_name=query_params['restaurant_name']).order_by('-order_id')
            return Response(
                OrderSerializer(queryset, many=True).data,
                status=status.HTTP_200_OK
            )

        return Response(
            OrderSerializer(self.get_queryset(), many=True).data,
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'])
    def restaurant_orders(self, request):
        if 'restaurant_name' not in request.query_params:
            return Response(
                {'error: restaurant_name missing'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if 'created_at' not in request.query_params:
            queryset = Order.objects.filter(restaurant_name=request.query_params['restaurant_name'])
            return Response(
                OrderSerializer(queryset, many=True).data,
                status=status.HTTP_200_OK
            )
        else:
            queryset = Order.objects.filter(
                restaurant_name=request.query_params['restaurant_name'],
                created_at__date=OrderService.parse_time(request.query_params['created_at'])
            )
            return Response(
                OrderSerializer(queryset, many=True).data,
                status=status.HTTP_200_OK
            )

    @action(detail=False, methods=['GET'])
    def user_orders(self, request):
        if 'user_id' not in request.query_params:
            return Response(
                {'error: user_id missing'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if 'created_at' not in request.query_params:
            if ('order_id' not in request.query_params):
                queryset = Order.objects.filter(user_id=request.query_params['user_id'])
            else:
                queryset = Order.objects.filter(
                    user_id=request.query_params['user_id'],
                    order_id=request.query_params['order_id'],
                )
            return Response(
                OrderSerializer(queryset, many=True).data,
                status=status.HTTP_200_OK
            )
        else:
            queryset = Order.objects.filter(
                user_id=request.query_params['user_id'],
                created_at__date=OrderService.parse_time(request.query_params['created_at'])
            )
            return Response(
                OrderSerializer(queryset, many=True).data,
                status=status.HTTP_200_OK
            )