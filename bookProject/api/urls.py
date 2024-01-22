from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('books/',views.BookListCreateView.as_view(), name='List-Create-book' ),
    path('books/<int:pk>',views.BookRetrieveUpdateDestroyView.as_view(), name='book-Retrieve-Update-Destroy' ),
    path('categories/',views.CategoryListCreateView.as_view(), name='List-Create-Category' ),
    path('category/<int:pk>',views.CategoryRetrieveUpdateDestroyView.as_view(), name='Category-Retrieve-Update-Destroy' ),
    path('books/<int:book_id>/reviews/', views.ReviewView.as_view(), name='list-reviews'),
    path('books/<int:book_id>/reviews/<int:pk>', views.ReviewRetrieveEditDeleteView.as_view(), name='crud-reviews'),

]
