from django.http import HttpResponse

def index(request):
    return HttpResponse("Desde la visa de laboratorio!")

def sumar(request, num1, num2):
    resultado = num1 + num2
    return HttpResponse(f'La suma de {num1} + {num2} = {resultado}')

def restar(request, num1, num2):
    resultado = num1 - num2
    return HttpResponse(f'La resta de {num1} - {num2} = {resultado}')

def multiplicar(request, num1, num2):
    resultado = num1 * num2
    return HttpResponse(f'La multiplicación de {num1} x {num2} = {resultado}')
