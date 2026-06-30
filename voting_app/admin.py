from django.contrib import admin
from .models import Student, Candidate, Vote

admin.site.register(Student)
admin.site.register(Candidate)
admin.site.register(Vote)