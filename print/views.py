from rest_framework import status
from rest_framework.decorators import api_view
from print.models import *
from print.serializers import *
from django.shortcuts import render


@api_view(['POST'])
def amiibo_print(request):   
    if request.method == 'POST':
        amiibo = AmiiboSerializer(data=request.data)
        if amiibo.is_valid():
            return render(request, 'print.html', {'amiibo': amiibo.data})
            # return Response(amiibo.data, status=status.HTTP_201_CREATED)
        # return Response(amiibo.errors, status=status.HTTP_400_BAD_REQUEST)
        return render(request, 'print.html', {'amiibo': amiibo.errors})