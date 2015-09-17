# -*- coding: utf-8 -*-
from django.shortcuts import render
from workarea.forms import WorkareaForm, CompanyForm
from .models import Company, Workarea
from django.shortcuts import redirect

# index view
def index( request ) :
    
    c_workareas = Workarea.objects.filter( company = Company.objects.get( id = request.session['temp_company_id'] ) )
    
    context = {
        
        'title' : 'Areas de Trabajo',
        'workareas' : c_workareas
    }
    
    return render( request, 'workarea/index.html', context )

#end index

# new view workarea
def new( request ) :
    
    form = WorkareaForm( request.POST or None )
    title = 'Nuevo espacio de trabajo'
    
    context = {
        'title' : title,
        'form' : form
    }
    
    if form.is_valid() : 
        
        title =  'Areas de Trabajo'
        msj = 'Su nueva área de trabajo se creo exitosamente'
        
        instance = form.save( commit = False )
        instance.company = Company.objects.get( id = request.session['temp_company_id'] )
        instance.save()
        
        context = {
            'title' : title,
            'form' : form,
            'msj' : msj
        }
        
        return redirect( '/workareas/' )
            
    return render( request, 'workarea/new.html', context )

#end index


#company_index workarea
def company_index( request ) :
    
    companies = Company.objects.filter( user = request.user )
    
    form = CompanyForm( request.POST or None )
    
    if form.is_valid() : 
        
        title = 'Compañías'
        msj = 'Su compañía ha sido creada exitosamente'
        
        instance = form.save( commit = False )
        instance.user = request.user
        instance.save()
        
        form = CompanyForm()
        
        context = {
            
            'title' : title,
            'form' : form,
            'msj' : msj,
            'companies' : companies
            
        }    
        
        return render( request, 'workarea/company_index.html', context )
        
    else : 
        
        title = 'Compañías'
        msj = 'Bienvenido %s' % ( request.user.first_name ) 
        
        context = {
            
            'title' : title,
            'welcome_msj' : msj,
            'form' : form,
            'companies' : companies
            
        }
            
        return render( request, 'workarea/company_index.html', context )
            
    context = {
            
        'title' : 'Compañias',
        'companies' : companies
            
    }
        
    return render( request, 'workarea/company_index.html', context )
    
#end company_index

#Company redirection
def get_into_company( request, company_id ) :
    
    request.session['temp_company_id'] = company_id
    
    return render( request, 'dashboard/dashboard.html' )