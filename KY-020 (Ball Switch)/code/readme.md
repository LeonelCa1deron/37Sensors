Respecto a los hallazgos, el sensor funciona gracias a las librerías Pin y time, donde Pin permite
hacer las conexiones con la Raspberry Pi Pico W, mientras que time es básicamente el tiempo que tarda en dar
respuesta tras respuesta. Se utiliza el Pin 17 para captar las señales al momento de que se agite y para ello
declaramos "value" como el valor que tendrá la pelotita en el interior del sensor; para diferenciar si se captó
agitación con el sensor se hace uso de la condición if-else, donde if tomará que value es 0 y despliegue como
resultado que la pelota se está moviendo, de lo contrario desplegará que no se está moviendo.
