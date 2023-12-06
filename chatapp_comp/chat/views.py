from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import openai

from .models import Message


def index(request):
    messages = Message.objects.order_by('-created_at').reverse
    context = {'messages': messages}
    return render(request, 'chat/index.html', context)


def post(request):
    openai.api_key = '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'

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",max_tokens=10,
        messages=[
            {"role": "system","content": "あなたは優秀なトレーナーです。返答にはすべて英語で答えてください"},
            {"role": "user","content":request.POST['contents'] },
        ]
    )
    results = response["choices"][0]["message"]["content"]

    Message.objects.create(
        contents=request.POST['contents'],
        response=results,
        created_at=timezone.now()
    )
    return redirect('chat:index')
