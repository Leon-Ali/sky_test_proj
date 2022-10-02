from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from .serializers import ResumeSerializer
from .models import Resume


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
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


