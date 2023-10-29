from django.urls import path, include
from rest_framework.routers import DefaultRouter
from  .import views

# Create a router and register our viewsets with it.
#for api view & generic route not necesary it necsecary for viewset
router = DefaultRouter()
router.register(r'books', views.BookListView,basename="book")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    #for api view
    # path('books/', views.BookListView.as_view()),
    # path('books/<int:pk>/', views.BookListDetailView.as_view()),
    #for generic class view
    # path('books/', views.BookListCreateAPIView.as_view()),
    # path('books/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view()),
     path('', include(router.urls)),
]