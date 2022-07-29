from django.shortcuts import render, get_list_or_404
from .models import Profile
# Create your views here.
def main(request):
    return render(request, "main.html")

def profile(request):
    profile_info = Profile.objects.filter(user_id="wltn") #특정 user_id로 .. 아마 request.user 같은 거로 바꾸면 될 듯
    return render(request, "mypage.html", {'profile_infos':profile_info})

def profile_mod(request):
    return render(request, "profile_mod.html")