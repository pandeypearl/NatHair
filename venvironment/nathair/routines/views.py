from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import HairRoutine, RoutineStep
from products.models import HairProduct
from .forms import HairRoutineForm, RoutineStepForm, DeleteRoutineStepForm, PublishRoutineForm

# Create your views here.
login_required(login_url='login')
def create_routine(request):
    template = 'create_routine.html'
    form = HairRoutineForm(request.POST)
    
    if request.method == 'POST':
        form = HairRoutineForm(request.POST)
        if form.is_valid():
            routine = form.save(commit=False)
            routine.user = request.user
            routine.name = form.cleaned_data['name'] 
            routine.description = form.cleaned_data['description'] 
            routine.notes = form.cleaned_data['notes']

            routine.save()
            messages.success(request, 'New hair routine created successfully.')
            return redirect('routine_detail', routine_id=routine.id)
        else:
            messages.warning(request, 'Something went wrong. Please try again.')
    else:
        form: HairRoutineForm()

    context = {
        'form': form,
    }

    return render(request, template, context)


login_required(login_url='login')
def routines_list(request):
    template= 'routines_list.html'
    routines = HairRoutine.objects.all()
    # routines = HairRoutine.objects.filter(is_draft=False)

    context = {
        'routines': routines,
    }

    return render(request, template, context)


login_required(login_url='login')
def routine_detail(request, routine_id):
    template = 'routine_detail.html'
    routine = get_object_or_404(HairRoutine, id=routine_id)
    routine_steps = RoutineStep.objects.filter(hair_routine=routine)
    form = RoutineStepForm(request.POST, request.FILES)
    publish_form = PublishRoutineForm()

    if request.method == 'POST':
        if 'delete_step' in request.POST:
            delete_form = DeleteRoutineStepForm(request.POST, request.FILES)
            if delete_form.is_valid():
                step_id_to_delete = delete_form.cleaned_data['routine_step_id']
                step_to_delete = get_object_or_404(RoutineStep, pk=step_id_to_delete)
                step_to_delete.delete()
                messages.success(request, 'Routine step deleted')
                return redirect('routine_detail', routine_id=routine_id)
            else:
                for field, errors in delete_form.errors.items():
                    for error in errors:
                        messages.warning(request, f"Error in {field}: {error}")
                    return redirect('routine_detail', routine_id=routine_id)
        elif 'publish_routine' in request.POST:
            publish_form = PublishRoutineForm(request.POST)
            if publish_form.is_valid():
                routine.publish()
                messages.success(request, 'Hair Routine published successfully.')
                return redirect('routine_detail', routine_id=routine_id)
        else:
            form = RoutineStepForm(request.POST, request.FILES)
            if form.is_valid():
                step = form.save(commit=False)
                step.title = form.cleaned_data['title']
                step.description = form.cleaned_data['description']
                step.product = form.cleaned_data['product']
                step = RoutineStep.objects.create(
                    hair_routine=routine,
                    title=step.title,
                    description=step.description,
                    product=step.product
                )
                step.save()
                messages.success(request, 'Routine step added.')
                return redirect('routine_detail', routine_id=routine_id)
            else:
                messages.warning(request, 'Something went wrong. Please try again.')
                return render(request, template, {'form': RoutineStepForm})
    else:
        form: RoutineStepForm()
        delete_form = DeleteRoutineStepForm()

    context = {
        'routine': routine,
        'routine_steps': routine_steps,
        'form': form,
        'delete_form': delete_form,
        'publish_form': publish_form,
    }

    return render(request, template, context)


login_required(login_url='login')
def delete_routine(request, pk):
    template = 'delete_routine.html'
    routine = get_object_or_404(HairRoutine, pk=pk)
    routine_steps = RoutineStep.objects.filter(hair_routine=routine)

    if request.method == 'POST':
        routine.delete()
        messages.success(request, 'Your Routine has been deleted.')
        return redirect('routines_list')
    
    context = {
        'routine': routine,
        'routine_steps': routine_steps,
    }

    return render(request, template, context)



            
