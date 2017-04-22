from django.http import HttpResponse, JsonResponse
import random
from .gpio import set_gpio_out
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def hello_world(request):
    print request.method
    if request.method == 'POST':
        print request
        json_data = json.loads(request.body)
        return HttpResponse(json_data['value'])
    else:
        return HttpResponse("GET")


def root_page(request):
    return JsonResponse({'data': 'xyz', 'result': 'successful'})

def export_pin(request, pin):
    print pin
    set_gpio_out(pin)
    return JsonResponse({'result': 'successful'})

def random_number(request, max_rand=100):
    random_number = random.randrange(0, int(max_rand))

    msg = "Random number between and %s : %d" %(max_rand, random_number)

    return HttpResponse(msg)