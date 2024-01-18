from django.shortcuts import render
from qrcode import *

data = None

def index(request):
    global data
    if request.method == 'POST':
        data = request.POST['data']
        img = make(data)
        img.save('static/qrweb/images/test.png')
    else:
        pass
    return render(request, 'user/index.html', {'data': data})
