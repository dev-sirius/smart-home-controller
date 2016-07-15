from smarthouse.models import Log
from django.utils import timezone
def outOfDB(ctype):
     typeLog = Log.objects.filter(type = ctype) 
     return typeLog[len(typeLog)-1].value
