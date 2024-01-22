from rest_framework import serializers
from api.models import Book, Category, Review
from pyuploadcare import Uploadcare

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','title','slug']

class ReviewSerializer(serializers.ModelSerializer):
    # date_posted = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Review
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'cover', 'category', 'author', 'pages', 'description','average_rate', 'reviews']
        read_only_fields = ['average_rate','author']
