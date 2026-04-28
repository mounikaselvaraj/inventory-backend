from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer


# ---------------- LIST + CREATE ----------------
@api_view(['GET', 'POST'])
def items_list_create(request):

    if request.method == 'GET':
        items = Item.objects.all()

        # 🔍 SEARCH by name
        search = request.GET.get('search')
        if search:
            items = items.filter(name__icontains=search)

        # ⚠️ LOW STOCK FILTER
        low_stock = request.GET.get('low_stock')
        if low_stock == 'true':
            items = items.filter(quantity__lt=10)

        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ---------------- DETAIL + UPDATE + DELETE ----------------
@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):

    try:
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        return Response(
            {"error": "Item not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(
            {"message": "Deleted successfully"},
            status=status.HTTP_200_OK
        )