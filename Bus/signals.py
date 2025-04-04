from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Ruta

@receiver(post_save, sender=Ruta)
def procesar_csv_ruta(sender, instance, created, **kwargs):
    """
    Señal que se activa después de guardar una Ruta.
    Si hay un CSV y no se han guardado coordenadas, las extrae y actualiza el campo.
    """
    if instance.archivo_csv and not instance.coordenadas:
        coords = instance.extraer_coordenadas_csv()
        if coords:
            instance.coordenadas = coords
            instance.save(update_fields=["coordenadas"])
