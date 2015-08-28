from django.shortcuts import render, redirect


def journal(request):
    return render(request, 'students/journal.html', {})
