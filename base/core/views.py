from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, TemplateView

from .models import Property


class HomeView(ListView):
    model = Property
    template_name = "home.html"
    # setting ordering to newest to oldest
    ordering = ['-listed_date']
