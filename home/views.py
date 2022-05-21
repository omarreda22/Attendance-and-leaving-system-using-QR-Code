from datetime import date
from enum import auto
from hashlib import new
from operator import le
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import AttListLogin, LeaveListLogin
from django.contrib.auth.decorators import login_required
from .models import Attendance, Attendance_List, Leave, Leave_List
# from .forms import AttendanceForm, LeaveForm

def title(request):
    return render(request, 'title.html')

def home(request):
    attendance = Attendance.objects.all().order_by('-id')
    leave = Leave.objects.all().order_by('-id')
    context = {
        'attendance': attendance,
        'leave': leave,
    }
    return render(request, 'home.html', context)

def attendance_list(request, dr_name,att_name):
    try:
        att_list = Attendance.objects.get(dr__slug=dr_name ,slug=att_name)
    except Exception as e:
        raise e

    student_list = Attendance_List.objects.order_by('-created_at').filter(qrcode_id=att_list.id)
    count = student_list.count()
    context = {
        'att_list': att_list,
        'student_list': student_list,
        'count':count,
    }
    return render(request, 'list/attendance_list.html', context)

def leave_list(request, dr_name, leave_name):
    try:
        leave_list = Leave.objects.get(dr__slug=dr_name ,slug=leave_name)
    except Exception as e:
        raise e

    student_list = Leave_List.objects.order_by('-created_at').filter(qrcode_id=leave_list.id)
    count = student_list.count()
    context = {
        'leave_list': leave_list,
        'student_list': student_list,
        'count':count,
    }
    return render(request, 'list/leave_list.html', context)


@login_required(login_url = 'accounts:login')
def attendance_login(request, dr_name, att_name):
    try:
        att_list = Attendance.objects.get(dr__slug=dr_name ,slug=att_name)
    except Exception as e:
        raise e
    context = {
        'att_list': att_list
    }
    return render(request, 'forms/attendance_form.html', context)


@login_required(login_url = 'accounts:login')
def leave_login(request, dr_name, leave_name):
    try:
        leave_list = Leave.objects.get(dr__slug=dr_name ,slug=leave_name)
    except Exception as e:
        raise e
    context = {
        'leave_list': leave_list
    }
    return render(request, 'forms/leave_form.html', context)


@login_required(login_url = 'accounts:login')
def attendance_submit(request, dr_id, qrcodeid):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            qr = Attendance_List.objects.get(dr__id=dr_id, user__id=request.user.id, qrcode__id=qrcodeid)
            form = AttListLogin(request.POST, instance=qr)
            form.save()
            messages.success(request, 'You are Already on the Attendance List!')
            return redirect(url)
        except Attendance_List.DoesNotExist:
            form = AttListLogin(request.POST)
            qrnew = Attendance.objects.get(id=qrcodeid)
            if form.is_valid():
                userid = form.cleaned_data['loginid']
                newstudent = Attendance_List()
                if request.user.nubmer_id == userid:
                    newstudent.loginid = userid
                    newstudent.user = request.user
                    newstudent.dr = qrnew.dr
                    newstudent.ip = request.META.get('REMOTE_ADDR')
                    newstudent.qrcode = qrnew
                    newstudent.save()
                    messages.success(request, 'Successfully Logged on the Attendance List')
                    return redirect('home:home')
                else:
                    messages.warning(request, 'Your Id Number Incorrect')
                    return redirect(url)

    return render(request, 'forms/attendance_form.html')


@login_required(login_url = 'accounts:login')
def leave_submit_new(request, leavedr_id, leaveqrcodeid):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            qr = Leave_List.objects.get(dr__id=leavedr_id, user__id=request.user.id, qrcode__id=leaveqrcodeid)
            form = LeaveListLogin(request.POST, instance=qr)
            form.save()
            messages.success(request, 'You are Already on the Leave List!')
            return redirect(url)
            
        except Leave_List.DoesNotExist:
            form = LeaveListLogin(request.POST)
            qrnew = Leave.objects.get(id=leaveqrcodeid)
            if form.is_valid():
                userid = form.cleaned_data['loginid']
                newstudent = Leave_List()
                if request.user.nubmer_id == userid:
                    newstudent.loginid = userid
                    newstudent.user = request.user
                    newstudent.dr = qrnew.dr
                    newstudent.ip = request.META.get('REMOTE_ADDR')
                    newstudent.qrcode = qrnew
                    newstudent.save()
                    messages.success(request, 'Successfully Logged on the Leave List')
                    return redirect('home:home')
                else:
                    messages.warning(request, 'Your Id Number Incorrect')
                    return redirect(url)

    return render(request, 'forms/leave_form.html')
