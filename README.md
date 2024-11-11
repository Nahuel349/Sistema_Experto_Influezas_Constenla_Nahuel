# *Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial* 
# *Politécnico Malvinas Argentinas.*

------------

## Desarrollo de Sistemas de Inteligencia Artificial 

Estudiante: Nahuel Constenla.

------------

# Gripe_Influenza

Detección previa de un diagnóstico de Gripes llamadas Influenza, Gripe, común, Covid19 o neumonía en la Provincia de Tierra del Fuego.

------------

##### Definición del problema 

La provincia de Tierra del Fuego, al igual que otras regiones con las mismas características climáticas, experimenta brotes de 
influenza de manera periódica o estacional. Esta enfermedad respiratoria aguda, causada por virus de la influenza, puede causar 
síntomas como fiebre, tos, dolor de garganta, congestión nasal, dolores musculares y fatiga.

La provincia de Tierra del fuego tiene características particulares como la estacionalidad que provoca que los casos de influenza 
aumenten durante en los meses más fríos del año, coincidiendo con el invierno austral. Una Población vulnerable, 
grupos de mayor riesgo que incluyen a los niños más pequeños, adultos mayores, las embarazadas y personas con enfermedades crónicas. 
Las autoridades sanitarias de la provincia de Tierra del Fuego suelen implementar campañas de vacunación antigripal, 
especialmente dirigidas a estos grupos de riesgo. 
Ocasionalmente, se producen brotes epidémicos de influenza, lo que puede generar una mayor demanda de atención médica y medidas de control.

Por otro lado la Influenza aviar, la provincia de Tierra del Fuego también se ha visto afectada, este virus que afecta principalmente 
a las aves pero que puede transmitirse a otros animales, incluidos los mamíferos marinos. Si bien esta enfermedad no se transmite 
fácilmente a los humanos, se han implementado medidas de vigilancia y control para evitar su propagación.

------------

##### OBJETIVO

Crear un Sistema experto que oriente a un previo diagnóstico de la presencia de alguna de las gripes llamadas “Influenza”, Gripe Común, 
Covid19 o algo más grave que requiera una atención medica más inmediata como la Neumonía, en las personas. 
Este sistema estará integrado en alguna Aplicación que permita acceder por vía Web.

------------

#### PROBLEMA A ABORDAR

Detección previa de un diagnóstico de Gripes llamadas Influenza, Gripe, común, Covid19 o neumonía en la Provincia de Tierra del Fuego.

------------

#### CONSULTA AL EXPERTO HUMANO

Para el desarrollo de Proyecto se consultó a dos especialistas en enfermedades Infectologicas, El Medico Infectologo del Hospital Regional 
de Río Grande Dr. Edgar Vega y la Enfermera infectologa especialista en casos, Lic. Marcela Digiorgi también del nosocomio local.

------------

#### DOMINIO
Gripe Influenza

------------

#### SELECCIÓN DEL SUBDOMINIO

El subdominio seleccionado dentro del dominio general de la influenza en la provincia de Tierra del Fuego será la detección y manejo de casos de influenza estaciona. Este subdominio es relevante debido a que la influenza tiene un impacto más significativo en ciertos grupos, como niños pequeños, ancianos, y personas con comorbilidades, lo que requiere un enfoque especializado en la detección temprana y el tratamiento adecuado.
PROBLEMA A ABORDAR
Detección previa de un diagnóstico de Gripes llamadas Influenza, Gripe, común, Covid19 o neumonía en la Provincia de Tierra del Fuego.

------------

#### DEFINICIÓN DE CRITERIOS Y ATRIBUTOS:

Se identificaron los diferentes atributos para las decisiones en torno al diagnóstico y tratamiento de la enfermedad.

1.- Diagnóstico Clínico
    a.- Criterios
        •	Síntomas iniciales
        •	Examen físico
        •	Pruebas diagnósticas
    b.- Atributos
        •	Síntomas iniciales (Fiebre alta, Dolor de cabeza, Dolor muscular, Tos seca, Fatiga)
        •	Examen físico (Frecuencia respiratoria elevada, Congestión nasal, Auscultación anormal o sonidos respiratorios)
        •	Pruebas diagnósticas (Test rápido de influenza, PCR para detectar el virus)

2.- Factores de riesgo
    a.- Criterios
        •	Edad
        •	Condiciones médicas preexistentes
        •	Exposición a personas infectadas
    b.- Atributos
        •	Edad (Mayores de 65 años, Niños menores de 5 años)
        •	Condiciones médicas preexistentes (Enfermedades respiratorias [ej. Asma o EPOC], Enfermedades crónicas [ej. Diabetes o enfermedades cardíacas], Inmunosupresión)
        •	Exposición a personas infectadas (Contacto cercano en las últimas 48 horas con personas infectadas)

3.- Complicaciones
    a.- Criterios
        •	Complicaciones respiratorias
        •	Complicaciones sistémicas
    b.- Atributos
        •	Complicaciones respiratorias (Neumonía viral, Neumonía bacteriana secundaria)
        •	Complicaciones sistémicas (Miocarditis, Síndrome de Guillain-Barré, Muerte en casos graves)

###### Ejemplo de preguntas:

    •	¿El paciente tiene fiebre alta?
    •	¿El paciente presenta dolor de cabeza o dolores musculares?
    •	¿La aparición de los síntomas fue repentina o gradual?
    •	¿Tiene tos o dolor de garganta?
    •	¿El paciente ha estado en contacto con alguien diagnosticado con influenza?

#### IMPORTANTE

La base de conocimiento propuesta proporciona una estructura para el desarrollo de un sistema experto en diagnóstico de influenza 
en Tierra del Fuego, la cual fue expuesta a la consulta y análisis de corrección de expertos humanos, en este caso, 
doctores del Hospital de Río Grande con conocimiento en Infectologia. Sin embargo, es importante destacar que este es solo 
un punto de partida y que se requiere un mayor desarrollo y validación para garantizar su utilidad en la práctica clínica. 

#### REGLAS, CRITERIOS Y ESTRUCTURAS DEL SISTEMA EXPERTO 

El conocimiento en este sistema está organizado en función de los síntomas, agrupándolos según su nivel y la jerarquización sigue un flujo lógico desde síntomas generales hasta síntomas más específicos para un diagnóstico más aproximado. Esto permite al sistema realizar diagnósticos progresivos y minimizar errores.

##### Ejemplos

    •	Síntomas Iniciales como Fiebre, escalofríos, tos persistente, dolor de garganta.
    •	Síntomas Adicionales Específicos tales como Congestión nasal, fatiga constante, dolores musculares, etc.
    •	Condiciones Externas o Específicas que pueden ser Contacto con animales, pérdida del olfato o gusto, etc.

##### MÉTODOS DE INFERENCIA REGLAS - IF-THEN - ÁRBOLE DE DECISIÓN

##### Ejemplo

1.- Supongamos que un paciente presenta los siguientes síntomas:

    •	Tiene fiebre de más de 38°C.
    •	Tiene escalofríos y fatiga constante.
    •	NO presenta vómitos ni diarrea.
    •	Tiene dolores musculares y tos seca con flema.
    •	NO ha perdido el olfato ni el gusto, pero tiene sudoración y pérdida de peso.

2.- El flujo de decisión en el sistema sería:

Fiebre alta (Sí) ➔ Escalofríos (Sí) ➔ Fatiga constante (Sí) ➔ Vómitos o diarrea (No) ➔ Dolores musculares (Sí) ➔ Tos seca con flema (Sí) ➔ Pérdida de peso (Sí).

3.- Resultado: 

    •	Diagnóstico de NEUMONIA.

##### Github

    •	https://github.com/Nahuel349/Sistema_Experto_Influezas_Constenla_Nahuel.git


##### Conocimiento de Sistema Experto

    •	Archivo: Enfermedades.JSON


##### Árbol de Decisión

    •	Archivo en la “Carpeta Documentación”: Árbol Decision.PNG


--------------------------------------------

## Guía para la Ejecución 

La guía ayudará a configurar y ejecutar el Sistema Experto utilizando el Framework Web **FastAPI** y la biblioteca de JavaScript **React**.

Seguir cada paso con precisión.

#### Es importante tener instalado

- **Python** y **pip** instalados en tu sistema.
- **Node.js** y **npm** instalados.
- Editor de código como **Visual Studio Code (VSC)**.

---

### Pasos de Instalación

#### 1. Guardar el Repositorio "Influenzas" 
Descargar del Repositorio el Sistema Experto **"Influenzas"** en su Disco Local, creara una carpeta con el proyecto.

---

#### 2. Configuración FastAPI

a.- Abrir el PRG **Visual Studio Code (VSC)** y Accede al directorio del Repositorio el Sistema Experto **"Influenzas"**. Debera de estar en la raíz del proyecto, donde se encuentra tu archivo `main.py`.
    
b.- En una **"TERMINAL"** debera ejecutar ejecuta el siguiente comando para iniciar el servidor
    
        uvicorn main:app --reload 
        
Esto inicia el servidor en `http://127.0.0.1:8000`. El parámetro `--reload` permite reiniciar automáticamente el servidor cada vez que realices cambios en el código.

c.- Verifica en el navegador que FastAPI esté corriendo correctamente en `http://127.0.0.1:8000/docs`.

---

#### 3. Configuración del Frontend (React)

a.- **Directorio frontend**, se ubicado en `frontend/frontend` dentro de tu proyecto. 
Debera abrir otra **"TERMINAL"**, luego poner le comando **"cd frontend"**. Debe hacerlo 2 veces.

b.- **Dependencias de Node.js Instaladas** - Necesarias para el proyecto

**Si YA las tiene Instaladas**  valla al Punto **"d"**.

**Si NO las tiene Instaladas** realice lo siguiente primero. 
    
    b1.- Ejecuta el siguiente comando en la terminal:
        npm install
    
    b2.- Si este comando da error, es probable que **Node.js** o **npm** no estén instalados.
    Para instalar Node.js: Descarga Node.js desde [nodejs.org](https://nodejs.org/).
    
    b3.- Sigue las instrucciones de instalación y asegúrate de que Node.js esté añadido a las **variables de entorno** del sistema (Path).
    
    b4.- **Verifica la instalación de Node.js** ejecutando:
        node -v
        npm -v
    Ambos comandos deberían mostrar un número de versión si están instalados correctamente.

c.- Si **aún tienes problemas con los permisos en PowerShell** al ejecutar `npm install`, ejecuta el siguiente comando en la terminal PowerShell para permitir la ejecución de scripts de manera segura: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned. Luego, vuelve a ejecutar `npm install`.

d.- **Inicia el servidor "React"** en el puerto 3000 con el siguiente comando:

    ´npm start´

Esto debería iniciar el frontend en `http://localhost:3000`. Asegúrate de que este
puerto no esté siendo utilizado por otra aplicación.

---

#### 4. Prueba de Conexión entre el Backend y el Frontend

a.- Asegúrate de que ambos servidores (El Puerto 8000 el Puerto 3000) se estén ejecutándose sin errores.
Sin no se "Abre", la pagina en el navegador copie...`http://localhost:3000` en el navegador para Intercambiar con el **"Sistema Experto INFLUENZAS"** a través de la interfaz cargada.

---

#### 5. Comandos en simples Pasos 
    
    a.- Iniciar el backend de FastAPI: "uvicorn main:app --reload"
    b.- Instalar dependencias de React en `frontend/frontend`: "npm install"
    c. Iniciar el servidor de React: "npm start"

Siguiendo estos pasos, deberías el Sistema Experto Funcionar Correctamente. Revisar cada paso.


### ARCHIVOS IMPORTANTES

#### ENFERMEDADES.JSON
El codigo describe la base del conocimiento del Sistema Experto Influenza en Tierra del Fuego

#### ACCIONES.Py
Este código implementa una interfaz de consola para gestionar la base de conocimientos usando un motor de inferencia.La interfaz permite cargar, modificar, guardar y recuperar información de la base de conocimientos.

#### MAIN.Py

Este código implementa una API con FastAPI para un sistema experto, que permite clasificar información con base en un conjunto de preguntas. La API permite cargar la base de conocimientos, iniciar las consulta y procesar las respuestas de usuarios.

#### CARPETA DOCUMENTACIÓN

* [Ver Documento](Documentacion/Arbol Decision.png)
* [Ver Documento](documentacion/Entrega N°1.pdf)
* [Ver Documento](documentacion/Entrega N°2.pdf)