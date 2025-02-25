from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Message, Listing
from .forms import MessageForm
from .serializers import ListingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


@login_required
def message_listing(request, listing_pk):
    """Handle sending a message for a specific listing."""
    listing = get_object_or_404(Listing, pk=listing_pk)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = listing.user
            message.listing = listing
            message.save()
            return redirect('listing_detail', pk=listing.pk)
    else:
        form = MessageForm()

    return render(request, 'ads/message_listing.html', {'listing': listing, 'form': form})


def view_messages(request):
    """View all messages received by the user."""
    messages = Message.objects.filter(receiver=request.user).order_by('-created_at')
    return render(request, 'ads/view_messages.html', {'messages': messages})
