from playtogether.models import Snippet
from playtogether.models import BilliardsUser,BilliardsInvite,BilliardsJoin
from playtogether.serializers import playtogethererializer,UserSerializer
from playtogether.serializers import BilliardsInviteSerializer,BilliardsUserSerializer,BilliardsJoinSerializer,\
    UserRegisterSerializer
from rest_framework import generics
from rest_framework import permissions
from playtogether.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework import viewsets

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'playtogether': reverse('snippet-list', request=request, format=format)
    })

from rest_framework import renderers

from rest_framework.decorators import detail_route
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class BilliardsUserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = BilliardsUser.objects.all()
    serializer_class = BilliardsUserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BilliardsInviteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = BilliardsInvite.objects.all()
    serializer_class = BilliardsInviteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BilliardsJoinViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = BilliardsJoin.objects.all()
    serializer_class = BilliardsJoinSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = playtogethererializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class UserLoginAPIView(APIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = (AllowAny,)

   def post(self, request, format=None):
       data = request.data
       username = data.get('username')
       password = data.get('password')
       user = User.objects.get(username__exact=username)
       if user.password == password:
           serializer = UserSerializer(user)
           new_data = serializer.data
           # 记忆已登录用户
           self.request.session['user_id'] = user.id
           return Response(new_data, status=HTTP_200_OK)
       return Response('password error', HTTP_400_BAD_REQUEST)


#用于注册

class UserRegisterAPIView(APIView):
   queryset = User.objects.all()
   serializer_class = UserRegisterSerializer
   permission_classes = (AllowAny,)

   def post(self, request, format=None):
       data = request.data
       username = data
       if User.objects.filter(username__exact=username):
           return Response("用户名已存在",HTTP_400_BAD_REQUEST)
       serializer = UserRegisterSerializer(data=data)
       if serializer.is_valid(raise_exception=True):
           serializer.save()
           return Response(serializer.data,status=HTTP_200_OK)
       return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
