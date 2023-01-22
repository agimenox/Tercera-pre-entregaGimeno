HOLA CODER TUTOR!!!! 
------------------------------------------------------
    Resumen: El proyecto posee una aplicacion. donde se manejan los modelos/clases de "Clients, Groups, Users"
    La barra de navegacion se encuentra del lado izquierdo para interactuar con la data de cada uno.
    Se puede consultar, Filtrar y agregar datos.

    NOTA: El formato de la fecha en los formularios debe ser:  yyyy-mm-dd   Ej:   2023-01-13
------------------------------------------------------

REQUERIMIENTOS
    
    Es necesario  dentro del entorno virtualle ejecucion de: 
    
    $ py install requeriments.txt 
    
        Detalle de los paquetes:
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

codertutor
CoderCoder123

------------------------------------------------------
ESTRUCTURA

CoderClases ------------Main Folder
    mvt_coderhouse_project ----------------Proyecto Django
        mvt_users_mgmt_app     ----------------App
        static                 ----------------Contenido estatico
        db.sqlite3             -----------------BD


