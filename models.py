from django.db import models
from django.contrib.auth.models import User

#Company model
class Company( models.Model ) :

    name = models.CharField( max_length = 200 )
    description = models.CharField( max_length = 1000, default='' )
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date uploaded
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    user = models.ForeignKey( User, default = 1, unique = False )
    
    #unicode return
    def __unicode__( self ) :
	    return self.name

#End of Company model

#WorkareType model
class WorkareaType( models.Model ) :
    
    name = models.CharField( max_length = 200 )
    description = models.CharField( max_length = 1000 )
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date uploaded
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    #unicode return
    def __unicode__( self ) :
	    return self.name
    
#End workareaType model

#Workarea model
class Workarea( models.Model ) :
    
    name = models.CharField( max_length = 200 )
    description = models.CharField( max_length = 1000 )
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date uploaded
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    workarea_type = models.ForeignKey( WorkareaType, default = 1, unique = False )
    company = models.ForeignKey( Company, default = 1, unique = False )
    
    #unicode return
    def __unicode__( self ) :
	    return self.name
	    
#End workarea model