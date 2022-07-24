from django.shortcuts import render
from .models import Sheet
from .functions import main


def check(request):
    dell = Sheet.objects.all()
    dell.delete()
    result = main()
    for i in result:

        data = {
            'id': i[0],
            'num': int(i[0]),
            'order': int(i[1]),
            'price': int(i[2]),
            'date': (i[3]),
        }

        Sheet.objects.filter(id=data['id']).update_or_create(num=data['num'], order=data['order'], price=data['price'], date=data['date'])

    sheet = Sheet.objects.all()

    return render(request, 'veed/sheet/check.html', {'sheets': sheet})




