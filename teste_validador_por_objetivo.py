from aura_products.body_dubai import ficha_body_dubai
from aura_schemas.body_v2 import StatusEvidencia


# ============================================================
# REGRAS DE VALIDAÇÃO POR OBJETIVO
# ============================================================

CAMPOS_OBRIGATORIOS_POR_OBJETIVO = {

    "titulo_marketplace": [
        "tipo_produto",
        "marca",
        "nome_modelo",
        "cor_principal",
    ],

    "ficha_tecnica_completa": [
        "marca",
        "nome_modelo",
        "referencia",
        "cor_principal",
        "tamanhos_disponiveis",
        "composicao_principal",
        "composicao_forro",
        "renda",
        "tule",
        "malha_canelada",
        "elanca",
        "manga",
        "decote_frente",
        "decote_costas",
        "construcao_busto_frente",
        "construcao_busto_costas",
        "construcao_tronco_frente",
        "construcao_tronco_costas",
        "construcao_inferior_frente",
        "construcao_inferior_costas",
        "construcao_mangas",
        "construcao_punhos",
        "possui_bojo",
        "possui_aro",
        "possui_forro",
        "regiao_forrada",
        "possui_fechamento_entrepernas",
        "tipo_fechamento_entrepernas",
        "acabamento_decote",
        "acabamento_pernas",
        "lavagem",
        "alvejamento",
        "secagem_tambor",
        "secagem_natural",
        "passadoria",
        "lavagem_seco",
        "limpeza_profissional_umido",
    ],
}


# ============================================================
# STATUS ACEITOS COMO SUFICIENTES
# ============================================================

STATUS_ACEITOS = {
    StatusEvidencia.CONFIRMADO,
    StatusEvidencia.IDENTIFICADO_VISUALMENTE,
    StatusEvidencia.INFORMADO_PELO_USUARIO,
}


# ============================================================
# VALIDADOR POR OBJETIVO
# ============================================================

def validar_por_objetivo(ficha, objetivo):

    if objetivo not in CAMPOS_OBRIGATORIOS_POR_OBJETIVO:
        raise ValueError(
            f"Objetivo '{objetivo}' não possui regras de validação."
        )

    campos_obrigatorios = CAMPOS_OBRIGATORIOS_POR_OBJETIVO[objetivo]

    aprovados = []
    bloqueadores = []

    for nome_campo in campos_obrigatorios:

        valor_campo = getattr(ficha, nome_campo, None)

        # --------------------------------------------
        # Campo inexistente ou sem informação
        # --------------------------------------------

        if valor_campo is None:
            bloqueadores.append(
                {
                    "campo": nome_campo,
                    "motivo": "SEM_INFORMACAO",
                }
            )
            continue

        # --------------------------------------------
        # Campos simples do schema
        # Exemplo: tipo_produto = "Body"
        # --------------------------------------------

        if not hasattr(valor_campo, "status"):
            aprovados.append(nome_campo)
            continue

        # --------------------------------------------
        # Campo com evidência
        # --------------------------------------------

        if valor_campo.status in STATUS_ACEITOS:
            aprovados.append(nome_campo)

        else:
            bloqueadores.append(
                {
                    "campo": nome_campo,
                    "motivo": (
                        valor_campo.status.value
                        if valor_campo.status
                        else "SEM_STATUS"
                    ),
                }
            )

    pode_continuar = len(bloqueadores) == 0

    return {
        "objetivo": objetivo,
        "pode_continuar": pode_continuar,
        "aprovados": aprovados,
        "bloqueadores": bloqueadores,
    }


# ============================================================
# EXIBIÇÃO DO RESULTADO
# ============================================================

def mostrar_resultado(resultado):

    print()
    print("==================================================")
    print(f"OBJETIVO: {resultado['objetivo']}")
    print("==================================================")
    print()

    if resultado["pode_continuar"]:

        print("DECISÃO: AURA PODE CONTINUAR")

    else:

        print("DECISÃO: AURA NÃO DEVE CONTINUAR")

    print()
    print(f"Campos aprovados: {len(resultado['aprovados'])}")
    print(f"Bloqueadores: {len(resultado['bloqueadores'])}")

    if resultado["bloqueadores"]:

        print()
        print("CAMPOS BLOQUEADORES")
        print("----------------------------------------------")

        for item in resultado["bloqueadores"]:
            print(
                f"- {item['campo']} "
                f"({item['motivo']})"
            )

    print()


# ============================================================
# TESTE 1 — TÍTULO DE MARKETPLACE
# ============================================================

resultado_titulo = validar_por_objetivo(
    ficha_body_dubai,
    "titulo_marketplace",
)

mostrar_resultado(resultado_titulo)


# ============================================================
# TESTE 2 — FICHA TÉCNICA COMPLETA
# ============================================================

resultado_ficha = validar_por_objetivo(
    ficha_body_dubai,
    "ficha_tecnica_completa",
)

mostrar_resultado(resultado_ficha)