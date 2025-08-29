from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Expense, Income
from datetime import datetime
from json import JSONEncoder

@csrf_exempt
def submit_income(request):
    """ user submits an income """

    try:
        token = request.POST.get('token')
        text = request.POST.get('text')
        amount = request.POST.get('amount')

        # validate token
        user = User.objects.filter(token__token=token).first()
        if not user:
            return JsonResponse({'status': 'error', 'message': 'Invalid token'}, status=400)

        # validate amount
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            return JsonResponse({'status': 'error', 'message': 'Invalid amount'}, status=400)

        if 'date' not in request.POST:
            now = datetime.now()
        else:
            date = request.POST.get('date')

        Income.objects.create(
            user=user,
            amount=amount,
            text=text,
            date=now
        )

        return JsonResponse({'status': 'ok'}, encoder=JSONEncoder)

    except Exception as e:
        # log error for debugging
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@csrf_exempt
def submit_expense(request):
    """ user submits an expense """

    try:
        token = request.POST.get('token')
        text = request.POST.get('text')
        amount = request.POST.get('amount')

        # validate token
        user = User.objects.filter(token__token=token).first()
        if not user:
            return JsonResponse({'status': 'error', 'message': 'Invalid token'}, status=400)

        # validate amount
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            return JsonResponse({'status': 'error', 'message': 'Invalid amount'}, status=400)

        if 'date' not in request.POST:
            now = datetime.now()
        else:
            date = request.POST.get('date')

        Expense.objects.create(
            user=user,
            amount=amount,
            text=text,
            date=now
        )

        return JsonResponse({'status': 'ok'}, encoder=JSONEncoder)

    except Exception as e:
        # log error for debugging
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
