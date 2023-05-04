from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import TeacherForm
from .models import Teacher


def teacher_create(request):
    """Create a new teacher."""
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("update_teacher", args=(form.instance.id,)))
    else:
        form = TeacherForm()
    return render(request, "new_teacher.html", {"title": "Create teacher", "form": form})


def update_teacher(request, id: int):
    """Update teacher."""
    try:
        current_teacher = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return HttpResponseRedirect(reverse("update_teacher"))
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=current_teacher)
        if not form.is_valid():
            return HttpResponseRedirect(reverse("new_teacher"))
        form.save()
    else:
        form = TeacherForm(instance=current_teacher)
    return render(request, "update_teacher.html", {"title": "Update teacher", "form": form})


def delete_teacher(request, id: int):
    """Delete teacher."""
    try:
        current_teacher = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return HttpResponseRedirect(reverse("update_teacher"))
    if request.method == "POST":
        current_teacher.delete()
        return HttpResponseRedirect(reverse("teachers_list"))
    else:
        context = {"title": "Delete teacher", "teacher": current_teacher}
    return render(request, "delete_teacher.html", context)


def get_teachers_list(request):
    """Get all teachers."""
    teachers = Teacher.objects.all().values()
    return render(
        request, "all_teachers.html", {"teachers": teachers, "title": "All teachers"}
    )
