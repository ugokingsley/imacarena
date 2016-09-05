from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

def main_page(request):
    template = get_template('bookmarks/main_page.html')
    variables = Context({
        'user': request.user
    })
    output = template.render(variables)
    return HttpResponse(output)

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('Requested user not found.')
    bookmarks = user.bookmark_set.all()
    template = get_template('bookmarks/user_page.html')
    variables = Context({
        'username': username,
        'bookmarks': bookmarks,
    })
    output = template.render(variables)
    return HttpResponse(output)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')