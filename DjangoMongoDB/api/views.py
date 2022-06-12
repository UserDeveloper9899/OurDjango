from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from rest_framework.parsers import JSONParser
from.serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    if request.method == 'GET':
        items=Item.objects.all()
        serializer=ItemSerializer(items, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def regData(request):
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def delData(request, c):
    if request.method == 'DELETE':
        items = Item.objects.get(ccode=c)
        items.delete()
        return Response("Record deleted successfully")

@api_view(['PUT'])
def addData(request, c1):
    try:
        items = Item.objects.get(ccode=c1)
    except Item.DoesNotExist:
        return Response("Item not Found to add stockprice")
    if request.method == 'PUT':
        item_data = JSONParser().parse(request)
        serializer = ItemSerializer(items, data=item_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def fetData(request, c1, sdate, edate):
    if request.method == 'POST':
        items = Item.objects.get(ccode=c1)
        Item.objects.filter(s=sdate,e=edate)




@api_view(['GET'])
def infoData(request, code):
    if request.method == 'GET':
        items= Item.objects.get(ccode=code)
        serializer=ItemSerializer(items, many=True)
        return Response(serializer.data)