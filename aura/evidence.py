from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel


# ============================================================
# TIPOS DE FONTE DE EVIDÊNCIA
# ============================================================

class FonteEvidencia(str, Enum):
    ETIQUETA = "etiqueta"
    MEDICAO_FISICA = "medicao_fisica"
    VERIFICACAO_FISICA = "verificacao_fisica"
    FOTOGRAFIA = "fotografia"
    INFORMACAO_FORNECIDA = "informacao_fornecida"
    INFERENCIA_AURA = "inferencia_aura"


# ============================================================
# NÍVEIS DE CONFIANÇA
# ============================================================

class NivelConfianca(str, Enum):
    ALTA = "alta"
    MEDIA = "media"
    BAIXA = "baixa"


# ============================================================
# MODELO DE EVIDÊNCIA
# ============================================================

class Evidencia(BaseModel):
    """
    Representa uma evidência utilizada pela AURA
    para aceitar ou avaliar uma informação do produto.
    """

    campo: str
    valor: Any
    fonte: FonteEvidencia
    confianca: NivelConfianca
    descricao: Optional[str] = None


# ============================================================
# CONFIANÇA PADRÃO POR FONTE
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
# CRIAR EVIDÊNCIA
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
# VERIFICAR SE A EVIDÊNCIA É FORTE
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
# VERIFICAR SE A AURA PODE ACEITAR A INFORMAÇÃO
# ============================================================

def aura_pode_aceitar(
    evidencia: Evidencia,
) -> bool:
    """
    A AURA pode aceitar automaticamente
    evidências de confiança ALTA ou MÉDIA.

    Evidências de confiança BAIXA
    precisam de confirmação.
    """

    return evidencia.confianca in [
        NivelConfianca.ALTA,
        NivelConfianca.MEDIA,
    ]