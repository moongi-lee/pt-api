from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from .engine import TestEngine


class TestAPI(APIView):

	def get(self, request):
		return Response("get test 성공.", status=status.HTTP_200_OK)

	def post(self, request):

		body_data = request.data
		print(body_data)
		print(request.data['image'])
		print(request.data['title'])

		# 이미지 저장
		image = request.data['image']
		prompt = request.data['title']
		path = default_storage.save(f'userImage/image{prompt}.png', ContentFile(image.read()))
		# tmp_file = os.path.join(settings.MEDIA_ROOT, path)


		# image = Image.open(request.data['image'])
		# image.show()
		# image.save('test.jpg')

		return Response("post test 성공.", status=status.HTTP_200_OK)


class SDTESTAPI(APIView):

	def post(self, request):
		print(request.data['title'])
		prompt = request.data['title']
		new_engine = TestEngine(prompt)
		image = new_engine.test_diffusion_pipeline()
		path = default_storage.save(f'userImage/image{prompt}.png', ContentFile(image.read()))

		return Response("sd post test 성공.", status=status.HTTP_200_OK)



