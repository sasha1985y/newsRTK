from django.shortcuts import render
from django.http import HttpResponse
from .forms import DemoForm, Demo
# Create your views here.
#from .models import News
# from .models import Link
def about(request):
    return render(request,'main/about.html')

def index(request):
    return render(request,'main/index.html')

def contacts(request):
    return render(request,'main/contacts.html')

def demoform(request):
    form = DemoForm()
    if request.method == 'POST':

        new_model = DemoForm(request.POST,request.FILES)
        new_model.save()

    context = {'form':form}
    return render(request,'home/image_Form.html',context)

def showlastmodel(request):
    model = Demo.objects.all().first()
    context = {'model':model }
    return render(request,'main/image_Form.html',context)

def custom_404(request, exeption):
    # context = {'exeption': exeption}
    # return render(request, 'main/page_404.html', context)
    return HttpResponse(f'jfdklfjdklfklsjklfjdkl:{exeption}')