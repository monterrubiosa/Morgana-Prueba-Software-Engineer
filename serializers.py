# -*- coding: utf-8 -*-
"""
Created on Wed May 25 16:31:46 2022

@author: monte
"""

from rest_framework_json_api import serializers
from yelp_datos.models import Business, User, Review

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool',
         'text', 'date')

class BusinessSerializer(serializers.HyperlinkedModelSerializer):
    review_set = ReviewSerializer(many = True, source = 'review_set.all')
    class Meta:
        model = Business
        fields = ('business_id', 'name', 'address', 'city', 'state', 'postal_code', 'latitude',
         'longitude', 'stars', 'review_count', 'is_open', 'attributes', 'categories',
         'hours', 'review_set')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    review_set = ReviewSerializer(many = True, source = 'review_set.all')
    class Meta:
        model = User
        fields = ('user_id', 'name', 'review_count', 'yelping_since', 'useful', 'funny', 'cool',
         'elite', 'friends', 'fans', 'average_stars', 'compliment_hot',
         'compliment_more', 'compliment_profile', 'compliment_cute',
         'compliment_list', 'compliment_note', 'compliment_plain', 'compliment_cool',
         'compliment_funny', 'compliment_writer', 'compliment_photos', 'review_set')