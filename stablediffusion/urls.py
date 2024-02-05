from django.urls import path
from stablediffusion.views import TestAPI, SDTESTAPI

# todo - rest api url 적용하기.
urlpatterns = [
	# /sd/test/get/
	path('test/get/', TestAPI.as_view()),
	path('sdtest/post/', SDTESTAPI.as_view()),
	# /one_punch/coupang/get/
	# path('coupang/get/', CoupangAPI.as_view()),
]