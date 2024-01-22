from rest_framework.response import Response
from rest_framework import generics, permissions, status , viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from api import serializers
from api.models import Book, Category, Review
from api.serializers import BookSerializer,CategorySerializer, ReviewSerializer
import requests
from rest_framework.decorators import api_view

class IsAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Author').exists()


class ReviewView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


    def perform_create(self, serializer):
        # Set the user and book for the review based on the request
        serializer.save(user=self.request.user, book_id=self.kwargs['book_id'])

        # After saving the review, update the average rate of the book
        book = serializer.instance.book
        book.calculate_rate_avg()

        # You may want to return additional data in the response if needed
        response_data = {
            'message': 'Review created successfully',
            'review_id': serializer.instance.id,
            'book_id': book.id,
            'average_rate': book.average_rate,
        }
        return Response(response_data, status=status.HTTP_201_CREATED) 


class ReviewRetrieveEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        return Review.objects.filter(book_id=book_id)

# Create your views here.
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'book_id'


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




    # def perform_create(self, serializer):
    #     # Assuming you send the file in the request.FILES['cover'] field
    #     uploaded_file = self.request.FILES.get('cover')

    #     if uploaded_file:
    #         # Upload the file to Uploadcare
    #         response = requests.post(
    #             'https://upload.uploadcare.com/base/',
    #             files={'file': uploaded_file.file},
    #         )

    #         # Check if the upload was successful
    #         if response.status_code == 200:
    #             # Get the UUID of the uploaded file
    #             file_uuid = response.json().get('file')
    #             # Construct the URL using the UUID
    #             file_url = f'https://ucarecdn.com/{file_uuid}/'

    #             # Set the cover field in the serializer with the file URL
    #             serializer.validated_data['cover'] = file_url

    #             # Call the parent perform_create method to save the instance
    #             super().perform_create(serializer)

    #             # Return the file URL in the response
    #             return Response({'cover': file_url}, status=status.HTTP_201_CREATED)

    #     return Response({'error': 'Invalid file'}, status=status.HTTP_400_BAD_REQUEST)