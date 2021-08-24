from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .forms import UserCreationForm


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
            return Response({"message": "Successfully logged in"})


class RegisterView(APIView):
    permission_classes = (AllowAny,)
    form = UserCreationForm
    def post(self, request):
       form = self.form(request.POST)
       if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            return Response({"message": f"Successfully created"})
       return Response({"message": "Not created"})

    def get_authenticators(self):
        return []
       


""" def homePage(request):
    dir(User)
    data = {"access_token": "892r0yfw7ohhhhhhhhh3u4qodri3h48y3;iuch4n78fu3ouxmiua4fih7ahy8x4fi;iuawh7jkf8yuifer;uiwaef",
        "secret_key": "sioejf93siury43irfeiuzjlreiaudhfshvrhvdfsdfhfhhjfs"}

    return JsonResponse(data) # serialization ORM - Objects Relationship """
