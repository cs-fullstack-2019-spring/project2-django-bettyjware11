from django.shortcuts import render, HttpResponse, _get_queryset
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from .forms import WikiPostsModel, WikiPostsForm, UserModel, NewUserForm, RelatedModel, RelatedForm
from django.contrib.auth.models import User
import operator
import re
from django.db.models import Q
def index(request):
    entry_list = WikiPostsModel.objects.all()
    context = {'entry_list': entry_list}
    return render(request, 'Project2App/index.html', context)
# function is redundanf...might delete...
def allEntries(request):
    entry_list = WikiPostsModel.objects.all()
    context = {'entry_list': entry_list}
    return render(request, 'Project2App/allEntries.html', context)

def yourEntries(request):
    # If the current person is logged in, do the code below
    if request.user.is_authenticated:
        # This puts the logged in user entry into the variable user
        user = UserModel.objects.get(username=request.user)
        # This will grab all of the entries for the logged in user using the variable you just created
        allEntries = WikiPostsModel.objects.filter(foreignKeyToUser = user)
    # If the user is not logged in...
    else:
        # Make all Entries blank because you need this because both the index.html page is expecting a allEntries variable
        allEntries = ""
    context = {"allEntries": allEntries}
    return render(request, "Project2App/yourEntries.html", context)




# This page will provide a form to add users
def createUser(request):
    new_form = NewUserForm(request.POST or None)
    if new_form.is_valid():
        new_form.save()
        return redirect('index')

    return render(request, 'Project2App/createUser.html', {'userform': new_form})


def editUser(request, username):
    user = get_object_or_404(User, pk=username)
    edit_form = NewUserForm(request.POST or None, instance=user)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')

    return render(request, 'Project2App/createUser.html', {'userform': edit_form})

def deleteuser(request, username):
    user = get_object_or_404(User, pk=username)
    if request.method == 'POST':
        user.delete()
        return redirect('index')

    return render(request, 'Project2App/delete.html', {'selecteduser':user})



def addNewEntry(request):
    form = WikiPostsForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "form": form
    }
    return render(request, "Project2App/addNewEntry.html", context)


def gotEntryInfo(request):
    # Put all the user's info from the HTML page into a new form variable
    form = WikiPostsForm(request.POST)
    # Put the logged in user's entry into the variable collector
    user = UserModel.objects.get(username=request.user)
    # create an entry from the logged in user...
    if form.is_valid():
        WikiPostsModel.objects.create(postTitle=request.POST["postTitle"], postText=request.POST["postText"], createdDateTime =request.POST["createdDateTime"], lastUpdatedDateTime=request.POST["lastUpdatedDateTime"], optionalPostImage=request.POST["optionalPostImage"], foreignKeyToUser=user)
        return redirect("index")
    else:
        context = {"form":form, "errors":form.errors}
        return render(request, "Project2App/addNewEntry.html", context)


def editEntries(request, postTitle):
    # Grab an exact entry of the WikiPostsModel using the primary key
    editExistingWikiPost = get_object_or_404(WikiPostsModel, pk=postTitle)

    # Post method
    if request.method == "POST":
        # This will fill in the form with the user's information and use the exact WikiPostsModel with primary key
        form = WikiPostsForm(request.POST, instance=editExistingWikiPost)
        if form.is_valid():
            form.save()
        else:
            print("Form is not valid")
        return redirect("index")

    # Get method
    # Grabbed the exact wikipost form using the existing WikiPosts model using the primary key from earlier
    form = WikiPostsForm(instance=editExistingWikiPost)
    context = {
        "form": form,
        "postTitle": postTitle
    }
    return render(request, "Project2App/editEntries.html", context)


def deleteEntries(request, postTitle):
    deleteThisWikiPost = get_object_or_404(WikiPostsModel, pk=postTitle)
    deleteThisWikiPost.delete()
    return redirect("index")

def relatedEntries(request):
    related_list = RelatedModel.objects.all()
    context = {
        "related_list": related_list
    }
    return render(request, 'Project2App/index.html', context)


def addRelated(request):
    form = RelatedForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "form": form
    }
    return render(request, "Project2App/addRelated.html", context)



def gotRelatedInfo(request):
    # Put all the user's info from the HTML page into a new form variable
    form = RelatedForm(request.POST)
     # Put the logged in user's related entry into  variable
    wikipost = WikiPostsModel.objects.get(postTitle=request.user)
    # create a related entry from the logged in user...
    if form.is_valid():
        RelatedModel.objects.create(itemTitle=request.POST["itemTitle"], itemText=request.POST["itemText"], createdDateTime =request.POST["createdDateTime"], lastUpdatedDateTime=request.POST["lastUpdatedDateTime"], optionalPostImage=request.POST["optionalPostImage"], foreignKeyToUser=User)
        return redirect("index")
    else:
        context = {"form":form, "errors":form.errors}
        return render(request, "Project2App/addRelated.html", context)


def editRelated(request, itemTitle):
    # Grab an exact entry of the RelatedModel using the primary key
    editExistingRelated = get_object_or_404(RelatedModel, pk=itemTitle)

    # Post method
    if request.method == "POST":
        # This will fill in the form with the user's information and use the exact RelatedModel with primary key
        form = RelatedForm(request.POST, instance=editExistingRelated)
        if form.is_valid():
            form.save()
        else:
            print("Form is not valid")
        return redirect("index")

    # Get method
    # Grabbed the exact related form using the existing Related model using the primary key from earlier
    form = RelatedForm(instance=editExistingRelated)
    context = {
        "form": form,
        "postTitle": itemTitle
    }
    return render(request, "Project2App/editRelated.html", context)


def deleteRelated(request, itemTitle):
    deleteThisRelated = get_object_or_404(RelatedModel, pk=itemTitle)
    deleteThisRelated.delete()
    return redirect("index")





def searchPosts(request):
   return HttpResponse("search here")



