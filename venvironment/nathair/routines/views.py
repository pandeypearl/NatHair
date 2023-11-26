from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import HairRoutine, RoutineStep, SavedRoutine, Comment, Like
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
    routines = HairRoutine.objects.filter(is_draft=False)

    context = {
        'routines': routines,
    }

    return render(request, template, context)


login_required(login_url='login')
def routine_detail(request, routine_id):
    template = 'routine_detail.html'
    routine = get_object_or_404(HairRoutine, id=routine_id)
    routine_steps = RoutineStep.objects.filter(hair_routine=routine)
    saved_routines_count = routine.num_saves()
    form = RoutineStepForm(request.POST, request.FILES)
    publish_form = PublishRoutineForm()

    #Getting likes and comments
    likes = routine.likes.all()
    comments = Comment.objects.filter(routine=routine, parent_comment=None).order_by('-created_at')


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
        elif 'like_routine' in request.POST:
            if request.user in routine.likes.all():
                routine.likes.remove(request.user)
                messages.success(request, 'You unliked this hair routine.')
            else:
                Like.objects.create(user=request.user, routine=routine)
                messages.success(request, 'You liked this hair routine.')
            return redirect('routine_detail', routine_id=routine_id)
        elif 'comment' in request.POST:
            comment_text = request.POST.get('comment_text')
            parent_comment_id = request.POST.get('parent_comment_id')
            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                Comment.objects.create(
                    user=request.user,
                    routine=routine,
                    text=comment_text,
                    parent_comment=parent_comment
                )
                messages.success(request, 'Your reply has been added.')
            else:
                Comment.objects.create(user=request.user, routine=routine, text=comment_text)
                messages.success(request, 'Your comment has been added.')
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
        'saved_routines_count': saved_routines_count,
        'likes': likes,
        'comments': comments,
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


login_required(login_url='login')
def save_routine(request, routine_id):
    routine = get_object_or_404(HairRoutine, id=routine_id)

    if not SavedRoutine.objects.filter(user=request.user, routine=routine).exists():
        SavedRoutine.objects.create(user=request.user, routine=routine)
        messages.success(request, 'Routine saved successfully.')
    else:
        messages.warning(request, 'You have already saved this routine')
    
    return redirect('routine_detail', routine_id=routine_id)


login_required(login_url='login')
def saved_routines(request):
    template = 'saved_routines.html'
    saved_routines = SavedRoutine.objects.filter(user=request.user)
    context = {
        'saved_routines': saved_routines,
    }
    return render(request, template, context)


login_required(login_url='login')
def unsave_routine(request, routine_id):
    saved_routine = get_object_or_404(SavedRoutine, user=request.user, routine__id=routine_id)
    saved_routine.delete()
    return redirect('saved_routines')


            
