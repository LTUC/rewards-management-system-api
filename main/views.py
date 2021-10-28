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
                "TAs":["Rania Abdullah","Saja Ismael","Diala Abedalqader","Ahmad Al-Mohammad","Ashjan Albarqi","Hanaa Al-Ghazzi","Emad Alzoubi","Yazan Alshikha","Mohammad Hadi","Mohammad Alnimrawi","Saleh Almasri"],
                "Students":["Anas Abusaif","Adham Mhaydat","Hamza Ahmad","Tasneem Al-Absi","Mohammed Al-Hanbali","Renad Al-Khlafat","Aseel Al-Saqer","Majed Al-Swaeer","Moayad Osama Alhaj","Tahany Ali","Morad Alkhatib","Shahd Alkhatib","Khaled Alqrainy","Ahmad Alrasheed","Ehab Ahmad","Haneen Hashlamoun","Du'a Jaradat","yousef Jariry","Jehad Abu Awwad","Faisal Kushha","Abdullah Nazzal","Ashrf Obeidat","Odeh Abuzaid","Mona Salih","Musa'b Shalaldeh","mohammad Silwadi","Suzan Ahmad Hiary","bashar taamneh"]
            }
        }


        return Response(data, status=status.HTTP_200_OK) 

class PointAPIList(generics.ListCreateAPIView):
    serializer_class = DataSerializer
    queryset = Points.objects.all()

    def get(self, request):
        try:
            if request.data['by_student']:
                data = Points.objects.filter(owner=request.data['by_student'])
                if len(data) < 1:
                    return Response({'error':'no points for this student'}, status=status.HTTP_400_BAD_REQUEST)

                serlized_data = []
                for i in range(len(data)):            
                    serlized_data.append({"id": data[i].id,"owner": data[i].owner,"reward": data[i].reward,"is_confirmed": data[i].is_confirmed,"created_at": data[i].created_at})
                return Response(serlized_data, status=status.HTTP_200_OK) 
        except:
            return self.list(request)
                