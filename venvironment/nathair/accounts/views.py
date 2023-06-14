"""
    Module for account views.
"""
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import  reverse_lazy
from django.views.generic import View, CreateView, UpdateView, TemplateView
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.contrib.auth import login
from .forms import HairProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin




# User Sign Up View.
class SignUpView(CreateView):
    """
        Class based view to send account activation details 
        via email when signing up.
    """
    form_class = SignUpForm
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            #user will be inactive until confirmation
            user.is_active = False 
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate your NatHair Account'
            message = render_to_string('emails/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            messages.success(request, ('Please confirmyour email to complete your NatHair registration'))

            return redirect('login')

        return render(request, self.template_name, {'form': form})

# Activate User Account
class ActivateAccount(View):
    """
        Class based view will check if user exists and if token is valid,
        then set user.is_active = True, user.profile.email_confirmed = True, 
        and log in user.
    """
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_encode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login(request.user)
            messages.success(request, ('Your NatHair account has been confirmed.'))
            return redirect('home')
        else:
            messages.warning(request, ('The confirmation link was invalid. It possibly has already been used.'))
            return redirect('home')

# User Edit Profile View.
class ProfileView(UpdateView):
    """
        Class based view to change/update user profile information.
    """
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'profile.html'

# User Hair Profile View
class HairProfileUpdateView(LoginRequiredMixin, TemplateView):
    form = HairProfileForm
    template_name = 'hair-profile-update.html'

    def post(self, request):

        post_data = request.POST or None

        form = HairProfileForm(post_data, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your Hair Profile Has Been Updated')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(form=form)

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
