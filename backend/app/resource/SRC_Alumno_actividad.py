from flask_restful import Resource
from flask import Flask, request
from app.controller import CTR_Alumno_Actividad as controller

class Obtener_entregables_actividad_por_alumno(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        # VALIDACION
        #
        #
        return controller.entregablesActividadXAlumno(idActividad)

class Ingresar_comentario_alumno(Resource):
    def post(self):
        data = request.get_json()
        idActividad = int(data['idActividad'])
        idAlumno = int(data['idAlumno'])
        comentario = data['comentario']
        # VALIDACION
        #
        #
        return controller.ingresarComentarioAlumno(idActividad, idAlumno, comentario)

class Responder_comentario_alumno(Resource):
    def post(self):
        data = request.get_json()
        idActividad = int(data['idActividad'])
        idAlumno = int(data['idAlumno'])
        idProfesor = int(data['idProfesor'])
        respuesta = data['respuesta']
        # VALIDACION
        #
        #
        return controller.responderComentarioAlumno(idActividad, idAlumno, idProfesor, respuesta)

class Listar_comentarios_actividad(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']

        return controller.listarComentarios(idActividad)

class Obtener_alumnos_actividad(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']

        return controller.listaAlumnos(idActividad)

class Obtener_nota_alumno(Resource):
    def post(self):
        data = request.get_json()
        idAlumno = data['idAlumno']
        idActividad = data['idActividad']
        tipo = data['tipo']
        idCalificador = data['idCalificador']
        return controller.obtenerNotaAlumno(idAlumno, idActividad, tipo, idCalificador)

class Calificar_alumno_actividad(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idAlumno = data['idAlumno']
        idJp = data['idJp']
        nota = data['nota']
        idRubrica = data['idRubrica']
        flgFalta = data['flgFalta']
        listaNotaAspectos = data['listaNotaAspectos']
        flgCompleto = data['flgCompleto']
        #flgCalifico = data['flgCalifico']

        return controller.calificarAlumno(idActividad, idAlumno, idRubrica, idJp, nota, listaNotaAspectos, flgFalta, flgCompleto)

class Calificar_grupo(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idGrupo = data['idGrupo']
        idJp = data['idJp']
        nota = data['nota']
        idRubrica = data['idRubrica']
        flgFalta = data['flgFalta']
        listaNotaAspectos = data['listaNotaAspectos']
        flgCompleto = data['flgCompleto']
        #flgCalifico = data['flgCalifico']

        return controller.calificarGrupo(idActividad, idGrupo, idRubrica, idJp, nota, listaNotaAspectos, flgFalta, flgCompleto)

class Obtener_nota_grupo(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idGrupo = data['idGrupo']
        idJp = data['idJp']
        ##print(idActividad,idGrupo,idJp)
        return controller.obtenerNotaGrupo(idActividad, idGrupo, idJp)

class Editar_nota_grupo(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idGrupo = data['idGrupo']
        idRubrica = data['idRubrica']
        nota = data['nota']
        listaNotaAspectos = data['listaNotaAspectos']
        idJpAnt = data['idJpAnt']
        idJpN = data['idJpN']
        flgFalta = data['flgFalta']
        flgCompleto = data['flgCompleto']
        return controller.editarNotaGrupo(idActividad, idGrupo, idRubrica, idJpAnt, idJpN, nota, listaNotaAspectos, flgFalta, flgCompleto)

class Editar_nota_alumno_actividad(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idAlumno = data['idAlumno']
        nota = data['nota']
        idRubrica = data['idRubrica']
        listaNotaAspectos = data['listaNotaAspectos']
        idJpAnt = data['idJpAnt']
        idJpN = data['idJpN']
        flgFalta = data['flgFalta']
        flgCompleto = data['flgCompleto']
        return controller.editarNotaAlumno(idActividad, idAlumno, idRubrica, idJpAnt, idJpN, nota, listaNotaAspectos, flgFalta, flgCompleto)

class Listar_alumnos_destacados(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']

        return controller.listarAlumnosDestacados(idActividad)

class Obtener_estadistica_actividad(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']

        return controller.obtenerEstadisticaActividad(idActividad)


#class Enviar_notificacion_profesor(Resource):
#    def post(self):
#        data = request.get_json()

class Lista_alumnos_notas(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']

        return controller.listarAlumnosNotas(idActividad)

class Obtener_autoevaluacion(Resource):
    def post(self):
        data = request.get_json()
        idAlumno = data['idAlumno']
        idActividad = data['idActividad']

        return controller.obtenerAutoevaluacion(idAlumno, idActividad)

class Obtener_coevaluacion(Resource):
    def post(self):
        data = request.get_json()
        idCalificado = data['idCalificado']
        idActividad = data['idActividad']
        idCalificador = data['idCalificador']

        return controller.obtenerCoevaluacion(idCalificado, idActividad, idCalificador)


class Calificar_autoevaluacion(Resource):
    def post(self):
        data = request.get_json()
        #print(data)
        idActividad = data['idActividad']
        idAlumno = data['idAlumno']
        nota = data['nota']
        idRubrica = data['idRubrica']
        flgFalta = data['flgFalta']
        listaNotaAspectos = data['listaNotaAspectos']
        flgCompleto = data['flgCompleto']
        
        return controller.calificarAutoevaluacion(idActividad, idAlumno, idRubrica, nota, listaNotaAspectos, flgFalta, flgCompleto)

class Calificar_coevaluacion(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idAlumno = data['idAlumno']
        idCalificador = data['idCalificador']
        nota = data['nota']
        idRubrica = data['idRubrica']
        flgFalta = data['flgFalta']
        listaNotaAspectos = data['listaNotaAspectos']
        flgCompleto = data['flgCompleto']
        return controller.calificarCoevaluacion(idActividad, idAlumno, idCalificador, idRubrica, nota, listaNotaAspectos, flgFalta, flgCompleto)

class Obtener_notas_coevaluacion(Resource):
    def post(self):
        data = request.get_json()
        idGrupo = data['idGrupo']
        idActividad = data['idActividad']
        return controller.sumaCoevaluacion(idGrupo, idActividad)

class Publicar_calificacion_para_revision(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idJpReviso = data['idJpReviso']
        return controller.publicarParaRevision(idActividad, idJpReviso)

class Listar_revisiones_profesor(Resource):
    def post(self):
        data = request.get_json()
        idProfesor = data['idProfesor']
        return controller.listarRevisiones(idProfesor)

class Publicar_notas_profesor(Resource):
    def post(Self):
        data = request.get_json()
        idActividad = data['idActividad']
        idProfesor = data['idProfesor']
        return controller.publicarProfesor(idActividad, idProfesor)

class Obtener_nota_grupo_publicada(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idGrupo = data['idGrupo']
        idJp = data['idJp']
        return controller.obtenerNotaGrupoPublicada(idActividad, idGrupo, idJp)

class Obtener_nota_alumno_publicada(Resource):
    def post(self):
        data = request.get_json()
        idAlumno = data['idAlumno']
        idActividad = data['idActividad']
        tipo = data['tipo']
        idCalificador = data['idCalificador']
        return controller.obtenerNotaAlumnoPublicada(idAlumno, idActividad, tipo, idCalificador)

class Obtener_notas_alumno_multicalificable(Resource):
    def post(self):
        data = request.get_json()
        idAlumno = data['idAlumno']
        idActividad = data['idActividad']
        return controller.obtenerTodasCalificacionesMulti(idAlumno, idActividad, 4)

class Elegir_nota_multicalificable(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idAlumno = data['idAlumno']
        notaFinal = data['notaFinal']
        return controller.elegirNotaMulticalificable(idActividad, idAlumno, notaFinal)

class Obtener_profesores_calificados(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idAlumno = data['idAlumno']
        return controller.obtenerProfesoresPublicados(idActividad, idAlumno)

class Obtener_profesores_calificados_grupal(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idGrupo = data['idGrupo']
        return controller.obtenerProfesoresPublicadosGrupal(idActividad, idGrupo)

class Elegir_nota_multicalificable_grupal(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idGrupo = data['idGrupo']
        notaFinal = data['notaFinal']
        return controller.elegirNotaMulticalificableGrupal(idActividad, idGrupo, notaFinal)

class Obtener_nota_final(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idAlumno = data['idAlumno']
        return controller.obtenerNotaFinal(idActividad, idAlumno)

class Obtener_nota_final_grupal(Resource):
    def post(self):
        data = request.get_json()
        idActividad = data['idActividad']
        idGrupo = data['idGrupo']
        return controller.obtenerNotaFinalGrupal(idActividad, idGrupo)
