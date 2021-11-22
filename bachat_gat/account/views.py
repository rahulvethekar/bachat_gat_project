from django.shortcuts import redirect, render
from .models import Register
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
import random
from django.core.mail import send_mail
from cryptography import fernet
# Create your views here.
def registrationForm(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if len(username) < 5 or len(username) >8:
            messages.error(request,"Minimum 5  and Maximun 8 character's are required in Username!")
            return redirect('register')
        if Register.objects.filter(username = username).exists():
            messages.error(request,'Username has already exists')
            return redirect('register')

        #password validation
        if not any(char.isdigit() for char in password):
            messages.error(request,'Atleast one digit is required in Password!')
            return redirect('register')

        if not any(char.isalpha() for char in password):
            messages.error(request,'Atleast one alphabet is required in Password')
            return redirect('register')
        #special character
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not any(char in special_characters for char in password):
            messages.error(request,'Atleast one special character is required in Password')
            return redirect('register')
        #password length
        if len(password) < 5 or len(password) >8:
            messages.error(request,"Minimum 5  and Maximum  8 character's are required in Password!")
            return redirect('register')
        #check first Character
        if password[0].isupper()==False:
            messages.error(request,'First character should be UpperCase!')
            return redirect('register')
        #password hashing
        encoded = make_password(password)
        obj = Register(fname = fname, 
                    username = username,
                    password = encoded,
                    email = email
                    )
        obj.save()
        return redirect('login')
    email = request.session.get('email')
    print(email)
    template_name = 'account/register.html'
    context = {'Email':email}
    return render(request,template_name,context)

def verifyEmail(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if Register.objects.filter(email=email).exists():
            messages.error(request,'Email id already exists!')
            return redirect('verifyEmail')
        otp = random.randint(1000,9999)
        request.session['otp']=otp
        request.session['email']= email
        
        #mail part

        subject = 'Verify Your Email'
        message = f'OTP:-{otp}\n Regards, Team Rahul'
        send_mail(
            subject,
            message,
            'rahulvethekar95@gmail.com',
            [email],
            fail_silently=False
        )
        messages.success(request,'OTP has been successfully send on your Email Id')
        return redirect('verifyOtp')
    template_name = 'account/verifyEmail.html'
    return render(request,template_name)
def otpVerify(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        sessionOtp=request.session.get('otp')
        try:
            if not int(otp) == int(sessionOtp):
                messages.error(request,'Invalid OTP!')
                return redirect('verifyOtp')
            return redirect('register')
        except ValueError:
            messages.error(request,'Please Enter Digits Only')
            return redirect('verifyOtp')

    template_name = 'account/verifyOtp.html'
    return render(request,template_name)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not Register.objects.filter(username = username).exists():
            messages.error(request,'Wrong Credentials')
            return redirect('login')
        obj = Register.objects.get(username = username)
        pwd = obj.password
        check = check_password(password,pwd)
        if check == False:
            messages.error(request,'Wrong Credentials')
            return redirect('login')
        else:
            request.session['username'] = username
            return redirect('home')

    template_name = 'account/login.html'
    return render(request,template_name)


def logout(request):
    request.session.clear()
    return redirect('login')

def changePassword(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        newPassword = request.POST.get('newPassword')

        if not Register.objects.filter(username = username).exists():
            messages.error(request,'Username does not exist!')
            return redirect('changePassword')
        obj = Register.objects.get(username = username)
        oldPassword=obj.password

        check = check_password(password,oldPassword)
        if check == False:
            messages.error(request,'Wrong Password')
            return redirect('changePassword')
        # password validation
        if not any(char.isdigit() for char in newPassword):
            messages.error(request, 'Atleast one digit is required in Password!')
            return redirect('register')

        if not any(char.isalpha() for char in newPassword):
            messages.error(request, 'Atleast one alphabet is required in Password')
            return redirect('register')
        # special character
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not any(char in special_characters for char in newPassword):
            messages.error(request, 'Atleast one special character is required in Password')
            return redirect('register')
        # newPassword length
        if len(newPassword) < 5 or len(newPassword) > 8:
            messages.error(request, "Minimum 5  and Maximum  8 character's are required in Password!")
            return redirect('register')
        # check first Character
        if newPassword[0].isupper() == False:
            messages.error(request, 'First character should be UpperCase!')
            return redirect('register')
        # newPassword hashing
        encodedNewPassword = make_password(newPassword)
        obj.password = encodedNewPassword
        obj.save()

        return redirect('login')
    template_name = 'account/changePassword.html'
    return render(request,template_name)

