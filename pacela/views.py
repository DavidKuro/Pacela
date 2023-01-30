from django.shortcuts import render, HttpResponse

# Create your views here.
# def index (render):
#     return HttpResponse('Value the person of the Holy Spirit')

# def index (render):
#     return render()
def index(request):
    return render (request, 'pacela/index.html')
