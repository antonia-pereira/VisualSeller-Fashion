from aura_products.body_dubai import ficha_body_dubai
from aura_schemas.body_v2 import StatusEvidencia


# ============================================================
# CAMPOS OBRIGATÓRIOS POR OBJETIVO
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
# STATUS CONSIDERADOS SUFICIENTES
# ============================================================

STATUS_ACEITOS = {
    StatusEvidencia.CONFIRMADO,
    StatusEvidencia.IDENTIFICADO_VISUALMENTE,
    StatusEvidencia.INFORMADO_PELO_USUARIO,
}


# ============================================================
# PERGUNTAS TÉCNICAS CADASTRADAS
# ============================================================

PERGUNTAS_POR_CAMPO = {

    "acabamento_pernas": (
        "Como é o acabamento da abertura das pernas? "
        "Observe a borda da peça e descreva como ela é finalizada."
    ),

    "possui_bojo": (
        "O body possui bojo?"
    ),

    "possui_aro": (
        "O body possui aro na região do busto?"
    ),

    "regiao_forrada": (
        "Em quais regiões da peça existe forro?"
    ),

    "decote_frente": (
        "Qual é o formato do decote da frente?"
    ),

    "decote_costas": (
        "Qual é o formato do decote das costas?"
    ),

    "construcao_mangas": (
        "De qual material é feita a manga e existem "
        "outros materiais ou detalhes aplicados nela?"
    ),
}


# ============================================================
# LOCALIZAR BLOQUEADORES
# ============================================================

def localizar_bloqueadores(ficha, objetivo):

    if objetivo not in CAMPOS_OBRIGATORIOS_POR_OBJETIVO:
        raise ValueError(
            f"Objetivo '{objetivo}' não possui regras cadastradas."
        )

    bloqueadores = []

    for nome_campo in CAMPOS_OBRIGATORIOS_POR_OBJETIVO[objetivo]:

        valor_campo = getattr(ficha, nome_campo, None)

        # Campo sem informação
        if valor_campo is None:
            bloqueadores.append(
                {
                    "campo": nome_campo,
                    "motivo": "SEM_INFORMACAO",
                }
            )
            continue

        # Campos simples, como tipo_produto
        if not hasattr(valor_campo, "status"):
            continue

        # Campo com evidência insuficiente
        if valor_campo.status not in STATUS_ACEITOS:

            motivo = (
                valor_campo.status.value
                if valor_campo.status
                else "SEM_STATUS"
            )

            bloqueadores.append(
                {
                    "campo": nome_campo,
                    "motivo": motivo,
                }
            )

    return bloqueadores


# ============================================================
# GERAR PERGUNTAS
# ============================================================

def gerar_perguntas(bloqueadores):

    perguntas = []

    for bloqueador in bloqueadores:

        campo = bloqueador["campo"]

        pergunta = PERGUNTAS_POR_CAMPO.get(campo)

        if pergunta:

            perguntas.append(
                {
                    "campo": campo,
                    "pergunta": pergunta,
                }
            )

        else:

            perguntas.append(
                {
                    "campo": campo,
                    "pergunta": (
                        f"Preciso confirmar a informação técnica "
                        f"referente ao campo '{campo}'."
                    ),
                }
            )

    return perguntas


# ============================================================
# QUESTIONADOR
# ============================================================

def questionar_por_objetivo(ficha, objetivo):

    bloqueadores = localizar_bloqueadores(
        ficha,
        objetivo,
    )

    perguntas = gerar_perguntas(
        bloqueadores
    )

    return {
        "objetivo": objetivo,
        "bloqueadores": bloqueadores,
        "perguntas": perguntas,
    }


# ============================================================
# TESTE — FICHA TÉCNICA COMPLETA
# ============================================================

resultado = questionar_por_objetivo(
    ficha_body_dubai,
    "ficha_tecnica_completa",
)


print()
print("==================================================")
print("        QUESTIONADOR TÉCNICO — AURA")
print("==================================================")
print()

print(f"Objetivo: {resultado['objetivo']}")
print()


if not resultado["bloqueadores"]:

    print("Nenhuma informação adicional é necessária.")
    print("AURA pode continuar.")

else:

    print(
        f"Pendências encontradas: "
        f"{len(resultado['bloqueadores'])}"
    )

    print()
    print("PERGUNTAS NECESSÁRIAS")
    print("----------------------------------------------")

    for numero, item in enumerate(
        resultado["perguntas"],
        start=1,
    ):

        print()
        print(f"{numero}. Campo: {item['campo']}")
        print(f"   Pergunta: {item['pergunta']}")


print()
print("==================================================")