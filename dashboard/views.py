from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from pets.models import AdoptionRequest, Pet


@login_required
def overview(request):
    if not request.user.is_staff:
        raise PermissionDenied
    context = {
        'pet_count': Pet.objects.count(),
        'available_count': Pet.objects.filter(is_available=True).count(),
        'request_count': AdoptionRequest.objects.count(),
        'pending_count': AdoptionRequest.objects.filter(status='pending').count(),
        'recent_requests': AdoptionRequest.objects.select_related('pet', 'applicant')[:8],
    }
    return render(request, 'dashboard/overview.html', context)
