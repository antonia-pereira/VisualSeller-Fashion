# aura/interpreter.py

from typing import Any


# ============================================================
# INTERPRETADOR DE RESPOSTAS DA AURA
# ============================================================


def normalizar_texto(texto: str) -> str:
    """
    Prepara o texto do usuário para interpretação.
    """

    return texto.strip().lower()


# ============================================================
# INTERPRETAÇÃO DE SIM / NÃO
# ============================================================


def interpretar_booleano(resposta: str) -> bool | None:
    """
    Tenta descobrir se a resposta do usuário significa
    verdadeiro (sim) ou falso (não).

    Retorna:
        True  -> resposta positiva
        False -> resposta negativa
        None  -> não foi possível determinar com segurança
    """

    texto = normalizar_texto(resposta)

    respostas_positivas = {
        "sim",
        "s",
        "tem",
        "possui",
        "sim, tem",
        "sim, possui",
        "tem sim",
        "possui sim",
    }

    respostas_negativas = {
        "não",
        "nao",
        "n",
        "não tem",
        "nao tem",
        "não possui",
        "nao possui",
        "não, não tem",
        "nao, nao tem",
    }

    if texto in respostas_positivas:
        return True

    if texto in respostas_negativas:
        return False

    return None


# ============================================================
# INTERPRETAÇÃO DE VALORES
# ============================================================


def interpretar_resposta(
    campo: str,
    resposta: str,
    tipo_esperado: type | None = None,
) -> Any:
    """
    Converte a resposta do usuário para um valor que
    possa ser utilizado pela ficha técnica.

    A função NÃO inventa informação.
    Se não conseguir interpretar com segurança,
    devolve o próprio texto.
    """

    texto = resposta.strip()

    if not texto:
        return None

    # --------------------------------------------------------
    # CAMPOS BOOLEANOS
    # --------------------------------------------------------

    if tipo_esperado is bool:
        valor_booleano = interpretar_booleano(texto)

        if valor_booleano is not None:
            return valor_booleano

        return None

    # --------------------------------------------------------
    # CAMPOS DE TEXTO
    # --------------------------------------------------------

    return texto


# ============================================================
# RESULTADO ESTRUTURADO
# ============================================================


def interpretar_para_campo(
    campo: str,
    resposta: str,
    tipo_esperado: type | None = None,
) -> dict:
    """
    Cria uma estrutura padronizada com o resultado
    da interpretação.
    """

    valor = interpretar_resposta(
        campo=campo,
        resposta=resposta,
        tipo_esperado=tipo_esperado,
    )

    return {
        "campo": campo,
        "resposta_original": resposta,
        "valor_interpretado": valor,
        "interpretado": valor is not None,
    }