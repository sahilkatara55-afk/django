from django.shortcuts import render, redirect

# Create your views here.
from .models import Service
from .forms import ServiceForm


# List View
def serviceList(request):

    services = Service.objects.all()

    return render(request, 'services/service_list.html', {
        'services': services
    })


# Create View
def addService(request):

    if request.method == 'POST':
        form = ServiceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('services:serviceList')

    else:
        form = ServiceForm()

    return render(request, 'services/service_form.html', {
        'form': form
    })


# Delete View
def deleteService(request, id):

    service = Service.objects.get(id=id)
    service.delete()

    return redirect('services:serviceList')
# Update View
def updateService(request, id):

    service = Service.objects.get(id=id)

    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)

        if form.is_valid():
            form.save()
            return redirect('services:serviceList')

    else:
        form = ServiceForm(instance=service)

    return render(request, 'services/service_form.html', {
        'form': form
    })
