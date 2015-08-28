from django.shortcuts import render, redirect

def index(request):
    students = (
        {
            'id': 1,
            'first_name': 'aaa',
            'last_name': 'bbb',
            'ticket': 234,
            'image': 'img/qeqw.png',
        },
        {
            'id': 2,
            'first_name': '333',
            'last_name': 'eee',
            'ticket': 34,
            'image': 'img/qeqw.png',
        },
        {
            'id': 3,
            'first_name': '44',
            'last_name': 'gfgd',
            'ticket': 565,
            'image': 'img/qeqw.png',
        },
    )
    context = {
        'students': students,
        'groups': [],
        'calendar': [],
    }
    return render(request, 'students/index.html', context)

def add_student(request):
    return render(request, 'students/student_edit.html', {})

def edit_student(request, sid):
    return render(request, 'students/student_edit.html', {})

def delete_student(request, sid):
    return redirect('index')


def add_group(request):
    return render(request, 'students/group_edit.html', {})

def edit_group(request, gid):
    return render(request, 'students/group_edit.html', {})

def delete_group(request, gid):
    return redirect('index')
