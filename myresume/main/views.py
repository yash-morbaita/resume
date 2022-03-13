from django.shortcuts import render
from . models import myservices, myskills, myexperiences, testimonials

# Create your views here.

def index(request):
    myservice = myservices.objects.all()
    myskill  = myskills.objects.all()
    myexperience  = myexperiences.objects.all()
    testimonial  = testimonials.objects.all()
    return render(request, 'index.html', {'services' : myservice, 'skills' : myskill, 'experience' : myexperience , 'test': testimonial})