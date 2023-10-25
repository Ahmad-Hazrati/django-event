from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Event, Comment, Category
from .forms import CommentForm

# Import Pagination stuff
from django.core.paginator import Paginator


def eventlist(request):
    event_list = Event.objects.all().order_by("-created_on")
    p = Paginator(Event.objects.all(), 3)
    page = request.GET.get("page")
    events = p.get_page(page)
    nums = "a" * events.paginator.num_pages
    return render(
        request, "home.html",
        {"event_list": event_list, "events": events, "nums": nums}
    )


def event_detail(request, slug, *args, **kwargs):
    """
    A function-based view to view the detail of a post.
    """
    queryset = Event.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    registered = request.user.events.filter(slug=slug).exists()
    participant_count = post.participants.all().count()
    liked = False
    commented = False

    if post.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment awaiting moderation."
            )
        else:
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(
        request,
        "event_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "liked": liked,
            "comment_form": comment_form,
            "participant_count": participant_count,
            "registered": registered,
        },
    )


def event_like(request, slug, *args, **kwargs):
    """
    The view to update the likes.
    """
    post = get_object_or_404(Event, slug=slug)

    if request.method == "POST" and request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.add_message(
                request, messages.SUCCESS, "You unliked this event!")
        else:
            post.likes.add(request.user)
            messages.add_message(
                request, messages.SUCCESS, "You liked this event!")

    return HttpResponseRedirect(reverse("event_detail", args=[slug]))


def registeration_confirmation(request, slug):
    event = Event.objects.get(slug=slug)
    if request.method == "POST":
        event.participants.add(request.user)
        messages.add_message(
            request, messages.SUCCESS,
            "You have successfully registered to the event!"
        )
        return redirect("event_detail", slug)

    return render(request, "event_confirmation.html", {"event": event})


def comment_delete(request, slug, comment_id, *args, **kwargs):
    """View to delete comment"""
    comment = Comment.objects.get(id=comment_id)

    if comment.name == request.user.username:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("event_detail", args=[slug]))


def comment_edit(request, slug, comment_id, *args, **kwargs):
    """
    view to edit comments
    """
    if request.method == "POST":
        queryset = Event.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = post.comments.filter(id=comment_id).first()

        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.name == request.user.username:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(
                request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("event_detail", args=[slug]))


def CategoryView(request, cats):
    """
    View to show the events based on the category
    """
    category = Category.objects.get(slug=cats)
    category_events = Event.objects.filter(category=category)

    return render(
        request,
        "category.html",
        {"cats": cats.title(), "category_events": category_events},
    )


def search_events(request):
    """
    View to list the events based on the matching keyword
    typed in the search bar.
    """
    if request.method == "POST":
        search = request.POST["search"]
        events = Event.objects.filter(name__icontains=search)
        return render(
            request, "search_events.html", {"search": search, "events": events}
        )
    else:
        return render(request, "search_events.html", {})
