from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,ListView,DetailView,
                                   TemplateView,CreateView,
                                    UpdateView,DeleteView)
from . import models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'ListDetailViewApp/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','Principal','Location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','Principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("ListDetailViewApp:list")