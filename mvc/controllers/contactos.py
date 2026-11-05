import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class Index:

    def GET(self):

        model_contactos = ModelContactos

        print(model_contactos.obtenerContactos())

        return render.contactos() 