from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.serializers import serialize
from django.contrib.auth import login, authenticate

@csrf_exempt
def loginView(request):
  if request.method == 'POST':
    username = request.POST['username']
    return HttpResponse('adf')