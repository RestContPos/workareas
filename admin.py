from django.contrib import admin
from .forms import WorkareaTypeForm, WorkareaForm, CompanyForm
from .models import WorkareaType, Workarea, Company

# Register your models here.
class WorkareaTypeAdmin( admin.ModelAdmin ) :
    
    list_display = [ "__unicode__", "description", "timestamp", "updated" ]
    form = WorkareaTypeForm
 
class WorkareaAdmin( admin.ModelAdmin ) :
    
    list_display = [ "__unicode__", "description", "timestamp", "updated" ]
    form = WorkareaForm

class CompanyAdmin( admin.ModelAdmin ) :
    
    list_display = [ "__unicode__", "description", "timestamp", "updated" ]
    form = CompanyForm


admin.site.register( WorkareaType, WorkareaTypeAdmin )
admin.site.register( Workarea, WorkareaAdmin )
admin.site.register( Company, CompanyAdmin )
