from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):
	return render_to_response(BASE_DIR + '/feed/friktion/index.html')

