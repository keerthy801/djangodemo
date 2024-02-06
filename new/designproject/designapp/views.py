from django.shortcuts import render

from designapp.models import Place

from designapp.models import team


# Create your views here.
def home(request):
    c=Place.objects.all()
    t=team.objects.all()
    return render(request,'home.html',{'c':c,'t':t})