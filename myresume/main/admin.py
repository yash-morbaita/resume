from django.contrib import admin
from main.models import myservices, myskills , testimonials, myexperiences

# Register your models here.
admin.site.register(myservices)
admin.site.register(myskills)
admin.site.register(testimonials)
admin.site.register(myexperiences)