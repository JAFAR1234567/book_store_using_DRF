from .models import BookStoreModel
from .serializers import BookStoreSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# 1st method api view

# class BookListView(APIView):
#     def get(self, request, format=None):
#         model = BookStoreModel.objects.all()
#         serializer = BookStoreSerializer(model, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = BookStoreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BookListDetailView(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return BookStoreModel.objects.get(pk=pk)
#         except BookStoreModel.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         model = self.get_object(pk)
#         serializer = BookStoreSerializer(model)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         model = self.get_object(pk)
#         serializer = BookStoreSerializer(model, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         model = self.get_object(pk)
#         model.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#2nd method generic class view

# from .models import BookStoreModel
# from .serializers import BookStoreSerializer
# from rest_framework import generics


# class BookListCreateAPIView(generics.ListCreateAPIView):#get,post request
#     queryset = BookStoreModel.objects.all()
#     serializer_class = BookStoreSerializer


# class BookRetrieveUpdateDestroyAPIView(generics. RetrieveUpdateDestroyAPIView):#update,delete,single element access
#     queryset = BookStoreModel.objects.all()
#     serializer_class = BookStoreSerializer
    


from rest_framework import viewsets

class BookListView(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer
    