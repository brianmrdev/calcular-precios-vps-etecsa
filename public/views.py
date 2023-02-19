import json
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from core.models import Precio


class Index(View):
    def get(self, request):
        vps_etecsa = Precio.objects.get(name_vps="ETECSA")
        
        limit_cpu = []
        for i in range(1, vps_etecsa.cpu_limit + 1):
            limit_cpu.append(i)
        
        limit_ram = []
        for i in range(1, vps_etecsa.ram_limit + 1):
            limit_ram.append(i)
        
        limit_hdd = []
        for i in range(20, vps_etecsa.hdd_limit + 1):
            limit_hdd.append(i)

        
        context_data = {
            'title': 'Calcular recursos VPS ETECSA',
            'limit_cpu': limit_cpu,
            'limit_ram': limit_ram,
            'limit_hdd': limit_hdd,
        }
        return render(request, 'index.html', context_data)


@csrf_exempt
def calcular_precio(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        cpu_cantidad = request.POST['CPU']
        ram_cantidad = request.POST['RAM']
        hdd_cantidad = request.POST['HDD']
        
        vps_etecsa = Precio.objects.get(name_vps="ETECSA")
        
        pago_diario = (int(cpu_cantidad) * vps_etecsa.cpu * 24) + (int(ram_cantidad) * vps_etecsa.ram * 24) + (int(hdd_cantidad) * vps_etecsa.hdd * 24)
        pago_mensual = pago_diario * 30       
        
        msg = {'status': True, 'msg': 'OK', 'diario': str(pago_diario), 'mensual': str(pago_mensual)}
        return HttpResponse(json.dumps(msg))
    else:
        msg = {'status': False, 'msg': 'Ocurrio un error, formulario no valido'}
        return HttpResponse(json.dumps(msg))