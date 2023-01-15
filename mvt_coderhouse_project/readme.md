HOLA CODER TUTOR!!!! 
------------------------------------------------------
    Descripción: El proyecto posee una aplicacion. que maneja los modelos/clases de "Clients, Groups, Users". aplicando django web como framework y formularios.
    
    Para probar/interactuar con el programa, contara con una barra de navegacion del lado izquierdo de la pantalla con las 3 clases. "CLIENT, USERS, GROUPS".
    
    Cada opcion lo llevara al panel correspondiente donde podra agregar otro registro con la opcion "ADD New..." y tambien podra consultar/filtrar utilizando el campo de texto.
    

    NOTA: El formato de la fecha en los formularios debe ser:  yyyy-mm-dd   Ej:   2023-01-13
------------------------------------------------------

REQUERIMIENTOS

pip install

    asgiref==3.6.0
    Django==4.1.5
    sqlparse==0.4.3
    tzdata==2022.7

------------------------------------------------------
URLs

    PAGINA DE INICIO 
    http://127.0.0.1:8000/home/home-page/


    ADMINISTRATION PANEL
    http://127.0.0.1:8000/admin/


    http://127.0.0.1:8000/home/home-page/  #Pagina Inicial
    http://127.0.0.1:8000/home/list-users/ #Consultas y adicion de usuarios. (FORMS)
    http://127.0.0.1:8000/home/list-clients/ #Consultas y adicion de clientes. (FORMS)
    http://127.0.0.1:8000/home/list-groups/  #Consultas y adicion de Grupos. (FORMS)

------------------------------------------------------
CREDENCIALES

Administration Panel:

User: codertutor
Pass: CoderCoder123

------------------------------------------------------
ESTRUCTURA

CoderClases ------------Main Folder
    mvt_coderhouse_project ----------------Proyecto Django
        mvt_users_mgmt_app     ----------------App
        static                 ----------------Contenido estatico
        db.sqlite3             -----------------BD


