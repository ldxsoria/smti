#service cron restart
def start():

    #LIBRERIAS GENERALES
    import psycopg2
    from datetime import date
    from datetime import datetime, timedelta
    from decouple import Config, RepositoryEnv

    #LIBRERIAS CORREO
    import smtplib 
    from email.message import EmailMessage 

    #VARIABLES GLOBALES
    DOTENV_FILE = '/code/docker_django/docker_django/.env'
    env_config = Config(RepositoryEnv(DOTENV_FILE))

    smtp = env_config.get('EMAIL_HOST')
    port_smtp = env_config.get('EMAIL_PORT')
    sender = env_config.get('EMAIL_HOST_USER')
    sender_password = env_config.get('USER_MAIL_PASSWORD')

    temp_list = []
    content_info = []

    # GET DATA ##############################################
    try:
        connection = psycopg2.connect(user = "postgres", password = "postgres", host = "db_postgres", port = "5432", database = "postgres")
        cursor = connection.cursor()
        
        cursor.execute("SELECT id, fecha_solicitud, hora_solicitud FROM myapp_ticket WHERE completado=False")
        records = cursor.fetchall()
        print (records)
        for record in records:
            temp_list.append(record)

        print (f"Conectado....")

    except (Exception, psycopg2.Error) as error :
        print (f"Error while connecting to PostgreSQL{error}")

    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print ("PostgreSQL connection is closed")

    #CONSTRUIR HTML #########################################

    for r in temp_list:
        #Obtengo ID
        id = r[0]

    #Obtegno fecha y hora para unirlos
    r1_r2 = f'{str(r[1])} {str(r[2])}'

    #los uno en una variable
    solicitud_time = datetime.strptime(r1_r2, '%Y-%m-%d %H:%M:%S.%f')

    #Obtengo la fecha y hora actual
    #now_time = datetime.strptime('2022-12-15 08:00:00.000', '%Y-%m-%d %H:%M:%S.%f')
    now_time = datetime.now()

    print (f'Ticket #{id}')
    tiempo_transcurrido = now_time - solicitud_time
    print (f'Pasaron {tiempo_transcurrido} desde la creacion del ticket')
    print('------------')
    print(solicitud_time)
    ticket_expired_time = solicitud_time + timedelta(days=5)#Aqui el tiempo para que mande una alerta
    print('------------')
    print(now_time)
    print(ticket_expired_time)
    print(now_time > ticket_expired_time)
    if now_time > ticket_expired_time:
        #print ('True')
        ticket_info = f'El Ticket #{id}, paso {ticket_expired_time - now_time} sin atenderse'
        content_info.append(ticket_info)


    else :
        print ('False')

    li_html = ''
    for ticket in content_info:
        li_html += f'<li>{ticket}</li>'

    fecha = datetime.now()
    subject = f"Hola, tienen tickets sin completar al {fecha}" 
    receiver = ["ldxnotes@gmail.com", ]
    content = f"<h1>Los tickets sin completar tienen m&aacute;s de 5 d&iacute;as </h1> \
                <br> \
                <p>Detalle:</p>\
                <ul>\
                {li_html}\
                </ul>\
                <p>Para ver m&aacute; informaci&oacute;n ve a SIGMA MIT</p>
                "
    # CORREO ################################################
    message = EmailMessage() 

    # Configure email headers 
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver

    # Set email body text 
    message.set_content(content, subtype="html") 

    # Set smtp server and port 
    server = smtplib.SMTP(smtp, port_smtp) 

    # Identify this client to the SMTP server 
    server.ehlo() 

    # Secure the SMTP connection 
    server.starttls() 

    # Login to email account 
    server.login(sender, sender_password) 

    # Send email 
    server.send_message(message) 

    # Close connection to server 
    server.quit()
    
def stop():
    pass