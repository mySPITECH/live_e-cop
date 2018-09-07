from django.shortcuts import render,redirect
from .models import UserInfo,UserInfoForm,UserAccount,UserAccountForm,Account_no
from django.views import generic
from .tables import UserTable,UserAccountTable
from django_tables2 import RequestConfig
from .forms import UserInfoData
from django_tables2.export.export import TableExport
from django.views.decorators.http import require_POST
from django.views.generic import DetailView
from django.db import transaction
import random
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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
@login_required
def record(request):
    table =UserTable(UserInfo.objects.all())
    RequestConfig(request).configure(table)
    export_formats = request.GET.get('_export', None)
    CONTEXT={'table': UserInfo.objects.all(),'page':table,'export_format':export_formats}
    if TableExport.is_valid_format(export_formats):
        exporter = TableExport(export_formats, table)
        return exporter.response('table.{}'.format(export_formats))

    return render(request,'coop/record.html',context=CONTEXT)

@login_required
def register(request):
    formz = UserInfoForm()  #UserInfoData()
    return render(request,'register.html',{'formz':formz})

    # save user Data
@require_POST
def save(request):
    a=UserInfo()
    #Account_no Insatnce
    
    if request.method == 'POST':
         formz = UserInfoForm(request.POST,instance=a) 
         formz.save()
         return render(request,'register.html',{'formz':formz})
        
#generate account number before registration
def validate(request):
    user= request.POST['phone_no']
    a=UserInfo()
    d=UserInfo.objects.filter(phone_no=user)
    formz = UserInfoForm(request.POST,instance=a) 
    unique_id=random.randint(1000,9999)
    error="user already exist"
    valuez = f'{UserInfo.dnmb}{user[8]}{user[2]}{user[0]}{unique_id}'
    if user in  d:
        return render(request,'register.html',{'formz':formz,'error':error})
    else:
        return render(request,'success.html',{'valuez':valuez,'formz':formz,'user':user})


        
            
       
           
        


    #return render(request,'success.html',{'valuez':valuez,'formz':formz})


#Payment Page
@login_required
def deposit(request):
    payment_form =UserAccountForm()
    return render(request,'deposit.html',{'payment_form':payment_form})
#POST PAYMENT
@require_POST
@transaction.atomic
def pay(request):
    b=UserAccount()
    table=UserAccountTable(UserAccount.objects.all())
    CONTEXT={'table': UserAccount.objects.all(),'page':table}
    pay_form= UserAccountForm(request.POST,instance=b)
    pay_form.save()
    account_no= request.POST['account_number']
    account_owner = UserInfo.objects.get(account_number__exact=account_no)
    amount = request.POST['amount']
    c = int(amount)    
                    
    if request.POST['txn_type']=='dr':
        payment_form =UserAccountForm()
        if c > account_owner.balance:
             message="Less current balance"
             return render (request,'deposit.html',{'message':message,'payment_form':payment_form}) 
        else:
            account_owner.balance -= c
            account_owner.save()
            sid = transaction.savepoint()
            transaction.savepoint_commit(sid)
            return render(request,'coop/payment-info.html',context=CONTEXT)             
    elif  request.POST['txn_type']=='cr':
        account_owner.balance +=c
        account_owner.save()
        sid = transaction.savepoint()
        transaction.savepoint_commit(sid)
        #accountname= request.POST['account_name ']
        txndetail= request.POST['txn_details']
        accountnum= request.POST['account_number']
        amounts=request.POST['amount']
        messages = "Payment Successful:"  + "Account name:"+"Account NO:"+ accountnum  +"Amount :"  + amounts +"NGN"  + "Txn Detail:" +txndetail
        return render(request,'deposit.html',{'messages':messages})  
#USER AUTHENTICATION

     
   
       
         
        
         
        
            
           
            
            
            
      
       
        
        
             
      
       
   


def pay_info(request):
    table=UserAccountTable(UserAccount.objects.all())
    CONTEXT={'table': UserAccount.objects.all(),'page':table}
    return render(request,'coop/payment-info.html',context=CONTEXT)


class AccoutDetailView(DetailView):
    model= UserAccount


#Account statement
@require_POST
def query(request):
    account_no= request.POST['account_number'] 
    table=UserAccountTable(UserAccount.objects.filter(account_number__exact=account_no))
    CONTEXT={'table': UserAccount.objects.filter(account_number__exact=account_no),'page':table}
    return render(request,'statement.html',context=CONTEXT)




        
       
            


          
   
     
  

    
