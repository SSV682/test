from rest_framework import viewsets
from ..models import News
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    pagination_class = None
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)
    queryset = News.objects.filter()
