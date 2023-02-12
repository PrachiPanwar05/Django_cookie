from django.shortcuts import render
from django.http import HttpResponse

# # Create your views here.

# def setcookie(request):
#     response = HttpResponse("cookie set")
#     response.set_cookie('hello', 'pynative.com')
#     return response

# def getcookie(request):
#     tutorial = request.COOKIES['hello']
#     return HttpResponse("python tutorials @: "+  tutorial)

# DELETING COOKIE

def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")

def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair<br> cookie created")
    else:
        response = HttpResponse("Dataflair <br> Your browser doesn't except cookies")
    return response