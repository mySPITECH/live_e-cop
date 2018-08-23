from django import forms

class UserInfoData(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    STATE = (('Ab','Abia'),
    ('Ad','Adamawa'),('Ak','AkwaIbom'),('An','Anambra'),
    ('Ba','Bauchi'),('By','Bayelsa'),('Be','Benue'),
    ('Br','Borno'),('Cr','Cross-River'),('Dt','Delta'),
    ('Eb','Ebonyi'),('Ed','Edo'),('En','Enugu'),('Ek','Ekiti'),
    ('Gb','Gombe'),('Im','Imo'),('Ji','Jigawa'),('Kd','Kaduna'),('Ka','kano'),
    ('Kt','Katisna'),('Kb','Kebi'),('kg','Kogi'),('Kw','Kwara'),('La','Lagos'),
    ('Na','Nasarawa'),('Ng','Niger'),('Og','Ogun'),('Oy','Oyo'),('Pl','Plateau'),
    ('Rv','Rivers'),('Sk','Sokoro'),('Tb','Taraba'),('Yb','Yobe'),('Zm','Zamfara'))

    gender = forms.CharField()#widget=forms.select(choice=STATE)
    phone_no = forms.CharField(max_length=20)
    email = forms.EmailField()
    home_address = forms.CharField()
    office_address = forms.CharField()
    state = forms.CharField()
    town= forms.CharField(max_length=20)
    state_origin= forms.CharField()
    local_govt = forms.CharField(max_length=20)
    nationalty = forms.CharField(max_length=20)


    
    
