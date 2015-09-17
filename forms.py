# -*- coding: utf-8 -*-
from django import forms
from .models import WorkareaType, Workarea, Company

class WorkareaTypeForm( forms.ModelForm ) :
        
    description = forms.CharField(widget=forms.Textarea)
        
    class Meta : 
            
        model = WorkareaType
        fields = [ 'name', 'description' ]
        
    
class WorkareaForm( forms.ModelForm ) :
        
    description = forms.CharField( widget = forms.Textarea )
        
    class Meta : 
            
        model = Workarea
        fields = [ 'name', 'description', 'workarea_type' ]

class CompanyForm( forms.ModelForm ) :
    
    name = forms.CharField( label=False, widget = forms.TextInput( attrs={ 'placeholder' : 'Nombre compañía'} ) )
    
    class Meta : 
            
        model = Company
        fields = [ 'name' ]