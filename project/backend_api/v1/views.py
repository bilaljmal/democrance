from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response,APIView

from ..models import Customers,InsurancePolicy
from ..filters import  CustomerFilter
from ..v1.serializer import CustomersSerializer, InsurancePolicySerializer, QuoteCreateSerializer

from rest_framework import permissions
# Create your views here.
from rest_framework import generics


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000




class CustomersView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CustomersSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['file_name','last_name','dob','policies__type']
    filterset_class = CustomerFilter

    def get_queryset(self):
        return Customers.objects.all()


class PoliciesView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = InsurancePolicySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['customer_id']

    def get_queryset(self):
        return InsurancePolicy.objects.all()



class PoliciesDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = InsurancePolicySerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return InsurancePolicy.objects.all()


class QuotesView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return InsurancePolicy.objects.all()
    def post(self, request, format=None):

        data=request.data
        if 'type' in data and 'customer_id' in data:
            data['customer'] = data['customer_id']
            serializer = QuoteCreateSerializer(data=request.data)
        elif 'quote_id' in data and 'status' in data:
            instance = InsurancePolicy.objects.filter(id=data['quote_id']).first()
            serializer = QuoteCreateSerializer(instance=instance,data=request.data)
        else:
            return Response({"detail": "Bad Data Keys"}, status=400)

        if serializer.is_valid():
            serializer.save()

            return Response({"detail":serializer.data},status=201)
        else:
            return Response({"detail":serializer.errors},status=400)


