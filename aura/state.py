from typing import Any

from aura_schemas.body import FichaBody


# ============================================================
# ESTADO DO PRODUTO — MEMÓRIA DE TRABALHO DA AURA
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
# MOSTRAR O ESTADO ATUAL DO PRODUTO
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