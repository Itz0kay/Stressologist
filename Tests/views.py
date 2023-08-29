from django.shortcuts import render
from django.http import JsonResponse
from .forms import ImageForm
from .models import Result
from Tests.prediction.predict import predict_emotions
from Tests.prediction.stresspercent import calculateStressPercent

# Import methods for imgupload
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from urllib.request import urlopen

# Create your views here.

def listView(request):
    cards = list(Result.objects.filter(user=request.user).values())
    # print(cards,"******")
    context = {
        'cards':cards,
    }
    return render(request, 'Tests/listview.html', context)


def detailView(request):
    context = {}
    return render(request, 'Tests/detailview.html', context)


def deleteView(request):
    context = {}
    return render(request, 'Tests/Dialog/deleteTest.html', context)

# def imageupload(request):
#     context = {
#     }
#     if request.method == 'POST':
#         username = request.POST["username"]
#         image_path = request.POST["src"]  # src is the name of input attribute in your html file, this src value is set in javascript code
        
#         webimg = urlopen(request.POST["src"])
#         data = webimg.read()
#         content_file = ContentFile( data, "webcam.jpg" )
        
#         image = NamedTemporaryFile()
#         image.write(urlopen(image_path).read())
#         image.flush()
#         image = File(image)
#         name = str(image.name).split('\\')[-1]
#         name += '.jpg'  # store image in jpeg format
#         image.name = name
#         if image is not None:
#             obj = Image.objects.create(username=username, image=content_file)  # create a object of Image type defined in your model
#             obj.save()
#             context["path"] = obj.image.url  #url to image stored in my server/local device
#             context["username"] = obj.username
#         else :
#             return redirect('/')
#         return redirect('/')
#     return render(request, 'Tests/test/imgupload.html', context=context)



def imageupload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():

            # Calculate the result
            result = calculateStressPercent(predict_emotions(request))

            # Create EmotionPrediction instance and associate with the user and image
            image_instance = form.save()
            Result.objects.create(user=request.user, image=image_instance, stresslevel=result)
            return render(request, 'Tests/result.html', {'result': result})
    else:
        form = ImageForm()
    return render(request, 'Tests/test/imguploadnew.html', {'form': form})

    