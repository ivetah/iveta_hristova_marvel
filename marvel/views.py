from django.views.generic.base import TemplateView
from .models import *
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.db.models import Q

class GroupsView(View):
    template_name = 'groups.html'
    def get(self, request):
        groups = Group.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(groups, 6)
        try:
            paginated_groups = paginator.page(page)
        except PageNotAnInteger:
            paginated_groups = paginator.page(1)
        except EmptyPage:
            paginated_groups = paginator.page(paginator.num_pages)
        context = {
          'groups': paginated_groups  
        }
        return render(request, self.template_name, context)

class IndexView(View):
    template_name = 'index.html'
    def get(self, request):
        characters = Character.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(characters, 6)
        try:
            paginated_characters = paginator.page(page)
        except PageNotAnInteger:
            paginated_characters = paginator.page(1)
        except EmptyPage:
            paginated_characters = paginator.page(paginator.num_pages)
        context = {
          'characters': paginated_characters  
        }
        return render(request, self.template_name, context)

class CharacterDetailsView(View):
    template_name = 'specific-character-profile.html'
    def get(self, request, *args, **kwargs):
        character = Character.objects.get(pk=self.kwargs['pk'])

        context = {
          'character': character
        }
        return render(request, self.template_name, context)

class SearchCharactersView(View):
    template_name = 'search-characters.html'
    def get(self, request, *args, **kwargs):
   
      return render(request, self.template_name, )
    
    def post(self, request, *args, **kwargs):
      data = {}
      if 'search' in request.POST:
        searched_name = request.POST.get('search', None)
        data = Character.objects.filter(Q(hero__icontains=searched_name) | Q(first_name__icontains=searched_name) | Q(last_name__icontains=searched_name))
      context = {
        'data': data,
      }
      return render(request, self.template_name, context)

class SearchGroupsView(View):
    template_name = 'search-groups.html'
    def get(self, request, *args, **kwargs):
   
      return render(request, self.template_name, )
    
    def post(self, request, *args, **kwargs):
      data = {}
      if 'search' in request.POST:
        searched_name = request.POST.get('search', None)
        data = Group.objects.filter(name__icontains=request.POST.get('search', None))
      context = {
        'data': data,
      }
      return render(request, self.template_name, context)