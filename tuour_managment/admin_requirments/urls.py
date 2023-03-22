from django.urls import path, include
from rest_framework import routers
from .views import*

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)

urlpatterns = [
    path('', include(router.urls)),

# Create,List and Update Branches 
    path('list/branches',BranchListAPIView.as_view(),name='branch-list'),
    path('create/branches',BranchCreateAPIView.as_view(),name='branch-list'),
    path('branches/update/<int:pk>',BranchRetrieveUpdateAPIView.as_view(),name='branch-update'),

# Create,List and Update Vehicle 
    path('create/vehicles',VehicleListCreateAPIView.as_view(),name='vehile-create'),
    path('list/vehicles',VehicleListAPIView.as_view(),name='vehile-list'),
    path('vehicles/update/<int:pk>',VehicleRetriveUpdateAPIView.as_view(),name='vehicle-update'),

# Create,List and Update Rooms
    path('create/rooms',RoomCreateAPIView.as_view(),name='rooms-list'),
    path('list/rooms',RoomListAPIView.as_view(),name='rooms-list'),
    path('rooms/update/<int:pk>',RoomRetriveUpdateAPIView.as_view(),name='rooms-update'),

# Create,List and Update Designatios
    path('designations/', DesignationList.as_view(), name='designation-list'),
    path('designations/<int:pk>/', DesignationDetail.as_view(), name='designation-detail'),

    

# Admin Dashboard ...!

    path('customer/counts', Customer_counts, name='update_password'),


]




    