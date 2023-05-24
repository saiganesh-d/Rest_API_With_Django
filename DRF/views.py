from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from .serializers import Productserializers

from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET','POST'])
def api_home(request, *args, **kwargs):
    if request.method == 'GET':

        Inst = Product.objects.all().filter(id =4)
        data = {}
        if Inst:
            for i in Inst:
                print(i)
                data.update(Productserializers(i).data)
        return Response(data)
    else:
        serializer = Productserializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response({"invalid":"not good data"},status=400)

