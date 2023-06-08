from flask import Blueprint, render_template, request, redirect, flash, url_for, session
import CapaNegocio.controlador_usuario as c_usuarios
usuarios_bp = Blueprint("usuario", __name__, template_folder="templates")

@usuarios_bp.route("/")
def login():
    if 'nombre' in session:
        return redirect(url_for('inicio.inicio')) #
    else:
        return render_template('login.html') #cargar un html

@usuarios_bp.route("/iniciar_sesion" , methods=["POST"])
def iniciar_sesion():
    usuario = c_usuarios.login(request.form['usuario'], request.form['contraseña'])
    if usuario == None:
        flash("El usuario no existe", "error")
    else:
        if usuario[4]:
            session['id'] = usuario[0]
            session['nombre'] = usuario[2]
            session['rol'] = usuario[7]
            return redirect(url_for('inicio.inicio'))
        else:
            flash("Contraseña incorrecta", "error")
    return redirect(url_for('usuario.login'))

@usuarios_bp.route("/cerrar_sesion")
def cerrar_sesion():
    session.clear()
    return redirect(url_for('usuario.login'))