from django.shortcuts import redirect

# ******* Authenticated *******
def auth(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated == False:
            return redirect('login_view')
        return view_function(request, *args, **kwargs)
    return wrapped_view

def guest(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard_view')
        return view_function(request, *args, **kwargs)
    return wrapped_view
