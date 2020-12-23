from rest_framework.decorators import api_view
from rest_framework.response import Response

from db.models import User, Transaction

from db.serializers import UserSerializer, TransactionSerializer, ReportSerializer


# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Users': '/users/',
        'Create': '/user-create/',
        'Modify': '/user-update/<int:pk>/',
        'Delete': '/user-delete/<int:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def status(request):
    return Response({
        'status': 'alive'
    })


@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def user_create(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def user_update(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def user_delete(request, pk):
    user = User.objects.get(id=pk)
    user.delete()

    return Response('User succesfully deleted!')


@api_view(['POST'])
def transaction_add(request):
    user = User.objects.filter(name=request.data['user']).first()

    serializer = TransactionSerializer(instance=user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def get_report(request, name):
    user = User.objects.filter(name=name).first()
    serializer = ReportSerializer(instance=user, many=False)
    return Response(serializer.data)
