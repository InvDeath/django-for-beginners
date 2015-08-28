from django.shortcuts import render, redirect


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


def groups_add(request):
    return render(request, 'students/groups_edit.html', {})


def groups_edit(request, gid):
    return render(request, 'students/groups_edit.html', {})


def groups_delete(request, gid):
    return redirect('home')
