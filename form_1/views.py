# form_1/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Dish
from .serializers import CategorySerializer, CreateOrderSerializer


@api_view(['GET'])
def menu_list(request):
    # 获取所有可售菜品
    dishes = Dish.objects.filter(is_available=True).select_related('category')

    # 按分类分组
    menu = {}
    for dish in dishes:
        cat_name = dish.category.name
        if cat_name not in menu:
            menu[cat_name] = []
        menu[cat_name].append({
            'id': dish.id,
            'name': dish.name,
            'price': str(dish.price),
            'description': dish.description,
            'image': dish.image.url if dish.image else None
        })

    return Response(list(menu.values()))

@api_view(['POST'])
def create_order(request):
    serializer = CreateOrderSerializer(data=request.data)
    if serializer.is_valid():
        customer_name = serializer.validated_data['customer_name']
        customer, _ = Customer.objects.get_or_create(name=customer_name)

        order = Order.objects.create(customer=customer)
        for item in serializer.validated_data['items']:
            OrderItem.objects.create(
                order=order,
                dish_id=item['dish_id'],
                quantity=item['quantity']
            )
        return Response({'order_id': order.id, 'customer_name': customer.name})
    return Response(serializer.errors, status=400)