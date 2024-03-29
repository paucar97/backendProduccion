from app.models.encuesta import Encuesta
from app.models.pregunta import Pregunta
from app.models.actividad import Actividad
from app.models.encuesta_pregunta import Encuesta_pregunta
from app.models.horario_encuesta import Horario_encuesta
from app.models.rubrica import Rubrica
from app.controller import CTR_Actividad
from sqlalchemy import *

def crearAutoEvaluacion(idActividad, idFlgEspecial, idUsuarioCreador, nombreRubrica, listaAspectos, tipo):
    if tipo == 2:
        d = CTR_Actividad.crearRubrica(idActividad, idFlgEspecial, idUsuarioCreador, nombreRubrica, listaAspectos, tipo)
        return d
    else:
        d = {}
        d['succeed'] = False
        d['message'] = "No se esta intentando crear una autoevaluacion."
        return d
"""
def crearAutoEvaluacion(idActividad,listaFamilia):
    encuestaObjecto =Encuesta(
        tipo = 'AUTOEVALUACION',
        nombre = 'Autoevaluacion de la actividad '+str(idActividad),
        descripcion = 'PIMER SERVICIO',
        flg_especial =0
    )
    idEncuesta = Encuesta().addOne(encuestaObjecto)
    listaIdPreguntas=[]
    for familia in listaFamilia:
        
        nombreFamilia = familia['familia']

        listaPregunta = familia['listaPregunta']

        for pregunta in listaPregunta:
            
            auxPreguntaObjecto = Pregunta(
                descripcion = pregunta['pregunta'],
                tipo_pregunta = 3,
                familia = nombreFamilia
            )
            aux = Pregunta().addOne(auxPreguntaObjecto)
            listaIdPreguntas.append(aux)
    
    for idPregunta in listaIdPreguntas:
        Encuesta_preguntaObjecto = Encuesta_pregunta(
            id_encuesta = idEncuesta,
            id_pregunta = idPregunta
        ) 
        Encuesta_pregunta().addOne(Encuesta_preguntaObjecto)
    idHorario = Actividad().getOne(idActividad).id_horario
    Horario_encuestaObjecto = Horario_encuesta(
        id_horario = idHorario, # ESTO TIENE Q CAMIAR XQ DEBERIA SER NO OBLIGAROTIOR
        id_encuesta =idEncuesta,
        id_actividad = idActividad 
    )
    Horario_encuesta().addOne(Horario_encuestaObjecto)
    return
"""
def listarObjetosAutoevaluacion(idActividad):   
    idRubrica = Rubrica.query.filter(and_(Rubrica.id_actividad == idActividad, Rubrica.tipo == 2, Rubrica.flg_activo == 1)).first()
    if idRubrica is not None:
        return CTR_Actividad.obtenerRubricaXidRubrica(idRubrica.id_rubrica)
    else:
        d = {}
        d['succeed'] = False
        d['message'] = "No existe autoevaluacion"
        return d
"""
def listarObjetosAutoevaluacion(idActividad):   
    listaEncuesta=Horario_encuesta().getAll(idActividad)
    idencuesta=0
    for horario_encuesta in listaEncuesta:
        id=horario_encuesta.id_encuesta
        encuesta=Encuesta().getOne(id)
        if encuesta.tipo=='AUTOEVALUACION':
            idencuesta=encuesta.id_encuesta


    #print(idencuesta)
    if idencuesta==0:
        #print('error')
        return
    encuesta=Encuesta().getOne(idencuesta)
    
    l={}
    listaPregunta=[]
    listaFamilia=[]
    listaEP=[]
    id=encuesta.id_encuesta
    listaEP=Encuesta_pregunta().getAll(id)#Lista de todos los objetos preguntas para esa pregunta
    lista=[]
    for EncuestaPregunta in listaEP:
        idPregunta=EncuestaPregunta.id_pregunta
        pregunta=Pregunta().getOne(idPregunta)#sacarpreguntas
        listaPregunta.append(pregunta)
        q=pregunta.familia
        if pregunta.familia not in listaFamilia:#nueva familia encontrada
            c={}
            c["pregunta"]=pregunta.descripcion
            d={}
            listaP=[]
            d['familia']=q
            listaP.append(c)
            d['listaPregunta']=listaP
            lista.append(d)#anades un json con nombre de la familia
            listaFamilia.append(q)#lista solo con nombre de la familia
        else:# si ya se encuentra en la lista familia
            i=0
            for familia in listaFamilia:# lo busca
                if pregunta.familia==familia:# encontro la familia
                    c={}
                    c["pregunta"]=pregunta.descripcion
                    lista[i]['listaPregunta'].append(c)#anade pregunta a esa familia
                    break
                else:
                    i=i+1
                    
    l={}

    l['listaFamilia']=lista     
    return l
"""
def editarAutoEvaluacion(idActividad,listaFamilia):
    #print("="*20)
    #print(listaFamilia)
    listaEncuesta=Horario_encuesta().getAll(idActividad)
    idencuesta=0
    for horario_encuesta in listaEncuesta:
        id=horario_encuesta.id_encuesta
        encuesta=Encuesta().getOne(id)
        if encuesta.tipo=='AUTOEVALUACION':
            idencuesta=encuesta.id_encuesta
            
      
    if idencuesta==0:
        #print('error')
        return

    listaEncuestaPregunta=Encuesta_pregunta().getAll(idencuesta)
    Encuesta_pregunta().eliminarFilas(idencuesta)
    for encuestapregunta in listaEncuestaPregunta:
        idpregunta=encuestapregunta.id_pregunta
        Pregunta().eliminarPregunta(idpregunta)
    
    listaIdPreguntas=[]
    for familia in listaFamilia:
        
        nombreFamilia = familia['familia']

        listaPregunta = familia['listaPregunta']

        for pregunta in listaPregunta:
            
            auxPreguntaObjecto = Pregunta(
                descripcion = pregunta['pregunta'],
                tipo_pregunta = 3,
                familia = nombreFamilia
            )
            aux = Pregunta().addOne(auxPreguntaObjecto)
            listaIdPreguntas.append(aux)

    
    for idPregunta in listaIdPreguntas:
        Encuesta_preguntaObjecto = Encuesta_pregunta(
            id_encuesta = idencuesta,
            id_pregunta = idPregunta
        ) 
        Encuesta_pregunta().addOne(Encuesta_preguntaObjecto)
    
    return

def eliminarAutoEvaluacion(idActividad):
    rubricaADesactivar = Rubrica.query.filter(and_(Rubrica.id_actividad == idActividad, Rubrica.tipo == 2, Rubrica.flg_activo == 1)).first()
    d = CTR_Actividad.desactivarRubrica(rubricaADesactivar.id_rubrica)
    return d
"""
def eliminarAutoEvaluacion(idActividad):
    listaEncuesta=Horario_encuesta().getAll(idActividad)
    idencuesta=0
    for horario_encuesta in listaEncuesta:
        id=horario_encuesta.id_encuesta
        encuesta=Encuesta().getOne(id)
        if encuesta.tipo=='AUTOEVALUACION':
            idencuesta=encuesta.id_encuesta
            
    if idencuesta==0:
        #print('error')
        return
    listaEncuestaPregunta=Encuesta_pregunta().getAll(idencuesta)
    Encuesta_pregunta().eliminarFilas(idencuesta)
    for encuestapregunta in listaEncuestaPregunta:
        idpregunta=encuestapregunta.id_pregunta
        Pregunta().eliminarPregunta(idpregunta)

    Horario_encuesta().eliminarHorarioEncuesta(idencuesta)
    flag=Encuesta().eliminarEncuesta(idencuesta)
    

    return flag
"""
def existeAutoevaluacion(idActividad):
    listaEncuesta = Horario_encuesta().getAll(idActividad)
    if listaEncuesta is None:
        return {'message':'False'}
    else:
        for horario_encuesta in listaEncuesta:
            id = horario_encuesta.id_encuesta
            encuesta = Encuesta().getOne(id)
            if encuesta.tipo == 'AUTOEVALUACION':
                return {'message':'True'}

    return {'message':'False'}