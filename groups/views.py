from django.shortcuts import render, redirect

from .models import Group

import random, string

#Create a new group
def create_group(request):
    if request.method == "POST":
        name = request.POST["name"]
        u_id = generate_id()
        Group.objects.create(name=name, u_id=u_id)
        return redirect("index")

#Display group
def group(request, u_id):
    group = Group.objects.get(u_id=u_id)
    return render(request, "groups/group.html", {"group": group})

#Generate unique group id
def generate_id():
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
