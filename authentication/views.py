from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import jwt
from .serializers import (
    RegisterSerializer,
    EmailVerficationSerializer,
    LoginSerializer,
    RegisterSuperUserSerializer,
    TeamMatesSerializer,
)
from .models import User
from .util import Util
from .permissions import IsInstructional


class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        user = User.objects.get(email=user_data["email"])
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain

        relativeLink = reverse("email-verify")
        absurl = "http://" + current_site + relativeLink + "?token=" + str(token)
        email_body = (
            "Hi " + user.username + " Use link below to verfy your email \n" + absurl
        )

        data = {
            "email_body": email_body,
            "to_email": user.email,
            "email_subject": "Verify your email",
        }

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class RegisterSuperUserView(generics.GenericAPIView):

    serializer_class = RegisterSuperUserSerializer
    permission_classes = [IsInstructional]

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # import pdb
        # pdb.set_trace()

        user_data = serializer.data

        user = User.objects.get(email=user_data["email"])
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain

        relativeLink = reverse("email-verify")
        absurl = "http://" + current_site + relativeLink + "?token=" + str(token)
        email_body = (
            "Hi " + user.username + " Use link below to verfy your email \n" + absurl
        )

        data = {
            "email_body": email_body,
            "to_email": user.email,
            "email_subject": "Verify your email",
        }

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    serializer_class = EmailVerficationSerializer

    token_param_config = openapi.Parameter(
        "token",
        in_=openapi.IN_QUERY,
        description="Description",
        type=openapi.TYPE_STRING,
    )

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get("token")

        pyload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")

        try:
            user = User.objects.get(id=pyload["user_id"])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response(
                {"email": "Successfuly activated"}, status=status.HTTP_200_OK
            )
        except jwt.ExpiredSignatureError:
            return Response(
                {"error": "Activation Expired"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.exceptions.DecodeError:
            return Response(
                {"error": "Invalid token!"}, status=status.HTTP_400_BAD_REQUEST
            )


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TeamMatesAPIView(generics.ListCreateAPIView):
    serializer_class = TeamMatesSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        return Response({"error": "ERORR"}, status=status.HTTP_403_FORBIDDEN)

    def get(self, request):
        try:
            if request.data["type"] == "students":
                mates = User.objects.filter(
                    course=request.user.course, is_superuser=False, is_ta=False
                )
        except:
            if request.user.course == "":
                return Response(
                    {"error": "user is not in any course!"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            mates = User.objects.filter(course=request.user.course)

        data = []
        for i in range(len(mates)):
            data.append({"username": mates[i].username})

        return Response(data, status=status.HTTP_200_OK)
