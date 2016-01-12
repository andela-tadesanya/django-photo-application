from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


# Mixins
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


# Views
class HomePageView(View):
    '''handles homepage requests'''
    template_name = 'photo/index.html'

    def get(self, request):
        # redirect to user dashboard if user is logged in
        if request.user and not request.user.is_anonymous:
            return HttpResponseRedirect(reverse('photo:user_home'))
        else:
            return render(request, self.template_name)


class DashboardView(LoginRequiredMixin, View):
    '''displays dashboard'''
    template_name = 'photo/dashboard.html'

    def get(self, request):
        social_user = request.user.social_auth.filter(provider='facebook').first()
        context = {'social_user': social_user}
        return render(request, self.template_name, context)
