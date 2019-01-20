from django.shortcuts import render, redirect
from django.http import request
from django.urls import reverse

from .models import Group

import random, string

#Create a new group
def create_group(request):
    if request.method == "POST":
        name = request.POST["name"]
        u_id = generate_group_id()
        Group.objects.create(name=name, u_id=u_id)
        return redirect("info", u_id=u_id)

#Display group
def group(request, u_id):
    group = Group.objects.get(u_id=u_id)
    posts = group.posts.all().order_by('-date')
    return render(request, "groups/group.html", {"group": group, "posts": posts})

#Display group info
def info_page(request, u_id):
    group = Group.objects.get(u_id=u_id)
    url = request.build_absolute_uri(reverse("group", args=[group.u_id])) #Get absolute URL
    return render(request, "groups/group_info.html", {"group": group, "url": url})

#Generate unique group id
def generate_group_id():
    unique = False
    random_id = 0

    #Check if id already exists
    while not unique:
        random_id = ''.join([random.choice(string.ascii_letters +
            string.digits) for n in range(8)])

        if Group.objects.filter(u_id=random_id).exists():
            unique = False
        else:
            unique = True

    return random_id
