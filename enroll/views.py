from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def showformdata(request):
    fm=StudentRegistration(auto_id=True,initial={"name":"Binod","email":"shresthabinod334@gmail.com"})
    return render(request,'userregistration.html',{'form1':fm})
