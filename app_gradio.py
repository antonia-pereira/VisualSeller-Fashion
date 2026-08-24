import gradio as gr

from aura.product_flow import (
    preparar_produto,
    obter_proxima_interacao,
    receber_resposta,
    produto_concluido,
    obter_ficha_final,
)


# ============================================================
# VISUALSELLER FASHION
# INTERFACE DA AURA — CONVERSA + FICHA
# ============================================================


# ============================================================
# ESTADO GLOBAL SIMPLES
# ============================================================

sessao_atual = None


# ============================================================
# 1. CONVERTER IMAGENS DO GRADIO
# ============================================================

def preparar_imagens_gradio(
    arquivos,
):
    """
    Converte os arquivos enviados pelo Gradio
    para o formato esperado pelo product_flow.
    """

    imagens = []

    if not arquivos:
        return imagens


    for arquivo in arquivos:

        caminho = arquivo.name

        nome = caminho.lower()


        # ----------------------------------------------------
        # CLASSIFICAÇÃO SIMPLES PELO NOME
        # ----------------------------------------------------

        if "frente" in nome:

            tipo = "frente"

        elif (
            "costa" in nome
            or "costas" in nome
        ):

            tipo = "costas"

        elif "compos" in nome:

            tipo = "composicao"

        elif "etiqueta" in nome:

            tipo = "etiqueta"

        else:

            tipo = "detalhe"


        imagens.append(
            {
                "caminho":
                    caminho,

                "tipo":
                    tipo,
            }
        )


    return imagens


# ============================================================
# 2. FORMATAR FICHA
# ============================================================

def formatar_ficha(
    ficha,
):
    """
    Transforma os dados internos da FichaBody
    em uma ficha clara e profissional para o usuário.

    Campos vazios não são exibidos.
    """

    dados = ficha.model_dump()


    # --------------------------------------------------------
    # FUNÇÕES AUXILIARES DE APRESENTAÇÃO
    # --------------------------------------------------------

    def vazio(valor):
        if valor is None:
            return True

        if isinstance(valor, str):
            return not valor.strip()

        if isinstance(valor, list):
            return len(valor) == 0

        return False


    def sim_nao(valor):
        if valor is True:
            return "Sim"

        if valor is False:
            return "Não"

        return str(valor)


    def texto_bonito(valor):
        if not isinstance(valor, str):
            return str(valor)

        texto = valor.strip()

        if not texto:
            return texto

        return texto[0].upper() + texto[1:]


    def lista_texto(valor):
        if vazio(valor):
            return None

        if not isinstance(valor, list):
            return texto_bonito(valor)

        return ", ".join(
            texto_bonito(str(item))
            for item in valor
        )


    def adicionar_secao(
        linhas,
        titulo,
        itens,
    ):
        itens_validos = [
            item
            for item in itens
            if item is not None
        ]

        if not itens_validos:
            return

        if linhas:
            linhas.append("")

        linhas.append(titulo)
        linhas.append("─" * 38)
        linhas.extend(itens_validos)


    linhas = [
        "FICHA DO PRODUTO",
        "",
    ]


    # ========================================================
    # IDENTIFICAÇÃO
    # ========================================================

    identificacao = []

    if not vazio(dados.get("categoria")):
        identificacao.append(
            f"Categoria: {texto_bonito(dados['categoria'])}"
        )

    if not vazio(dados.get("tipo_produto")):
        identificacao.append(
            f"Produto: {texto_bonito(dados['tipo_produto'])}"
        )

    if not vazio(dados.get("marca")):
        identificacao.append(
            f"Marca: {texto_bonito(dados['marca'])}"
        )

    if not vazio(dados.get("nome_modelo")):
        identificacao.append(
            f"Modelo: {texto_bonito(dados['nome_modelo'])}"
        )

    if not vazio(dados.get("referencia")):
        identificacao.append(
            f"Referência: {dados['referencia']}"
        )

    if not vazio(dados.get("codigo_barras")):
        identificacao.append(
            f"Código de barras: {dados['codigo_barras']}"
        )

    adicionar_secao(
        linhas,
        "IDENTIFICAÇÃO",
        identificacao,
    )


    # ========================================================
    # VARIAÇÕES E ESTOQUE
    # ========================================================

    variacoes = []

    cores = lista_texto(
        dados.get("cores_disponiveis")
    )

    if cores:
        variacoes.append(
            f"Cores disponíveis: {cores}"
        )

    tamanhos = lista_texto(
        dados.get("tamanhos_disponiveis")
    )

    if tamanhos:
        variacoes.append(
            f"Tamanhos: {tamanhos}"
        )

    grade = dados.get("grade") or []

    if grade:
        variacoes.append("")
        variacoes.append("Grade:")

        for item in grade:
            if isinstance(item, dict):
                tamanho = item.get("tamanho")
                quantidade = item.get("quantidade")
            else:
                tamanho = getattr(item, "tamanho", None)
                quantidade = getattr(item, "quantidade", None)

            if tamanho is None:
                continue

            if quantidade is None:
                variacoes.append(
                    f"• {tamanho}"
                )
            else:
                variacoes.append(
                    f"• {tamanho} — {quantidade} unidades"
                )

    if dados.get("quantidade_total") is not None:
        variacoes.append("")
        variacoes.append(
            f"Estoque total: {dados['quantidade_total']} unidades"
        )

    adicionar_secao(
        linhas,
        "VARIAÇÕES E ESTOQUE",
        variacoes,
    )


    # ========================================================
    # COMPOSIÇÃO
    # ========================================================

    composicao = []

    if not vazio(dados.get("composicao_principal")):
        composicao.append(
            "Composição principal: "
            f"{dados['composicao_principal']}"
        )

    if not vazio(dados.get("composicao_forro")):
        composicao.append(
            f"Composição do forro: {dados['composicao_forro']}"
        )

    adicionar_secao(
        linhas,
        "COMPOSIÇÃO",
        composicao,
    )


    # ========================================================
    # MODELAGEM E ESTRUTURA
    # ========================================================

    modelagem = []

    campos_modelagem = [
        ("manga", "Manga"),
        ("decote_frente", "Decote frontal"),
        ("decote_costas", "Decote das costas"),
        ("fechamento", "Fechamento"),
    ]

    for campo, rotulo in campos_modelagem:
        valor = dados.get(campo)

        if not vazio(valor):
            modelagem.append(
                f"{rotulo}: {texto_bonito(valor)}"
            )

    if dados.get("possui_bojo") is not None:
        modelagem.append(
            f"Possui bojo: {sim_nao(dados['possui_bojo'])}"
        )

    if not vazio(dados.get("tipo_bojo")):
        modelagem.append(
            f"Tipo de bojo: {texto_bonito(dados['tipo_bojo'])}"
        )

    if dados.get("possui_forro") is not None:
        modelagem.append(
            f"Possui forro: {sim_nao(dados['possui_forro'])}"
        )

    adicionar_secao(
        linhas,
        "MODELAGEM E ESTRUTURA",
        modelagem,
    )


    # ========================================================
    # ACABAMENTOS E DETALHES VISUAIS
    # ========================================================

    detalhes = []

    materiais = dados.get("materiais_visuais") or []

    if materiais:
        detalhes.append("Materiais e detalhes identificados:")

        for material in materiais:
            detalhes.append(
                f"• {texto_bonito(str(material))}"
            )

    campos_detalhes = [
        ("transparencia", "Transparência"),
        ("acabamento_mangas", "Acabamento das mangas"),
        ("acabamento_pernas", "Acabamento das pernas"),
        ("acabamento_decote", "Acabamento do decote"),
    ]

    for campo, rotulo in campos_detalhes:
        valor = dados.get(campo)

        if not vazio(valor):
            detalhes.append(
                f"{rotulo}: {texto_bonito(valor)}"
            )

    adicionar_secao(
        linhas,
        "DETALHES VISUAIS E ACABAMENTOS",
        detalhes,
    )


    # ========================================================
    # MEDIDAS
    # ========================================================

    medidas = []

    if not vazio(dados.get("tamanho_medido")):
        medidas.append(
            "Tamanho identificado/medido: "
            f"{str(dados['tamanho_medido']).upper()}"
        )

    medidas_campos = [
        ("busto_cm", "Busto"),
        ("cintura_cm", "Cintura"),
        ("quadril_cm", "Quadril"),
        ("comprimento_cm", "Comprimento"),
    ]

    for campo, rotulo in medidas_campos:
        valor = dados.get(campo)

        if valor is not None:
            medidas.append(
                f"{rotulo}: {valor} cm"
            )

    adicionar_secao(
        linhas,
        "MEDIDAS",
        medidas,
    )


    # ========================================================
    # CUIDADOS
    # ========================================================

    cuidados = dados.get("instrucoes_conservacao") or []
    linhas_cuidados = []

    if cuidados:
        for cuidado in cuidados:
            linhas_cuidados.append(
                f"• {texto_bonito(str(cuidado))}"
            )

    adicionar_secao(
        linhas,
        "CUIDADOS E CONSERVAÇÃO",
        linhas_cuidados,
    )


    # ========================================================
    # OBSERVAÇÕES
    # ========================================================

    observacoes = dados.get("observacoes") or []
    linhas_observacoes = []

    if observacoes:
        for observacao in observacoes:
            linhas_observacoes.append(
                f"• {texto_bonito(str(observacao))}"
            )

    adicionar_secao(
        linhas,
        "OBSERVAÇÕES",
        linhas_observacoes,
    )


    return "\n".join(linhas).strip()


# ============================================================
# 3. CRIAR HISTÓRICO INICIAL
# ============================================================

def criar_historico_inicial():
    """
    Cria o histórico no formato
    exigido pelo Chatbot desta versão do Gradio.
    """

    return [
        {
            "role":
                "assistant",

            "content":
                (
                    "Mostre seu produto para a Aura. "
                    "Envie as imagens e eu vou analisar "
                    "o máximo possível antes de fazer perguntas."
                ),
        }
    ]


# ============================================================
# 4. ADICIONAR MENSAGEM DA AURA
# ============================================================

def adicionar_mensagem_aura(
    historico,
    mensagem,
):
    """
    Adiciona uma nova mensagem da Aura.
    """

    if historico is None:

        historico = []


    historico.append(
        {
            "role":
                "assistant",

            "content":
                mensagem,
        }
    )


    return historico


# ============================================================
# 5. ADICIONAR MENSAGEM DO USUÁRIO
# ============================================================

def adicionar_mensagem_usuario(
    historico,
    mensagem,
):
    """
    Adiciona uma nova mensagem do usuário.
    """

    if historico is None:

        historico = []


    historico.append(
        {
            "role":
                "user",

            "content":
                mensagem,
        }
    )


    return historico


# ============================================================
# 6. ANALISAR PRODUTO
# ============================================================

def analisar_interface(
    arquivos,
    historico,
):
    """
    Inicia o fluxo completo da Aura.
    """

    global sessao_atual


    if historico is None:

        historico = criar_historico_inicial()


    if not arquivos:

        historico = adicionar_mensagem_aura(
            historico,
            "Envie pelo menos uma imagem do produto.",
        )


        return (
            historico,

            "",

            gr.update(
                visible=False
            ),

            "",
        )


    imagens = preparar_imagens_gradio(
        arquivos
    )


    historico = adicionar_mensagem_aura(
        historico,
        (
            f"Recebi {len(imagens)} imagens. "
            "Estou analisando o produto..."
        ),
    )


    # --------------------------------------------------------
    # EXECUTAR AURA
    # --------------------------------------------------------

    try:

        sessao_atual = preparar_produto(
            imagens
        )


    except Exception as erro:

        historico = adicionar_mensagem_aura(
            historico,
            (
                "Ocorreu um erro durante a análise:\n\n"
                f"{erro}"
            ),
        )


        return (
            historico,

            "",

            gr.update(
                visible=False
            ),

            "",
        )


    # --------------------------------------------------------
    # PRODUTO JÁ COMPLETO
    # --------------------------------------------------------

    if produto_concluido(
        sessao_atual
    ):

        ficha = obter_ficha_final(
            sessao_atual
        )


        historico = adicionar_mensagem_aura(
            historico,
            (
                "Produto compreendido. "
                "A ficha técnica está pronta."
            ),
        )


        return (
            historico,

            formatar_ficha(
                ficha
            ),

            gr.update(
                visible=False
            ),

            "",
        )


    # --------------------------------------------------------
    # AURA PRECISA PERGUNTAR
    # --------------------------------------------------------

    pergunta = obter_proxima_interacao(
        sessao_atual
    )


    if pergunta is None:

        mensagem = (
            "Não encontrei nenhuma pergunta pendente."
        )

    else:

        mensagem = pergunta.get(
            "mensagem",
            "Preciso de mais uma informação.",
        )


    historico = adicionar_mensagem_aura(
        historico,
        mensagem,
    )


    return (
        historico,

        "",

        gr.update(
            visible=True
        ),

        "",
    )


# ============================================================
# 7. RECEBER RESPOSTA DO USUÁRIO
# ============================================================

def responder_interface(
    resposta,
    historico,
):
    """
    Recebe uma resposta do usuário
    e continua o fluxo da Aura.
    """

    global sessao_atual


    if historico is None:

        historico = criar_historico_inicial()


    # --------------------------------------------------------
    # NENHUM PRODUTO EM ANÁLISE
    # --------------------------------------------------------

    if sessao_atual is None:

        historico = adicionar_mensagem_aura(
            historico,
            "Envie e analise um produto primeiro.",
        )


        return (
            historico,

            "",

            "",

            gr.update(
                visible=False
            ),
        )


    # --------------------------------------------------------
    # RESPOSTA VAZIA
    # --------------------------------------------------------

    if not resposta.strip():

        historico = adicionar_mensagem_aura(
            historico,
            "Digite uma resposta para continuar.",
        )


        return (
            historico,

            "",

            "",

            gr.update(
                visible=True
            ),
        )


    # --------------------------------------------------------
    # MOSTRAR RESPOSTA DO USUÁRIO NO CHAT
    # --------------------------------------------------------

    historico = adicionar_mensagem_usuario(
        historico,
        resposta,
    )


    # --------------------------------------------------------
    # ENVIAR RESPOSTA PARA O CÉREBRO DA AURA
    # --------------------------------------------------------

    resultado = receber_resposta(
        sessao=sessao_atual,
        resposta=resposta,
    )


    campos = resultado.get(
        "campos_atualizados",
        [],
    )


    # --------------------------------------------------------
    # AURA NÃO ENTENDEU
    # --------------------------------------------------------

    if not campos:

        historico = adicionar_mensagem_aura(
            historico,
            (
                "Recebi sua resposta, mas não consegui "
                "identificar uma informação válida. "
                "Pode responder novamente de outra forma?"
            ),
        )


        return (
            historico,

            "",

            "",

            gr.update(
                visible=True
            ),
        )


    # --------------------------------------------------------
    # FLUXO CONCLUÍDO
    # --------------------------------------------------------

    if produto_concluido(
        sessao_atual
    ):

        ficha = obter_ficha_final(
            sessao_atual
        )


        historico = adicionar_mensagem_aura(
            historico,
            (
                "Perfeito. Produto compreendido. "
                "A ficha técnica está pronta."
            ),
        )


        return (
            historico,

            "",

            formatar_ficha(
                ficha
            ),

            gr.update(
                visible=False
            ),
        )


    # --------------------------------------------------------
    # PRÓXIMA PERGUNTA
    # --------------------------------------------------------

    pergunta = obter_proxima_interacao(
        sessao_atual
    )


    if pergunta is None:

        mensagem = (
            "As informações necessárias foram registradas."
        )

    else:

        mensagem = pergunta.get(
            "mensagem",
            "Preciso de mais uma informação.",
        )


    historico = adicionar_mensagem_aura(
        historico,
        mensagem,
    )


    return (
        historico,

        "",

        "",

        gr.update(
            visible=True
        ),
    )


# ============================================================
# 8. NOVO PRODUTO
# ============================================================

def novo_produto():
    """
    Limpa a sessão atual e inicia
    uma nova análise.
    """

    global sessao_atual

    sessao_atual = None


    return (
        None,

        criar_historico_inicial(),

        "",

        "",

        gr.update(
            visible=False
        ),
    )


# ============================================================
# 9. INTERFACE
# ============================================================

with gr.Blocks(
    title="VisualSeller Fashion — Aura"
) as app:


    # ========================================================
    # CABEÇALHO
    # ========================================================

    gr.Markdown(
        """
# VisualSeller Fashion

## Mostre seu produto para a Aura

Envie as imagens do produto.

A Aura irá observar o máximo possível primeiro,
cruzar as informações encontradas e perguntar
somente o que ainda for necessário.
        """
    )


    # ========================================================
    # UPLOAD
    # ========================================================

    imagens_input = gr.File(
        label="Imagens do produto",
        file_count="multiple",
        file_types=[
            "image"
        ],
    )


    # ========================================================
    # BOTÕES PRINCIPAIS
    # ========================================================

    with gr.Row():

        botao_analisar = gr.Button(
            "Analisar com a Aura",
            variant="primary",
        )

        botao_novo = gr.Button(
            "Novo produto"
        )


    # ========================================================
    # CHAT
    # ========================================================

    gr.Markdown(
        "### Converse com a Aura"
    )


    chatbot = gr.Chatbot(
        value=criar_historico_inicial(),
        height=350,
        label="Aura",
    )


    # ========================================================
    # RESPOSTA
    # ========================================================

    grupo_resposta = gr.Group(
        visible=False
    )


    with grupo_resposta:

        resposta_usuario = gr.Textbox(
            label="Sua resposta",
            placeholder=(
                "Digite aqui a informação "
                "solicitada pela Aura..."
            ),
            lines=2,
        )


        botao_responder = gr.Button(
            "Enviar resposta",
            variant="primary",
        )


    # ========================================================
    # FICHA
    # ========================================================

    gr.Markdown(
        "### Ficha técnica"
    )


    ficha_final = gr.Textbox(
        label="Ficha consolidada pela Aura",
        interactive=False,
        lines=22,
        placeholder=(
            "A ficha aparecerá aqui "
            "quando a análise estiver concluída."
        ),
    )


    # ========================================================
    # EVENTO — ANALISAR
    # ========================================================

    botao_analisar.click(
        fn=analisar_interface,

        inputs=[
            imagens_input,
            chatbot,
        ],

        outputs=[
            chatbot,
            ficha_final,
            grupo_resposta,
            resposta_usuario,
        ],
    )


    # ========================================================
    # EVENTO — RESPONDER PELO BOTÃO
    # ========================================================

    botao_responder.click(
        fn=responder_interface,

        inputs=[
            resposta_usuario,
            chatbot,
        ],

        outputs=[
            chatbot,
            resposta_usuario,
            ficha_final,
            grupo_resposta,
        ],
    )


    # ========================================================
    # EVENTO — RESPONDER COM ENTER
    # ========================================================

    resposta_usuario.submit(
        fn=responder_interface,

        inputs=[
            resposta_usuario,
            chatbot,
        ],

        outputs=[
            chatbot,
            resposta_usuario,
            ficha_final,
            grupo_resposta,
        ],
    )


    # ========================================================
    # EVENTO — NOVO PRODUTO
    # ========================================================

    botao_novo.click(
        fn=novo_produto,

        inputs=[],

        outputs=[
            imagens_input,
            chatbot,
            resposta_usuario,
            ficha_final,
            grupo_resposta,
        ],
    )


# ============================================================
# 10. INICIAR
# ============================================================

if __name__ == "__main__":

    app.launch()