from django.shortcuts import redirect

def middleware(get_resp):
    def innerFunc(request):
        if not request.session.get('username'):
            return redirect('login')
        response = get_resp(request)
        return response
    return innerFunc
    
