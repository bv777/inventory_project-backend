from django.http import HttpResponse, JsonResponse
from .models import CurrentInventory
import http
import json

import logging

logger = logging.getLogger(__name__)


def current_inventory(request):
    inventory_list = CurrentInventory.objects.all()
    result = []
    for i in inventory_list:
        result.append(i.to_dict())

    return JsonResponse({'data': result}, safe=False)


def add_inventory_item(request):
    logger.info(f'add_inventory_item(): called with request={request}')
    if request.method != 'POST':
        return HttpResponse(status=http.HTTPStatus.METHOD_NOT_ALLOWED)
    
    try:
        logger.debug(f"body={request.body}")
        data = json.loads(request.body)['data']
        logger.debug(f"data={data}")
        item = {}
        c = CurrentInventory(
            name=data['name'],
            unitPrice=float(data['unitPrice']),
            quantity=float(data['quantity']),
            minimalSupply=float(data['minimalSupply'])
        )
        c.save()
        return HttpResponse(f"Successfully added {data['name']}")
    except Exception as e:
        logger.error(e)
        return HttpResponse(e, status=http.HTTPStatus.BAD_REQUEST)

