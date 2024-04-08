from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from .serializers import AdvocateSerializer
from .models import Advocate
# Create your views here.
# GET /advocates
# POST /advoctes

# GET /advocates/:id
# PUT /advocates/:id
# DELETE /advocates/:id

@api_view(["GET"])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(["GET", "POST"])
def advocates_list(request):
    # Handles GET requests
    if request.method == 'GET':
        query = request.GET.get('query')
        
        if query == None:
            query = ''
            
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        advocate = Advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
        )
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

@api_view(["GET", "PUT", "DELETE"])
def advocates_detail(request, username):
    advocate = Advocate.objects.get(username__iexact=username)

    if request.method == 'GET':
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        
        advocate.save()
        
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        advocate.delete()
        return Response('user was deleted!')