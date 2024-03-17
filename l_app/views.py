from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.core.mail import send_mail
from Last_Project import settings
from .forms import *
from .models import *

otp=0
import random

# Create your views here.
def index(request):
    msg = ''
    user = request.session.get('user')
    if request.method == 'POST':
        # Signup
        if request.POST.get('signup') == 'signup':
            newdata = signupForm(request.POST)
            if newdata.is_valid():
                username = newdata.cleaned_data.get('username')
                try:
                    signupModel.objects.get(username=username)
                    print('Username already exists, please choose onther username')
                    msg = 'Username already exists, please choose onther username...!'
                except signupModel.DoesNotExist:
                    newdata.save()
                    msg = 'Signup Successfully...!'
                    print("Signup SuccessFully")

                    # Send OTP
                    global otp   
                    otp = random.randint(100000,999999)
                    print('Your OTP is -: ',otp)
                    send_mail(subject='MyTrip OTP', message=f'Your OTP is-: {otp}', from_email=settings.EMAIL_HOST_USER, recipient_list=[request.POST['username']])
                    return redirect('otpverify')
            else:
                msg = 'Something went wrong, Please try agian...!'
                print(newdata.errors)
        # Login
        elif request.POST.get('login') == 'login':
            unm = request.POST['username']
            pas = request.POST['password']
            
            user = signupModel.objects.filter(username=unm, password=pas)
            upid = signupModel.objects.get(username=unm)
            if user:
                print('Login Successfuly.')
                request.session['user'] = unm
                request.session['userid'] = upid.id
                return redirect('feedback')
            else:
                print('Something went wrong, please try again')
    
    return render(request, 'index.html', {'message':msg,'user':user})

def feedback(request):
    msg = ''
    user = request.session.get('user')
    return render(request, 'feedback.html', {'msg':msg,'user':user})
    
def about(request):
    msg = ''
    user = request.session.get('user')
    if request.method == 'POST':
        booktrip = tripForm(request.POST)
        
        if booktrip.is_valid():
            booktrip.save()
            print('Your trip has been Booked.')
            msg = 'Your trip has been Booked...!'

            # Send mail
            sub = 'MyTrip - Thank You for Booking Your Honeymoon Trip'

            mess = f'''
                    Dear {request.POST['firstname']},
                    \n
                    We are thrilled to have you on board for your special honeymoon trip with [Your Company Name]! We are excited to create an unforgettable experience for you both during this remarkable journey.
                    \n
                    Please find below the details of your honeymoon trip booking:
                    \n
                    1. Couple's Name: {request.POST['firstname']} & {request.POST['lastname']}
                    2. Mobile Number: {request.POST['mobile']}
                    3. Trip Location: {request.POST['place']}
                    4. Trip Time: {request.POST['time']}
                    \n
                    Our dedicated team is now working on creating a personalized itinerary for you, including accommodations, sightseeing, and other exciting activities tailored to your preferences. You can expect to receive your comprehensive itinerary within the next 2-3 business days.
                    \n
                    In the meantime, if you have any questions or need further assistance, please do not hesitate to reach out to us. We are here to ensure your honeymoon trip is nothing short of perfect.
                    \n
                    Thank you once again for choosing MyTrip for your special occasion. We look forward to welcoming you soon!
                    \n\n
                    Warm Regards,
                    \n
                    Parth Chavda,
                    Halvad,
                    MyTrip
                    +91 9328553159# | parthchavda@gmail.com | www.MyTrip.com'''

            from_id = settings.EMAIL_HOST_USER

            to_id = [request.POST['email']]

            send_mail(subject=sub, message=mess, from_email=from_id, recipient_list=to_id)
        else:
            print(booktrip.errors)
            msg = 'Something went wrong, please try again...!'
        
    return render(request, 'about.html', {'msg':msg, 'user':user})

def contact(request):
    return render(request, 'contact.html')

def update_profile(request):
    msg = ''
    user = request.session.get('user')
    userid = request.session.get('userid')
    upid = signupModel.objects.get(id=userid)
    # Update profile
    if request.method == 'POST':
        updatedata = updateForm(request.POST, instance=upid)
        if updatedata.is_valid():
            updatedata.save()
            msg = 'Update Successfully...!'
            print("Update SuccessFully")
            return redirect('feedback')
        else:
            msg = 'Something went wrong, Please try agian...!'
            print(updatedata.errors)
    return  render(request, 'update.html',{'user':user,'upid':upid, 'msg':msg})

def user_logout(request):
    logout(request)
    return redirect('/')

def otpverify(request):
    global otp
    msg = ''
    if request.method == "POST":
        if request.POST['otp']==str(otp):
            print('OTP varification Successfully.')
            msg = 'OTP varification Successfully.'
            return redirect('/')
        else:
            print('Invaliad OTP number')
            msg = 'Please enter valid OTP...!'
    
    return render(request, 'otp.html', {'msg':msg})