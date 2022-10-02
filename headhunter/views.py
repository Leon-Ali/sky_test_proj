from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from .serializers import ResumeSerializer
from .models import Resume
from .permissions import IsOwnerPermission


class ResumeListView(generics.ListAPIView):
    """
    API endpoint that allows to list resumes.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class ResumeUpdateView(generics.UpdateAPIView):
    """
    API endpoint that allows to to update user's resume.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


