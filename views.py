#from django.shortcuts import render

# Create your views here.

from yelp_datos.models import Business, User, Review
from yelp_datos.serializers import BusinessSerializer, UserSerializer, ReviewSerializer
from rest_framework import viewsets

from rest_framework import filters
#from django_filters.rest_framework import DjangoFilterBackend

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    #filterset_fields = ['business_id', 'name', 'address', 'city', 'state', 'postal_code', 'latitude','longitude', 'stars', 'review_count', 'is_open', 'attributes', 'categories','hours']
    search_fields = ['business_id', 'name', 'address', 'city', 'state', 'postal_code', 'latitude','longitude', 
	'stars', 'review_count', 'is_open', 'attributes', 'categories','hours']
    ordering_fields = ['stars']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user_id', 'name', 'review_count', 'yelping_since', 'useful', 'funny', 'cool',
         'elite', 'friends', 'fans', 'average_stars', 'compliment_hot',
         'compliment_more', 'compliment_profile', 'compliment_cute',
         'compliment_list', 'compliment_note', 'compliment_plain', 'compliment_cool',
         'compliment_funny', 'compliment_writer', 'compliment_photos']

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool',
         'text', 'date']