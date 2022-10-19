from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/libros', ApptiendaViewSetlibro, 'apptiendalibros'),
router.register('api/personas', ApptiendaViewSetpersona, 'apptiendapersonas'),
router.register('api/facturacion', ApptiendaViewSetfacturacion, 'apptiendafacturacion'),
router.register('api/usuario', ApptiendaViewSetusuario, 'apptiendausuario')

urlpatterns = router.urls