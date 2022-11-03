from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def search_box(request):
    pass

def subscription(request):
    pass

def followers(request):
    pass