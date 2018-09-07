from django.db import models
from django.urls import reverse
from django.forms import ModelForm
import uuid
import random
#from django.db import transaction

# Create your models here.
class UserInfo(models.Model):
    first_name= models.CharField(max_length=20,null=False)
    last_name = models.CharField(max_length=20,null=False)

    SEX = (('m','male'),
    ('f','female'),
    ('o','other'))
    gender = models.CharField(choices=SEX,null=False,max_length=10)
    date_birth = models.DateField(auto_now=False,null=False,blank=False)
    dnmb = 101

    STATE = (('Ab','Abia'),
    ('Ad','Adamawa'),('Ak','AkwaIbom'),('An','Anambra'),
    ('Ba','Bauchi'),('By','Bayelsa'),('Be','Benue'),
    ('Br','Borno'),('Cr','Cross-River'),('Dt','Delta'),
    ('Eb','Ebonyi'),('Ed','Edo'),('En','Enugu'),('Ek','Ekiti'),
    ('Gb','Gombe'),('Im','Imo'),('Ji','Jigawa'),('Kd','Kaduna'),('Ka','kano'),
    ('Kt','Katisna'),('Kb','Kebi'),('kg','Kogi'),('Kw','Kwara'),('La','Lagos'),
    ('Na','Nasarawa'),('Ng','Niger'),('Og','Ogun'),('Oy','Oyo'),('Pl','Plateau'),
    ('Rv','Rivers'),('Sk','Sokoro'),('Tb','Taraba'),('Yb','Yobe'),('Zm','Zamfara'),('Os','Osun'))

    state_origin = models.CharField(choices=STATE,null=False,max_length=10)
    local_govt = models.CharField(max_length= 20, null= False)
    nationalty= models.CharField(default='Nigeria',max_length=20)
    phone_no = models.CharField(max_length=20,help_text='+23480xxxxxxxxxx')

    

    email = models.EmailField(help_text='user@example.com')
    home_address = models.CharField(max_length=20,null=False)
    office_address = models.CharField(max_length=20)
    state = models.CharField(choices=STATE,max_length=10)
    town = models.CharField(max_length=10, null=False)
    passport=models.ImageField(null=True,upload_to='uploads')
    balance = models.DecimalField(decimal_places=2,blank=True,
    default=0.00,max_digits=12)

     
    def __str__(self):
        value=f'{self.dnmb}{self.phone_no}{self.id}'
       
        return value
    account_number = models.CharField(max_length=20,null=True,blank=True,unique=True)

    class Meta:
        ordering=['last_name','first_name']
class Account_no(UserInfo):
    def acct(self,value):
        value=f'{UserInfo.dnmb}{UserInfo.phone_no[8]}{UserInfo.phone_no[0]}{UserInfo.phone_no[6]}{UserInfo.id}'
        print(value)


        
        
   
  
    
class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['first_name','last_name','gender','date_birth',
        'state_origin','local_govt','nationalty','phone_no',
        'email','home_address','office_address','town','account_number']
#User Account
class UserAccount(models.Model):
    account_number = models.CharField(max_length=20,null=True)
    account_name = models.CharField(max_length=20,null=True)
    TXN_TYPE =(('dr','Debit'),
    ('cr','Credit')) 
    amount= models.DecimalField(decimal_places=2,blank=True,max_digits=12)
    txn_type=models.CharField(choices=TXN_TYPE,null=True,max_length=10)
    txn_details=models.CharField(max_length=20)
    txn_date=models.DateTimeField(auto_now=True)
   
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, 
    help_text='Unique ID for user account')
    def get_absolute_url(self):
         return reverse('member-details',args=[str(self.account_number)])
#UserAccount Form
class UserAccountForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = ['account_number','txn_type','amount',
       'txn_details','account_name']
        exclude =['transaction_id']
        
    
       
    
        
       
    

    
          

     
     
   
   

     

     
   
    


    
    