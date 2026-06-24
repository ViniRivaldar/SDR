class AIService:
    def generate(self, prompt: str) -> str:

        if "Quem está falando" in prompt:
            return "Prazer! Meu nome é Vinicius. Posso te fazer uma pergunta rápida sobre como vocês atendem novos interessados?"

        if "Como funciona" in prompt:
            return "Antes de explicar, fiquei curioso: hoje quem normalmente responde os contatos que chegam pelo WhatsApp?"

        if "Não tenho interesse" in prompt:
            return "Sem problemas. Só por curiosidade, vocês já estão satisfeitos com o processo atual de atendimento?"

        return "Entendi. Me conta um pouco mais sobre como funciona hoje."