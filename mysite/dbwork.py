from smarthouse.models import Log
from django.utils import timezone
def outOfDB(ctype):
     typeLog = Log.objects.get(type = ctype)
     return typeLog[len(typeLog)-1].value