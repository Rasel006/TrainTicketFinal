from django.shortcuts import render
from train.models import BorrowedTicket
from account.models import UserAccount

# Create your views here.
def dashboard(req):
    bought_ticket = BorrowedTicket.objects.filter(user= req.user)
    return render(req, 'dashboard/dashboard.html',{
        'ticket': bought_ticket
    })

def users_all(req):
    users = UserAccount.objects.all()
    return render(req, 'dashboard/AllUsers.html',{'users': users})

def borrowed_list(req):
    borrowed = BorrowedTicket.objects.all()
    return render(req, 'dashboard/borrow_tickets.html', {'borroweds': borrowed})