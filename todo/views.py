from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import TodoList
from .serializers import TodoSerializer, UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group

# api_view 데코레이터 방식
'''
@api_view(['get'])
def todo_list(request):
    queryset = TodoList.objects.all()

    serialized_list = TodoSerializer(queryset, many=True)

    return Response(data=serialized_list.data)
'''


# 클래스 기반 APIView

class APIViewTodo(APIView):

    def get(self, req):
        queryset = TodoList.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, req):
        print(req.data)
        queryset = TodoList.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)


class ListAPIViewTodo(ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer


class SeeTodoView(RetrieveAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer
    # lookup_url_kwarg = 'seq'


# 유저 관련

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
