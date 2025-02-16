from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def inbox(request):
    received_messages = Message.objects.filter(receiver=request.user, is_archived=False)
    return render(request, 'messaging/inbox.html', {'messages': received_messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'messaging/send_message.html', {'form': form})

@login_required
def archive_message(request, pk):
    message = Message.objects.get(pk=pk)
    message.is_archived = True
    message.save()
    return redirect('inbox')