from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonForm

def index(request):
    persons = Person.objects.all()
    return render(request, 'person_data/index.html', {'persons': persons})

def add_person(request):
    if request.method=='POST':
        form =PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=PersonForm()

    return render(request, 'person_data/add_person.html', {'form': form})




