#los slices sirven para cortr la cadena de texto y extraer las letras que necesitas o quieres usar la sintaxis es la siguiente

nombre = ("perro") #tenemos la variable principal con el perro dentro
nombre[1:3] #en paython empeamos a contar desde 0 o sea 0 seria la primera letra de la cadena de texto luego vemos que se pone en corchetes y ponemos le numero del cual
# se quiere empezar a contar + : dos puntos y luego el numero donde se uiqere terminar que seria igual a la letra dondense quiere nterminar

nombre[:5] #si se qiere empezar desde el primer elemento, me lo salto y pongo los dos puntos lugo el numero donde quiero terminar

nombre[3:] #aqui inicio desde el indice 3 y lo dejo hasta el final , como ven no se pone nada en el final o sea la operacion anterior inversamente
nombre[2:3:2] # en este ejmplo pongo el primer nuemero que es donde uqiero empezar luego el donde quiero terminar y el tercer numero en saltos de 2 letras
#lo que quiere decir que cada dos letras estaria trayendo las letras hasta finalizar el texto que quiero sacar
nombre[::-1] #en este ejemplo le estoy diciendo a python que quiero ir desde el iicio al fin pero en pasos negativos, lo que me traera el nombre completo pero al reves 
nombre[::]# aqui puedes ir desde el inicio hasta el final de uo en uno
nombre[1::3]#aqi podemos ir desde el numero uno hasta el final en pasos de 3
