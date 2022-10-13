# KY-023 (Joystick)

El joystick no requiere alguna librería descargable para trabajar con el, con contar con micropython puedes trabajar
siempre y cuanto tengas los pines 26 y 27 disponitbles para el input de los ejes, el btn funciona como cuando tienes un btn switch externo.

Los valores de los pines ADC 26 y 27 de los ejes, van de 0 a 65535, una vez capturas esos datos y los alojas en una variable para mayor manejabilidad,
puedes usarlos para que dentro de un loop manejes el if que defina que hacer con los valores, ya depende de cada usuario el como definir el uso de estos valores 
para interpetar que vemos como derecha o izquierda, arriba o abajo, etc.

Puedes convertir este codigo base en una libreria similar al trabajo de la picozero para usarla en otro proyectos, o si queires tener la memoria de la pico limpia,
usar el code raw solo cuando lo necesites.


