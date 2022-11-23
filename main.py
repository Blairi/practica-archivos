from Estadisticas import Estadisticas
import matplotlib.pyplot as plt

def main():

    estadisticas = Estadisticas()

    pass_iguales = estadisticas.password_iguales()
    pass_incidente = estadisticas.passwords_incidencia()
    n_empresas = estadisticas.numero_empresas()
    correos_iguales = estadisticas.correos_iguales()

    datos = ['Passwords iguales', 'Password incidente', 'Número de empresas', 'Correos iguales']
    numeros = [pass_iguales, pass_incidente, n_empresas, correos_iguales]

    plt.bar(datos, numeros)
    plt.title('Estadisticas')
    plt.xlabel('Estadisticas')
    plt.ylabel('Número')
    plt.show()

    my_colors = ['lightblue', 'lightsteelblue', 'green', 'red']
    # my_explode = (0, 0.1, 0, 0)
    plt.pie(numeros, labels=datos, autopct='%1.1f%%', startangle=15, shadow=True, colors=my_colors,)
    plt.title('My Tasks')
    plt.axis('equal')
    plt.show()

main()
