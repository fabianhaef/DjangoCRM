from django.shortcuts import reverse
from django.core.mail import send_mail
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth import views as auth_views, authenticate, login
from .models import Lead
from .forms import LeadModelForm, CustomUserCreationForm

"""

class LoginView(auth_views.LoginView):
    template_name = 'registration/login.html'


    def get_success_url(self):
        return reverse("leads")
"""


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LandingPageView(TemplateView):
    template_name = 'landing.html'


class LeadListView(ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


class LeadCreateView(CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        # TODO send email
        send_mail(
            subject="A Lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@mail.com"]
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(UpdateView):
    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadDeleteView(DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")
