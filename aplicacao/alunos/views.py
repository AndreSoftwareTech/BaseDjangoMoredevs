from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'index.html')
    
def aluno(request):
    return render(request,'aluno.html')