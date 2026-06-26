def get_niche_context(niche: str) -> str:

    niche = niche.lower()

    if "academia" in niche:
        return """
CONTEXTO DO NEGÓCIO

Você está conversando com uma academia.

Os interessados normalmente entram em contato perguntando sobre:

- planos
- horários
- aula experimental
- musculação
- treinamento funcional

Quem normalmente responde é o dono, gerente ou recepção.

Responder rapidamente aumenta bastante a chance de matrícula.

Escreva como alguém que realmente conhece o mercado de academias.
"""

    elif "clínica" in niche or "clinica" in niche:
        return """
CONTEXTO DO NEGÓCIO

Você está conversando com uma clínica.

Os pacientes normalmente entram em contato para:

- marcar consultas
- exames
- convênios
- tirar dúvidas

Quem responde costuma ser a recepção ou a gestão.

Rapidez transmite confiança ao paciente.

Escreva como alguém que realmente conhece o mercado de clínicas.
"""

    elif "advocacia" in niche:
        return """
CONTEXTO DO NEGÓCIO

Você está conversando com um escritório de advocacia.

Os clientes normalmente procuram:

- orientação jurídica
- atendimento urgente
- informações sobre processos
- primeira consulta

Quem responde costuma ser um advogado ou uma secretária.

Confiança e rapidez fazem muita diferença.

Escreva como alguém que realmente conhece escritórios de advocacia.
"""

    return """
CONTEXTO DO NEGÓCIO

Você está conversando com uma empresa.

Antes de escrever, imagine como funciona esse tipo de negócio.
"""