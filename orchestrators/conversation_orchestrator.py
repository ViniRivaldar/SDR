from services.ai_service import AIService


class ConversationOrchestrator:
    def __init__(self):
        self.ai = AIService()

    def continue_conversation(
        self,
        company_name: str,
        niche: str,
        conversation_history: str,
        lead_message: str,
    ):

        prompt = f"""
Você é um SDR.

Empresa:
{company_name}

Nicho:
{niche}

Histórico:
{conversation_history}

Última mensagem do lead:
{lead_message}

Objetivo:

- Continuar a conversa.
- Ser natural.
- Fazer apenas uma pergunta por vez.
- Não apresentar preço.
- Não marcar reunião imediatamente.
- Não parecer um robô.

Gere apenas a próxima mensagem.
"""

        return self.ai.generate(prompt)