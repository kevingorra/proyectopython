from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'index.html')
def Registrar(request):
    return render(request,'registro.html')