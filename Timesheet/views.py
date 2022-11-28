from django.shortcuts import render, redirect
from .models import Checkin
from .forms import CheckinForm
from django.contrib import messages

# Create your views here.
def index(request):
    all_checkin = Checkin.objects.all
    return render(request, "index.html", {'all':all_checkin})

def retrieve(request):
    all_checkin = Checkin.objects.all
    distinct_user = Checkin.objects.order_by('user').values('user').distinct()
    distinct_project = Checkin.objects.order_by('project').values('project').distinct()
    if request.method == "POST":
        user = request.POST.get('selectUser', None)
        date_checkin = request.POST.get('date_checkin', None)
        project = request.POST.get('project', None)
        query = request.POST.get('query')
        if user:
            diff_user = Checkin.objects.raw('SELECT * FROM Timesheet_checkin WHERE user = %s', [user])
        return render(request, "retrieve.html",  {'all':diff_user, 'distinct_user':distinct_user, 'distinct_project': distinct_project})
    else:
        return render(request, "retrieve.html", {'distinct_user':distinct_user, 'distinct_project': distinct_project})
