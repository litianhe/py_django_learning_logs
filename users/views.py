from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

#from learning_log.settings import logger
import logging
logger = logging.getLogger('django.utils.autoreload')

# Create your views here.
def register(request):
    if request.method != 'POST':
        logger.info("tianhe new form:   11")
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        logger.info("tianhe post form:   11")
        if form.is_valid():
            # autologin, then redirect to index
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, 
                    password=request.POST['password2'])
            logger.info("hahah2:%s" , request.POST['password2'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    logger.info("tianhe post form:   99")
    context = {'form': form}
    return render(request, 'users/register.html', context)
