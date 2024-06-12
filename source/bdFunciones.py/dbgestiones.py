from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from .models import MiModelo  # Asegúrate de reemplazar 'MiModelo' con el nombre de tu modelo real
from django.core.exceptions import ObjectDoesNotExist
import json

@require_http_methods(["POST"])
def guardar_datos(request):
    try:
        # Asumiendo que los datos vienen en formato JSON
        datos = json.loads(request.body)
        
        # Aquí deberías validar los datos recibidos
        
        # Crear o actualizar la instancia del modelo
        # Esto es solo un ejemplo, ajusta según tu modelo
        objeto, created = MiModelo.objects.update_or_create(
            id=datos.get('id', None),  # Asume que 'id' es opcional y se usa para actualizar
            defaults=datos,
        )
        
        # Guardar el objeto en la base de datos
        objeto.save()
        
        # Devolver una respuesta
        return JsonResponse({"success": True, "msg": "Datos guardados correctamente."})
    except Exception as e:
        return JsonResponse({"success": False, "msg": str(e)})

@require_http_methods(["GET"])
def obtener_informacion(request):
    try:
        # Asumiendo que se busca por un campo específico, por ejemplo, 'nombre'
        nombre = request.GET.get('nombre', '')
        
        # Filtrar los datos en la base de datos
        resultados = MiModelo.objects.filter(nombre__icontains=nombre).values()
        
        # Devolver los datos filtrados
        return JsonResponse(list(resultados), safe=False)
    except ObjectDoesNotExist:
        return HttpResponse("No se encontraron datos.", status=404)