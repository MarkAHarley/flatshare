from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from flatshare.models import Flat, UserProfile
from flatshare.forms import AddFlatForm, UserProfileForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import reverse
from django.contrib.auth.models import User


def index(request):
    return render(request, 'flatshare/index.html')


def about(request):
    context_dict = {}
    if request.user.is_authenticated:
        context_dict["user_authenticated"] = True
        user = UserProfile.objects.get(user=request.user)
        context_dict['user'] = user
    return render(request, 'flatshare/about.html', context=context_dict)


def contact(request):
    context_dict = {}
    if request.user.is_authenticated:
        context_dict["user_authenticated"] = True
        user = UserProfile.objects.get(user=request.user)
        context_dict['user'] = user
    return render(request, 'flatshare/contact.html', context=context_dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(password)
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('flatshare:index'))
            else:
                return HttpResponse('Your flatshare account is disabled')
        else:
            print(f"invalid login details: {username}, {password}".format(username=username, password=password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'flatshare/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('flatshare:index'))


def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
            return redirect(reverse('flatshare:index'))
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'flatshare/signup.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def view_profile(request, username):
    context_dict = {}
    try:
        user = User.objects.get(username=username)
        user_profile = UserProfile.objects.get(user=user)
        context_dict['user_profile'] = user_profile
    except UserProfile.DoesNotExist:
        context_dict['user_profile'] = None
    return render(request, 'flatshare/user.html', context=context_dict)


@login_required
def my_matches(request):
    user_profile = UserProfile.objects.get(user=request.user)
    flat_matches = []
    for flat in user_profile.liked_flats:
        if flat.owner in user_profile.user.liked_by_set:  # TODO: complete comparison
            flat_matches.append(flat)
    return render(request, 'flatshare/matches.html', {'flat_matches': flat_matches})


def add_flat(request):
    if request.user.is_authenticated:
        form = AddFlatForm()

        if request.method == 'POST':
            form = AddFlatForm(request.POST)

            if (form.is_valid()):
            
                flat = form.save(commit=False)
                flat.save()
                return redirect('/')
            else:
                print('YIKES')
                print(form.errors)
        return render(request, 'flatshare/add_flat.html', {'form': form, })
    else:
        return HttpResponse("please log in first!")


def show_flat(request, flat_id):
    context_dict = {}
    try:
        flat = Flat.objects.get(flat_id=flat_id)
        context_dict['flat'] = flat
    except Flat.DoesNotExist:
        context_dict['flat'] = None
    return render(request, 'flatshare/flat.html', context=context_dict)


def list_flats(request):
    context_dict = {}
    SELECTED_ORDER = 'rent'
    flat_list = Flat.objects.order_by(SELECTED_ORDER)
    context_dict['flats'] = flat_list

    return render(request, 'flatshare/flats.html', context=context_dict)
