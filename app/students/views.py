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
            'title': 'aaa',
            'leader': {
                'id': 2,
                'first_name': 'asd',
                'last_name': 'sadd',
            },
        }, {
            'id': 2,
            'title': 'eee',
            'leader': {
                'id': 2,
                'first_name': 'qwq',
                'last_name': 'sadd',
            },
        }, {
            'id': 3,
            'title': 'aa32a',
            'leader': {
                'id': 2,
                'first_name': 'asd',
                'last_name': 'sadd',
            },
        },
    )

    return render(request, 'students/groups_list.html', {'groups': groups})


def journal(request):
    return render(request, 'students/journal.html', {})


def students_add(request):
    return render(request, 'students/students_edit.html', {})


def students_edit(request, sid):
    return render(request, 'students/students_edit.html', {})


def students_delete(request, sid):
    return redirect('home')


def groups_add(request):
    return render(request, 'students/groups_edit.html', {})


def groups_edit(request, gid):
    return render(request, 'students/groups_edit.html', {})


def groups_delete(request, gid):
    return redirect('home')
