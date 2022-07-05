from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)

# mysql coneccion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='consulta'
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM paciente ORDER BY  paciente.noHistorialMedico desc')
    datas = cur.fetchall()
    
    return render_template('index.html', data = datas)
    
##atender pacientes
@app.route('/atenderPedriatria')
def atenderPedriatria():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT p.*,ninop.relacionPesoEstatura
    FROM paciente p
    INNER JOIN ninop ON ninop.paciente_id = p.id
    WHERE NOT EXISTS (SELECT * FROM salaespera s
    WHERE p.id = s.id_paciente ) AND p.edad >=1 AND p.edad <=15 and prioridad <= 4
    ORDER BY ninop.relacionPesoEstatura desc""")
    prediatria = cur.fetchall() 

    cur.execute("SELECT * FROM consulta where estado = 'espera' and tipoFconsulta= 'Pediatria'")
    consultas = cur.fetchall() 
    cur.execute("""SELECT a.*
        FROM paciente a
        WHERE a.edad = ( 
        SELECT MAX( edad )  FROM paciente)""")
    mAnciano = cur.fetchall() 


    return render_template('atenderPaciente.html', data = prediatria,consulta = consultas,maxEdad = mAnciano)

@app.route('/atenderGeneral')
def atenderGeneral():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT p.*
    FROM paciente p
    WHERE NOT EXISTS (SELECT * FROM salaespera s
    WHERE p.id = s.id_paciente ) AND p.edad > 15  and prioridad <= 4
    ORDER BY p.prioridad desc""")
    general = cur.fetchall() 

    cur.execute("SELECT * FROM consulta where estado = 'espera' and tipoFconsulta= 'Consulta General Integral'")
    consultas = cur.fetchall() 

    cur.execute("SELECT * FROM consulta where estado = 'espera' and tipoFconsulta= 'Pediatria'")
    consultas = cur.fetchall() 
    cur.execute("""SELECT a.*
        FROM paciente a
        WHERE a.edad = ( 
        SELECT MAX( edad )  FROM paciente)""")
    mAnciano = cur.fetchall() 
    return render_template('atenderGeneral.html', data = general,consulta = consultas, maxEdad = mAnciano)   

@app.route('/atenderUrgencia')
def atenderUrgencia():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT p.*
    FROM paciente p
    WHERE NOT EXISTS (SELECT * FROM salaespera s
    WHERE p.id = s.id_paciente ) AND p.prioridad > 4
    ORDER BY p.prioridad desc""")
    general = cur.fetchall() 

    cur.execute("SELECT * FROM consulta where estado = 'espera' and tipoFconsulta= 'Urgencia'")
    consultas = cur.fetchall() 

    cur.execute("""SELECT a.*
        FROM paciente a
        WHERE a.edad = ( 
        SELECT MAX( edad )  FROM paciente)""")
    mAnciano = cur.fetchall()
    return render_template('atencionUrgencia.html', data = general,consulta = consultas, maxEdad = mAnciano)       

##insert pacientes ninos
@app.route('/insert_ninos' , methods=['POST'])
def insert_ninos():
    if request.method == 'POST':
       nombre= request.form['nombre']
       peso= request.form['peso']
       edad= request.form['edad'] 
       estatura= request.form['estatura']     
       cur = mysql.connection.cursor()
       nedad=int(edad)
       elpeso=int(peso)
       laestatura=int(estatura)
       if nedad >= 1 and nedad <= 5:
            calculo= elpeso-laestatura+3
            cur.execute('INSERT INTO paciente (nombre,edad,noHistorialMedico,prioridad) VALUES (%s, %s, %s, %s)',
            (nombre, edad, 0,calculo))
            mysql.connection.commit()
            # select ultimo
            cur.execute('SELECT id FROM paciente ORDER BY id DESC LIMIT 1')
            ultimo = cur.fetchall()
            # insert ninop
            cur.execute('INSERT INTO ninop (paciente_id,relacionPesoEstatura) VALUES (%s, %s)',
            (ultimo, calculo))
            mysql.connection.commit()
            flash('Paciente inmgresado exitosamente')
           
    if nedad >= 6 and nedad <= 12:
                calculo= elpeso-laestatura+2
                cur.execute('INSERT INTO paciente (nombre,edad,noHistorialMedico,prioridad) VALUES (%s, %s, %s, %s)',
                (nombre, edad, 0,calculo))
                mysql.connection.commit()
                # select ultimo
                cur.execute('SELECT id FROM paciente ORDER BY id DESC LIMIT 1')
                ultimo = cur.fetchall()
                # insert ninop
                cur.execute('INSERT INTO ninop (paciente_id,relacionPesoEstatura) VALUES (%s, %s)',
                (ultimo, calculo))
                mysql.connection.commit()
                flash('Paciente inmgresado exitosamente')
                
                if nedad >= 13 and nedad <= 15:
                    calculo= elpeso-laestatura+1
                    cur.execute('INSERT INTO paciente (nombre,edad,noHistorialMedico,prioridad) VALUES (%s, %s, %s.%s)',
            (nombre, edad, 0,calculo))
                    mysql.connection.commit()
                    # select ultimo
                    cur.execute('SELECT id FROM paciente ORDER BY id DESC LIMIT 1')
                    ultimo = cur.fetchall()
                    # insert ninop
                    cur.execute('INSERT INTO ninop (paciente_id,relacionPesoEstatura) VALUES (%s, %s)',
                    (ultimo, calculo))
                    mysql.connection.commit()
                    flash('Paciente inmgresado exitosamente')
    return redirect(url_for('Index'))

##insert pacientes cgi
@app.route('/insert_cgi' , methods=['POST'])
def insert_cgi():
    if request.method == 'POST':
       nombre= request.form['nombre']
       edad= request.form['edad']
       fumador= request.form['fumador'] 
       afumador= request.form['afumador']  
       dieta= request.form['dieta']
       nedad=int(edad)
       nfuma=int(fumador)
       ndieta=int(dieta)
       anfuma=int(afumador)
       cur = mysql.connection.cursor()
       if nedad > 16 and nedad <= 40:
            if nfuma == 1:
                calculo=anfuma/4+2
                cur.execute('INSERT INTO paciente (nombre,edad,noHistorialMedico,prioridad) VALUES (%s, %s, %s, %s)',
                (nombre, edad, 0,calculo))
            mysql.connection.commit()
            cur.execute('SELECT id FROM paciente ORDER BY id DESC LIMIT 1')
            ultimo = cur.fetchall()
            cur.execute('INSERT INTO pjoven (paciente_id,fumador) VALUES (%s, %s)',
            (ultimo, nfuma))
            mysql.connection.commit()
            flash('Paciente inmgresado exitosamente')
          
            
            if nfuma == 0:
                calculo=2
                cur.execute('INSERT INTO paciente (nombre,edad,noHistorialMedico,prioridad) VALUES (%s, %s, %s, %s)',
                (nombre, edad, 0,calculo))
            mysql.connection.commit()
            cur.execute('SELECT id FROM paciente ORDER BY id DESC LIMIT 1')
            ultimo = cur.fetchall()
            cur.execute('INSERT INTO pjoven (paciente_id,fumador) VALUES (%s, %s)',
            (ultimo, nfuma))
            mysql.connection.commit()
            flash('Paciente ingresado exitosamente')
    if nedad >40 and nedad <=60:    
        calculo= nedad/30+3
        cur.execute('INSERT INTO paciente (nombre,edad,noHistorialMedico,prioridad) VALUES (%s, %s, %s, %s)',
                (nombre, edad, 0,calculo))
        mysql.connection.commit()
        cur.execute('SELECT id FROM paciente ORDER BY id DESC LIMIT 1')
        ultimo = cur.fetchall()
        cur.execute('INSERT INTO panciano (paciente_id,tieneDieta) VALUES (%s, %s)',
        (ultimo, ndieta))
        mysql.connection.commit()
        flash('Paciente inmgresado exitosamente')
       

    if nedad >=60 and nedad <=100 and ndieta == 1: 
         
         calculo= nedad/20+4
         cur.execute('INSERT INTO paciente (nombre,edad,noHistorialMedico,prioridad) VALUES (%s, %s, %s, %s)',
                (nombre, edad, 0,calculo))
         mysql.connection.commit()
         cur.execute('SELECT id FROM paciente ORDER BY id DESC LIMIT 1')
         ultimo = cur.fetchall()
         cur.execute('INSERT INTO panciano (paciente_id,tieneDieta) VALUES (%s, %s)',
         (ultimo, ndieta))
         mysql.connection.commit()
         flash('Paciente inmgresado exitosamente')
    return redirect(url_for('Index'))

@app.route('/salaEspera/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM salaespera WHERE id_paciente = {0}'.format(id))
    mysql.connection.commit()
    flash('Paciente ingresado a sala atencion')
    return redirect(url_for('Index'))

#asignar paciente consulta

@app.route('/insert_consultaPaciente/<id>', methods=['POST'])
def insert_consultaPaciente(id):
    if request.method == 'POST':
        consulta = request.form['consulta']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO salaespera (id_consulta,id_paciente) VALUES (%s, %s)',
                (consulta, id))
        mysql.connection.commit()

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE consulta
        SET estado = %s
        WHERE id = %s    
        """, ("OCUPADO",consulta))
        mysql.connection.commit()

    historial = """SELECT  noHistorialMedico FROM paciente WHERE id = %s"""
    numHisatorial=cur.execute(historial, (id,))
    nHistorial=cur.fetchall()
    for x in nHistorial:
        suma=x[0]+1
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE paciente
        SET noHistorialMedico = %s
        WHERE id = %s    
        """, (suma, id))
        mysql.connection.commit()

    canPacientes = """SELECT  canPacientes FROM consulta WHERE id = %s"""
    numPacientes=cur.execute(canPacientes, (consulta,))
    nPacientes=cur.fetchall()
    for x in nPacientes:
        suma=x[0]+1
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE consulta
        SET canPacientes = %s
        WHERE id = %s    
        """, (suma, consulta))
        mysql.connection.commit()

    flash('Consulta asignada a paciente')
    return redirect(url_for('Index'))
#consultas
@app.route('/consultas')
def consultas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM consulta   ')
    datas = cur.fetchall()

    cur.execute("""SELECT t.*
    FROM consulta t
    WHERE t.canPacientes = ( 
    SELECT MAX( canPacientes )  FROM consulta)""")
    masConsulta = cur.fetchall()
    return render_template('consultas.html', data = datas, max = masConsulta) 

@app.route('/liberarConsulta')
def liberarConsulta():
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE consulta
        SET estado = %s
        WHERE estado = %s    
        """, ('espera', 'ocupado'))
    mysql.connection.commit()
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM consulta   ')
    datas = cur.fetchall()
    flash('Consultas Liberadas')
    return render_template('consultas.html', data = datas) 





if __name__ == '__main__':
    app.run(port = 3000, debug = True) 