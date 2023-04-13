from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import IncomeSerializer
from .models import Income
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class IncomeListAPIView(ListCreateAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    

class IncomeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = (IsAuthenticated,IsOwner,)
    lookup_field = "id"

    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
