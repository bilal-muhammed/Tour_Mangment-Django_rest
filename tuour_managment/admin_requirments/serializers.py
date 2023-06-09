from rest_framework import serializers

from trippens.serializers import TrippensTourSerializer
from .models import*

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

    
class BranchSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    class Meta:
        model = Branches
        fields = '__all__'


class UpdateBranchSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    class Meta:
        model = Branches
        fields = '__all__'



class BranchCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'

class VehicleListSerializer(serializers.ModelSerializer):
    place = TrippensTourSerializer()
    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'



class UpdateVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        exclude = ['place']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class UpdateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        exclude = ['place']


class RoomListSerializer(serializers.ModelSerializer):
    place = TrippensTourSerializer()

    class Meta:
        model = Rooms
        fields = '__all__'



class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'



class ListStaffSerializer(serializers.ModelSerializer):
    designation = DesignationSerializer(read_only=True)
    branch = BranchCreateSerializer(read_only=True)
    class Meta:
        model = UserStaff
        fields = '__all__'



class CreateTourFormSerialiser(serializers.ModelSerializer):
    class Meta :
        model = TourForm
        fields = '__all__'



class AddInetenarySerialiser(serializers.ModelSerializer):
    class Meta :
        model = CustomInetenary
        fields = '__all__'