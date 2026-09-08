from collections import Counter

from aura_schemas.body_v2 import StatusEvidencia
from aura_products.body_dubai import ficha_body_dubai


# ============================================================
# VALIDADOR DA FICHA BODY V2
# ============================================================


def validar_ficha(ficha):
    """
    Analisa os campos da ficha e classifica o estado
    das informações registradas.
    """

    contagem = Counter()

    confirmados = []
    identificados_visualmente = []
    informados_usuario = []
    inferidos = []
    nao_confirmados = []
    sem_informacao = []

    dados = ficha.model_dump()

    for nome_campo, valor_campo in dados.items():

        # Campos simples do schema:
        # categoria, tipo_produto etc.
        if valor_campo is not None and not isinstance(valor_campo, dict):
            continue

        # Campo existe no schema, mas não foi preenchido.
        if valor_campo is None:
            sem_informacao.append(nome_campo)
            contagem["SEM_INFORMACAO"] += 1
            continue

        status = valor_campo.get("status")

        if status == StatusEvidencia.CONFIRMADO:
            confirmados.append(nome_campo)
            contagem["CONFIRMADO"] += 1

        elif status == StatusEvidencia.IDENTIFICADO_VISUALMENTE:
            identificados_visualmente.append(nome_campo)
            contagem["IDENTIFICADO_VISUALMENTE"] += 1

        elif status == StatusEvidencia.INFORMADO_PELO_USUARIO:
            informados_usuario.append(nome_campo)
            contagem["INFORMADO_PELO_USUARIO"] += 1

        elif status == StatusEvidencia.INFERIDO:
            inferidos.append(nome_campo)
            contagem["INFERIDO"] += 1

        elif status == StatusEvidencia.NAO_CONFIRMADO:
            nao_confirmados.append(nome_campo)
            contagem["NAO_CONFIRMADO"] += 1

        else:
            sem_informacao.append(nome_campo)
            contagem["SEM_INFORMACAO"] += 1

    return {
        "contagem": contagem,
        "confirmados": confirmados,
        "identificados_visualmente": identificados_visualmente,
        "informados_usuario": informados_usuario,
        "inferidos": inferidos,
        "nao_confirmados": nao_confirmados,
        "sem_informacao": sem_informacao,
    }


# ============================================================
# EXECUÇÃO DO VALIDADOR
# ============================================================

resultado = validar_ficha(ficha_body_dubai)


print()
print("==============================================")
print("      VALIDAÇÃO DA FICHA — BODY DUBAI")
print("==============================================")
print()

print("RESUMO")
print("----------------------------------------------")

ordem_status = [
    "CONFIRMADO",
    "IDENTIFICADO_VISUALMENTE",
    "INFORMADO_PELO_USUARIO",
    "INFERIDO",
    "NAO_CONFIRMADO",
    "SEM_INFORMACAO",
]

for status in ordem_status:
    quantidade = resultado["contagem"].get(status, 0)
    print(f"{status}: {quantidade}")


print()
print("CAMPOS QUE PRECISAM DE ATENÇÃO")
print("----------------------------------------------")

problemas_encontrados = False


if resultado["inferidos"]:
    problemas_encontrados = True

    print()
    print("INFERIDOS:")

    for campo in resultado["inferidos"]:
        print(f"- {campo}")


if resultado["nao_confirmados"]:
    problemas_encontrados = True

    print()
    print("NÃO CONFIRMADOS:")

    for campo in resultado["nao_confirmados"]:
        print(f"- {campo}")


if resultado["sem_informacao"]:
    problemas_encontrados = True

    print()
    print("SEM INFORMAÇÃO:")

    for campo in resultado["sem_informacao"]:
        print(f"- {campo}")


if not problemas_encontrados:
    print("Nenhum campo pendente encontrado.")


print()
print("==============================================")