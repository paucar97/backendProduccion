# IMPORTAS LOS MODELOS QUE NECESISTES CUIDADO CON LAS DEPENDENCIAS
from app.models.usuario import Usuario
from app.models.semestre import Semestre
from app.models.permiso_usuario_horario import Permiso_usuario_horario 
def Login_Controlador(email,clave):
    usuario = Usuario().getOne(email,clave)
    semestreActivo = Semestre().getOne()
    ##print(semestreActivo,usuario.flg_admin)
    if usuario is None:
        return {'message':'error datos'}
    if semestreActivo == None and str(usuario.flg_admin) == "1":
            d = {}
            d['idUser'] = usuario.id_usuario
            d['codigoPUCP'] = usuario.codigo_pucp
            d['nombre'] = usuario.nombre + ' ' + usuario.apellido_paterno
            d['superUsuario'] = usuario.flg_admin
            d['profesor'] = 0
            d['jp'] = 0
            d['alumno'] = 0
            return d
    
    lista = Permiso_usuario_horario().getHorarioActivo(semestreActivo.id_semestre,usuario.id_usuario)
    contProfesor =0
    contJP = 0
    contAlumno = 0
    for usuarioHorario in lista:
        if usuarioHorario.id_permiso == 1:
            contProfesor = 1
        elif usuarioHorario.id_permiso == 2:
            contAlumno = 1
        else:
            contJP = 1
    d = {}
    d['idUser'] = usuario.id_usuario
    d['codigoPUCP'] = usuario.codigo_pucp
    d['nombre'] = usuario.nombre + ' ' + usuario.apellido_paterno
    d['superUsuario'] = usuario.flg_admin
    d['profesor'] = contProfesor
    d['jp'] = contJP
    d['alumno'] = contAlumno

    return d
    

    
