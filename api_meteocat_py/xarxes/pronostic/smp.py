from typing import List
from ...excepcions import MeteocatLocalError
from ...helpers.utils import formateja_valors_data, neteja_diccionari, genera_info


class SMP:
    def smp_episodis_oberts(self) -> List[dict]:
        """
        Retorna els episodis oberts pel dia actual.

        Returns:
            List[dict]: [
                            {
                                estat: {
                                nom: "Obert",
                                data: null
                                },
                                meteor: {
                                nom: "Acumulació de Pluja"
                                },
                                avisos: [
                                {
                                    tipus: "Avís",
                                    dataEmisio: "2015-11-25T17:17Z",
                                    dataInici: "2015-11-25T00:00Z",
                                    dataFi: "2015-11-25T23:59Z",
                                    evolucions: [
                                    {
                                        dia: "2015-11-25T00:00Z",
                                        comentari: "",
                                        representatiu: 1,
                                        llindar1: "Acumulada &gt; 100 mm /24 hores",
                                        llindar2: null,
                                        distribucioGeografica: "LOCAL",
                                        periodes: [
                                        {
                                            nom: "00-06",
                                            afectacions: [
                                            {
                                                dia: "2015-11-25T00:00Z",
                                                llindar: "Acumulada &gt; 100 mm /24 hores",
                                                auxiliar: false,
                                                perill: 1,
                                                idComarca: 38,
                                                nivell: 1
                                            }
                                            ]
                                        },
                                        {
                                            nom: "06-12",
                                            afectacions: null
                                        },
                                        {
                                            nom: "12-18",
                                            afectacions: null
                                        },
                                        {
                                            nom: "18-00",
                                            afectacions: [
                                            {
                                                dia: "2015-11-25T00:00Z",
                                                llindar: "Acumulada &gt; 100 mm /24 hores",
                                                auxiliar: false,
                                                perill: 1,
                                                idComarca: 2,
                                                nivell: 1
                                            }
                                            ]
                                        }
                                        ],
                                        valorMaxim: ""
                                    }
                                    ],
                                    estat: "Vigent"
                                }
                                ]
                            }
                        ]
        """
        recurs = "smp/episodis-oberts"
        return self._aconsegueix(recurs)

    def smp_preavisos(self) -> List[dict]:
        """
        Retorna els preavisos publicats actualment.

        Returns:
            List[dict]: [
                            {
                                "<span class="hljs-attr">estat</span>": {
                                "<span class="hljs-attr">nom</span>": <span class="hljs-string">"Obert"</span>,
                                "<span class="hljs-attr">data</span>": <span class="hljs-literal">null</span>
                                },
                                "<span class="hljs-attr">meteor</span>": {
                                "<span class="hljs-attr">nom</span>": <span class="hljs-string">"Calor"</span>
                                },
                                "<span class="hljs-attr">avisos</span>": [
                                {
                                    "<span class="hljs-attr">nivell</span>": <span class="hljs-number">1</span>,
                                    "<span class="hljs-attr">tipus</span>": <span class="hljs-string">"Preavís"</span>,
                                    "<span class="hljs-attr">dataInici</span>": <span class="hljs-string">"2017-03-06T00:00Z"</span>,
                                    "<span class="hljs-attr">dataFi</span>": <span class="hljs-string">"2017-03-08T23:59Z"</span>,
                                    "<span class="hljs-attr">dataEmisio</span>": <span class="hljs-string">"2017-03-06T12:07Z"</span>,
                                    "<span class="hljs-attr">estat</span>": <span class="hljs-string">"Vigent"</span>,
                                    "<span class="hljs-attr">llindar</span>": <span class="hljs-string">"Temperatura màxima extrema"</span>,
                                    "<span class="hljs-attr">perill</span>": <span class="hljs-number">2</span>,
                                    "<span class="hljs-attr">comentari</span>": <span class="hljs-string">""</span>
                                }
                                ]
                            },
                            ...,
                            {
                                "<span class="hljs-attr">estat</span>": {
                                "<span class="hljs-attr">nom</span>": <span class="hljs-string">"Obert"</span>,
                                "<span class="hljs-attr">data</span>": <span class="hljs-literal">null</span>
                                },
                                "<span class="hljs-attr">meteor</span>": {
                                "<span class="hljs-attr">nom</span>": <span class="hljs-string">"Vent"</span>
                                },
                                "<span class="hljs-attr">avisos</span>": [
                                {
                                    "<span class="hljs-attr">nivell</span>": <span class="hljs-number">1</span>,
                                    "<span class="hljs-attr">tipus</span>": <span class="hljs-string">"Preavís"</span>,
                                    "<span class="hljs-attr">dataInici</span>": <span class="hljs-string">"2017-03-06T00:00Z"</span>,
                                    "<span class="hljs-attr">dataFi</span>": <span class="hljs-string">"2017-03-06T23:59Z"</span>,
                                    "<span class="hljs-attr">dataEmisio</span>": <span class="hljs-string">"2017-03-06T11:19Z"</span>,
                                    "<span class="hljs-attr">estat</span>": <span class="hljs-string">"Vigent"</span>,
                                    "<span class="hljs-attr">llindar</span>": <span class="hljs-string">"Ratxa màxima &gt; 25m/s"</span>,
                                    "<span class="hljs-attr">perill</span>": <span class="hljs-number">3</span>,
                                    "<span class="hljs-attr">comentari</span>": <span class="hljs-string">""</span>
                                }
                                ]
                            }
                            ]
        """
        recurs = "smp/episodis-oberts/preavisos"
        return self._aconsegueix(recurs)
