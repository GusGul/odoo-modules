from . import models
from . import wizard

def _gus_pre_init_hook(cr):
    print("Olá, este hook é executado antes do início da instalação")
    # cr.execute()
    # cr.commit()
    # env = api.Environment(cr, SUPERUSER_ID, {})
    # env['res.partner'].custom_hook_method()

def _gus_post_init_hook(cr, registry):
    print("Olá, este hook é executado após o fim da instalação")
    # cr.execute()
    # cr.commit()
    # env = api.Environment(cr, SUPERUSER_ID, {})
    # env['res.partner'].custom_hook_method()

def _gus_uninstall_hook(cr, registry):
    print("Olá, este hook é executado após a desinstalação")
    # cr.execute()
    # cr.commit()
    # env = api.Environment(cr, SUPERUSER_ID, {})
    # env['res.partner'].custom_hook_method()

def _gus_post_load_hook():
    # Pode sobrescrever (overwrite) de métodos http
    pass