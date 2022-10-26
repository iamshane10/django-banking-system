from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, OptionsForm, DebitForm, CreditForm, LoginForm
from .models import Customer
from decimal import Decimal
from django.urls import reverse

#API Dependencies
#from django.http import HttpResponse, JsonResponse
#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from .serializers import CustomerSerializer

# Views

def loginView(request):
    pForm=LoginForm(request.POST or None)
    if pForm.is_valid():
        obj = pForm.cleaned_data['account']
        return redirect(reverse("profile",kwargs={'my_id':obj}))
    context = {'pForm':pForm}
    return render(request, 'login.html', context)

def registerView(request):
    pForm=RegistrationForm(request.POST or None)
    if pForm.is_valid():
        profile         = pForm.save(commit=False)
        profile.account = pForm.cleaned_data.get('account')
        profile.phone   = pForm.cleaned_data.get('phone')
        profile.age     = pForm.cleaned_data.get('age')
        profile.address = pForm.cleaned_data.get('address')
        profile.save()
        return redirect('../')
    context = {'pForm':pForm}
    return render(request, 'register.html', context)

def profileView(request, my_id):
    obj     = Customer.objects.get(account=my_id)
    context = {'customer':obj}
    return render(request, 'profile.html', context)

def optionsView(request):
    pForm = OptionsForm(request.POST or None)
    if pForm.is_valid():
        query = pForm.cleaned_data['choice']
        if query == 'Credit':
            return redirect("../credit")
        else:
            return redirect("../debit")
    else:
        query = None        
    context = {'pForm':pForm, 'value':query}
    return render(request, 'options.html', context)
    
def debitView(request):
    pForm = DebitForm(request.POST or None)
    if pForm.is_valid():
        query                   = pForm.cleaned_data['account'] #storing form data
        instance                = Customer.objects.get(account=query) #creating instance
        instance.balance        = Decimal(instance.balance)-Decimal(pForm.cleaned_data['value']) #transaction logic
        instance.transactions  += "(Debited, -" + str(pForm.cleaned_data['value']) + "), " #adding ledger
        instance.save() #saving instance
        messages.success(request, f'Your account balance has been updated!')
        return redirect(reverse("profile",kwargs={'my_id':query}))

    context = {
        'pForm': pForm,
    }
    return render(request, 'debit.html', context)

def creditView(request):
    pForm = CreditForm(request.POST or None)
    if pForm.is_valid():
        #storing form data
        query_from = pForm.cleaned_data['source']
        query_to   = pForm.cleaned_data['destination']
        #creating instances
        instance_from = Customer.objects.get(account=query_from)
        instance_to   = Customer.objects.get(account=query_to)
       #transaction logic
        instance_from.balance = Decimal(instance_from.balance)-Decimal(pForm.cleaned_data['amount'])
        instance_to.balance   = Decimal(instance_to.balance)+Decimal(pForm.cleaned_data['amount'])
        #transaction ledger
        instance_from.transactions  += "(Debited -" + str(pForm.cleaned_data['amount']) + "), "
        instance_to.transactions    += "(Credited +" + str(pForm.cleaned_data['amount']) + " from " + query_from + "), "
        #saving instances
        instance_from.save()
        instance_to.save()

        messages.success(request, f'Your account balance has been updated!')
        return redirect(reverse("profile",kwargs={'my_id':query_from}))

    context = {'pForm': pForm}
    return render(request, 'credit.html', context)


#REST API Views

#def loginView(request):
#    pForm=LoginForm(request.POST or None)
#    if pForm.is_valid():
#        obj = pForm.cleaned_data['account']
#        return redirect(reverse("profile",kwargs={'my_id':obj}))
#    context = {'pForm':pForm}
#    return render(request, 'login.html', context)

#def registerView(request):
#    pForm=RegistrationForm(request.POST or None)
#    if pForm.is_valid():
#        profile         = pForm.save(commit=False)
#        profile.account = pForm.cleaned_data.get('account')
#        profile.phone   = pForm.cleaned_data.get('phone')
#        profile.age     = pForm.cleaned_data.get('age')
#        profile.address = pForm.cleaned_data.get('address')
#        profile.save()
#        return redirect('../')
#    context = {'pForm':pForm}
#    return render(request, 'register.html', context)

#def profileView(request, my_id):
#    obj         = Customer.objects.get(account=my_id)
#    serializer  = CustomerSerializer(obj)
#    return Response(serializer.data)

#def optionsView(request):
#    pForm = OptionsForm(request.POST or None)
#    if pForm.is_valid():
#        query = pForm.cleaned_data['choice']
#        if query == 'Credit':
#            return redirect("../credit")
#        else:
#            return redirect("../debit")
#    else:
#        query = None        
#    context = {'pForm':pForm, 'value':query}
#    return render(request, 'options.html', context)
    
#def debitView(request):
#    pForm = DebitForm(request.POST or None)
#    if pForm.is_valid():
#        query                   = pForm.cleaned_data['account'] #storing form data
#        instance                = Customer.objects.get(account=query) #creating instance
#        instance.balance        = Decimal(instance.balance)-Decimal(pForm.cleaned_data['value']) #transaction logic
#        instance.transactions  += "(Debited, -" + str(pForm.cleaned_data['value']) + "), " #adding ledger
#        instance.save() #saving instance
#        messages.success(request, f'Your account balance has been updated!')
#        return redirect(reverse("profile",kwargs={'my_id':query}))

#    context = {
#        'pForm': pForm,
#    }
#    return render(request, 'debit.html', context)

#def creditView(request):
#    pForm = CreditForm(request.POST or None)
#    if pForm.is_valid():
#        #storing form data
#        query_from = pForm.cleaned_data['source']
#        query_to   = pForm.cleaned_data['destination']
#        #creating instances
#        instance_from = Customer.objects.get(account=query_from)
#        instance_to   = Customer.objects.get(account=query_to)
#        #transaction logic
#        instance_from.balance = Decimal(instance_from.balance)-Decimal(pForm.cleaned_data['amount'])
#        instance_to.balance   = Decimal(instance_to.balance)+Decimal(pForm.cleaned_data['amount'])
#        #transaction ledger
#        instance_from.transactions  += "(Debited -" + str(pForm.cleaned_data['amount']) + "), "
#        instance_to.transactions    += "(Credited +" + str(pForm.cleaned_data['amount']) + " from " + query_from + "), "
        #saving instances
#        instance_from.save()
#        instance_to.save()

#        messages.success(request, f'Your account balance has been updated!')
#        return redirect(reverse("profile",kwargs={'my_id':query_from}))
#
#    context = {'pForm': pForm}
#    return render(request, 'credit.html', context)
