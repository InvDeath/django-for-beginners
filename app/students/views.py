from django.shortcuts import render, redirect

def students_list(request):
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

    return render(request, 'students/students_list.html', {'students': students})

def groups_list(request):
    groups = (
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

    return render(request, 'students/groups_list.html', {'groups': groups})

def journal(request):
    return render(request, 'students/journal.html', {})

def add_student(request):
    return render(request, 'students/students_edit.html', {})

def edit_student(request, sid):
    return render(request, 'students/students_edit.html', {})

def delete_student(request, sid):
    return redirect('home')


def add_group(request):
    return render(request, 'students/groups_edit.html', {})

def edit_group(request, gid):
    return render(request, 'students/groups_edit.html', {})

def delete_group(request, gid):
    return redirect('index')
