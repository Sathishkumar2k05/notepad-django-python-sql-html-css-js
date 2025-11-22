from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *

class NotePadListView(View):

    def get(self,request):

        context = {
            "notepad":NotePad.objects.all()
        }

        return render(request, 'notepad_list.html', context)
    
class NotePadDetailView(View):

    def get(self, request, id):

        context = {
            "note":NotePad.objects.get(id=id)
        }

        return render(request, 'notepad_detail.html', context)
    
class NotePadAddView(View):

    def get(self, request):

        context = {
            "notepad_form":NotePadForm()
        }

        return render(request, 'notepad_add.html', context)
    
    def post(self, request):

        notepad_form = NotePadForm(request.POST)

        if notepad_form.is_valid():

            notepad_form.save()

        return redirect("notepad_list")

class NotePadEditView(View):

    def get(self, request, id):

        selected_note = NotePad.objects.get(id=id)

        context = {
            "notepad_form":NotePadForm(instance=selected_note)
        }

        return render(request, 'notepad_add.html', context)
    
    def post(self, request, id):

        selected_note = NotePad.objects.get(id=id)

        notepad_form = NotePadForm(request.POST, instance = selected_note)

        if notepad_form.is_valid():

            notepad_form.save()

        return redirect("notepad_list")
    
class NotePadDeleteView(View):

    def get(self, request, id):

        selected_note = NotePad.objects.get(id = id)

        selected_note.delete()

        return redirect("notepad_list")


    