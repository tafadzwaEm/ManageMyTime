from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Todo, Upcoming
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RegisterUserForm
from django.contrib.auth.models import User
from itertools import chain

class TodoView(LoginRequiredMixin,ListView):
    model = Todo 
    template_name = 'todo/todo_home.html'
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        context = super(TodoView, self).get_context_data(**kwargs)
        context['events'] = Upcoming.objects.filter(creator = self.request.user)
        return context

    def get_queryset(self):
        return super(TodoView, self).get_queryset().filter(creator=self.request.user) 
    
   


class CreateTodoView(LoginRequiredMixin,CreateView):
    model = Todo
    fields = ['todoname']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request,"Task Added Successfully")
        return super().form_valid(form)

class UpdateTodoView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Todo
    fields = ['todoname']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request,"Task Updated Successfully")
        return super().form_valid(form)
    
    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.creator:
            return True
        return False

class DeleteTodoView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Todo
    success_url= '/'

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.creator:
            return True
        return False

class CreateUpcomingView(LoginRequiredMixin,CreateView):
    model = Upcoming
    fields = ['eventname']
    template_name = 'todo/upcoming_form.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request,"Event Added Successfully")
        return super().form_valid(form)

class UpdateUpcomingView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Upcoming
    fields = ['eventname']
    template_name = 'todo/upcoming_form.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request,"Event Updated Successfully")
        return super().form_valid(form)
    
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.creator:
            return True
        return False

class DeleteUpcomingView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Upcoming
    success_url = '/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.creator:
            return True
        return False


def Register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.info(request,f'Account created for {username}!')
            return redirect('/')
    else:
        form = RegisterUserForm()

    return render(request,'todo/register.html',{'form':form})

