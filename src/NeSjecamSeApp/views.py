from django.shortcuts import render
from .models import Note

def notes_list(request):
    notes = Note.objects.order_by('last_edited_date')
    return render(request, 'NeSjecamSeApp/notes_list.html', {'all_notes' : notes})
