from django.shortcuts import redirect, render
from .models import MonthName, UserDetails,Calculation
from .forms import UserDetailsForm,MonthName
from django.db.models import Max,Min,Avg,Sum,Count
from django.contrib import messages
from .midleware import middleware
# Create your views here.

def home(request):
    template_name = 'record/home.html'
    return render(request,template_name)



def contactUs(request):
    template_name = 'record/contactus.html'
    return render(request,template_name)

@middleware
def insertRecord(request):
    form = UserDetailsForm
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            monthId = form.cleaned_data['month']
            username = form.cleaned_data['username']
            print(monthId)
            obj = UserDetails.objects.filter(month=monthId)
            user=obj
            for i in user:
                if i.username == username:
                    messages.error(request,"User's data has already filled!")
                    return redirect('insertRecords')
            messages.success(request,"User's data has been successfully submitted!")
            form.save()
            return redirect('months')
    
    context = {'form':form}
    template_name = 'record/insertForm.html'
    return render(request,template_name,context)

@middleware
def months(request):
    obj = MonthName.objects.all()
    context = {'months':obj}
    template_name = 'record/months.html'
    return render(request,template_name,context)
def monthDetails(request,id):
    obj = UserDetails.objects.filter(month_id = id)
    savingSum = UserDetails.objects.filter(month_id = id).aggregate(Sum('saving'))
    intrestSum = UserDetails.objects.filter(month_id = id).aggregate(Sum('intrest'))
    paidLoanSum = UserDetails.objects.filter(month_id = id).aggregate(Sum('paidLoan'))
    borrowLoanSum = UserDetails.objects.filter(month_id = id).aggregate(Sum('borrowLoan'))
    fineSum = UserDetails.objects.filter(month_id = id).aggregate(Sum('fine'))

    mn = MonthName.objects.get(id=id)
    monthName = mn.month
    context = {'allData':obj,'savingSum':savingSum,'intrestSum':intrestSum,'paidLoanSum':paidLoanSum,'borrowLoanSum':borrowLoanSum,'fineSum':fineSum,'monthName':monthName}
    template_name = 'record/userRecords.html'
    return render(request,template_name,context)

@middleware
def calculationsView(request):
    # monthName = request.session.get('mName')
    # print(monthName)
    # monthId = MonthName.objects.get(month=monthName)
    # id=int(monthId.id)
    savingSum = UserDetails.objects.all().aggregate(Sum('saving'))
    intrestSum = UserDetails.objects.all().aggregate(Sum('intrest'))
    fineSum = UserDetails.objects.all().aggregate(Sum('fine'))
    print(savingSum.get('saving__sum'))
    save = int(savingSum.get('saving__sum'))
    intrest = int(intrestSum.get('intrest__sum'))
    fine = int(fineSum.get('fine__sum'))

    borrowLoanSum = UserDetails.objects.all().aggregate(Sum('borrowLoan'))
    paidLoanSum = UserDetails.objects.all().aggregate(Sum('paidLoan'))
    borrow = int(borrowLoanSum.get('borrowLoan__sum'))
    paid = int(paidLoanSum.get('paidLoan__sum'))
    total = save+intrest+fine
    totalAvailable = total+paid-borrow

    context = {'amounts':total,'available':totalAvailable}
    template_name = 'record/finalAmounts.html'
    return render(request,template_name,context)



    # obj = Calculation.objects.get(id=2)
    # totalAmount=obj.totalAmount
    # finalTotalAmount=totalAmount+total#Total amount
    # print(finalTotalAmount)
    # obj.totalAmount = finalTotalAmount
    # obj.save()

    # borrowLoanSum = UserDetails.objects.filter(month_id=id).aggregate(Sum('borrowLoan'))
    # paidLoanSum = UserDetails.objects.filter(month_id=id).aggregate(Sum('paidLoan'))
    # borrow = int(borrowLoanSum.get('borrowLoan__sum'))
    # paid = int(paidLoanSum.get('paidLoan__sum'))


    # obj = Calculation.objects.get(id=2)
    # availableAmount = obj.availableAmount
    # finalAvailableAmount = availableAmount+paid-borrow
    # obj.availableAmount = finalAvailableAmount
    # obj.save()
    # return redirect('months')

    # context = {'totalAmount':finalTotalAmount,'availableAmount':finalTotalAmount}
    # template_name = 'record/finalAmounts.html'
    # return render(request,template_name,context)
@middleware
def finalAmounts(request):
    obj = request.session.get('finalAmount')
    context = {'amounts':obj}
    template_name = 'record/finalAmounts.html'
    return render(request,template_name,context)

def updateRecord(request,uid):
    obj = UserDetails.objects.get(pk = uid)
    form = UserDetailsForm(instance= obj)
    if request.method == 'POST':
        form = UserDetailsForm(request.POST,instance = obj)
        if form.is_valid():
            form.save()
            return redirect('months')
    context = {'form':form}
    template_name = 'record/insertForm.html'
    return render(request,template_name,context)







