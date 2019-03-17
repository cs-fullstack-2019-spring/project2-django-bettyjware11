from django.shortcuts import render, HttpResponse, _get_queryset
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from .forms import WikiPostsModel, WikiPostsForm, RelatedModel, RelatedForm, AuthorModel, AuthorForm
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
import operator
import re
from django.db.models import Q


# function to show all entries at index
def index(request):
    allEntries = WikiPostsModel.objects.all()
    context = {
        "allEntries": allEntries
    }
    print()
    return render(request, 'Project2App/index.html', context)



# function is redundanf...might delete...
def allEntries(request):
    entry_list = WikiPostsModel.objects.all()
    context = {'entry_list': entry_list}
    return render(request, 'Project2App/allEntries.html', context)

# function to allow entering new wiki posts if user is logged in
@login_required
def yourEntries(request):
    # If the current person is logged in, do the code below
    if request.user.is_authenticated:
        # This puts the logged in user entry into the variable author
        author= AuthorModel.objects.get(id=1)
        # This will grab all of the entries for the logged in user using the variable you just created
        allEntries = WikiPostsModel.objects.filter(foreignkeyToAuthor=author).order_by('id')
    # If the user is not logged in...
    else:
        # Make all Entries blank because you need this because both the index.html page is expecting a allEntries variable
        allEntries = ""
    context = {"allEntries": allEntries}
    return render(request, "Project2App/index.html", context)



# This page will provide a form to add users
def createUser(request):
    # POST Request
    # If the form is being pushed to this function
    if request.method == "POST":
        print(request.method)
        # This will put all the user's information from the HTML page into this new form variable
        form = AuthorForm(request.POST)
        # Run all the validation on this form
        if form.is_valid():
            # Save the form's information in the model
            form.save()
            # Create a new Django User entry
            User.objects.create_user(request.POST["username"], request.POST["password1"], request.POST["password2"])
            return redirect("index")
        else:
            context = {
                "errors": form.errors,
                "form": form
            }
            return render(request, "Project2App/createUser.html", context)


    # GET Request
    else:
        # This will create a blank form using AuthorForm
        form = AuthorForm()
        context = {"form": form}
        return render(request, "Project2App/createUser.html", context)


# Allows the edit of user information
def editUser(request, username):
    user = get_object_or_404(User, pk=username)
    edit_form = AuthorForm(request.POST or None, instance=AuthorModel)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')

    return render(request, 'Project2App/createUser.html', {'userform': edit_form})


def deleteuser(request, username):
    user = get_object_or_404(User, pk=username)
    if request.method == 'POST':
        user.delete()
        return redirect('index')

    return render(request, 'Project2App/delete.html', {'selecteduser': user})


# this function allow only logged in users to add new wiki posts
def addNewEntry(request):
    # This will create a blank form using CollectorForm
    form = WikiPostsForm()
    context = {
        "form": form
    }
    return render(request, "Project2App/addNewEntry.html", context)


def gotNewEntryInfo(request):
    # This will put all the user's information from the HTML page into this new form variable
    form = WikiPostsForm(request.POST)
    # This puts the logged in user entry into the variable collector
    author = AuthorModel.objects.get(username=request.user)

    # create a wiki post entry from the logged in user
    if form.is_valid():
        # Created a new WikiPostModel entry usin the user's form information that was passed using the request.POST
        WikiPostsModel.objects.create(postTitle=request.POST["postTitle"], postText=request.POST["postText"],
                                      createdDateTime=request.POST["createdDateTime"],
                                      lastUpdatedDateTime=request.POST["lastUpdatedDateTime"],
                                      optionalPostImage=request.POST["optionalPostImage"],
                                      foreignKeyToAuthor=author)
        return redirect("index")
    else:
        context = {"form": form, "errors": form.errors}
        return render(request, "Project2App/addNewEntry.html", context)


# this function allows the edit of wiki post entries
def editEntries(request, wikipostsID):
    # Grab an exact entry of the WikiPostsModel using the primary key
    editExistingWikiPost = get_object_or_404(WikiPostsModel, pk=wikipostsID)

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
        "wikipostsID": wikipostsID
    }
    return render(request, "Project2App/editEntries.html", context)


def deleteEntries(request, wikipostsID):
    deleteThisWikiPost = get_object_or_404(WikiPostsModel, pk=wikipostsID)
    deleteThisWikiPost.delete()
    return redirect("index")


def relatedEntries(request):
    related_list = RelatedModel.objects.all()
    context = {
        "related_list": related_list
    }
    return render(request, 'Project2App/index.html', context)


def addRelated(request):
    # This will create a blank form using CollectorForm
    form = RelatedForm()
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
        RelatedModel.objects.create(itemTitle=request.POST["itemTitle"], itemText=request.POST["itemText"],
                                    createdDateTime=request.POST["createdDateTime"],
                                    lastUpdatedDateTime=request.POST["lastUpdatedDateTime"],
                                    optionalPostImage=request.POST["optionalPostImage"], foreignKeyToUser=User)
        return redirect("index")
    else:
        context = {"form": form, "errors": form.errors}
        return render(request, "Project2App/addRelated.html", context)


def editRelated(request, relatedID):
    # Grab an exact entry of the RelatedModel using the primary key
    editExistingRelated = get_object_or_404(RelatedModel, pk=relatedID)

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
        "relatedID": relatedID
    }
    return render(request, "Project2App/editRelated.html", context)


def deleteRelated(request, relatedID):
    deleteThisRelated = get_object_or_404(RelatedModel, pk=relatedID)
    deleteThisRelated.delete()
    return redirect("index")


def searchPosts(request):
    return HttpResponse("search here")
