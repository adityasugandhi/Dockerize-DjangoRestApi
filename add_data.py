from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
from api.models import Product
from api.serializers import ProductSerializer

print("Script Started!")
print("Adding Data.......")

with open("data.json", "r+") as file:
    data = json.load(file)
    for doc in data:
        product_serializer = ProductSerializer(data=doc)
        if product_serializer.is_valid():
            product_serializer.save()\

print("Done! Data Loaded!")