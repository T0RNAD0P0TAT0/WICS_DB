from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import wicsMember
from .forms import EmailForm

# Create your views here.
def index(request):
	memberList = wicsMember.objects.order_by('firstName')[:]
	template = loader.get_template('../templates/index.html')
	context = RequestContext(request, {
		'memberList': memberList
		})
	return HttpResponse(template.render(context))

def detail(request, capturedEmail):
	memberList = wicsMember.objects.order_by('email');
	output = 'Member not found'
	for member in memberList:
		if(member.email == capturedEmail):
			output = "First Name: {}<br>LastName: {}<br>Email: {}<br>Meetings Attended: {}".format(member.firstName, member.lastName, member.email, member.numMeetingsAttended)
			#todo: do not know how to make new line in python so it shows in html
			#todo: fil in formas as needed
			break;
	return HttpResponse(output)

def allUsers(request):
	memberList = wicsMember.objects.order_by('firstName')[:]
	output=', '.join([m.firstName + " " + m.lastName for m in memberList])
	return HttpResponse(output)

def fillForm(request):
	#fillForm is the html that will have spaces 
	#	for user to input their information
	if request.method == 'POST':
		return HttpResponse("here")
		form = EmailForm(request.POST)
		if form.is_valid():
			return HTTPResponse("done inputting email")
		#if it is a GET(or any other method), this will create a blank form
		else:
			form = EmailForm()
	return HttpResponse("not valid input")
