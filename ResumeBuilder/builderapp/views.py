from django.shortcuts import render, redirect, get_object_or_404
from .models import ResumeModel
from .forms import ResumeForm

def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_resume')
    else:
        form = ResumeForm()
    return render(request, 'form.html', {'form': form})

def view_resume(request):
    resumes = ResumeModel.objects.all()
    return render(request, 'view.html', {'resumes': resumes})

def edit_resume(request, id):
    resume = get_object_or_404(ResumeModel, id=id)
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('view_resume')
    else:
        form = ResumeForm(instance=resume)
    return render(request, 'edit.html', {'form': form, 'resume': resume})

def delete_resume(request, id):
    resume = get_object_or_404(ResumeModel, id=id)
    resume.delete()
    return redirect('view_resume')

def view_single(request, id):
    resume = get_object_or_404(ResumeModel, id=id)
    return render(request, 'single_view.html', {'resume': resume})