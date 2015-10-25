from django.shortcuts import render_to_response
from totest.decorators import check_if_ajax
from forms import UserProfileForm

@check_if_ajax
def index(request):
    '''
    index
    '''
    form = UserProfileForm()
    return render_to_response('test.html', {'age':30, 'form':form})


