from rest_framework import viewsets

from users.models import StudentUser

from .serializers import StudentUserSerializer


class StudentUserViewSet(viewsets.ModelViewSet):
    queryset = StudentUser.objects.all()
    serializer_class = StudentUserSerializer
