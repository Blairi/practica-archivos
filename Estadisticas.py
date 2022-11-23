from AccesoDatos import AccesoDatos

class Estadisticas:

    def __init__(self) -> None:
        self.datos = AccesoDatos().obtener_datos()


    def password_iguales(self):
        
        passwords = {}
        for dato in self.datos:

            password = dato["password"]

            if password in list(passwords.keys()):
                passwords[password] += 1
            else:
                passwords[password] = 1

        passwords_iguales = 0
        for passw in passwords:
            if passwords[passw] > 1:
                passwords_iguales += 1

        return passwords_iguales


    def passwords_incidencia(self):

        passwords = {}
        for dato in self.datos:

            password = dato["password"]

            if password in list(passwords.keys()):
                passwords[password] += 1
            else:
                passwords[password] = 1

        password_incidente = max(passwords, key=passwords.get)
        
        pass_incidente = 0

        if passwords[password_incidente] > 1:
            pass_incidente += 1

        return pass_incidente

    
    def numero_empresas(self):

        empresas = {}
        for dato in self.datos:

            empresa = dato["email"].split("@")[1].split(".")[0]

            if empresa in list(empresas.keys()):
                empresas[empresa] += 1
            else:
                empresas[empresa] = 1

        return len( empresas )
    

    def correos_iguales(self):

        correos = {}
        for dato in self.datos:

            correo = dato["email"]

            if correo in list( correos.keys() ):
                correos[correo] += 1
            else:
                correos[correo] = 1
        
        correos_iguales = 0
        for correo in correos:
            if correos[correo] > 1:
                correos_iguales += 1

        return correos_iguales
        
