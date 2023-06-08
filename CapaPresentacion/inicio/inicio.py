from flask import Blueprint, render_template, request, redirect, flash, session, url_for

inicio_bp = Blueprint("inicio", __name__, template_folder="templates")


@inicio_bp.route("/inicio")
def inicio():
    if 'rol' in session:
        if session['rol'] == "Administrador":
            inicio ='Inicio_administrador.html'
        else:
            if session['rol'] == "Ventas":
                inicio = 'Inicio_ventas.html' #cambiar luego
            else:
                inicio = 'Inicio_logistica.html'   #cambiar luego
        return render_template(inicio)
    else:
        return redirect(url_for('usuario.login'))