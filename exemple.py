from meteocat_api_client.connexio import Connexio, habilita_memoria_cau
from meteocat_api_client.xarxes import Pronostic, XEMA, Quotes, Referencia, XDDE
from meteocat_api_client.excepcions import MeteocatApiError, MeteocatLocalError
from key import KEY


def main():
    # Habilitem la memòrica cau amb un temps de peristència d'1 hora.
    habilita_memoria_cau(3600)

    # Creem un objecte connexio que farà les peticions a l'API del meteocat
    # utilitzant el token que tenim emmagatzemat a la constant KEY del
    # fitxer key.py (veure el fitxer key_plantilla.py).
    connexio = Connexio(KEY)

    # Crearem un objecte per a cada xarxa de la que volguem consultar
    # dades. L'únic paràmetre que necessitem per instanciar les classes
    # de les xarxes és un objecte de la classe Connexio.
    referencia = Referencia(connexio)
    # A tall d'exemple, executem el metode de l'objecte referencia que
    # ens retorna les metadades de les comarques.
    # De moment, l'aplicació retorna una llista de diccionaris que obtenen la
    # informació del json que retorna l'API.
    # Més endavant, si aconseguim prou temps, ens agradaria estructurar les dades
    # en dataclasses.
    print("referencia.comarques()")
    print(referencia.comarques())
    print("------------------------------------\n")

    # Les consultes de quotes no s'emmagatzemen a la memòria cau.
    quotes = Quotes(connexio)
    print("quotes.consum_actual()")
    print(quotes.consum_actual())
    print("------------------------------------\n")

    pronostic = Pronostic(connexio)
    print("pronostic.prediccio_catalunya_general(2022, 3, 15)")
    try:
        print(pronostic.prediccio_catalunya_general(2022, 3, 15))
    except MeteocatApiError as e:
        print("********* ERROR **********")
        print(e)
        print("------------------------------------\n")

    xema = XEMA(connexio)
    # Provoquem un error (el codi de variable de la petició no és correcte).
    print(
        'xema.representatives_codis_estacions_x_1_municipi_i_1_variable("081691", "31")'
    )
    try:
        print(
            xema.representatives_codis_estacions_x_1_municipi_i_1_variable(
                "081691", "31"
            )
        )
    except MeteocatApiError as e:
        print("********* ERROR **********")
        print(e)
        print("------------------------------------\n")

    # Ara consultem una variable que sí que existeix.
    print(
        'xema.representatives_codis_estacions_x_1_municipi_i_1_variable("081691", "32")'
    )
    print(
        xema.representatives_codis_estacions_x_1_municipi_i_1_variable("081691", "32")
    )


if __name__ == "__main__":
    main()
