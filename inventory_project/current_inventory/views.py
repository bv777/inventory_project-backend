from django.http import HttpResponse, JsonResponse
from .models import CurrentInventory, ProductionLog
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
        c = CurrentInventory(
            name=data['name'],
            unit_price=float(data['unitPrice']),
            quantity=float(data['quantity']),
            minimal_supply=float(data['minimalSupply'])
        )
        c.save()
        return HttpResponse(f"Successfully added {data['name']}")
    except Exception as e:
        logger.error(e)
        return HttpResponse(e, status=http.HTTPStatus.BAD_REQUEST)


def update_inventory_item(request):
    logger.info(f'update_inventory_item(): called with request={request}')
    if request.method != 'PUT':
        return HttpResponse(status=http.HTTPStatus.METHOD_NOT_ALLOWED)
    
    try:
        logger.debug(f"body={request.body}")
        data = json.loads(request.body)['data']
        logger.debug(f"data={data}")
        inventoryID = int(data["inventoryID"])
        item = CurrentInventory.objects.get(pk=inventoryID)
        item.name = data['name']
        item.unit_price = float(data['unitPrice'])
        item.quantity = float(data['quantity'])
        item.minimal_supply = float(data['minimalSupply'])
        item.save()
        return HttpResponse(f"Successfully updated {data['name']}")
    except Exception as e:
        logger.error(e)
        return HttpResponse(e, status=http.HTTPStatus.BAD_REQUEST)

def get_produced_items(request):
    logger.info(f'get_produced_items(): called with request={request}')
    if request.method != 'GET':
        return HttpResponse(status=http.HTTPStatus.METHOD_NOT_ALLOWED)
    
    produced = list(map(lambda x: x.to_dict(), ProductionLog.objects.all()))
    produced.reverse()
    return JsonResponse({'data': produced}, safe=False)

def produce_item(request):
    logger.info(f'produce_item(): called with request={request}')
    if request.method != 'POST':
        return HttpResponse(status=http.HTTPStatus.METHOD_NOT_ALLOWED)
    
    try:
        logger.debug(f"body={request.body}")
        data = json.loads(request.body)['data']
        logger.debug(f"data={data}")
        inventoryID = int(data['inventoryID'])
        item = CurrentInventory.objects.get(pk=inventoryID)
        quantity = float(data['quantity'])
        item.quantity = round(float(item.quantity) + quantity, 2)
        produced = item.productionlog_set.create(quantity=quantity)
        item.save()
        return HttpResponse(f"Successfully produced {produced.productionID}")
    except Exception as e:
        logger.error(e)
        return HttpResponse(e, status=http.HTTPStatus.BAD_REQUEST)
