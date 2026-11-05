
import re


def limpiar_texto(texto):
    """Normaliza espacios y saltos de línea de un texto OCR."""
    texto = re.sub(r"[ \t]+", " ", texto)
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto.strip()


if __name__ == "__main__":
    original = "La  prensa   histórica\n\n\ncontiene   errores."
    resultado = limpiar_texto(original)
    print(resultado)
