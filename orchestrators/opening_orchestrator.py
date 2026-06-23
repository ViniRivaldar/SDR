import random
from services.ai_service import AIService


class Orchestrator:
    def __init__(self):
        self.ai = AIService()

    def get_niche_context(self, niche: str) -> str:
        niche = niche.lower()

        if "academia" in niche:
            return """
Dores comuns:
- demora para responder interessados
- perda de matrículas
- atendimento fora do horário comercial
- concorrência local

Público:
- dono da academia
- gerente
- responsável comercial
"""

        elif "clínica" in niche:
            return """
Dores comuns:
- demora no retorno aos pacientes
- agenda com horários ociosos
- recepção sobrecarregada
- cancelamentos

Público:
- dono da clínica
- gestor
- recepcionista chefe
"""

        elif "advocacia" in niche:
            return """
Dores comuns:
- demora para responder potenciais clientes
- muitas consultas sem fechamento
- triagem manual
- perda de oportunidades

Público:
- advogado
- sócio
- gestor do escritório
"""

        return """
Dores comuns:
- perda de leads
- demora na resposta
- atendimento inconsistente
"""

    def start_conversation(self, company_name: str, niche: str):

        niche_context = self.get_niche_context(niche)

        strategy = self.get_strategy()

        prompt = f"""
        Você é um SDR especialista em prospecção outbound.

        OBJETIVO:

    Conseguir uma resposta.

    Você NÃO está tentando vender.
    Você NÃO está tentando marcar uma reunião.
    Você NÃO está apresentando uma solução.

    A única meta é fazer o lead responder.

    Informações do nicho:

    {niche_context}

    Empresa:
    {company_name}

    Nicho:
    {niche}

    ESTRATÉGIA ESCOLHIDA:

    {strategy}

    Definições:

    curiosity:
    Faça uma pergunta que desperte curiosidade.

    diagnostic:
    Faça uma pergunta para entender como o processo atual funciona.

    pain:
    Faça uma pergunta relacionada a uma possível dor do nicho.

    comparison:
    Faça uma pergunta comparando canais, processos ou situações.

    REGRAS:

    - Seja humano.
    - Seja breve.
    - No máximo 2 frases.
    - Não use linguagem de vendedor.
    - Não use emojis.
    - Não faça pitch.
    - Não fale de IA.
    - Não fale de automação.
    - Faça apenas uma pergunta.

    Gere apenas a mensagem final.
    """

        message = self.ai.generate(prompt)

        return strategy, message
    
    def get_strategy(self):
        return random.choice([
        "curiosity",
        "diagnostic",
        "pain",
        "comparison"
        ])