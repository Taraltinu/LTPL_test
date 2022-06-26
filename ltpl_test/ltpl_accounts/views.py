from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from ltpl_accounts.models import User
from ltpl_accounts.serializers import UserSerializer
from ltpl_accounts.image_detect.smile_detect import smile_detect
import cv2
import numpy as np
from ltpl_test.util import APIResponse

class UserView(viewsets.ModelViewSet):
    queryset = (User.objects.all())
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image = request.FILES.get("image")
        image = np.asarray(bytearray(image.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        is_smiled = smile_detect(image)
        if is_smiled is False:
            return APIResponse(code=0,message="Please upload smileys image.")
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)