from django.shortcuts import render

from .models import support
from .forms import supportForm

def support_submit(request):
    if request.method == 'POST':
        form = supportForm(request.POST)
        if form.is_valid():
            new_support = support.objects.create()
            new_support.save()
            return render (request,'date/support.html',{'form': form})
    else:
        form = supportForm()
    
    return render (request,'date/support.html',{'form': form})
      

