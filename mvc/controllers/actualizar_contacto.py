import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class ActualizarContacto:

    def GET(self, id_contacto):
        model_contactos = ModelContactos()
        #busca en supabase el contacto con ese id
        datos = model_contactos.buscarContacto(int(id_contacto))
        #si no existe el contacto, envia una lista vacia para mostrar el mensaje
        if datos == []:
            return render.actualizar_contacto([])
        #envia a actualizar_contacto.html el primer contacto de la lista
        return render.actualizar_contacto(datos[0])