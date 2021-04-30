from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    room_name = "room_name"
    return render(request, 'chatPrivate.html', {
         'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    })
    # return render(request, 'index.html', {})

# @login_required
def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    })

# def index(request):
#     return render(request, 'index.html')
#     # return render(request, 'searchh.html')