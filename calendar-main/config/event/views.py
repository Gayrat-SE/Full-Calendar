from django.shortcuts import render
from .models import Event
from .serializers import (
    CreateEventSerializer,
    GetEventsSerializer,
    GetEventSerializer,
    UpdateEventSerializer
)
from rest_framework.views import APIView
from rest_framework import status, generics
from  rest_framework.response import Response
import calendar
from datetime import date, datetime

class CreateEvent(APIView):
    serializer_class =CreateEventSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid():
            title = serializer.data.get('title')
            start_date = serializer.data.get('start_date')
            end_date = serializer.data.get('end_date')
            url = serializer.data.get('url')


            event = Event(title=title, start_date=start_date, end_date=end_date, url=url)
            event.save()

            return Response(CreateEventSerializer(event).data, status=status.HTTP_201_CREATED)

        return Response({"msg":"No Content"}, status=status.HTTP_204_NO_CONTENT)


class GetEvents(APIView):
    def get(self, request):
        year = datetime.now().year
        month = datetime.now().month
        events = Event.objects.filter(end_date__year = year, end_date__month=month)
        if events.exists():
            serializer = GetEventsSerializer(events, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"msg":"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)


class GetArchivesEvents(APIView):

    def get(self, request):
        year = datetime.now().year
        archives_year = 0
        for i in range(year-1, year):
            archives_year+=i
        events = Event.objects.filter(end_date__year = archives_year)
        if events.exists():
            serializer = GetEventsSerializer(events, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"msg":"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

class GetDetailEvent(APIView):
    lookup_url_kwarg = 'id'
    def get(self, request):
        id = request.GET.get(self.lookup_url_kwarg)
        event = Event.objects.filter(id=id)
        if event.exists():
            data = GetEventSerializer(event[0], many=False)
            return Response(data.data, status=status.HTTP_200_OK)
        return  Response({"msg":"No Content"}, status=status.HTTP_204_NO_CONTENT)



class UpdateEvent(APIView):
    serializer_class = UpdateEventSerializer
    lookup_url_kwarg = 'id'
    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        id = request.GET.get('id')
        if serializer.is_valid(raise_exception=True):
            title = serializer.data.get('title')
            start_date = serializer.data.get('start_date')
            end_date = serializer.data.get('end_date')
            url = serializer.data.get('url')

            queryset = Event.objects.filter(id=id)
            if not queryset.exists():
                return Response({"msg":"Event Not Found"}, status=status.HTTP_404_NOT_FOUND)
            event = queryset[0]

            event.title = title
            event.start_date = start_date
            event.end_date = end_date
            event.url = url
            event.save(update_fields=["title", "start_date", "end_date", "url"])

            return Response(UpdateEventSerializer(event, many=False).data, status=status.HTTP_200_OK)

        return Response({"msg":"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)



def calendar_s(request):
    return render(request, 'index.html')