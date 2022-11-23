
class AccesoDatos:

    ARCHIVO = "./dataset.xml"

    def obtener_datos(self) -> list[dict]:

        file = open( self.ARCHIVO, "r" )

        datos = list()
        for line in file:

            dato = {}
            linea = line.rstrip()

            dato["user"] = linea.split("user")[1].replace(">", "").replace("</", "")
            dato["password"] = linea.split("password")[1].replace(">", "").replace("</", "")
            dato["email"] = linea.split("email")[1].replace(">", "").replace("</", "")

            datos.append( dato )

        file.close()

        return datos


