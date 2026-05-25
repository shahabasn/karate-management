from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'students/',
        views.students_list,
        name='students'
    ),

    path(
        'add-student/',
        views.add_student,
        name='add_student'
    ),

    path(
        'edit-student/<int:id>/',
        views.edit_student,
        name='edit_student'
    ),

    path(
        'delete-student/<int:id>/',
        views.delete_student,
        name='delete_student'
    ),

    path(
        'fee-pending/',
        views.fee_pending,
        name='fee_pending'
    ),

    # BATCHES
    path(
        'batches/',
        views.batches,
        name='batches'
    ),

    path(
        'add-batch/',
        views.add_batch,
        name='add_batch'
    ),

    path(
        'edit-batch/<int:id>/',
        views.edit_batch,
        name='edit_batch'
    ),

    path(
        'delete-batch/<int:id>/',
        views.delete_batch,
        name='delete_batch'
    ),

    # IMPORTANT 🔥
    path(
        'batch-details/<int:id>/',
        views.batch_details,
        name='batch_details'
    ),
    path(
    'fee-packages/',
    views.fee_packages,
    name='fee_packages'
),

path(
    'add-fee-package/',
    views.add_fee_package,
    name='add_fee_package'
),

path(
    'delete-fee-package/<int:id>/',
    views.delete_fee_package,
    name='delete_fee_package'
),
]