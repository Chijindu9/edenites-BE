from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import item
from .serializers import itemSerializer


@api_view(['GET'])
def getData(resquest):
    items = item.objects.all()
    serializer = itemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])

def addItem(request):
    serializer= itemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)