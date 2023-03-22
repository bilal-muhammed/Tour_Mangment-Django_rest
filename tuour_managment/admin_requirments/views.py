
from rest_framework import viewsets,generics

from user_managment.models import Customers
from .views import*
from .models import*
from .serializers import*

# Create your views here.
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer





class BranchListAPIView(generics.ListCreateAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchSerializer    

class BranchCreateAPIView(generics.ListCreateAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchCreateSerializer

class BranchRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Branches.objects.all()
    serializer_class = UpdateBranchSerializer



class VehicleListAPIView(generics.ListAPIView):
    queryset = Vehicle.objects.all().order_by('id')
    serializer_class = VehicleListSerializer

class VehicleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleRetriveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = UpdateVehicleSerializer

class RoomListAPIView(generics.ListAPIView):
    queryset =Rooms.objects.all().order_by('id')
    serializer_class = RoomListSerializer

class RoomCreateAPIView(generics.ListCreateAPIView):
    queryset =Rooms.objects.all()
    serializer_class = RoomSerializer


class RoomRetriveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset =Rooms.objects.all()
    serializer_class = UpdateRoomSerializer


class DesignationList(generics.ListCreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class DesignationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer



#>>>>>>> ADMIN DASHBOARD VIEWSETS <<<<<<<<#

from rest_framework.decorators import api_view
from datetime import datetime
from rest_framework.response import Response
#######################################################################################################

@api_view(['GET'])
def Customer_counts(request):
    customer_count = Customers.objects.all().count()
    today_count = Customers.objects.filter(is_created=datetime.now().date()).count()
    not_assigned = Customers.objects.filter(is_asigned=False).count()
    return Response({'customer_count': customer_count,
                     'today_count': today_count,
                     'not_assigned': not_assigned})


