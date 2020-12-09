from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from EBA.models import Location_Restaurant, Restaurant_Food_New
from .forms import Location
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm,CustomerForm



def get_location(request):
    if request.method == 'POST':
        form = Location(request.POST)
        loc = form['location'].value()

        if form.is_valid():
            # return redirect('rlist',{'location':loc}) 
            rd_url = reverse('rlist', kwargs={'loc': loc})
            print(rd_url)
            return HttpResponseRedirect(rd_url)
    else:
        form = Location()

    return render(request, 'location.html', {'form': form})


    
def Restaurant_List(request, loc):
  RL = Location_Restaurant.objects.filter(Location=loc)
  return render(request,'res_list.html',{'rl':RL})


def Food_List(request, r_id):
  FL = Restaurant_Food_New.objects.filter(Restaurant_Id__Restaurant_Id=r_id)
  return render(request,'food.html',{'fl':FL})


def register(request):
  if request.method == 'POST':
    user_form = UserForm(request.POST)
    customer_form = CustomerForm(request.POST)

    if user_form.is_valid() and customer_form.is_valid():
      user_form.save()
      customer_form.save()
      return redirect('location')

  else:
    user_form = UserForm()
    customer_form = CustomerForm()

  context = {
    'user_form': user_form,
    'customer_form': customer_form 
  }

  return render(request, 'register.html', context)