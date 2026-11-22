from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect, render
from .models import AdoptionRequest, Pet


def pet_list(request):
    pets = Pet.objects.filter(is_available=True)
    return render(request, 'pets/pet_list.html', {'pets': pets})


@login_required
@require_POST
def request_adoption(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id, is_available=True)
    if request.method == 'POST':
        message = request.POST.get('message', '').strip()
        AdoptionRequest.objects.create(pet=pet, applicant=request.user, message=message)
        messages.success(request, f'Your request for {pet.name} was sent.')
    return redirect('pets:list')
