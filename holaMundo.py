"""
print(prediccion({"nombre":"Manchester", "PG" : 5, "PE": 3, "PP": 2, "Ganador": 2, "GF": 38, "GC": 20, "Nomina": 800, "Continente": "Europa", "Posesion": 0.52}))
//El equipo Manchester tiene el 0.9 de probabilidad de ganar el torneo
print(prediccion({"nombre":"Boca", "PG" : 5, "PE": 2, "PP": 3, "Ganador": "3+", "GF": 20, "GC": 29, "Nomina": 600, "Continente": "Sudamerica", "Posesion": 0.45}))
//El equipo Boca tiene el 0.4 de probabilidad de ganar el torneo
print(prediccion({"nombre":"Zamalek", "PG" : 5, "PE": 2, "PP": 3, "Ganador": 0, "GF": 20, "GC": 29, "Nomina": 600, "Continente": "Africa", "Posesion": 0.45}))
//El equipo Zamalek tiene el 0.4 de probabilidad de ganar el torneo
print(prediccion({"nombre":"Manchester City", "PG" : 5, "PE": 3, "PP": 2, "Ganador": 0, "GF": 38, "GC": 20, "Nomina": 800, "Continente": "Europa", "Posesion": 0.52}))
//El equipo Manchester City tiene el 0.8 de probabilidad de ganar el torneo
"""

def prediccion(objeto):

    if objeto["Continente"]=="Europa":

        if (objeto["PG"]>objeto["PP"]) or (objeto["PE"]>objeto["PP"]):

            if (objeto["PG"]>0) and (objeto["Posesion"]>0.5):
                
                if objeto["Ganador"]>0:
                    return "El equipo  "+ objeto["nombre"]+ "  tiene 0.9 de probabilidad de ganar el torneo"
                
                else:

                    if objeto["Nomina"]>700:
                        return "El equipo  "+ objeto["nombre"]+ "  tiene 0.8 de probabilidad de ganar el torneo"

                    else:
                        return "El equipo  "+ objeto["nombre"]+ "  tiene 0.7 de probabilidad de ganar el torneo"

            else:
                return "El equipo  "+ objeto["nombre"]+ "  tiene 0.5 de probabilidad de ganar el torneo"

        else:

            if (objeto["PG"]>0) and (objeto["Posesion"]>0.4):
                return "El equipo  "+ objeto["nombre"]+ "  tiene 0.5 de probabilidad de ganar el torneo"
            
            else:
                return "El equipo  "+ objeto["nombre"]+ "  tiene 0.4 de probabilidad de ganar el torneo"

    else: 

        if objeto["Ganador"]>0:

            if (objeto["PG"] > objeto["PP"]) and (objeto["PE"] > objeto["PP"]):

                if (objeto["PG"]>0) or (objeto["Posesion"]>0.5):
                    return "El equipo  "+ objeto["nombre"]+ "  tiene 0.85 de probabilidad de ganar el torneo"
                
                else:
                    return "El equipo  "+ objeto["nombre"]+ "  tiene 0.8 de probabilidad de ganar el torneo"
            
            else:

                if (objeto["Nomina"]>700) and (objeto["Posesion"]>0.4):
                    return "El equipo  "+ objeto["nombre"]+ "  tiene 0.6 de probabilidad de ganar el torneo"
                
                else:
                    return "El equipo  "+ objeto["nombre"]+ "  tiene 0.4 de probabilidad de ganar el torneo"
            
        else:

            if objeto["Continente"]=="Sudamerica":

                if objeto["PG"]>0:
                    return "El equipo  "+ objeto["nombre"]+ "  tiene 0.6 de probabilidad de ganar el torneo"

                else:
                    return "El equipo  "+ objeto["nombre"]+ "  tiene 0.5 de probabilidad de ganar el torneo"

            else:
                    return "El equipo  "+ objeto["nombre"]+ "  tiene 0.4 de probabilidad de ganar el torneo"
#PRIMER EJERCICIO


print(prediccion({
"nombre":"Manchester",
"PG" : 5,
"PE": 3,
"PP": 2, 
"Ganador": 2, 
"GF": 38, 
"GC": 20, 
"Nomina": 800, 
"Continente": "Europa", 
"Posesion": 0.52
}))


#SEGUNDO EJERCICIO


print(prediccion({
"nombre":"Boca", 
"PG" : 5, 
"PE": 2,
"PP": 3, 
"Ganador": 3, 
"GF": 20, 
"GC": 29, 
"Nomina": 600, 
"Continente": "Sudamerica", 
"Posesion": 0.45
}))


#TERCER EJERCICIO


print(prediccion({
"nombre":"Zamalek", 
"PG" : 5, 
"PE": 2, 
"PP": 3, 
"Ganador": 0, 
"GF": 20, 
"GC": 29, 
"Nomina": 600, 
"Continente": "Africa", 
"Posesion": 0.45
}))


#CUARTO EJERCICIO


print(prediccion({
"nombre":"Manchester City", 
"PG" : 5, 
"PE": 3, 
"PP": 2, 
"Ganador": 0, 
"GF": 38, 
"GC": 20, 
"Nomina": 800, 
"Continente": "Europa", 
"Posesion": 0.52
}))
