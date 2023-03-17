from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from django.utils import timezone
from django.db.models import F
import secrets
from .models import URL

def homePage(request):
    return render(request, 'base.html')

def create_random_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        if not long_url:
            return HttpResponseBadRequest('Missing long_url parameter')
        if len(long_url) > 250:
            return HttpResponseBadRequest('Url too long')
        while True:
            short_name = secrets.token_urlsafe(6)[:6]
            try:
                URL.objects.get(short_name=short_name)
            except URL.DoesNotExist:
                break
        
        url = URL.objects.create(short_name=short_name, long_url=long_url)
        return render(request, 'created.html', {short_name: short_name})
    else:
        return render(request, "create.html")
    

def create_custom_url(request, short_name):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        if not long_url:
            return HttpResponseBadRequest('missing long_url parameter')
        if len(long_url) > 250:
            return HttpResponseBadRequest('url too long')
        if URL.objects.filter(short_name=short_name).exists():
            return HttpResponseBadRequest('short name already in use')
        url = URL.objects.create(short_name=short_name, long_url=long_url)
        return render(request, 'created.html', {'short_name': short_name})
    
    else:
        return render(request, 'create.html')

def redirect_url(request, short_name):
    url = get_object_or_404(URL, short_name=short_name)
    url.access_count = F('access_count') + 1
    url.save()
    return redirect(url.long_url)
