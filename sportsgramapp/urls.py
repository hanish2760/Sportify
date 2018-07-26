from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
# import sportsgramapp.rest_views.api_views
from sportsgramapp.rest_views.api_views import *
from sportsgramapp.rest_views.auth import*
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
urlpatterns = [

    #jwt authentication :
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),


    path('api/sports_list/', sports_list ),#list of sports and add a sport
    path('api/sports_details/<int:pk>/',sport_detail), #geta sports details and also update , delete it

    path('api/grounds_list/', grounds_list),  # list of grnds and add a grnd
    path('api/ground_details/<int:pk>/', ground_detail),  # gets details and also update , delete it


    # user urls !

    # path('login/',), no need of usr login ! we can get the details of the user from request object by sending the authenticaton deatils i.e,jwt !

    path('signup/', SignUpAPi.as_view(), name="sign_up"),
    path('api/user_details/',UserDetailesApi.as_view()),

    path('api/user_credentials/<int:pk>/',user_credentials), #can get a user details,update and delete  a user.
    path('api/users_list/', users_list), #we can  get list of users and also add a  user


    ]



if settings.DEBUG:
    urlpatterns+=[
        url('api/uploaded_media/(?P<path>.*)$',serve,{
            'document_root':settings.MEDIA_ROOT ,
        }),
    ]

"""
only the urls  which uses APIView are protected by the jwt authentication.

function based views are not protected.

permission_classes = (IsAuthenticated)
or we can ad this to the class based view.
"""