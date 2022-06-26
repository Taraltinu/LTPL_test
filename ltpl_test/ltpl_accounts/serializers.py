import numpy
import cv2
from rest_framework import serializers
from ltpl_accounts.models import User
from ltpl_accounts.image_detect.smile_detect import smile_detect

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email","name","mobile","image"]


    # def create(self,vali)