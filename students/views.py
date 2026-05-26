from datetime import date, timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Student, Batch, FeePackage
from .forms import StudentForm, BatchForm, FeePackageForm


@login_required
def home(request):
    query = request.GET.get('q')
    students = []

    if query:
        students = Student.objects.filter(name__icontains=query)

    return render(request, 'students/home.html', {
        'students': students
    })


@login_required
def students_list(request):
    query = request.GET.get('q')
    students = Student.objects.all()

    if query:
        students = students.filter(name__icontains=query)

    return render(request, 'students/students.html', {
        'students': students
    })


@login_required
def add_student(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('students')

    return render(request, 'students/add_student.html', {
        'form': form
    })


@login_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)

        if form.is_valid():
            form.save()
            return redirect('students')

    return render(request, 'students/edit_student.html', {
        'form': form
    })


@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()

    return redirect('students')


@login_required
def fee_pending(request):
    today = date.today()
    next_week = today + timedelta(days=7)

    students = Student.objects.filter(fee_end_date__lte=next_week)

    return render(request, 'students/fee_pending.html', {
        'students': students
    })


@login_required
def batches(request):
    query = request.GET.get('q')
    batches = Batch.objects.all()

    if query:
        batches = batches.filter(name__icontains=query)

    return render(request, 'students/batches.html', {
        'batches': batches
    })


@login_required
def add_batch(request):
    form = BatchForm()

    if request.method == 'POST':
        form = BatchForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('batches')

    return render(request, 'students/add_batch.html', {
        'form': form
    })


@login_required
def edit_batch(request, id):
    batch = get_object_or_404(Batch, id=id)
    form = BatchForm(instance=batch)

    if request.method == 'POST':
        form = BatchForm(request.POST, instance=batch)

        if form.is_valid():
            form.save()
            return redirect('batches')

    return render(request, 'students/edit_batch.html', {
        'form': form
    })


@login_required
def delete_batch(request, id):
    batch = get_object_or_404(Batch, id=id)
    batch.delete()

    return redirect('batches')


@login_required
def batch_details(request, id):
    batch = get_object_or_404(Batch, id=id)
    students = Student.objects.filter(batch=batch)

    return render(request, 'students/batch_details.html', {
        'batch': batch,
        'students': students
    })


@login_required
def fee_packages(request):
    packages = FeePackage.objects.all()

    return render(request, 'students/fee_packages.html', {
        'packages': packages
    })


@login_required
def add_fee_package(request):
    form = FeePackageForm()

    if request.method == 'POST':
        form = FeePackageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('fee_packages')

    return render(request, 'students/add_fee_package.html', {
        'form': form
    })


@login_required
def edit_fee_package(request, id):
    package = get_object_or_404(FeePackage, id=id)
    form = FeePackageForm(instance=package)

    if request.method == 'POST':
        form = FeePackageForm(request.POST, instance=package)

        if form.is_valid():
            form.save()
            return redirect('fee_packages')

    return render(request, 'students/edit_fee_package.html', {
        'form': form
    })


@login_required
def delete_fee_package(request, id):
    package = get_object_or_404(FeePackage, id=id)
    package.delete()

    return redirect('fee_packages')