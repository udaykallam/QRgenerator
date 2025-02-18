from django.shortcuts import render
import qrcode
import os
from django.conf import settings

def index(request):
    data = None
    img_path = None  # To store the dynamically generated QR code path

    if request.method == 'POST':
        data = request.POST['data']
        img = qrcode.make(data)

        # Define the path to save the QR code image inside STATICFILES_DIRS
        img_dir = os.path.join(settings.MEDIA_ROOT, 'qrweb/images')
        os.makedirs(img_dir, exist_ok=True)  # Ensure the directory exists

        img_path = os.path.join(img_dir, 'test.png')
        img.save(img_path)

        # Convert file path to a relative URL
        img_path = f"/media/qrweb/images/test.png"

    return render(request, 'user/index.html', {'data': data, 'img_path': img_path})
