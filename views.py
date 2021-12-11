from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddDataForm, EditDataForm
from .models import MvnsCollectedData

# Create your views here.


def index(request):
    return render(request, 'MVNS/index.html')


def login(request):
    return render(request, 'MVNS/mvns_login.html', {'title': 'Login'})


def view(request):
    result = ''
    allData = MvnsCollectedData.objects.all()
    if allData.count() == 0:
        allData = {}
    else:
        allData = allData
    if 'enteredOrderNumber' in request.POST:
        orNum = request.POST['enteredOrderNumber']
        if orNum == '':
            result = 'Enter Valid Order Number'
        else:
            data = MvnsCollectedData.objects.filter(orderNumber=orNum)
            if data.count() == 0:
                result = 'Order Number Not Found'
            else:
                return redirect('MVNS-edit-data', data[0].pk)
    context = {
        'title': 'View',
        'result': result,
        'allData': allData,
    }
    return render(request, 'MVNS/mvns_view.html', context)


def add_data(request):
    addForm = AddDataForm()
    if request.method == 'POST':
        addForm = AddDataForm(request.POST)
        if addForm.is_valid():
            addForm.save()
            return redirect('/view')
    context = {
        'title': 'Add Data',
        'addForm': addForm,
    }
    return render(request, 'MVNS/mvns_add_data.html', context)


def edit_data(request, pk=None):
    dataID = MvnsCollectedData.objects.get(id=pk)
    info = EditDataForm(instance=dataID)
    editForm = EditDataForm()
    if request.method == 'POST':
        editForm = EditDataForm(request.POST, instance=dataID)
        if editForm.is_valid():
            editForm.save()
            return redirect('/view')
    context = {
        'title': 'Edit Data',
        'info': info,
    }
    return render(request, 'MVNS/mvns_edit_data.html', context)
