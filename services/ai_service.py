class AIService:
    def generate(self, prompt: str) -> str:

        if "diagnostic" in prompt:
            return "Olá! Quem normalmente responde os interessados que entram em contato pelo WhatsApp?"

        if "curiosity" in prompt:
            return "Olá! Posso te fazer uma pergunta rápida sobre o atendimento da academia?"

        if "pain" in prompt:
            return "Olá! Vocês conseguem responder todos os interessados ainda no mesmo dia?"

        if "comparison" in prompt:
            return "Olá! Hoje vocês recebem mais contatos pelo WhatsApp ou Instagram?"

        return "Olá!"