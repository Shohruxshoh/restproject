from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


# @api_view(['GET'])
# def api_home(request, *args, **kwargs):


#     if request.method != 'POST':
#         return Response({"detail": 'GET not allowed'}, status=405)
#     data = request.data

#     instance = Product.objects.all().order_by("?").last()
#     data = {}
#     if instance:
#         data = model_to_dict(instance)
#         data = ProductSerializer(instance).data
#     return Response(data)

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
