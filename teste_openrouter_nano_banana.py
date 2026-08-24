from dotenv import load_dotenv

load_dotenv()

from aura.product_image_generator import gerar_imagem_com_referencias


print("=" * 60)
print("VISUALSELLER FASHION")
print("TESTE MÍNIMO — OPENROUTER + NANO BANANA 2")
print("=" * 60)


referencias = [
    "imagens/body_frente.jpg.jpeg"
]

prompt = """
Create a clean commercial product photograph
based strictly on the provided garment reference image.

Preserve the original garment design, shape, color,
materials, construction and visible details.

Present the garment professionally for an e-commerce
fashion marketplace.

Use a simple neutral studio background.

Do not add text, logos, accessories, prints,
new materials or new design elements.
"""


print("\nREFERÊNCIA:")
print(referencias[0])

print("\nPROVIDER:")
print("openrouter")

print("\nMODELO:")
print("google/gemini-3.1-flash-image")

print("\nATENÇÃO:")
print("A partir daqui haverá uma chamada real à API.")
print("-" * 60)


resultado = gerar_imagem_com_referencias(
    prompt=prompt,
    referencias=referencias,
    caminho_saida="outputs/teste_openrouter_nano_banana.png",
    provider="openrouter",
)


print("\n" + "=" * 60)
print("RESULTADO")
print("=" * 60)

print(resultado)

print("\n" + "=" * 60)
print("FIM DO TESTE")
print("=" * 60)