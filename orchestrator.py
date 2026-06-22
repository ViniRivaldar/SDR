from ai_service import AIService


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

        return self.ai.generate(prompt)