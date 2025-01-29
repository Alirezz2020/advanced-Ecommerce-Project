
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class OrderDetailView(LoginRequiredMixin,View):
    pass



class OrderCreateView(LoginRequiredMixin,View):
    pass
