def check_if_ajax(view_func):
    def the_func(request):
        if request.is_ajax():
            return True
        return view_func(request)
    return the_func