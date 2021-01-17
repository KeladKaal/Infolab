from django.contrib.auth.forms import PasswordChangeForm
from django.db.models.signals import post_save
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, resolve_url
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from .forms import LoginForm, UserRegistrationForm
from catalog.models import Clubs
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin


def show_clubs(request):
    club_list = Clubs.objects.order_by('clubs_id')
    template = loader.get_template('catalog/show_clubs.html')
    context = {
        'club_list': club_list,
    }
    return render(request, 'catalog/show_clubs.html', context)


def wow(request):
    return render(request, 'registration/wow.html')


def detail(request, clubs_id):
    try:
        clubs = Clubs.objects.get(pk=clubs_id)
    except Clubs.DoesNotExist:
        raise Http404("Club does not exist")
    return render(request, 'catalog/detail.html', {'clubs': clubs})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:

                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:

                    return HttpResponse('Disabled account')
            else:

                return HttpResponse('Invalid login')
    else:
        print('d'),
        form = LoginForm()
    return render(request, 'catalog/login.html', {'form': form})


@csrf_protect
@login_required
def password_change(request,
                    template_name='registration/password_change_form.html',
                    post_change_redirect=None,
                    password_change_form=PasswordChangeForm,
                    current_app=None, extra_context=None):
    if post_change_redirect is None:
        post_change_redirect = reverse('change_done')
    else:
        post_change_redirect = resolve_url(post_change_redirect)
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # Updating the password logs out all other sessions for the user
            # except the current one if
            # django.contrib.auth.middleware.SessionAuthenticationMiddleware
            # is enabled.
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
        'title': ('Password change'),
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()


post_save.connect(create_profile, sender=User)
