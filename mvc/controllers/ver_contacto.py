import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class VerContacto:

    def GET(self,id_contacto):
        return render.ver_contacto()
