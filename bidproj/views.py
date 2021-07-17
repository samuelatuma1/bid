from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import Registration
from .models import BidProduct
# Create your views here.
from django.contrib.auth.models import User


def index(request):
    uploads = BidProduct.objects.all().order_by('-upload_time')[:10]
    recentUploads = []
    
    for item in uploads:
        bid = {
            'product_name' : item.product_name,
            'uploaded_by': item.uploaded_by.username,
            'current_bid': float(item.current_bid),
            'product_image': item.product_image.url,
            'description': item.description
        }
        recentUploads.append(bid)
    if request.method == 'POST':
        
        search = request.POST['search']
        bidsQuery = BidProduct.objects.filter(product_name__icontains=search).order_by('-upload_time').all()[:20]
        categoryQuery = BidProduct.objects.filter(category__icontains=search).order_by('-upload_time').all()[:20]
        bids = list(categoryQuery)
        for item in bidsQuery:
            if not item in categoryQuery:
                bids.append(item)
        
        bidnames = [{"bid_name":bid.product_name,"uploaded_by": bid.uploaded_by.username} for bid in bids]
                    
        return JsonResponse({'bids': str(bidnames)})
    return render(request, 'bidproj/index.html', {'recentUploads': recentUploads})

def register(request):
    form = Registration()
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            User.objects.create_user(username, email, password)
            user = User.objects.get(username=username)
            user.first_name = first_name
            user.save()
            
            return render(request, 'registration/registration_done.html', {'form': form})
            
    return render(request, 'registration/register.html',{'form': form})

