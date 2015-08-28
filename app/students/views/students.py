from django.shortcuts import render, redirect


def students_list(request):
    students = (
        {
            'id': 1,
            'first_name': 'aaa',
            'last_name': 'bbb',
            'ticket': 234,
            'image': 'p.jpg',
        },
        {
            'id': 2,
            'first_name': '333',
            'last_name': 'eee',
            'ticket': 34,
            'image': 'p.jpg',
        },
        {
            'id': 3,
            'first_name': '44',
            'last_name': 'gfgd',
            'ticket': 565,
            'image': 'p.jpg',
        },
    )

    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return render(request, 'students/students_edit.html', {})


def students_edit(request, sid):
    return render(request, 'students/students_edit.html', {})


def students_delete(request, sid):
    return redirect('home')
