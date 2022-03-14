# meteocat-api-client

Client en Python (no oficial) que consumeix dades de l'API REST del Servei Meteorològic de Catalunya (https://apidocs.meteocat.gencat.cat/documentacio/).

En aquesta primera implementació, les dades es consulten de forma síncrona utilitzant la llibreria Requests (https://docs.python-requests.org/en/latest/). La memòria cau de les consultes (opcional) s'ha implementat amb la llibreria requests-cache (https://pypi.org/project/requests-cache/).

# Instal·lació

Per instal·lar el client podem utilitzar pip (com sempre, és recomanable crear un entorn virtual abans):\
``pip install meteocat-api-client``

O clonar el repositori:\
``git clone https://github.com/herrera-lu/meteocat-api-client.git``


# Ús

## Memòria cau

Si volem emmagatzemar en memòria cau el resultat de les consultes a l'api:
```python
from meteocat_api_client.connexio import habilita_memoria_cau
habilita_memoria_cau({temps de persistència en segons})
```

## Consultes a l'API

El funcionament del client és relativament senzill. El primer que farem és instanciar un objecte de la classe Connexio amb el token que el meteo.cat ens ha proporcionat.
```python
from meteocat_api_client.connexio import Connexio
connexio = Connexio({token_api_meteocat})
```

Si encara no el tenim, el podem demanar a:\
https://apidocs.meteocat.gencat.cat/section/informacio-general/plans-i-registre/

A banda de la classe Connexio, tenim altres classes que representen les diferents xarxes i altres conjunts de dades consultables via API:
<ol>
    <li>XDDE (Xarxa de Detecció de Descàrregues Elèctriques).</li>
    <li>XEMA (Xarxa d'Estacions Meteorològiques Automàtiques).</li>
    <li>Pronostic (Dades de Predicció).</li>
    <li>Referencia (Dades de Referència).</li>
    <li>Quotes (Dades de Consum de l'API).</li>
</ol>

S'han implementat totes les consultes documentades a la web del meteo.cat.

Per consultar dades d'una determinada xarxa, crearem un objecte de la classe corresponent i li passarem la informació de la connexio. Després cridarem el mètode que ens proporciona les dades que cerquem:

```python
from meteocat_api_client.xarxes import XEMA
from meteocat_api_client.excepcions import MeteocatApiError, MeteocatLocalError

    xema = XEMA(connexio)
    try:
        codis_estacions = xema.representatives_codis_estacions_x_1_municipi_i_1_variable(
            "081691", "32"
        )

    except MeteocatApiError as e:
        # Tractament de l'error
        pass

    except MeteocatLocalError as e:
        # Tractament de l'error
        pass
    
```

Hi ha 2 tipus d'excepcions possibles:
<ol>
    <li>MeteocatApiError: es produeix si el codi de resposta proporcionat pel meteo.cat no és 200 OK.</li>
    <li>MeteocatLocalError: es produeix si hi ha errors en la validació de les dades abans d'enviar la petició al meteo.cat</li>
</ol>


Podeu provar ràpidament les consultes que permet aquest paquet instal·lant-lo amb pip. En el REPL de python podeu executar qualsevol dels mètodes següents:

```python
from meteocat_api_client.connexio import Connexio, habilita_memoria_cau
from meteocat_api_client.xarxes import Pronostic, XEMA, Quotes, Referencia, XDDE

KEY = "{token_api_meteocat}"

connexio = Connexio(KEY)

xdde = XDDE(connexio)
xdde.descarregues_x_tota_catalunya(2022, 1, 13, 15)
xdde.descarregues_resum_x_comarques(31, 2022, 1, 13)

xema = XEMA(connexio)
xema.representatives_codis_estacions_x_1_municipi_i_1_variable("080057", 32)
xema.representatives_metadades_x_totes_variables()
xema.estacions_metadades()
xema.estacions_metadades("ope", "2017-03-27Z")
xema.estacions_metadades_x_1_estacio("UG")
xema.mesurades_x_1_variable_d_totes_estacions_o_1_estacio(32, 2017, 3, 27)
xema.mesurades_x_1_variable_d_totes_estacions_o_1_estacio(32, 2017, 3, 27, "UG")
xema.mesurades_x_totes_variables_d_1_estacio("CC", 2020, 6, 16)
xema.mesurades_ultimes_dades_x_1_variable_d_totes_estacions_o_1_estacio(5)
xema.mesurades_ultimes_dades_x_1_variable_d_totes_estacions_o_1_estacio(5, "UG")
xema.mesurades_metadades_x_totes_variables_d_1_estacio("UG")
xema.mesurades_metadades_x_totes_variables_d_1_estacio("UG", "ope", "2017-03-27Z")
xema.mesurades_metadades_x_1_variable_d_1_estacio("UG", 3)
xema.mesurades_metadades_x_totes_variables()
xema.mesurades_metadades_x_1_variable(1)
xema.estadistics_anuals_x_1_variable_d_totes_estacions_o_1_estacio(3000)
xema.estadistics_anuals_x_1_variable_d_totes_estacions_o_1_estacio(3000, "UG")
xema.estadistics_mensuals_x_1_variable_d_totes_estacions_o_1_estacio(2000, 2021)
xema.estadistics_mensuals_x_1_variable_d_totes_estacions_o_1_estacio(2000, 2021, "UG")
xema.estadistics_diaris_x_1_variable_d_totes_estacions_o_1_estacio(2000, 2021, 12)
xema.estadistics_diaris_x_1_variable_d_totes_estacions_o_1_estacio(2000, 2021, 12, "UG")
xema.estadistics_metadades_anuals_x_totes_variables()
xema.estadistics_metadades_anuals_x_1_variable(3001)
xema.estadistics_metadades_mensuals_x_totes_variables()
xema.estadistics_metadades_mensuals_x_1_variable(2001)
xema.estadistics_metadades_diaris_x_totes_variables()
xema.estadistics_metadades_diaris_x_1_variable(1001)
xema.estadistics_metadades_anuals_x_totes_variables_d_1_estacio("CC")
xema.estadistics_metadades_anuals_x_1_variable_d_1_estacio("CC", 3000)
xema.estadistics_metadades_mensuals_x_totes_variables_d_1_estacio("CC")
xema.estadistics_metadades_mensuals_x_1_variable_d_1_estacio("CC", 2000)
xema.estadistics_metadades_diaris_x_totes_variables_d_1_estacio("CC")
xema.estadistics_metadades_diaris_x_1_variable_d_1_estacio("CC", 1000)
xema.calcul_multivariable_x_1_variable_d_totes_estacions_o_1_estacio(6006, 2020, 6, 30)
xema.calcul_multivariable_x_1_variable_d_totes_estacions_o_1_estacio(
    6006, 2020, 6, 30, "CC"
)
xema.calcul_multivariable_metadades_x_totes_variables_d_1_estacio("UG")
xema.calcul_multivariable_metadades_x_1_variable_d_1_estacio("UG", 6006)
xema.calcul_multivariable_metadades_x_totes_variables()
xema.calcul_multivariable_metadades_x_1_variable(6006)
xema.auxiliars_x_1_variable_d_1_estacio("CC", 900, 2022, 3, 14)
xema.auxiliars_metadades_x_totes_variables_d_1_estacio("CC")
xema.auxiliars_metadades_x_totes_variables_d_1_estacio("CC", "2017-03-30Z", "ope")
xema.auxiliars_metadades_x_1_variable_d_1_estacio("CC", 900)
xema.auxiliars_metadades_x_totes_variables()
xema.auxiliars_metadades_x_1_variable(900)

pronostic = Pronostic(connexio)
pronostic.prediccio_catalunya_general(2022, 3, 15)
pronostic.prediccio_comarcal(2022, 3, 15)
pronostic.prediccio_municipal_horaria_a_72_hores("250019")
pronostic.prediccio_municipal_a_8_dies("250019")
pronostic.smp_episodis_oberts()
pronostic.smp_preavisos()
pronostic.uvi_prediccio_municipal("080018")
pronostic.pirineu_pics_prediccio("el-taga", 2022, 3, 15)
pronostic.pirineu_pics_metadades()
pronostic.pirineu_refugis_prediccio("refugi-colomina", 2022, 3, 15)
pronostic.pirineu_refugis_metadades()
pronostic.pirineu_zones_prediccio(2022, 3, 15)
pronostic.platges_prediccio("alcanar-del-marjal", 2022, 3, 15)
pronostic.platges_metadades()

referencia = Referencia(connexio)
referencia.comarques()
referencia.municipis()
referencia.simbols()

quotes = Quotes(connexio)
quotes.consum_actual()
```
        