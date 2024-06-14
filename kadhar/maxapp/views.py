from django.shortcuts import render,redirect
from .forms import TableForm
from django.views import View
from .models import*
# Create your views here.
class AddTable(View):
    def get(self, request):
        form = TableForm()
        return render(request, 'add.html', {'form': form})

    def post(self, request):
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loading')
        return render(request, 'add.html', {'form': form})

class Viewtable(View):
    def get(self,request):
        form = table.objects.all()
        return render(request, 'view.html', {'form': form})
class edittable(View):
    def get(self,request,id):
        nmn=table.objects.get(pk=id)
        form=TableForm(instance=nmn)
        return render(request,'edit.html' , {'form': form})
    def post(self,request,id):
        nmn=table.objects.get(pk=id)
        form=TableForm(request.POST,instance=nmn)
        if form.is_valid():
            form.save()
            return redirect('loading')
        return render(request, 'edittable.html', {'form': form})
class deletetable(View):
    def get(self, request, id):
        nmn = table.objects.get(pk=id)
        return render(request, 'delete.html')
    def post(self,request,id):
        nmn = table.objects.get(pk=id)
        nmn.delete()
        return redirect('loading')