from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class HomePageView(View):
    '''handles homepage requests'''
    template_name = 'photo/index.html'

    def get(self, request):
        return render(request, self.template_name)


class DashboardView(View):
    '''displays dashboard'''
    template_name = 'photo/dashboard.html'

    def get(self, request):
        social_user = request.user.social_auth.filter(provider='facebook').first()
        context = {'social_user': social_user}
        return render(request, self.template_name, context)
