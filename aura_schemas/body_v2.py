from enum import Enum
from typing import Optional

from pydantic import BaseModel


class StatusEvidencia(str, Enum):
    CONFIRMADO = "CONFIRMADO"
    IDENTIFICADO_VISUALMENTE = "IDENTIFICADO_VISUALMENTE"
    INFORMADO_PELO_USUARIO = "INFORMADO_PELO_USUARIO"
    INFERIDO = "INFERIDO"
    NAO_CONFIRMADO = "NAO_CONFIRMADO"


class EvidenciaCampo(BaseModel):
    valor: Optional[str] = None
    fonte: Optional[str] = None
    status: Optional[StatusEvidencia] = None


class FichaBodyV2(BaseModel):
    """
    Ficha Técnica AURA - BODY v2.0

    Cada fato técnico pode registrar:
    - valor;
    - fonte;
    - status da evidência.

    A ficha separa fatos confirmados, observações visuais,
    informações fornecidas pelo usuário, inferências e
    informações ainda não confirmadas.
    """

    # ========================================================
    # 1. IDENTIFICAÇÃO DO PRODUTO
    # ========================================================

    categoria: str = "Moda íntima"
    tipo_produto: str = "Body"

    marca: Optional[EvidenciaCampo] = None
    nome_modelo: Optional[EvidenciaCampo] = None
    referencia: Optional[EvidenciaCampo] = None
    codigo_barras: Optional[EvidenciaCampo] = None

    # ========================================================
    # 2. VARIAÇÕES COMERCIAIS
    # ========================================================

    cor_principal: Optional[EvidenciaCampo] = None
    cores_disponiveis: Optional[EvidenciaCampo] = None
    tamanhos_disponiveis: Optional[EvidenciaCampo] = None
    grade_estoque: Optional[EvidenciaCampo] = None
    quantidade_total: Optional[EvidenciaCampo] = None

    # ========================================================
    # 3. MATERIAIS E COMPOSIÇÃO
    # ========================================================

    composicao_principal: Optional[EvidenciaCampo] = None
    composicao_forro: Optional[EvidenciaCampo] = None

    renda: Optional[EvidenciaCampo] = None
    tule: Optional[EvidenciaCampo] = None
    malha_canelada: Optional[EvidenciaCampo] = None
    elanca: Optional[EvidenciaCampo] = None

    # ========================================================
    # 4. MODELAGEM E CONSTRUÇÃO
    # ========================================================

    manga: Optional[EvidenciaCampo] = None
    decote_frente: Optional[EvidenciaCampo] = None
    decote_costas: Optional[EvidenciaCampo] = None

    construcao_busto_frente: Optional[EvidenciaCampo] = None
    construcao_busto_costas: Optional[EvidenciaCampo] = None

    construcao_tronco_frente: Optional[EvidenciaCampo] = None
    construcao_tronco_costas: Optional[EvidenciaCampo] = None

    construcao_inferior_frente: Optional[EvidenciaCampo] = None
    construcao_inferior_costas: Optional[EvidenciaCampo] = None

    construcao_mangas: Optional[EvidenciaCampo] = None
    construcao_punhos: Optional[EvidenciaCampo] = None

    # ========================================================
    # 5. ESTRUTURA FUNCIONAL
    # ========================================================

    possui_bojo: Optional[EvidenciaCampo] = None
    tipo_bojo: Optional[EvidenciaCampo] = None
    possui_aro: Optional[EvidenciaCampo] = None

    possui_forro: Optional[EvidenciaCampo] = None
    regiao_forrada: Optional[EvidenciaCampo] = None

    transparencia: Optional[EvidenciaCampo] = None

    # ========================================================
    # 6. FECHAMENTO ENTRE PERNAS
    # ========================================================

    possui_fechamento_entrepernas: Optional[EvidenciaCampo] = None
    tipo_fechamento_entrepernas: Optional[EvidenciaCampo] = None
    quantidade_colchetes: Optional[EvidenciaCampo] = None
    niveis_ajuste_fechamento: Optional[EvidenciaCampo] = None
    acabamento_fechamento: Optional[EvidenciaCampo] = None

    # ========================================================
    # 7. GRADE CORPORAL
    # Medidas recomendadas pelo fabricante para o corpo.
    # NÃO são medidas físicas da peça.
    # ========================================================

    tabela_medidas_corpo: Optional[EvidenciaCampo] = None

    busto_recomendado: Optional[EvidenciaCampo] = None
    cintura_recomendada: Optional[EvidenciaCampo] = None
    quadril_recomendado: Optional[EvidenciaCampo] = None

    # ========================================================
    # 8. MEDIDAS FÍSICAS DA PEÇA
    #
    # Protocolo:
    # - peça deitada em superfície plana;
    # - tecido naturalmente acomodado;
    # - sem esticar;
    # - larguras de uma lateral à outra;
    # - NÃO multiplicar as larguras por 2;
    # - válidas somente para o tamanho medido;
    # - não extrapolar para outros tamanhos sem regra de
    #   graduação fornecida pelo fabricante.
    # ========================================================

    tamanho_amostra_medida: Optional[EvidenciaCampo] = None

    largura_busto_peca: Optional[EvidenciaCampo] = None
    largura_cintura_peca: Optional[EvidenciaCampo] = None
    largura_quadril_peca: Optional[EvidenciaCampo] = None

    comprimento_total_ajuste_curto: Optional[EvidenciaCampo] = None
    comprimento_total_ajuste_longo: Optional[EvidenciaCampo] = None
    variacao_comprimento_fechamento: Optional[EvidenciaCampo] = None

    comprimento_manga: Optional[EvidenciaCampo] = None
    comprimento_punho_canelado: Optional[EvidenciaCampo] = None

    condicao_medicao_peca: Optional[EvidenciaCampo] = None

    # ========================================================
    # 9. ACABAMENTOS
    # ========================================================

    acabamento_decote: Optional[EvidenciaCampo] = None
    acabamento_pernas: Optional[EvidenciaCampo] = None

    # ========================================================
    # 10. CUIDADOS E CONSERVAÇÃO
    # ========================================================

    lavagem: Optional[EvidenciaCampo] = None
    alvejamento: Optional[EvidenciaCampo] = None
    secagem_tambor: Optional[EvidenciaCampo] = None
    secagem_natural: Optional[EvidenciaCampo] = None
    passadoria: Optional[EvidenciaCampo] = None
    lavagem_seco: Optional[EvidenciaCampo] = None
    limpeza_profissional_umido: Optional[EvidenciaCampo] = None