from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.
# class CBView(View):                            # Class Based View
#     def get(self,request):
#         return HttpResponse('Class Based Views are Cool!')

class IndexView(TemplateView):                 # Template View
    template_name = 'index1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "BASIC INJECTION"
        return context