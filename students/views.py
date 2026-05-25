from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import Student

from .forms import StudentForm
from .models import Student, Batch ,FeePackage

from .forms import (
    StudentForm,
    BatchForm
)
@login_required


# HOME PAGE
def home(request):
    
    query = request.GET.get('q')

    students = []

    if query:

        students = Student.objects.filter(
            name__icontains=query
        )

    return render(

        request,

        'students/home.html',

        {
            'students': students
        }
    )



# STUDENTS LIST
def students_list(request):
    
    query = request.GET.get('q')

    students = Student.objects.all()

    if query:

        students = students.filter(
            name__icontains=query
        )

    return render(

        request,

        'students/students.html',

        {
            'students': students
        }
    )


# ADD STUDENT
def add_student(request):

    form = StudentForm()

    if request.method == 'POST':

        form = StudentForm(

            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect('students')


    return render(

        request,

        'students/add_student.html',

        {
            'form': form
        }
    )


# DELETE STUDENT
def delete_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    student.delete()

    return redirect('students')
# EDIT STUDENT
def edit_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    form = StudentForm(
        instance=student
    )

    if request.method == 'POST':

        form = StudentForm(

            request.POST,
            request.FILES,

            instance=student
        )

        if form.is_valid():

            form.save()

            return redirect('students')


    return render(

        request,

        'students/edit_student.html',

        {
            'form': form
        }
    )
    # FEE PENDING
def fee_pending(request):

    today = date.today()

    next_week = today + timedelta(days=7)

    students = Student.objects.filter(

        fee_end_date__lte=next_week
    )

    return render(

        request,

        'students/fee_pending.html',

        {
            'students': students
        }
    )
    # ALL BATCHES
def batches(request):

    batches = Batch.objects.all()

    return render(

        request,

        'students/batches.html',

        {
            'batches': batches
        }
    )


# ADD BATCH
def add_batch(request):

    form = BatchForm()

    if request.method == 'POST':

        form = BatchForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('batches')


    return render(

        request,

        'students/add_batch.html',

        {
            'form': form
        }
    )


# DELETE BATCH
def delete_batch(request, id):

    batch = get_object_or_404(
        Batch,
        id=id
    )

    batch.delete()

    return redirect('batches')
# EDIT BATCH
def edit_batch(request, id):

    batch = get_object_or_404(
        Batch,
        id=id
    )

    form = BatchForm(
        instance=batch
    )

    if request.method == 'POST':

        form = BatchForm(

            request.POST,

            instance=batch
        )

        if form.is_valid():

            form.save()

            return redirect('batches')


    return render(

        request,

        'students/edit_batch.html',

        {
            'form': form
        }
    )
    # BATCH DETAILS
def batch_details(request, id):

    batch = get_object_or_404(
        Batch,
        id=id
    )

    students = Student.objects.filter(
        batch=batch
    )

    return render(

        request,

        'students/batch_details.html',

        {
            'batch': batch,
            'students': students
        }
    )
# ALL PACKAGES
def fee_packages(request):

    packages = FeePackage.objects.all()

    return render(

        request,

        'students/fee_packages.html',

        {
            'packages': packages
        }
    )


# ADD PACKAGE
def add_fee_package(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        days = request.POST.get('days')

        FeePackage.objects.create(

            name=name,
            days=days
        )

        return redirect('fee_packages')


    return render(

        request,

        'students/add_fee_package.html'
    )


# DELETE PACKAGE
def delete_fee_package(request, id):

    package = get_object_or_404(
        FeePackage,
        id=id
    )

    package.delete()

    return redirect('fee_packages')