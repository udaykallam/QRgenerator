from django.shortcuts import render
import qrcode
import os
from django.conf import settings

def index(request):
    data = None
    img_path = None
    if request.method == 'POST':
        data = request.POST['data']
        img = qrcode.make(data)
        img_dir = os.path.join(settings.MEDIA_ROOT, 'qrweb/images')
        os.makedirs(img_dir, exist_ok=True)
        img_path = os.path.join(img_dir, 'test.png')
        img.save(img_path)
        img_path = f"/media/qrweb/images/test.png"
    return render(request, 'user/index.html', {'data': data, 'img_path': img_path})
