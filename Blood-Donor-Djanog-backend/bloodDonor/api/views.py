# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BloodDonor
from .serializers import BloodDonorSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination
from rest_framework import  generics
from django.db.models import Q
class CreateBloodDonorView(APIView):
    @swagger_auto_schema(request_body=BloodDonorSerializer)
    def post(self, request):
        serializer = BloodDonorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # Assuming the ID is auto-generated by the database
            blood_donor_id = serializer.instance.id  # Get the ID of the newly created blood donor

            # Create a success message
            message = f"Blood donor with ID {blood_donor_id} has been created."
            return Response({"message": message, "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBloodDonorsView(APIView):
    def get(self, request, format=None):
        blood_type_param = request.GET.get("blood_type", "")
        city_param = request.GET.get("city", "")

        # Define a filter condition using Q objects to match blood type and city name
        filter_condition = Q(blood_type__startswith=blood_type_param) & Q(city__startswith=city_param)

        bloodDonors = BloodDonor.objects.filter(filter_condition)

        # Apply pagination
        paginator = PageNumberPagination()
        paginated_donors = paginator.paginate_queryset(bloodDonors, request)

        serializer = BloodDonorSerializer(paginated_donors, many=True)

        return paginator.get_paginated_response(serializer.data)


class BloodDonorDetailView(APIView):
    def get(self, request, pk, format=None):
        try:
            bloodDonor = BloodDonor.objects.get(id=pk)
            serializer = BloodDonorSerializer(bloodDonor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BloodDonor.DoesNotExist:
            return Response({"error": "BloodDonor not found"}, status=status.HTTP_404_NOT_FOUND)


class DeleteBloodDonorView(APIView):
    def delete(self, request, pk):
        try:
            bloodDonor = BloodDonor.objects.get(id=pk)
            bloodDonor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


class UpdateBloodDonorView(generics.UpdateAPIView):
    queryset = BloodDonor.objects.all()
    serializer_class = BloodDonorSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)