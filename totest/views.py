from django.shortcuts import render_to_response
from totest.decorators import check_if_ajax

@check_if_ajax
def index(request):
    '''
    index
    '''
    return render_to_response('test.html', {'age':30})


