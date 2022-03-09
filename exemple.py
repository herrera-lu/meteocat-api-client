from connexio import Connexio, habilita_memoria_cau
from xarxes import Quotes, Referencia, XEMA
from key import KEY


def main():
    habilita_memoria_cau(3600)
    connexio = Connexio(KEY)

    # print(xema.metadades_municipis_variables("081691", "32"))
    # quotes = Quotes()

    referencia = Referencia(connexio)
    # print(referencia.comarques())
    quotes = Quotes(connexio)
    # print(quotes.consum_actual())
    xema = XEMA(connexio)
    # print(xema.metadades_municipis_variables("081691", "31"))
    # print(xema.estacions_metadades("081691"))
    print(xema.estadistics_mensuals_x_1_variable_d_totes_estacions(2000, 2013))


if __name__ == "__main__":
    main()
