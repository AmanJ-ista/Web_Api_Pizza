from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import pizzaSerializers

@api_view(['GET'])
def list1(request):
    pizza1=Pizza.objects.all()
    serialiser=pizzaSerializers(pizza1,many=True)
    return Response(serialiser.data)  

@api_view(['GET'])
def detail(request,pk):
    if pk in ['Regular','Square','regular','square']:
        pizza1=Pizza.objects.filter(Pizza_Type=pk)
    else:
        pizza1=Pizza.objects.filter(Pizza_Size=pk)    
    serialiser=pizzaSerializers(pizza1,many=True)
    return Response(serialiser.data)

@api_view(['POST'])
def create(request):
    serializer=pizzaSerializers(data=request.data)

    if serializer.is_valid():
        if request.data['Pizza_Type']=='Regular' or request.data['Pizza_Type']=='Square':
            if request.data['Pizza_Size'] in Pizza.objects.filter(Pizza_Size=request.data['Pizza_Size']):
                serializer.save()


    return Response(serializer.data)        


@api_view(['POST'])
def update(request,pk):

    pizza1=Pizza.objects.get(id=pk)
    serializer=pizzaSerializers(instance=pizza1,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)        


@api_view(['DELETE'])
def delete(request,pk):

    pizza1=Pizza.objects.get(id=pk)
    pizza1.delete()
    return Response('Item successfully deleted')  
              
