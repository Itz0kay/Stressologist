from django.shortcuts import render, redirect
from django.urls import reverse
from Programs.forms import *
from Programs.models import *
from Tests.models import *
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from datetime import datetime

curr_time = datetime.now()

# Create your views here.

@login_required
def listView(request):
    program = Program.objects.filter()
    programs = list(program.values())
    context = {
        'programs' : programs,
    }
    return render(request, 'Programs/listview.html', context)

@login_required
def recView(request):
    all_results = list(Result.objects.filter(user=request.user).values())
    if len(all_results) != 0:
        total = 0
        count = 0
        for i in all_results:
            count += 1
            total += i["stresslevel"]
        total //= count
    else:
        total = 0
    
    
    ongoing = list(ProgramLog.objects.filter(user=request.user).select_related('Program').values('program_id'))
    ongoing = [k['program_id'] for k in ongoing]
    program = Program.objects.filter(level__lte=total)
    program = program.exclude(id__in=ongoing)
    programs = list(program.values())
    context = {
        'programs' : programs,
        'ongoing': ongoing,
    }
    return render(request, 'Programs/reclistview.html', context)


@login_required
def ongoingView(request):
    ongoing = list(ProgramLog.objects.filter(user=request.user).select_related('Program').values('program_id'))
    ongoing = [k['program_id'] for k in ongoing]
    program = Program.objects.filter(id__in=ongoing)
    programs = list(program.values())
    context = {
        'programs' : programs,
        'ongoing': ongoing,
    }
    return render(request, 'Programs/ongoinglistview.html', context)


@login_required
def detailView(request):
    if request.method == "POST":
        pass
    else:
        ongoing = list(ProgramLog.objects.filter(user=request.user).select_related('Program').values('program_id'))
        ongoing = [k['program_id'] for k in ongoing]
        pid = request.GET.get('id')

        program = Program.objects.filter(id=pid)
        program = list(program.values())[0]
        # print(program)
    context = {
        'program':program,
        'ongoing': ongoing,
    }
    return render(request, 'Programs/detailview.html', context)

@login_required
def take_program(request):
    pid = request.GET.get('pid')
    program = Program.objects.get(pk=pid)
    
    start_date = date.today()
    end_date = start_date + timedelta(days=2)
    
    program_log = ProgramLog.objects.create(
        user=request.user, 
        program=program, 
        start_date=start_date, 
        end_date=end_date
    )
    
    context = {}
    return redirect(reverse("Programs:listview"))

@login_required
def inptest(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newform = form.save(commit=False)
            newform.save()
            print(newform)
            # redirect to a new URL:
            return redirect('Programs:inptest')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProgramForm()
    
    context = {
        'form': form
    }

    return render(request, 'Programs/test.html', context)
