from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import AddTrainForm,TrainInfoUpdateForm
from django.urls import reverse_lazy
from .models import Train_list
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

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

    # def post(self, req, *args, **kwargs):
    #     train = self.get_object()
    #     return self.get(req, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        train = self.get_object()
        stations = train.station.all()

        
        if train.seat_number: 
            seat_numbers = train.seat_number.split(",") 
        else:
            seat_numbers = []

        prices = []  # Initialize prices list

        # Assuming 'price' is a DecimalField in the Train model
        # You need to handle DecimalField differently than splitting a string
        if train.price:
            prices.append(train.price)  # Add price to the prices list
        else:
            prices = []

        context['stations'] = stations
        context['seat_numbers'] = seat_numbers
        context['prices'] = prices

        return context
    

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