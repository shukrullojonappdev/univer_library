from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
  if request.method == 'POST':
    # user = authenticate(request, username=username, password=password)
    if request.user.is_authenticated:
      return HttpResponse('yes auth')
    return HttpResponse('no auth')

@csrf_exempt
def logout_view(request):
  if request.user.is_authenticated:
    logout(request)
  return HttpResponse('first logged in')