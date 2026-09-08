from datetime import datetime
from typing import Any, Optional

from aura_schemas.body import FichaBody
from aura_schemas.body_v2 import FichaBodyV2


# ============================================================
# VISUALSELLER FASHION
# AURA — ESTADO / MEMÓRIA DE TRABALHO
# ============================================================


# ============================================================
# 1. ESTADO DO PRODUTO — V1
# ============================================================

class EstadoProduto:
    """
    Guarda tudo o que aconteceu durante a análise
    de um produto pela AURA.

    A memória separa:

    - informações aceitas;
    - informações recusadas;
    - informações aguardando confirmação;
    - histórico completo das decisões.
    """

    def __init__(
        self,
        ficha: FichaBody,
    ):
        self.ficha = ficha

        self.informacoes_aceitas = []
        self.informacoes_recusadas = []
        self.aguardando_confirmacao = []
        self.historico = []


    # ========================================================
    # REGISTRAR UMA DECISÃO DA AURA
    # ========================================================

    def registrar_resultado(
        self,
        resultado: dict[str, Any],
    ):
        """
        Salva na memória o resultado produzido
        pelo processador da AURA.
        """

        registro = resultado.copy()

        self.historico.append(
            registro
        )

        acao = resultado.get(
            "acao"
        )

        if acao == "INFORMACAO_REGISTRADA":

            self.informacoes_aceitas.append(
                registro
            )

        elif acao == "PRECISA_CONFIRMACAO":

            self.aguardando_confirmacao.append(
                registro
            )

        else:

            self.informacoes_recusadas.append(
                registro
            )


    # ========================================================
    # INFORMAÇÕES ACEITAS
    # ========================================================

    def obter_informacoes_aceitas(
        self,
    ):
        return self.informacoes_aceitas


    # ========================================================
    # INFORMAÇÕES RECUSADAS
    # ========================================================

    def obter_informacoes_recusadas(
        self,
    ):
        return self.informacoes_recusadas


    # ========================================================
    # CONFIRMAÇÕES PENDENTES
    # ========================================================

    def obter_confirmacoes_pendentes(
        self,
    ):
        return self.aguardando_confirmacao


    # ========================================================
    # HISTÓRICO COMPLETO
    # ========================================================

    def obter_historico(
        self,
    ):
        return self.historico


    # ========================================================
    # EXISTEM CONFIRMAÇÕES PENDENTES?
    # ========================================================

    def possui_confirmacoes_pendentes(
        self,
    ):
        return (
            len(
                self.aguardando_confirmacao
            )
            > 0
        )


    # ========================================================
    # RESUMO DA MEMÓRIA
    # ========================================================

    def resumo(
        self,
    ):
        return {
            "informacoes_aceitas":
                len(
                    self.informacoes_aceitas
                ),

            "aguardando_confirmacao":
                len(
                    self.aguardando_confirmacao
                ),

            "informacoes_recusadas":
                len(
                    self.informacoes_recusadas
                ),

            "total_decisoes":
                len(
                    self.historico
                ),
        }


# ============================================================
# 2. MOSTRAR O ESTADO ATUAL DO PRODUTO — V1
# ============================================================

def mostrar_estado_produto(
    estado: EstadoProduto,
):
    """
    Exibe um resumo simples da memória
    atual da AURA.
    """

    resumo = estado.resumo()

    print(
        "\n"
        "========================================"
    )

    print(
        "ESTADO ATUAL DO PRODUTO"
    )

    print(
        "========================================"
    )

    print(
        "INFORMAÇÕES ACEITAS:",
        resumo["informacoes_aceitas"],
    )

    print(
        "AGUARDANDO CONFIRMAÇÃO:",
        resumo["aguardando_confirmacao"],
    )

    print(
        "INFORMAÇÕES RECUSADAS:",
        resumo["informacoes_recusadas"],
    )

    print(
        "TOTAL DE DECISÕES:",
        resumo["total_decisoes"],
    )


# ============================================================
# 3. ESTADO DO PRODUTO — V2
# ============================================================

class EstadoProdutoV2:
    """
    Memória de trabalho da AURA V2.

    A FichaBodyV2 representa o conhecimento técnico
    atual sobre o produto.

    O EstadoProdutoV2 representa o processo:

    - qual é o objetivo atual;
    - quais eventos aconteceram;
    - quais evidências foram recebidas;
    - quais bloqueios foram encontrados;
    - quais perguntas foram feitas;
    - quais respostas foram recebidas;
    - quais decisões foram tomadas.

    O estado não decide se uma evidência é verdadeira.
    Essa responsabilidade pertence ao sistema de
    evidências e às regras da AURA.
    """

    def __init__(
        self,
        ficha: FichaBodyV2,
        objetivo: str,
    ):
        self.ficha = ficha
        self.objetivo = objetivo

        self.historico: list[dict[str, Any]] = []

        self.evidencias_recebidas: list[
            dict[str, Any]
        ] = []

        self.bloqueios_encontrados: list[
            dict[str, Any]
        ] = []

        self.perguntas_realizadas: list[
            dict[str, Any]
        ] = []

        self.respostas_recebidas: list[
            dict[str, Any]
        ] = []

        self.decisoes: list[
            dict[str, Any]
        ] = []


    # ========================================================
    # REGISTRAR EVENTO GENÉRICO — V2
    # ========================================================

    def registrar_evento(
        self,
        tipo: str,
        dados: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """
        Registra um evento no histórico geral.

        O histórico funciona como uma linha do tempo
        do raciocínio operacional da AURA.
        """

        if dados is None:
            dados = {}

        evento = {
            "tipo":
                tipo,

            "objetivo":
                self.objetivo,

            "dados":
                dados.copy(),

            "timestamp":
                datetime.now().isoformat(
                    timespec="seconds"
                ),
        }

        self.historico.append(
            evento
        )

        return evento


    # ========================================================
    # REGISTRAR EVIDÊNCIA — V2
    # ========================================================

    def registrar_evidencia(
        self,
        evidencia: dict[str, Any],
    ):
        """
        Guarda uma evidência recebida durante
        o processo de análise.
        """

        registro = evidencia.copy()

        self.evidencias_recebidas.append(
            registro
        )

        self.registrar_evento(
            tipo="EVIDENCIA_RECEBIDA",
            dados=registro,
        )


    # ========================================================
    # REGISTRAR BLOQUEIO — V2
    # ========================================================

    def registrar_bloqueio(
        self,
        bloqueio: dict[str, Any],
    ):
        """
        Registra um bloqueio identificado
        para o objetivo atual.
        """

        registro = bloqueio.copy()

        self.bloqueios_encontrados.append(
            registro
        )

        self.registrar_evento(
            tipo="BLOQUEIO_ENCONTRADO",
            dados=registro,
        )


    # ========================================================
    # REGISTRAR PERGUNTA — V2
    # ========================================================

    def registrar_pergunta(
        self,
        pergunta: dict[str, Any],
    ):
        """
        Registra uma pergunta apresentada
        ao usuário.
        """

        registro = pergunta.copy()

        self.perguntas_realizadas.append(
            registro
        )

        self.registrar_evento(
            tipo="PERGUNTA_REALIZADA",
            dados=registro,
        )


    # ========================================================
    # REGISTRAR RESPOSTA — V2
    # ========================================================

    def registrar_resposta(
        self,
        campo: str,
        resposta: Any,
    ):
        """
        Registra uma resposta fornecida
        pelo usuário.
        """

        registro = {
            "campo":
                campo,

            "resposta":
                resposta,
        }

        self.respostas_recebidas.append(
            registro
        )

        self.registrar_evento(
            tipo="RESPOSTA_RECEBIDA",
            dados=registro,
        )


    # ========================================================
    # REGISTRAR DECISÃO — V2
    # ========================================================

    def registrar_decisao(
        self,
        decisao: dict[str, Any],
    ):
        """
        Registra uma decisão tomada
        pela AURA.
        """

        registro = decisao.copy()

        self.decisoes.append(
            registro
        )

        self.registrar_evento(
            tipo="DECISAO_TOMADA",
            dados=registro,
        )


    # ========================================================
    # ALTERAR OBJETIVO — V2
    # ========================================================

    def definir_objetivo(
        self,
        objetivo: str,
    ):
        """
        Altera o objetivo atual da AURA
        e registra a mudança no histórico.
        """

        objetivo_anterior = (
            self.objetivo
        )

        self.objetivo = objetivo

        self.registrar_evento(
            tipo="OBJETIVO_ALTERADO",
            dados={
                "objetivo_anterior":
                    objetivo_anterior,

                "novo_objetivo":
                    objetivo,
            },
        )


    # ========================================================
    # OBTER HISTÓRICO — V2
    # ========================================================

    def obter_historico(
        self,
    ) -> list[dict[str, Any]]:
        """
        Retorna a linha do tempo completa.
        """

        return self.historico


    # ========================================================
    # OBTER ÚLTIMO EVENTO — V2
    # ========================================================

    def obter_ultimo_evento(
        self,
    ):
        """
        Retorna o evento mais recente.
        """

        if not self.historico:
            return None

        return self.historico[-1]


    # ========================================================
    # RESUMO DO ESTADO — V2
    # ========================================================

    def resumo(
        self,
    ) -> dict[str, Any]:
        """
        Retorna um resumo da memória de trabalho.
        """

        return {
            "objetivo":
                self.objetivo,

            "evidencias_recebidas":
                len(
                    self.evidencias_recebidas
                ),

            "bloqueios_encontrados":
                len(
                    self.bloqueios_encontrados
                ),

            "perguntas_realizadas":
                len(
                    self.perguntas_realizadas
                ),

            "respostas_recebidas":
                len(
                    self.respostas_recebidas
                ),

            "decisoes":
                len(
                    self.decisoes
                ),

            "total_eventos":
                len(
                    self.historico
                ),
        }


# ============================================================
# 4. MOSTRAR ESTADO DO PRODUTO — V2
# ============================================================

def mostrar_estado_produto_v2(
    estado: EstadoProdutoV2,
):
    """
    Exibe um resumo simples da memória
    de trabalho da AURA V2.
    """

    resumo = estado.resumo()

    print(
        "\n"
        "========================================"
    )

    print(
        "ESTADO ATUAL DO PRODUTO — V2"
    )

    print(
        "========================================"
    )

    print(
        "OBJETIVO:",
        resumo[
            "objetivo"
        ],
    )

    print(
        "EVIDÊNCIAS RECEBIDAS:",
        resumo[
            "evidencias_recebidas"
        ],
    )

    print(
        "BLOQUEIOS ENCONTRADOS:",
        resumo[
            "bloqueios_encontrados"
        ],
    )

    print(
        "PERGUNTAS REALIZADAS:",
        resumo[
            "perguntas_realizadas"
        ],
    )

    print(
        "RESPOSTAS RECEBIDAS:",
        resumo[
            "respostas_recebidas"
        ],
    )

    print(
        "DECISÕES:",
        resumo[
            "decisoes"
        ],
    )

    print(
        "TOTAL DE EVENTOS:",
        resumo[
            "total_eventos"
        ],
    )