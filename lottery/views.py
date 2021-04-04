from django.shortcuts import render
from django.utils import timezone
from .models import Lottery

def lottery_list(request):
    posts = Lottery.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'lottery/lottery_list.html', {'posts':posts})

