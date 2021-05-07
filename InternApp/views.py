from django.shortcuts import render
from InternApp.models import Pizza
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view
from django.http import HttpResponseForbidden
from django.http import JsonResponse


@csrf_exempt
@api_view(['POST'])
def add_pizza(request):
    ptype = request.GET["type"]
    if(ptype == "Regular" or ptype == "Square" ):
        post = Pizza(
            ptype = ptype,
            size = request.GET["size"],
            toppings = request.GET["toppings"],
        )
        post.save()
        return HttpResponse("Addded Pizza")
    else:
        return HttpResponseForbidden()

@api_view(['GET'])
def show_pizza(request):
    pizzas = Pizza.objects.all()
    all_dict = {}
    for pizza in pizzas:
        temp_dict = {}
        temp_dict["ptype"] = pizza.ptype
        temp_dict["size"] = pizza.size
        temp_dict["toppings"] = pizza.toppings
        all_dict[pizza.id] = temp_dict
    return JsonResponse(all_dict)


@api_view(['POST'])
def update_pizza(request):
    id = request.GET['id']
    pizza = Pizza.objects.get(id = id)
    try:
        pizza.ptype = request.GET["type"]
        pizza.size = request.GET["size"]
        pizza.toppings = request.GET["toppings"]
        pizza.save()
        return HttpResponse("Updated")
    except:    
        try:
            pizza.ptype = request.GET["type"]
            pizza.save()
            return HttpResponse("Updated")
        except:
            try:
                pizza.size = request.GET["size"]
                pizza.save()
                return HttpResponse("Updated")
            except:
                try:
                    pizza.toppings = request.GET["toppings"]
                    pizza.save()
                    return HttpResponse("Updated")
                except:
                    return HttpResponse(status = 404)
        
@api_view(['POST'])
def delete_pizza(request):
    try:
        id = request.GET['id']
        pizza = Pizza.objects.get(id = id)
        pizza.delete()
        return HttpResponse("Deleted")
    except:
        return HttpResponse(status = 404)

@api_view(['POST'])
def filter_pizzas(request):
    try:
        size = request.GET["size"]
        pizzas = Pizza.objects.filter(size = size)
        all_dict = {}
        for pizza in pizzas:
            temp_dict = {}
            temp_dict["ptype"] = pizza.ptype
            temp_dict["size"] = pizza.size
            temp_dict["toppings"] = pizza.toppings
            all_dict[pizza.id] = temp_dict
        return JsonResponse(all_dict)
    except:
        try:
            ptype = request.GET["type"]
            pizzas = Pizza.objects.filter(ptype = ptype)
            all_dict = {}
            for pizza in pizzas:
                temp_dict = {}
                temp_dict["ptype"] = pizza.ptype
                temp_dict["size"] = pizza.size
                temp_dict["toppings"] = pizza.toppings
                all_dict[pizza.id] = temp_dict
            return JsonResponse(all_dict)
        except:
            return HttpResponseForbidden()



        



