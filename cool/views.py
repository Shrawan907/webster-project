from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cool
from django.utils import timezone 

def home(request):
    reads = Cool.objects
    return render(request, 'home.html',{'reads': reads})         # take us to home page

@login_required(login_url="/accounts/signup") # i.e create page only shown when a user is login
def create(request):
    if request.method == 'POST':        
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            cools = Cool()
            cools.title = request.POST['title']
            cools.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                cools.url = request.POST['url']
            else:
                cools.url = 'https://' + request.POST['url']
            cools.icon = request.FILES['icon']
            cools.image = request.FILES['image']        # image are of file type
            cools.pub_date = timezone.datetime.now()
            cools.hunter = request.user                 # hunter is set to current user
            cools.save()                                # it saves all
            return redirect('/cool/' + str(cools.id))             # at this moment redirect to home
        else:
            return render(request, 'create.html',{'error': 'All fields required!'})
    else:
        return render(request, 'create.html')

def detail(request, cools_id):          # it give details of each user eith specific id
    cools = get_object_or_404(Cool, pk=cools_id)
    return render(request, 'detail.html',{'cools': cools})

@login_required(login_url="/accounts/signup")
def upvote(request, cools_id):
    if request.method == "POST":
        cools = get_object_or_404(Cool, pk=cools_id)
        cools.votes_total += 1
        cools.save()
        return redirect('/cool/' + str(cools.id))