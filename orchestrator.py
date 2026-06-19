from ai_service import AIService


class Orchestrator:
    def __init__(self):
        self.ai = AIService()

    def start_conversation(self, company_name: str, niche: str):
        prompt = f"""
Você é um SDR especializado em prospecção B2B.

Objetivo:
Marcar uma reunião.

Empresa:
{company_name}

Nicho:
{niche}

Crie uma mensagem curta, educada e personalizada.
Não pareça robótico.
Não seja insistente.
"""

        return self.ai.generate(prompt)

    def continue_conversation(
        self,
        company_name: str,
        niche: str,
        conversation_history: str,
        lead_message: str,
    ):
        prompt = f"""
Você é um SDR especializado em prospecção B2B.

Empresa:
{company_name}

Nicho:
{niche}

Histórico:
{conversation_history}

Mensagem do lead:
{lead_message}

Seu objetivo é avançar a conversa
e tentar marcar uma reunião.

Gere apenas a próxima mensagem.
"""

        return self.ai.generate(prompt)