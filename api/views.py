from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page")
    friends=[
        'gaurav',
        'akash',
        'suraj'
    ]
    return JsonResponse(friends,safe=False)