from django.shortcuts import render, redirect
from .models import Double
from .forms import DoubleForm
import re


def double_list(request):
    doubles = Double.objects.all()
    return render(request, 'double_list.html', {'doubles': doubles})


def double_create(request):
    form = DoubleForm(request.POST or None)
    name_user_form = form.data.get('name')
    val_user_form = request.POST.get('value')
    value_user_form = int(val_user_form or 0)
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    data_obj = None

    obj = Double.objects.filter(name=name_user_form, value=value_user_form)
    if obj.count() > 0:
        data_obj = obj[0]

    if data_obj is not None:
        return render(request, 'double_exist.html', {'name_obj': data_obj.name,
                                                'value_obj': data_obj.value,
                                                'double_obj': data_obj.double_value,
                                                'date_obj': data_obj.date})

    elif value_user_form > 1000 or value_user_form < - 100:
        erro_value = 'Erro maximum 1000 and minimum -1000'
        return render(request, 'double_create.html', {'form': form, 'erro_value': erro_value})

    elif form.is_valid() and (regex.search(name_user_form) != None):
        erro_char = "Please Don't use especial character!"
        return render(request, 'double_create.html', {'form': form, 'erro_char': erro_char})

    elif form.is_valid() and (regex.search(name_user_form) == None):
        form.save()
        return redirect('double_list')
    return render(request, 'double_create.html', {'form': form})
