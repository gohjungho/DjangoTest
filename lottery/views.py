from django.shortcuts import render

def lottery_list(request):
    return render(request, 'lottery/lottery_list.html', {})
