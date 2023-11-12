from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def together(request):
  template = loader.get_template('base.html')
  return HttpResponse(template.render())

def base(request):
  template = loader.get_template('base.html')
  return HttpResponse(template.render())

def ina(request):
  template = loader.get_template('ina.html')
  return HttpResponse(template.render())

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())