from django.conf.urls import url

from . import views

# urlpatterns = [
# 	url(r'^$', views.index, name = 'index'),
# 	url(r'^buttonClicked$', views.buttonClicked, name = 'buttonClicked')
# 	]

urlpatterns = [
	#/wics_database/
    url(r'^$', views.index, name='index'),
    #/wics_database/<email>
    #1 or more caseInsensitive characters@domain.
    url(r'^(?P<capturedEmail>[a-zA-Z0-9]+@[a-zA-Z]+.+edu|com)/$', views.detail, name='detail'),
    
    #/wics_databaase/allUsers
    url(r'^allUsers/$', views.allUsers, name='allUsers'),
    #/wics_database/fillForm
    url(r'^fillForm/$', views.fillForm, name='fillForm')
    #/wics_database/fillForm/thanks
    
]

"""
to capture email from regex:
r'^(?P<capturedEmail>[a-zA-Z0-9]+@[a-zA-Z]+.+edu|com)
^   ^ ^              ^ 
start of regex expression
	tells them that you are trying to capture regex
	  name of caputured regex
	                 start of regex    
"""