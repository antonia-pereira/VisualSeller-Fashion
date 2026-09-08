from aura_schemas.body_v2 import (
    FichaBodyV2,
    EvidenciaCampo,
    StatusEvidencia,
)


ficha_body_dubai = FichaBodyV2(

    # ========================================================
    # 1. IDENTIFICAÇÃO DO PRODUTO
    # ========================================================

    marca=EvidenciaCampo(
        valor="Linda Sedução Lingerie",
        fonte="etiqueta",
        status=StatusEvidencia.CONFIRMADO,
    ),

    nome_modelo=EvidenciaCampo(
        valor="Body Dubai",
        fonte="informado pelo usuário",
        status=StatusEvidencia.INFORMADO_PELO_USUARIO,
    ),

    referencia=EvidenciaCampo(
        valor="277",
        fonte="tag comercial",
        status=StatusEvidencia.CONFIRMADO,
    ),

    codigo_barras=EvidenciaCampo(
        valor="7002770010015",
        fonte="tag comercial da amostra P",
        status=StatusEvidencia.CONFIRMADO,
    ),

    # ========================================================
    # 2. VARIAÇÕES COMERCIAIS
    # ========================================================

    cor_principal=EvidenciaCampo(
        valor="Preto",
        fonte="produto físico e informado pelo usuário",
        status=StatusEvidencia.CONFIRMADO,
    ),

    cores_disponiveis=EvidenciaCampo(
        valor="Preto",
        fonte="informado pelo usuário",
        status=StatusEvidencia.INFORMADO_PELO_USUARIO,
    ),

    tamanhos_disponiveis=EvidenciaCampo(
        valor="P, M, G, GG",
        fonte="informado pelo usuário",
        status=StatusEvidencia.INFORMADO_PELO_USUARIO,
    ),

    grade_estoque=EvidenciaCampo(
        valor="P: 8 | M: 10 | G: 11 | GG: 15",
        fonte="informado pelo usuário",
        status=StatusEvidencia.INFORMADO_PELO_USUARIO,
    ),

    quantidade_total=EvidenciaCampo(
        valor="44 unidades",
        fonte="calculado a partir da grade informada pelo usuário",
        status=StatusEvidencia.CONFIRMADO,
    ),

    # ========================================================
    # 3. MATERIAIS E COMPOSIÇÃO
    # ========================================================

    composicao_principal=EvidenciaCampo(
        valor="85% poliamida, 15% elastano",
        fonte="etiqueta de composição",
        status=StatusEvidencia.CONFIRMADO,
    ),

    composicao_forro=EvidenciaCampo(
        valor="100% algodão",
        fonte="etiqueta de composição",
        status=StatusEvidencia.CONFIRMADO,
    ),

    renda=EvidenciaCampo(
        valor=(
            "Renda floral presente no busto, laterais da frente, "
            "tronco das costas e detalhes da parte inferior frontal"
        ),
        fonte="análise visual e verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    tule=EvidenciaCampo(
        valor="Tule transparente utilizado no corpo das mangas",
        fonte="verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    malha_canelada=EvidenciaCampo(
        valor=(
            "Malha canelada presente no centro da frente do tronco, "
            "centro da parte inferior frontal e punhos"
        ),
        fonte="verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    elanca=EvidenciaCampo(
        valor="Elanca presente na parte inferior das costas",
        fonte="material identificado pelo usuário na peça física",
        status=StatusEvidencia.INFORMADO_PELO_USUARIO,
    ),

    # ========================================================
    # 4. MODELAGEM E CONSTRUÇÃO
    # ========================================================

    manga=EvidenciaCampo(
        valor="Manga longa",
        fonte="análise visual do produto",
        status=StatusEvidencia.IDENTIFICADO_VISUALMENTE,
    ),

    decote_frente=EvidenciaCampo(
        valor="Decote em V",
        fonte="análise visual e verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    decote_costas=EvidenciaCampo(
        valor="Decote em V, com construção semelhante à frente",
        fonte="verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    construcao_busto_frente=EvidenciaCampo(
        valor="Renda externa com forro interno de algodão",
        fonte="verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    construcao_busto_costas=EvidenciaCampo(
        valor="Renda externa com forro interno de algodão",
        fonte="verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    construcao_tronco_frente=EvidenciaCampo(
        valor="Malha canelada no centro e renda nas laterais",
        fonte="verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    construcao_tronco_costas=EvidenciaCampo(
        valor="Renda",
        fonte="verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    construcao_inferior_frente=EvidenciaCampo(
        valor="Malha canelada no centro e renda nas laterais",
        fonte="verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    construcao_inferior_costas=EvidenciaCampo(
        valor="Elanca",
        fonte="material identificado pelo usuário na peça física",
        status=StatusEvidencia.INFORMADO_PELO_USUARIO,
    ),

    construcao_mangas=EvidenciaCampo(
        valor="Corpo da manga em tule transparente, sem aplicação de renda",
        fonte="verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    construcao_punhos=EvidenciaCampo(
        valor="Punho em malha canelada",
        fonte="verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    # ========================================================
    # 5. ESTRUTURA FUNCIONAL
    # ========================================================

    possui_bojo=EvidenciaCampo(
        valor="Não",
        fonte="verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    tipo_bojo=EvidenciaCampo(
        valor="Não se aplica",
        fonte="produto não possui bojo",
        status=StatusEvidencia.CONFIRMADO,
    ),

    possui_aro=EvidenciaCampo(
        valor="Não",
        fonte="verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    possui_forro=EvidenciaCampo(
        valor="Sim",
        fonte="etiqueta de composição e verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    regiao_forrada=EvidenciaCampo(
        valor="Busto e entrepernas",
        fonte="verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    transparencia=EvidenciaCampo(
        valor="Sim, nas mangas em tule e nas áreas em renda",
        fonte="análise visual e verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    # ========================================================
    # 6. FECHAMENTO ENTRE PERNAS
    # ========================================================

    possui_fechamento_entrepernas=EvidenciaCampo(
        valor="Sim",
        fonte="análise visual do detalhe da entreperna",
        status=StatusEvidencia.IDENTIFICADO_VISUALMENTE,
    ),

    tipo_fechamento_entrepernas=EvidenciaCampo(
        valor="Colchetes",
        fonte="análise visual do detalhe da entreperna",
        status=StatusEvidencia.IDENTIFICADO_VISUALMENTE,
    ),

    quantidade_colchetes=EvidenciaCampo(
        valor="2 colchetes por posição",
        fonte="análise visual do detalhe do fechamento",
        status=StatusEvidencia.IDENTIFICADO_VISUALMENTE,
    ),

    niveis_ajuste_fechamento=EvidenciaCampo(
        valor="2 posições de ajuste",
        fonte="análise visual do detalhe do fechamento",
        status=StatusEvidencia.IDENTIFICADO_VISUALMENTE,
    ),

    acabamento_fechamento=EvidenciaCampo(
        valor="Base têxtil reforçada",
        fonte="análise visual do detalhe do fechamento",
        status=StatusEvidencia.IDENTIFICADO_VISUALMENTE,
    ),

    # ========================================================
    # 7. GRADE CORPORAL
    # ========================================================

    tabela_medidas_corpo=EvidenciaCampo(
        valor=(
            "P: busto 81-86 cm | cintura 62-69 cm | quadril 82-92 cm; "
            "M: busto 87-91 cm | cintura 70-77 cm | quadril 93-100 cm; "
            "G: busto 92-97 cm | cintura 78-95 cm | quadril 101-108 cm; "
            "GG: busto 98-108 cm | cintura 86-96 cm | quadril 109-116 cm"
        ),
        fonte="imagem da tabela de medidas do fabricante",
        status=StatusEvidencia.CONFIRMADO,
    ),

    busto_recomendado=EvidenciaCampo(
        valor="P: 81-86 cm | M: 87-91 cm | G: 92-97 cm | GG: 98-108 cm",
        fonte="imagem da tabela de medidas do fabricante",
        status=StatusEvidencia.CONFIRMADO,
    ),

    cintura_recomendada=EvidenciaCampo(
        valor="P: 62-69 cm | M: 70-77 cm | G: 78-95 cm | GG: 86-96 cm",
        fonte="imagem da tabela de medidas do fabricante",
        status=StatusEvidencia.CONFIRMADO,
    ),

    quadril_recomendado=EvidenciaCampo(
        valor="P: 82-92 cm | M: 93-100 cm | G: 101-108 cm | GG: 109-116 cm",
        fonte="imagem da tabela de medidas do fabricante",
        status=StatusEvidencia.CONFIRMADO,
    ),

    # ========================================================
    # 8. MEDIDAS FÍSICAS DA PEÇA
    # ========================================================

    tamanho_amostra_medida=EvidenciaCampo(
        valor="P",
        fonte="tag comercial da peça física utilizada na medição",
        status=StatusEvidencia.CONFIRMADO,
    ),

    largura_busto_peca=EvidenciaCampo(
        valor="35 cm",
        fonte="medição física da amostra P pelo usuário",
        status=StatusEvidencia.CONFIRMADO,
    ),

    largura_cintura_peca=EvidenciaCampo(
        valor="30 cm",
        fonte="medição física da amostra P pelo usuário",
        status=StatusEvidencia.CONFIRMADO,
    ),

    largura_quadril_peca=EvidenciaCampo(
        valor="34 cm",
        fonte="medição física da amostra P pelo usuário",
        status=StatusEvidencia.CONFIRMADO,
    ),

    comprimento_total_ajuste_curto=EvidenciaCampo(
        valor="64 cm",
        fonte="medição física da amostra P com fechamento na posição mais curta",
        status=StatusEvidencia.CONFIRMADO,
    ),

    comprimento_total_ajuste_longo=EvidenciaCampo(
        valor="65 cm",
        fonte="medição física da amostra P com fechamento na posição mais longa",
        status=StatusEvidencia.CONFIRMADO,
    ),

    variacao_comprimento_fechamento=EvidenciaCampo(
        valor="1 cm",
        fonte="calculado a partir das duas medições físicas do fechamento",
        status=StatusEvidencia.CONFIRMADO,
    ),

    comprimento_manga=EvidenciaCampo(
        valor="61 cm",
        fonte="medição física da amostra P pelo usuário",
        status=StatusEvidencia.CONFIRMADO,
    ),

    comprimento_punho_canelado=EvidenciaCampo(
        valor="6 cm",
        fonte="medição física da amostra P pelo usuário",
        status=StatusEvidencia.CONFIRMADO,
    ),

    condicao_medicao_peca=EvidenciaCampo(
        valor=(
            "Peça deitada em superfície plana, tecido naturalmente acomodado "
            "e sem esticar; larguras medidas de uma lateral à outra e não "
            "multiplicadas por 2"
        ),
        fonte="protocolo de medição aplicado à amostra física P",
        status=StatusEvidencia.CONFIRMADO,
    ),

    # ========================================================
    # 9. ACABAMENTOS
    # ========================================================

    acabamento_decote=EvidenciaCampo(
        valor=(
            "Acabamento formado pela própria borda da renda, "
            "com desenho recortado ornamental"
        ),
        fonte="verificação física do produto",
        status=StatusEvidencia.CONFIRMADO,
    ),

    acabamento_pernas=EvidenciaCampo(
        valor="Acabamento presente, porém tipo técnico ainda não identificado",
        fonte="verificação física do produto",
        status=StatusEvidencia.NAO_CONFIRMADO,
    ),

    # ========================================================
    # 10. CUIDADOS E CONSERVAÇÃO
    # ========================================================

    lavagem=EvidenciaCampo(
        valor="Lavar à mão",
        fonte="símbolo de conservação na etiqueta",
        status=StatusEvidencia.CONFIRMADO,
    ),

    alvejamento=EvidenciaCampo(
        valor="Não usar alvejante",
        fonte="símbolo de conservação na etiqueta",
        status=StatusEvidencia.CONFIRMADO,
    ),

    secagem_tambor=EvidenciaCampo(
        valor="Não secar em tambor",
        fonte="símbolo de conservação na etiqueta",
        status=StatusEvidencia.CONFIRMADO,
    ),

    secagem_natural=EvidenciaCampo(
        valor="Secar na vertical",
        fonte="símbolo de conservação na etiqueta",
        status=StatusEvidencia.CONFIRMADO,
    ),

    passadoria=EvidenciaCampo(
        valor="Não passar a ferro",
        fonte="símbolo de conservação na etiqueta",
        status=StatusEvidencia.CONFIRMADO,
    ),

    lavagem_seco=EvidenciaCampo(
        valor="Não lavar a seco",
        fonte="símbolo de conservação na etiqueta",
        status=StatusEvidencia.CONFIRMADO,
    ),

    limpeza_profissional_umido=EvidenciaCampo(
        valor="Limpeza profissional a úmido em processo muito suave",
        fonte="símbolo de conservação na etiqueta",
        status=StatusEvidencia.CONFIRMADO,
    ),
)