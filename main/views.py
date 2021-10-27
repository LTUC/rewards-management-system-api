from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, status, views
from .models import Points
from .serializers import DataSerializer
from rest_framework.response import Response


class DataAPIView(generics.ListAPIView):
    serializer_class = DataSerializer
    queryset = Points.objects.all()


    def get(self, request):
        data = {
            'py-d6':{
                "Instructor":"Dario Thornhill",
                "TAs":['Rania Abdullah','Saja Ismael','Diala Abedalqader','Ahmad Al-Mohammad','Ashjan Albarqi','Hanaa Al-Ghazzi','Emad Alzoubi','Yazan Alshikha','Mohammad Hadi','Mohammad Alnimrawi','Saleh Almasri'],
                "Students":['Anas Abusaif','Adham_Mhaydat','Hamza Ahmad','Tasneem Al-Absi','Mohammed Al-Hanbali','Renad Al-Khlafat','Aseel Al-Saqer','Majed Al-Swaeer','Moayad Osama Alhaj','Tahany Ali','Morad Alkhatib','Shahd Alkhatib','Khaled Alqrainy','ahmad alrasheed','ehab-ahmad','haneen hashlamoun',"Du'a Jaradat",'yousef jariry','Jehad Abu Awwad','Faisal Kushha','Abdullah Nazzal','Ashrf Obeidat','Odeh Abuzaid','Mona Salih',"Musa'b Shalaldeh",'mohammad silwadi','Suzan Ahmad Hiary','bashar taamneh']
            }
        }


        return Response(data, status=status.HTTP_200_OK) 

