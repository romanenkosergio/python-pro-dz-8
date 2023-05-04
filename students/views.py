from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import StudentForm
from .models import Student


def home(request):
    """Home page."""
    return render(request, "home.html", {"title": "Home"})


def student_create(request):
    """Create a new student."""
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("update_student", args=(form.instance.id,)))
    else:
        form = StudentForm()
    return render(request, "new_student.html", {"title": "Create Student", "form": form})


def update_student(request, id: int):
    """Update Student."""
    try:
        current_student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponseRedirect(reverse("update_student"))
    if request.method == "POST":
        form = StudentForm(request.POST, instance=current_student)
        if not form.is_valid():
            return HttpResponseRedirect(reverse("new_student"))
        form.save()
    else:
        form = StudentForm(instance=current_student)
    return render(request, "update_student.html", {"title": "Update Student", "form": form})


def delete_student(request, id: int):
    """Delete student."""
    try:
        current_student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponseRedirect(reverse("update_student"))
    if request.method == "POST":
        current_student.delete()
        return HttpResponseRedirect(reverse("students_list"))
    else:
        context = {"title": "Delete Student", "student": current_student}
    return render(request, "delete_student.html", context)


def get_students_list(request):
    """Get all students."""
    students = Student.objects.all().values()
    return render(
        request, "all_students.html", {"students": students, "title": "All Students"}
    )
