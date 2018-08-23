import django_tables2 as tables
from .models import UserInfo

class UserTable(tables.Table):
    class META:
        model=UserInfo
        template_name= 'django_tables2/bootstrap.html'
    
        
