from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from bookmarks.forms import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from bookmarks.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def main_page(request):
    return render_to_response(
    'bookmarks/main_page.html', RequestContext(request)
    )
    '''
    template = get_template('bookmarks/main_page.html')
    variables = Context({
        'user': request.user
    })
    output = template.render(variables)
    return HttpResponse(output)
    '''
def user_page(request, username):
    '''
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('Requested user not found.')
    bookmarks = user.bookmark_set.all()
    '''
    user = get_object_or_404(User, username=username)
    bookmarks = user.bookmark_set.order_by('-id')
    variables = RequestContext(request, {
        'bookmarks': bookmarks,
        'username': username,
        'show_tags': True
    })


    return render_to_response('bookmarks/user_page.html', variables)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@csrf_exempt
def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response(
        'registration/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
        context)


@csrf_exempt
@login_required(login_url='/bookmarks/login/')
def bookmark_save_page(request):
    if request.method == 'POST':
        form = BookmarkSaveForm(request.POST)
        if form.is_valid():
            # Create or get link.
            link, dummy = Link.objects.get_or_create(
                url=form.cleaned_data['url']
            )
            # Create or get bookmark.
            bookmark, created = Bookmark.objects.get_or_create(
                user=request.user,
                link=link
            )
            # Update bookmark title.
            bookmark.title = form.cleaned_data['title']
            # If the bookmark is being updated, clear old tag list.
            if not created:
                bookmark.tag_set.clear()
            # Create new tag list.
            tag_names = form.cleaned_data['tags'].split()
            for tag_name in tag_names:
                tag, dummy = Tag.objects.get_or_create(name=tag_name)
                bookmark.tag_set.add(tag)
            # Save bookmark to database.
            bookmark.save()
            return HttpResponseRedirect(
                '/bookmarks/user/%s/' % request.user.username
            )
    else:
        form = BookmarkSaveForm()
    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response('bookmarks/bookmark_save.html', variables)

def tag_page(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    bookmarks = tag.bookmarks.order_by('-id')
    variables = RequestContext(request, {
        'bookmarks': bookmarks,
        'tag_name': tag_name,
        'show_tags': True,
        'show_user': True
    })
    return render_to_response('bookmarks/tag_page.html', variables)

def tag_cloud_page(request):
    MAX_WEIGHT = 5
    tags = Tag.objects.order_by('name')
    # Calculate tag, min and max counts.
    min_count = max_count = tags[0].bookmarks.count()
    for tag in tags:
        tag.count = tag.bookmarks.count()
        if tag.count < min_count:
            min_count = tag.count
            if max_count < tag.count:
                max_count = tag.count
     # Calculate count range. Avoid dividing by zero.
    range = float(max_count - min_count)
    if range == 0.0:
        range = 1.0
        # Calculate tag weights.
    for tag in tags:
        tag.weight = int(
            MAX_WEIGHT * (tag.count - min_count) / range)
    variables = RequestContext(request, {
        'tags': tags
    })
    return render_to_response('bookmarks/tag_cloud_page.html', variables)











