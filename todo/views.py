from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TodoList
from .serializers import TodoSerializer


@api_view(['get'])
def todo_list(request):
    queryset = TodoList.objects.all()

    serialized_list = TodoSerializer(queryset, many=True)

    return Response(data=serialized_list.data)
