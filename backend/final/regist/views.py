from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework_jwt.settings import api_settings
from user.models import UserInfo
from user.serializers import UserSerializer
import hashlib,time
import json

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

# def md5(user):
#     ctime = str(time.time())
#     m = hashlib.md5(bytes(user,encoding='utf-8'))
#     m.update(bytes(ctime,encoding='utf-8'))
#     return m.hexdigest()

@api_view(['GET', 'POST'])
def getlist(request, format=None):
   if request.method == 'GET':
       users = UserInfo.objects.all()
       serializer = UserSerializer(users, many=True)
       return Response(serializer.data)

   elif request.method == 'POST':
       get_json = json.loads(request.body)
       username = get_json['username']
       password = get_json['password']
       user = UserInfo.objects.filter(username=username)
       if not user:
           UserInfo.objects.create(username = username,password = password)
           user = UserInfo.objects.filter(username=username,password=password).first()
           payload = jwt_payload_handler(user)
           token = jwt_encode_handler(payload)
           return Response({"msg": "注册成功","token":token},status = status.HTTP_200_OK)
       else:
           return Response({"msg": "注册失败，有重名用户"},status= status.HTTP_400_BAD_REQUEST)
                #   print(request.GET.get('test'))



# class UserAPI(APIView):
#     #用户登录类
#     def post(self,request,*args,**kwargs):
#         ret = {'code': 200, 'msg': None}
#         try:
#         #取前台数据
#             user = request._request.POST.get('username')
#             pwd = request._request.POST.get('password')
#         #验证数据
#             obj = UserInfo.objects.filter(username=user,password=pwd).first()
#             if not obj:
#                 ret['code']= 201
#                 ret['msg'] = '用户名或密码错误'    
#             else:
#                 ret['msg'] = '用户名或密码错误'  
#             #     #为登录用户创建TOKEN
#             #     token = md5(user)
#             #     #存在就更新，不存在就创建,token表user对应的是userinfo表，这里user=obj
#             #     UserToken.objects.update_or_create(user=obj,defaults={'token':token})
#             #     ret['token'] = token
#         except Exception as e:
#             ret['code'] = 1001
#             ret['msg'] = '请求异常'
#         return JsonResponse(ret)