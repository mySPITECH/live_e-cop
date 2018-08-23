from django.shortcuts import render
from .models import UserInfo,UserInfoForm
from django.views import generic
from .tables import UserTable
from django_tables2 import RequestConfig
from .forms import UserInfoData

# Create your views here.

def index(request):
    num_member = UserInfo.objects.count()
    num_male = UserInfo.objects.filter(gender__exact='m').count()
    num_female = UserInfo.objects.filter(gender__exact='f').count()
   # data_set  =  UserInfo.objects.all()
    Context={'num_member':num_member,
    'num_female':num_female,
    'num_male':num_male,
    #'data_set':data_set
    }

    return render(request,'index.html',context=Context)
      
class UserInfoDetaiVew(generic.ListView):
    model = UserInfo

def record(request):
    table =UserTable(UserInfo.objects.all())
    RequestConfig(request,paginate={'per_page':10}).configure(table)
    CONTEXT={'table': UserInfo.objects.all(),'page':table}
    return render(request,'coop/record.html',context=CONTEXT)

def register(request):
    formz = UserInfoForm()  #UserInfoData()
    return render(request,'register.html',{'formz':formz})

    # save user Data
def save_user(request):
    a=UserInfo()
   
    if request.method == 'POST':
         formz = UserInfoForm(request.POST,instance=a) 
         formz.save()
         return render(request,'register.html',{'formz':formz})
 
       
        
       
            


          
   
     
  
"""RequestConfig(request).configure(table)
     table =UserInfo(UserInfo.objects.all())
     return render(request,'coop/record.html',{'tables':table)"""
       
    
