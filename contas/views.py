from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime

from .models import Transacao
from .form import TransacaoForm


def home(request):
    """
    :param request: class 'django.core.handlers.wsgi.WSGIRequest'
    :return: Dict
    """
    data = {}
    data['transacoes'] = ['t1', 't2', 't3', 't4']
    data['now'] = datetime.datetime.now()
    return render(request, 'contas/home.html', data)


def listagem(request):
    """
    :param request: class 'django.core.handlers.wsgi.WSGIRequest'
    :return: Dict
    """
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    """
    :param request: class 'django.core.handlers.wsgi.WSGIRequest'
    :return: Dict
    """
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    return render(request, 'contas/form.html', {'form':form}) # {'form':form} - cria um dicionário.


def update(request, pk):
    """
    :param request: class 'django.core.handlers.wsgi.WSGIRequest'
    :param pk: Primary Key
    :return: Dict
    """
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)


def delete(request, pk):
    """
    :param request: class 'django.core.handlers.wsgi.WSGIRequest'
    :param pk: Primary Key
    :return: Dict
    """

    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')

