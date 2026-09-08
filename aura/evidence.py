from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel

from aura_schemas.body_v2 import StatusEvidencia


# ============================================================
# VISUALSELLER FASHION
# AURA — SISTEMA DE EVIDÊNCIAS
# ============================================================


# ============================================================
# 1. TIPOS DE FONTE DE EVIDÊNCIA
# ============================================================

class FonteEvidencia(str, Enum):
    ETIQUETA = "etiqueta"
    MEDICAO_FISICA = "medicao_fisica"
    VERIFICACAO_FISICA = "verificacao_fisica"
    FOTOGRAFIA = "fotografia"
    INFORMACAO_FORNECIDA = "informacao_fornecida"
    INFERENCIA_AURA = "inferencia_aura"


# ============================================================
# 2. NÍVEIS DE CONFIANÇA
# ============================================================

class NivelConfianca(str, Enum):
    ALTA = "alta"
    MEDIA = "media"
    BAIXA = "baixa"


# ============================================================
# 3. MODELO DE EVIDÊNCIA
# ============================================================

class Evidencia(BaseModel):
    """
    Representa uma evidência utilizada pela AURA
    para aceitar ou avaliar uma informação do produto.

    A evidência registra:

    - qual campo está sendo analisado;
    - qual valor foi encontrado;
    - de onde veio a informação;
    - qual é o nível de confiança;
    - uma descrição opcional.
    """

    campo: str
    valor: Any
    fonte: FonteEvidencia
    confianca: NivelConfianca
    descricao: Optional[str] = None


# ============================================================
# 4. CONFIANÇA PADRÃO POR FONTE
# ============================================================

CONFIANCA_POR_FONTE = {

    FonteEvidencia.ETIQUETA:
        NivelConfianca.ALTA,

    FonteEvidencia.MEDICAO_FISICA:
        NivelConfianca.ALTA,

    FonteEvidencia.VERIFICACAO_FISICA:
        NivelConfianca.ALTA,

    FonteEvidencia.FOTOGRAFIA:
        NivelConfianca.MEDIA,

    FonteEvidencia.INFORMACAO_FORNECIDA:
        NivelConfianca.MEDIA,

    FonteEvidencia.INFERENCIA_AURA:
        NivelConfianca.BAIXA,
}


# ============================================================
# 5. CRIAR EVIDÊNCIA
# ============================================================

def criar_evidencia(
    campo: str,
    valor: Any,
    fonte: FonteEvidencia,
    descricao: Optional[str] = None,
    confianca: Optional[NivelConfianca] = None,
) -> Evidencia:
    """
    Cria uma evidência.

    Quando uma confiança explícita é informada,
    ela é preservada.

    Quando nenhuma confiança é informada,
    a AURA utiliza a confiança padrão da fonte.
    """

    if confianca is None:

        confianca = CONFIANCA_POR_FONTE[
            fonte
        ]

    return Evidencia(
        campo=campo,
        valor=valor,
        fonte=fonte,
        confianca=confianca,
        descricao=descricao,
    )


# ============================================================
# 6. VERIFICAR SE A EVIDÊNCIA É FORTE
# ============================================================

def evidencia_forte(
    evidencia: Evidencia,
) -> bool:
    """
    Considera forte uma evidência
    com nível de confiança ALTA.
    """

    return (
        evidencia.confianca
        == NivelConfianca.ALTA
    )


# ============================================================
# 7. VERIFICAR SE A AURA PODE ACEITAR A INFORMAÇÃO — V1
# ============================================================

def aura_pode_aceitar(
    evidencia: Evidencia,
) -> bool:
    """
    Regra legada.

    A AURA pode aceitar automaticamente
    evidências de confiança ALTA ou MÉDIA.

    Evidências de confiança BAIXA
    precisam de confirmação.
    """

    return evidencia.confianca in [
        NivelConfianca.ALTA,
        NivelConfianca.MEDIA,
    ]


# ============================================================
# 8. STATUS PADRÃO POR FONTE — V2
# ============================================================
#
# Confiança e status são conceitos diferentes.
#
# A confiança indica a força da evidência.
#
# O status indica como aquela informação deve ser
# representada dentro da ficha técnica.
# ============================================================

STATUS_POR_FONTE = {

    FonteEvidencia.ETIQUETA:
        StatusEvidencia.CONFIRMADO,

    FonteEvidencia.MEDICAO_FISICA:
        StatusEvidencia.CONFIRMADO,

    FonteEvidencia.VERIFICACAO_FISICA:
        StatusEvidencia.CONFIRMADO,

    FonteEvidencia.FOTOGRAFIA:
        StatusEvidencia.IDENTIFICADO_VISUALMENTE,

    FonteEvidencia.INFORMACAO_FORNECIDA:
        StatusEvidencia.INFORMADO_PELO_USUARIO,

    FonteEvidencia.INFERENCIA_AURA:
        StatusEvidencia.INFERIDO,
}


# ============================================================
# 9. VERIFICAR SE A EVIDÊNCIA POSSUI VALOR ÚTIL — V2
# ============================================================

def evidencia_possui_valor(
    evidencia: Evidencia,
) -> bool:
    """
    Verifica se a evidência realmente possui
    uma informação utilizável.

    A existência de uma fonte não significa
    que exista um valor técnico válido.
    """

    valor = evidencia.valor

    if valor is None:
        return False

    if isinstance(
        valor,
        str,
    ):

        if not valor.strip():
            return False

    if isinstance(
        valor,
        list,
    ):

        if len(
            valor
        ) == 0:
            return False

    return True


# ============================================================
# 10. DETERMINAR STATUS DA EVIDÊNCIA — V2
# ============================================================

def determinar_status_evidencia(
    evidencia: Evidencia,
) -> StatusEvidencia:
    """
    Determina como uma evidência deve aparecer
    na FichaBodyV2.

    Regras:

    - ausência de valor útil -> NAO_CONFIRMADO;
    - etiqueta -> CONFIRMADO;
    - medição física -> CONFIRMADO;
    - verificação física -> CONFIRMADO;
    - fotografia -> IDENTIFICADO_VISUALMENTE;
    - informação fornecida -> INFORMADO_PELO_USUARIO;
    - inferência da AURA -> INFERIDO.

    A confiança continua existindo como dimensão
    independente e não é convertida diretamente
    em status.
    """

    if not evidencia_possui_valor(
        evidencia
    ):

        return StatusEvidencia.NAO_CONFIRMADO

    return STATUS_POR_FONTE[
        evidencia.fonte
    ]


# ============================================================
# 11. VERIFICAR SE EVIDÊNCIA EXIGE CONFIRMAÇÃO — V2
# ============================================================

def evidencia_exige_confirmacao(
    evidencia: Evidencia,
) -> bool:
    """
    Indica se a evidência ainda precisa ser
    confirmada antes de ser tratada como
    conhecimento aceito para objetivos que
    exigem evidência validada.
    """

    status = determinar_status_evidencia(
        evidencia
    )

    return status in {
        StatusEvidencia.INFERIDO,
        StatusEvidencia.NAO_CONFIRMADO,
    }


# ============================================================
# 12. CONVERTER EVIDÊNCIA PARA CONHECIMENTO DA FICHA — V2
# ============================================================

def converter_evidencia_para_ficha(
    evidencia: Evidencia,
) -> dict[str, Any]:
    """
    Converte uma Evidencia em uma estrutura
    compatível com aplicar_conhecimento_na_ficha_v2().

    O evidence.py determina o status.

    O ficha_manager.py apenas registra
    o resultado na ficha.
    """

    status = determinar_status_evidencia(
        evidencia
    )

    return {
        "valor":
            evidencia.valor,

        "fonte":
            evidencia.fonte.value,

        "status":
            status,
    }


# ============================================================
# 13. DESCREVER CLASSIFICAÇÃO DA EVIDÊNCIA — V2
# ============================================================

def classificar_evidencia_v2(
    evidencia: Evidencia,
) -> dict[str, Any]:
    """
    Retorna uma visão completa da classificação
    realizada pela AURA.

    Útil para testes, auditoria e explicabilidade.
    """

    status = determinar_status_evidencia(
        evidencia
    )

    return {
        "campo":
            evidencia.campo,

        "valor":
            evidencia.valor,

        "fonte":
            evidencia.fonte.value,

        "confianca":
            evidencia.confianca.value,

        "status":
            status.value,

        "exige_confirmacao":
            status in {
                StatusEvidencia.INFERIDO,
                StatusEvidencia.NAO_CONFIRMADO,
            },

        "descricao":
            evidencia.descricao,
    }