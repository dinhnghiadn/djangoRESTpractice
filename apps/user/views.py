from django.contrib.auth.hashers import make_password
from rest_framework import status, response, generics
from rest_framework.response import Response

from apps.user.serializer import UserSerializer


class UserRegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()
            return response.Response({'message:': 'Register successfully !'}, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error_message': 'This email has already exist!',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)
