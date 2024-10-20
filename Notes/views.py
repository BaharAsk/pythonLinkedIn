from django.shortcuts import render

from .models import Notes

def list(request):
    all_notes=Notes.objects.all()
    return render(request,'Notes/notes_list.html',{'Notes':all_notes})


def detail(request,pk):
    note=Notes.objects.get(pk=pk)
    return render(request,'Notes/notes_detail.html',{'note':note})
