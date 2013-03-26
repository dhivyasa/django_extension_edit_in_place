# Create your views here.
from datetime import datetime
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import sys


@login_required
def edit_in_place(request):
    """
    id of the edit in place select box is of the format
     <id>__<full modulename>__<modelname>__<fieldname>
    example: <td class="editinplace" 
      id="{{modelname.id}}__modulename__modelname__{{fielname}}">{{fieldvalue}}</td>
    if date field name cointains the words 'date' or time, the data is converted
        into datetime object and stored
    if field is a boolean select box, valid values are enable,disable  or True,False
    """
    try:
        id_list = request.POST['element_id'].split('__',3)
        update_value = request.POST['update_value'].strip()
        id = id_list[0]
        module_name = id_list[1]
        model_name = id_list[2]
        field_name = id_list[3]
        kwargs = {}

        if 'date' in field_name or 'Date' in field_name or \
            'time' in field_name or 'Time' in field_name:
            try:
                formatteddate = datetime.strptime(update_value.strip(), "%m-%d-%Y %H:%M:%S")
            except ValueError, e:
               return HttpResponseBadRequest(str(e))
            kwargs[str(field_name)] = str(formatteddate)
        elif update_value == "disable":
            kwargs[str(field_name)] = False
        elif update_value == "enable":
            kwargs[str(field_name)] = True
        elif update_value == "True":
            kwargs[str(field_name)] = True
        elif update_value == "False":
            kwargs[str(field_name)] = False
        else:
            kwargs[str(field_name)] = update_value

        try:
            __import__(module_name)
            module = sys.modules[module_name]
            model_class = getattr(module, model_name)
            model_object_queryset = model_class.objects.filter(id=id)
            model_object_queryset.update(**kwargs)
        except ObjectDoesNotExist, e:
            update_value = ''

        return HttpResponse(update_value)
    except Exception, e:
        return HttpResponse(update_value)
