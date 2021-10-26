from rest_framework.response import Response
from .serializers import CohortSerializer, PointSerializer
from .models import Cohort, Point
from rest_framework import generics, status
from authentication.models import User
from rest_framework.permissions import  IsAuthenticated
from authentication.permissions import  IsTaAndReadOnly

class CohortView(generics.ListCreateAPIView):

    serializer_class = CohortSerializer
    queryset = Cohort.objects.all()
    permission_classes = (IsTaAndReadOnly,)
    def post(self, request):
          
        name = request.data['name']

        try:
            instructr = User.objects.get(username=request.data['instructr'])
            if not instructr.is_superuser:
                return Response({'error':'this user is not Instructr!'}, status=status.HTTP_400_BAD_REQUEST) 
        except:
            return Response({'error':'this Instructr is not exist!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cohort = Cohort.objects.get(name=name)
            if cohort:
                return Response({'error':'cohort is already exist!'}, status=status.HTTP_400_BAD_REQUEST) 
        except:
            cohort = Cohort.objects.create(name=name, instructr=instructr)
            cohort.save()
            # import pdb
            # pdb.set_trace()
            return Response({'success': 'cohort created successfuly'}, status=status.HTTP_201_CREATED)

    

class PointView(generics.ListCreateAPIView):

    serializer_class = PointSerializer
    queryset = Point.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        if request.user.is_superuser or request.user.is_ta:
            return self.list(request)
        
        try:
            points = Point.objects.get(owner=request.user)
            serializer = self.serializer_class(points)
            return Response(serializer.data, status=status.HTTP_200_OK) 
        except:
            return Response({'error':'you have no points'}, status=status.HTTP_204_NO_CONTENT)
        
    
    def post(self, request):

        if request.user.is_superuser or request.user.is_ta:
            return self.create(request)

        return Response({'error':'sorry dude .. you had no permission!'}, status=status.HTTP_403_FORBIDDEN)
    

class PointDetailsView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = PointSerializer
    queryset = Point.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        if request.user.is_ta or request.user.is_superuser:
            return self.retrieve(request)
        return Response({'error':'no .. you cant get points from this route.. :/'}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, id):
        # import pdb
        # pdb.set_trace()
        point = Point.objects.get(id=id)

        if point.is_confirmed:
            return Response({'error':'point already confirmed, you cant donate it or edit it!'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if request.data['is_donated']:
            if len(request.data['donated_to']) < 1:
                return Response({'error':'make sure to fill donated_to field'}, status=status.HTTP_400_BAD_REQUEST)
            new_user = User.objects.get(username=request.data['donated_to'])
            if new_user.is_ta and not new_user.is_superuser:
                return Response({'error':'thx, but TAs dosent use points! :)'}, status=status.HTTP_406_NOT_ACCEPTABLE)

            new_point = Point.objects.create(donated_from=request.user.username, owner=new_user, notes=request.data['notes'])
            self.destroy(request)
            new_point.save()

            return Response({'success':'point transferd successfuly..'}, status=status.HTTP_200_OK)
    
        if request.data['is_confirmed'] and (not request.user.is_ta or not request.user.is_superuser):
            return Response({'error':'only instructional team can confirm your point!'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        if request.data['owner'] != point.owner.username:
            return Response({'error':'you can dontae this point but not change the owner directly!'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        return self.update(request)

    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.destroy(request, *args, **kwargs)
        return Response({'error':'only Instrtuctor can delete point!'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def patch(self, request, id):
        if request.user.is_ta:
            point = Point.objects.get(id=id)
            if not point.is_confirmed:
                point.is_confirmed = True
                point.save()
                return Response({'success':'point confirmed..'}, status=status.HTTP_200_OK)
            return Response({'error':'point is already confirmed'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'you can only confirm points by this method'}, status=status.HTTP_403_FORBIDDEN)
    