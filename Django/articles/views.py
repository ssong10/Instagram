from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleSerializers

# Create your views here.
@api_view(['GET','POST'])
def create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializers = ArticleSerializers(articles,many=True)
        return Response(serializers.data)

