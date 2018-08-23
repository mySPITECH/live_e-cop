from django.db import models
from django.urls import reverse
from django.forms import ModelForm
import uuid
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
    phone_no = models.CharField(max_length=13,help_text='+23480xxxxxxxxxx')
    email = models.EmailField(help_text='user@example.com')
    home_address = models.CharField(max_length=20,null=False)
    office_address = models.CharField(max_length=20)
    state = models.CharField(choices=STATE,max_length=10)
    town = models.CharField(max_length=10, null=False)
    passport=models.ImageField(null=True)
    

     
   

    def __str__(self):
        return f'{self.last_name},{self.first_name}'
    class Meta:
        ordering=['last_name','first_name']
    
class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['first_name','last_name','gender','date_birth',
        'state_origin','local_govt','nationalty','phone_no',
        'email','home_address','office_address','town']
#User Account
class UserAccount(models.Model):
    account_owner = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2,default=0.00,blank=True,max_digits=12,null=True  ) 

    TXN_TYPE =(('dr','Debit'),
    ('cr','Credit')) 
    debit = models.DecimalField(decimal_places=2,blank=True,max_digits=12)
    credit = models.DecimalField(decimal_places=2,blank=True,max_digits=12)
    txn_type=models.CharField(choices=TXN_TYPE,null=True,max_length=10)
    txn_details=models.CharField(max_length=20)
    txn_date=models.DateField(auto_now=True)
   
    account_id = models.UUIDField(primary_key=True, default=uuid.uuid4, 
    help_text='Unique ID for user account')
    def get_absolute_url(self):
         return reverse('member-details',args=[str(self.account_id)])

    
        
       
    

    
          

     
     
   
   

     

     
   
    


    
    