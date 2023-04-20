# from django.shortcuts import render
# from django.http import HttpResponse
# #from chat import chat_model
# # Create your views here.

# def chat (request):
#     return HttpResponse("Hello world!")
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chat import chat_model

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        chatbot = chat_model()

        chatbot.start_conversation()

        message = request.POST.get('message', '')

        response = chatbot.converse(message)

        return JsonResponse({'message': response})

    return JsonResponse({})
