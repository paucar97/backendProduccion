from flask_restful import Resource
from flask import Flask, request
from app.controller.CTR_Entregable import *

class Subir_entregable(Resource):
    def post(self):
        #img_file = request.files.get('file')
        #request.files.getlist('file')[0]
        ##print(type(request))
        #print(request.form)
        
        idActividad  = int(request.form['idActividad'])
        
        idUsuario = int(request.form['idUsuario'])
        
        tipo = int(request.form['tipo'])
        
        listaFiles=None
        url=""
        
        if tipo == 1:
            cantidadFiles = int(request.form['cantidadFiles'])
            listaFiles=[]
            for i in range(1,cantidadFiles+1):
                key = 'file {}'.format(i)
                #rint(key)p
                listaFiles.append(request.files.get(key))
            #listaIdFiles= request.files.get('file 1')

            #ImmutableMultiDict([('file 1', <FileStorage: 'ricardo.png' ('image/png')>), ('files 2', <FileStorage: 'ricardo.jpg' ('image/jpeg')>)])
            #print(listaFiles)
        elif tipo == 2:
            url = request.form['url']
        else:
            cantidadFiles = int(request.form['cantidadFiles'])
            listaFiles=[]
            for i in range(1,cantidadFiles+1):
                key = 'file {}'.format(i)
                #rint(key)p
                listaFiles.append(request.files.get(key))
            url = request.form['url']
        

        return subirEntregable(idActividad,idUsuario,listaFiles,url,tipo)


class Mostar_entregable(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idUsuario = data['idUsuario']
        rpta = mostrarEntregable(idActividad,idUsuario)
        return rpta

class Descarga_entregabla(Resource):

    def post(self):
        data = request.get_json()
        idEntregable = data['idEntregable']
        return descargaEntregable(idEntregable) 