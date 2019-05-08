from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import check_password, make_password
from django.utils import timezone

from publicgoods.models import Game_Instance, Game_Response
from publicgoods.forms import CreateInstanceForm, ParticipateForm, InstructorViewLoginForm, ParticipateLoginForm

from gametheory import nplayergame

def index(request):
    #open_instances = Game_Instance.objects.all()
    open_instances = Game_Instance.objects.filter(available=True).order_by('-time_opened')
    closed_instances = Game_Instance.objects.filter(available=False).order_by('-time_closed')
    context = {'open_instances': open_instances, 'closed_instances': closed_instances}
    return render(request, 'publicgoods/index.html', context)

def create_game(request):
    if request.method == 'POST':
        form = CreateInstanceForm(request.POST)

        if (form.is_valid()):
            instance_id = form.process()
            target = '/publicgoods/instructor_view/'+str(instance_id)
            request.session['logged_in_to'] = instance_id
            return HttpResponseRedirect(target);

    else:
        form = CreateInstanceForm()

    context = {'form': form}
    return render(request, 'publicgoods/create_game.html', context)

def instructor_view(request, instance_id=None, response_id=None, close_id=None):
    if not close_id is None:
        instance_id = close_id

    instance = get_object_or_404(Game_Instance, pk=instance_id)

    loggedto = request.session.get('logged_in_to', None)

    if loggedto is not None and loggedto==instance_id:
       
        #if response_id is not none, then delete the corresponding response
        if not response_id is None:
            try:
                Game_Response.objects.get(pk=response_id).delete()
            except Game_Response.DoesNotExist:
                pass

        if not close_id is None:
            instance.available = False;
            instance.time_closed = timezone.now()
            instance.save()
        
        context = nplayergame.get_game_outcome_context(instance_id)
        return render(request, 'publicgoods/instructor_view.html', context)
    else:
        if request.method == 'POST':
            form = InstructorViewLoginForm(request.POST, instructor_password=instance.instructor_password)

            if form.is_valid():
                context = nplayergame.get_game_outcome_context(instance_id)
                request.session['logged_in_to'] = instance_id
                return render(request, 'publicgoods/instructor_view.html', context)
        
        else:
            form = InstructorViewLoginForm(instructor_password=instance.instructor_password)
        
        context = {'form': form, 'instance': instance}
        return render(request, 'publicgoods/instructor_view_login.html', context)


def play_game(request, instance_id):
    instance = get_object_or_404(Game_Instance, pk=instance_id)

    #If the instructor has closed the game, you're not able to participate
    if not instance.available:
        return HttpResponseRedirect('/publicgoods/anon_results/'+str(instance_id))

    if request.method == 'POST':
        #If the request originates from a user entering the keyword
        if 'keywordsubmit' in request.POST:
            loginform = ParticipateLoginForm(request.POST, user_keyword=instance.user_keyword)

            # If the player has successfully logged into the game,
            # then note this in the session and refresh the page
            if loginform.is_valid():
                request.session['can_play'] = instance_id
                return HttpResponseRedirect('/publicgoods/play/'+str(instance_id))
            else:
                context = {'button_name': 'keywordsubmit', 'form': loginform, 'instance': instance}
                return render(request, 'publicgoods/play.html', context)
        #If the request originates from the user participating in the game
        else:
            participateform = ParticipateForm(request.POST, max_contribution=instance.max_contribution)

            if participateform.is_valid():
                pseudonym, contribution = participateform.process(instance)
                context = {'instance': instance, 'success': True, 'pseudonym': pseudonym, 'contribution': contribution}
                return render(request, 'publicgoods/play.html', context)
            else:
                context = {'instance': instance, 'button_name': 'participate', 'form': participateform}
                return render(request, 'publicgoods/play.html', context)

    else:
        session_id = request.session.get('can_play', None)

        if session_id is None or session_id != instance_id:
            loginform = ParticipateLoginForm(user_keyword=instance.user_keyword)
            context = {'button_name': 'keywordsubmit', 'form': loginform, 'instance': instance}
            return render(request, 'publicgoods/play.html', context)
        else:
            participateform = ParticipateForm(max_contribution=instance.max_contribution)
            context = {'button_name': 'participate', 'form': participateform, 'instance': instance}
            return render(request, 'publicgoods/play.html', context)

def anon_results(request, instance_id):
    instance = get_object_or_404(Game_Instance, pk=instance_id)

    # Players cannot view the results of an ongoing game
    if instance.available:
        return render(request, 'publicgoods/results_not_ready.html', {'instance': instance})

    context = nplayergame.get_game_outcome_context(instance_id)
    return render(request, 'publicgoods/anon_results.html', context)


