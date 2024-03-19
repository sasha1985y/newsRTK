from django.shortcuts import render
from django.http import HttpResponse
from .forms import DemoForm, Demo
# Create your views here.
#from .models import News
# from .models import Link
def about(request):
    return render(request,'main/about.html')

# def get_commit_count(username, repository):
#     url = f"https://api.github.com/repos/{username}/{repository}/commits"
#     headers = {
#         "Authorization": "Token ..."
#     }
#     commit_count = 0
#     page = 1
#     while True:
#         params = {"page": page, "per_page": 100}
#         response = requests.get(url, headers=headers, params=params)
#         commits = response.json()
#         commit_count += len(commits)
#         if len(commits) < 100:
#             break
#         page += 1
#     return commit_count
#
# def index(request):
#     username = "..."
#     repository = "..."
#     commit_count = get_commit_count(username, repository)
#     return render(request, 'main/index.html', {'commit_count': commit_count})

def index(request):
    return render(request,'main/index.html')

def contacts(request):
    return render(request,'main/contacts.html')

def offer(request):
    return render(request,'main/offer.html')

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

# def custom_404(request, exeption):
#     # context = {'exeption': exeption}
#     # return render(request, 'main/page_404.html', context)
#     return HttpResponse(f'1000:{exeption}')

def custom_404(request, exception):
    return render(request, 'main/page_404.html')