from rest_framework.decorators import api_view, APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import TodoList
from .serializers import TodoSerializer

# api_view 데코레이터 방식
'''
@api_view(['get'])
def todo_list(request):
    queryset = TodoList.objects.all()

    serialized_list = TodoSerializer(queryset, many=True)

    return Response(data=serialized_list.data)
'''

# 클래스 기반 APIView
'''
class ListTodoView(APIView):

    def get(self, req):
        queryset = TodoList.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, req):
        pass
'''


class ListTodoView(ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer


class SeeTodoView(RetrieveAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer
    # lookup_url_kwarg = 'seq'
