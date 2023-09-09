from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View
import datetime

class GetInfoView(View):
    def get(self, request):
        slack_name = request.GET.get('slack_name')
        track = request.GET.get('track')
        github_file_url = 'https://github.com/abdulmalikadebayo/HNG_X/tree/main/HNG_1'  
        github_repo_url = 'https://github.com/abdulmalikadebayo/HNG_X'  

        # current day of the week and UTC time
        current_day = datetime.datetime.now().strftime('%A')
        utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

        # Validating UTC time within +/-2 hours
        current_utc_time = datetime.datetime.strptime(utc_time, '%Y-%m-%dT%H:%M:%SZ')
        two_hours_ago = datetime.datetime.utcnow() - datetime.timedelta(hours=2)
        two_hours_later = datetime.datetime.utcnow() + datetime.timedelta(hours=2)

        if two_hours_ago <= current_utc_time <= two_hours_later:
            status_code = 200
        else:
            status_code = 400

        info = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_time,
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": status_code
        }

        return JsonResponse(info)
