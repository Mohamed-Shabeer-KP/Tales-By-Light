from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.utils import timezone
from django.contrib import messages

from .models import voteData

import collections

def index(request):
    context={
        'iterator': range(1,93)
        }
    
    if request.method == "POST" :
        if request.POST.get("name") and request.POST.get("img_number"):
            name = request.POST.get("name")
            img_no = request.POST.get("img_number")
            v = voteData(v_name=name,v_img_no=img_no,v_date=timezone.now())
            v.save()

            messages.info(request, 'Thank you for voting.')

        return render(request,'talesbylight/index.html',context)
    else :
        return render(request,'talesbylight/index.html',context)

def vote_table(request):
    q_result = voteData.objects.all()
    out = [x.v_img_no for x in q_result]

    count = collections.Counter(out)

    out = zip(count.keys(),count.values())
    context = {"votes": out}

    return render(request,'talesbylight/result.html',context)

