from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from teachers.models import Teacher
from .forms import GroupForm
from .models import Group


def create_group(request):
    """Create a new group."""
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("update_group", args=(form.instance.id,)))
    else:
        form = GroupForm()
    return render(request, "new_group.html", {"title": "Create group", "form": form})


def update_group(request, id: int):
    """Update group."""
    try:
        current_group = Group.objects.get(id=id)
    except Group.DoesNotExist:
        return HttpResponseRedirect(reverse("update_group"))
    if request.method == "POST":
        form = GroupForm(request.POST, instance=current_group)
        if not form.is_valid():
            return HttpResponseRedirect(reverse("new_group"))
        form.save()
    else:
        form = GroupForm(instance=current_group)
    return render(request, "update_group.html", {"title": "Update group", "form": form})


def delete_group(request, id: int):
    """Delete group."""
    try:
        current_group = Group.objects.get(id=id)
    except Group.DoesNotExist:
        return HttpResponseRedirect(reverse("update_group"))
    if request.method == "POST":
        current_group.delete()
        return HttpResponseRedirect(reverse("groups_list"))
    else:
        context = {"title": "Delete group", "group": current_group}
    return render(request, "delete_group.html", context)


def get_groups_list(request):
    """Get all groups."""
    groups = Group.objects.all().values()
    for group in groups:
        group["teacher"] = Teacher.objects.get(id=group["teacher_id"])
    return render(
        request, "all_groups.html", {"groups": groups, "title": "All groups"}
    )
