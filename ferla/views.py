from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def mestre_ferla(
    request,
):
    return JsonResponse(
        {"message": "Olá mestre Ferla blz? Já tomou teu todinho? HAHAHAHA"}, status=200
    )
