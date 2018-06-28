from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Tarea
from .forms import TareaForm

def tarea_list(request):
    tareas = Tarea.objects.filter(created_date__lte = timezone.now()).order_by('created_date')
    return render(request, 'tarea/tarea_list.html', {'tareas' : tareas})

def tarea_detail(request, pk):
    tarea = get_object_or_404(Tarea, pk = pk)
    return render(request, 'tarea/tarea_detail.html', {'tarea' : tarea})

def tarea_new(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit = False)
            tarea.author = request.user
            tarea.created_date = timezone.now()
            tarea.save()
            return redirect('tarea_detail', pk = tarea.pk)
    else:
        form = TareaForm()
    return render(request, 'tarea/tarea_edit.html', {'form':form})

def tarea_edit(request, pk):
    tarea = get_object_or_404(Tarea, pk = pk)
    if request.method == "POST":
        form = TareaForm(request.Tarea, instance = tarea)
        if form.is_valid():
            tarea = form.save(commit = False)
            tarea.author = request.user
            tarea.created_date = timezone.now()
            tarea.save()
            return redirect('tarea_detail', pk = tarea.pk)
    else:
        form = TareaForm(instance = tarea)
    return render(request, 'tarea/tarea_edit.html', {'form':form})
