from typing import Optional, List
from pydantic import BaseModel, Field


class GradeTamanho(BaseModel):
    tamanho: str
    quantidade: Optional[int] = None


class FichaBody(BaseModel):
    """
    Ficha Técnica AURA — BODY v1.0

    Esta estrutura define quais informações a AURA deve
    conhecer antes de considerar a análise técnica concluída.
    """

    # 1. IDENTIFICAÇÃO DO PRODUTO
    categoria: str = "Moda íntima"
    tipo_produto: str = "Body"
    marca: Optional[str] = None
    nome_modelo: Optional[str] = None
    referencia: Optional[str] = None
    codigo_barras: Optional[str] = None

    # 2. VARIAÇÕES COMERCIAIS
    cores_disponiveis: List[str] = Field(default_factory=list)
    tamanhos_disponiveis: List[str] = Field(default_factory=list)
    grade: List[GradeTamanho] = Field(default_factory=list)
    quantidade_total: Optional[int] = None

    # 3. MATERIAIS
    composicao_principal: Optional[str] = None
    composicao_forro: Optional[str] = None
    materiais_visuais: List[str] = Field(default_factory=list)

    # 4. MODELAGEM
    manga: Optional[str] = None
    decote_frente: Optional[str] = None
    decote_costas: Optional[str] = None
    fechamento: Optional[str] = None

    # 5. ESTRUTURA
    possui_bojo: Optional[bool] = None
    tipo_bojo: Optional[str] = None
    possui_forro: Optional[bool] = None
    transparencia: Optional[str] = None

    # 6. ACABAMENTOS
    acabamento_mangas: Optional[str] = None
    acabamento_pernas: Optional[str] = None
    acabamento_decote: Optional[str] = None

    # 7. MEDIDAS
    tamanho_medido: Optional[str] = None
    busto_cm: Optional[float] = None
    cintura_cm: Optional[float] = None
    quadril_cm: Optional[float] = None
    comprimento_cm: Optional[float] = None

    # 8. CUIDADOS
    instrucoes_conservacao: List[str] = Field(default_factory=list)

    # 9. EVIDÊNCIAS
    observacoes: List[str] = Field(default_factory=list)