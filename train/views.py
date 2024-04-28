from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import FormView
from .forms import AddTrainForm,TrainInfoUpdateForm
from django.urls import reverse_lazy
from .models import Train_list
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from account.models import UserAccount
from .models import BorrowedTicket
from django.contrib import messages

# Create your views here.
class Add_trainView(FormView):
    template_name= 'train/add_train.html'
    form_class = AddTrainForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        add_train = form.save()
        print(add_train)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Add_trainView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the trains
        context['trains'] = Train_list.objects.all()
        return context

    
def train_list(req):
    data= Train_list.objects.all()
    return render(req, 'train/train_list.html', {'trains': data})

class Detail_train(DetailView):
    model = Train_list
    pk_url_kwarg = 'id'
    template_name= 'train/detail_train.html'
    context_object_name = 'train'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        train = self.get_object()
        stations = train.station.all()
        seat_formations = train.seat_formation.all()
        seat_rows = []
        # print(train)
        

        for seat_form in seat_formations:
            seat_list = seat_form.name.split()
            # rows = [seat_list[i:i+2] for i in range(0, len(seat_list),2)]
            seat_rows.append(seat_list)

        if train.seat_number: 
            seat_numbers = train.seat_number.split(",") 
            print(seat_numbers)
        else:
            seat_numbers=[]
        
        context['stations'] = stations 
        context['seat_numbers'] = seat_numbers
        context['seat_rows'] = seat_rows
        return context

@login_required
def buyTicket(req, train_id):
    train = Train_list.objects.filter(id=train_id).first()
    user_acc = get_object_or_404(UserAccount, user=req.user)
    acc_balance = user_acc.balance
    ticketPrice = train.price

    if acc_balance >= ticketPrice:
        acc_balance -= ticketPrice
        user_acc.balance = acc_balance
        user_acc.save()

        profile, created= BorrowedTicket.objects.get_or_create(user=req.user, train = train)
        messages.success(req,"Great, Ticket Purchased Successfully")
        print(profile)

    # else:
    #     print("not working")
    #     messages.error(req,"Balance not sufficient")
    else:
        print("not eror")
        messages.error(req,"Your Balance is not sufficient.")
        redirect("deposite")

    return redirect("dashboard")


def editTrainInfo(req,id):
    train = Train_list.objects.filter(pk=id).first()
    edit_form = TrainInfoUpdateForm(instance=train)

    if req.method=='POST':
        edit_form = TrainInfoUpdateForm(req.POST,instance=train)
        # print(edit_form)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('home')
        else:
            print("error")
    return render(req, 'train/edit_train.html', {'form':edit_form})


def delete_train(req,id):
    data= Train_list.objects.get(pk=id)
    data.delete()
    return redirect('add_train')