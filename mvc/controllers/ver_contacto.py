import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class VerContacto:

    #recibe el id del contacto desde la url /ver_contacto/<id>
    def GET(self, id_contacto):
        model_contactos = ModelContactos()

        #busca en supabase el contacto con ese id
        datos = model_contactos.buscarContacto(int(id_contacto))

        #si no existe, regresa una lista vacia
        if len(datos) == 0:
            web.header('Content-Type', 'text/html; charset=utf-8')
            return "<h1>Contacto no encontrado</h1><a href='/contactos'>Regresar</a>"

        #envia a ver_contacto.html el primer (y unico) registro
        return render.ver_contacto(datos[0])
