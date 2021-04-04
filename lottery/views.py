from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Lottery

def lottery_list(request):
    posts = Lottery.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'lottery/lottery_list.html', {'posts':posts})

def lottery_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'lottery/lottery_detail.html', {'post': post})