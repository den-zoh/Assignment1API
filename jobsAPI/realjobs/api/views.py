from realjobs.api.serializer import JobOfferSerializer
from realjobs.models import JobOffer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404


class JobOfferListView(APIView):
    def get(self, request):
        jobs = JobOffer.objects.filter(available=True)
        serializer = JobOfferSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class JobOfferDetailView(APIView):
    def get_object(self, pk):
        jobs = get_object_or_404(JobOffer, pk=pk)
        return jobs

    def get(self, request, pk):
        jobs = self.get_object(pk)
        serializer = JobOfferSerializer(jobs)
        return Response(serializer.data)

    def put(self, request, pk):
        jobs = self.get_object(pk)
        serializer = JobOfferSerializer(jobs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        jobs = self.get_object(pk)
        jobs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
