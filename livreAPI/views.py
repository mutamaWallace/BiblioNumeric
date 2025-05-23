from django.shortcuts import render
from rest_framework import viewsets
from livre.models import Livre
from livreAPI.serializers import LivreSerializer
from rest_framework.permissions import IsAuthenticated



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


# Create your views here.


class LivreViewSet(viewsets.ModelViewSet):
    
     
    queryset= Livre.objects.all()
    serializer_class = LivreSerializer
    permission_classes = (IsAuthenticated, )
    # filterset_fields = ['titre']
    search_fields = ['titre']
    
    

class LivreListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'rest_framework/base.html'

    def get(self, request):
        livres = Livre.objects.all()
        return Response({'livres': livres})
