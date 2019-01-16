from django.shortcuts import render, redirect

from .models import Post
from groups.models import Group

#Google imports
from google.cloud import storage

#Python imports
import random, string, os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="creds.json"

#Upload photo and create post
def upload_photo(request):
    if request.method == "POST":
        group = Group.objects.get(u_id=request.POST["group_u_id"])
        post_u_id = generate_post_id()
        description = request.POST["description"]

        storage_client = storage.Client()
        bucket = storage_client.get_bucket("tack-media-store")
        blob = bucket.blob(post_u_id)

        photo = request.FILES["file"]
        blob.upload_from_file(photo, content_type=photo.content_type)
        blob.make_public()

        new_post = Post.objects.create(u_id=post_u_id, url=blob.public_url,
                                        description=description)
        group.posts.add(new_post)
        return redirect("group", u_id=request.POST["group_u_id"])

#Generate unique post id
def generate_post_id():
    unique = False
    random_id = 0

    #Check if id already exists
    while not unique:
        random_id = ''.join([random.choice(string.ascii_letters +
            string.digits) for n in range(11)])

        if Post.objects.filter(u_id=random_id).exists():
            unique = False
        else:
            unique = True

    return random_id
