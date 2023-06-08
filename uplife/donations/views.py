# Importing necessary modules
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import BloodDonation, MedicineDonation, DonationAppointment
from .serializers import (
    BloodDonationSerializer,
    MedicineDonationSerializer,
    DonationAppointmentSerializer
)
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from donations.models import DonationAppointment
from donations.serializers import DonationAppointmentSerializer
from users.models import User

# Creating a view to list and create BloodDonations
@extend_schema(tags=["Donation Management | Blood"])  # adds tags to the schema
@extend_schema(description="List all blood donations", methods=["GET"])  # adds description and methods to the schema
@extend_schema(description="Create a blood donation", methods=["POST"])  # adds description and methods to the schema
class BloodDonationListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BloodDonation.objects.all()  # gets all BloodDonation objects from the database
    serializer_class = BloodDonationSerializer  # uses the BloodDonationSerializer to serialize the data

# Creating a view to retrieve, update, or delete a BloodDonation
@extend_schema(tags=["Donation Management | Blood"])  # adds tags to the schema
@extend_schema(description="Retrieve, update or delete a blood donation", methods=["GET", "PUT", "DELETE"])  # adds description and methods to the schema
class BloodDonationDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BloodDonation.objects.all()  # gets all BloodDonation objects from the database
    serializer_class = BloodDonationSerializer  # uses the BloodDonationSerializer to serialize the data

# Creating a view to list and create MedicineDonations
@extend_schema(tags=["Donation Management | Medicine"])  # adds tags to the schema
@extend_schema(description="List all medicine donations", methods=["GET"])  # adds description and methods to the schema
@extend_schema(description="Create a medicine donation", methods=["POST"])  # adds description and methods to the schema
class MedicineDonationListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MedicineDonation.objects.all()  # gets all MedicineDonation objects from the database
    serializer_class = MedicineDonationSerializer  # uses the MedicineDonationSerializer to serialize the data

# Creating a view to retrieve, update, or delete a MedicineDonation
@extend_schema(tags=["Donation Management | Medicine"])  # adds tags to the schema
@extend_schema(description="Retrieve, update or delete a medicine donation", methods=["GET", "PUT", "DELETE"])  # adds description and methods to the schema
class MedicineDonationDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MedicineDonation.objects.all()  # gets all MedicineDonation objects from the database
    serializer_class = MedicineDonationSerializer  # uses the MedicineDonationSerializer to serialize the data

# Creating a view to list and create DonationAppointments
@extend_schema(tags=["Donation Management | Appointment"])  # adds tags to the schema
@extend_schema(description="List all donation appointments", methods=["GET"])  # adds description and methods to the schema
@extend_schema(description="Create a donation appointment", methods=["POST"])  # adds description and methods to the schema
class DonationAppointmentListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = DonationAppointment.objects.all()  # gets all DonationAppointment objects from the database
    serializer_class = DonationAppointmentSerializer  # uses the DonationAppointmentSerializer to serialize the data

# Creating a view to retrieve, update, or delete a DonationAppointment
@extend_schema(tags=["Donation Management | Appointment"])
@extend_schema(description="Retrieve, update or delete a donation appointment", methods=["GET", "PUT", "DELETE"])
class DonationAppointmentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = DonationAppointment.objects.all() # gets all DonationAppointment objects from the database
    serializer_class = DonationAppointmentSerializer # uses the DonationAppointmentSerializer to serialize the data
    
    
@extend_schema(tags=["Donation Management | Appointment"])
@extend_schema(description="List all of a user's Appointments", methods=["GET"])
class UserAppointmentsViewSet(ReadOnlyModelViewSet):
    serializer_class = DonationAppointmentSerializer
    queryset = DonationAppointment.objects.all()
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        
        user = get_object_or_404(User, pk=user_id)
        return self.queryset.filter(donor=user)
    
    def list(self, request, user_id=None):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_id=None):
        queryset = self.get_queryset()
        appointment = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(appointment)
        return Response(serializer.data)