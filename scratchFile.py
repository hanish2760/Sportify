import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportsgram.settings")
django.setup()

from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from sportsgramapp.models import Sport
from sportsgramapp.serializers.app_serializers import SportsSerializer
# content=Sport()
# content.sport_title="Cricket"
# content.save()


# serializer=SportsSerializer(content)
#
# print(serializer.data)
#
# content = JSONRenderer().render(serializer.data)
#
# print(content)
# content={'sport_title': 'Football' ,}
# # stream = BytesIO(content)
# content=dict(content)
# data = JSONParser().parse(content)
#
# print(data)
from django.utils.dateparse import parse_datetime
time="Wednesday, July 25th 2018, 2:47:41 am"
t=parse_datetime(time)

print(t)

def trySomething():
    print('hello')

