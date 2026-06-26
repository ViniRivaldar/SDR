from services.ai_service import AIService
from prompts.opening_prompt import build_prompt
from contexts.niche_context import get_niche_context

import random


class Orchestrator:

    def __init__(self):
        self.ai = AIService()

    def start_conversation(self, company_name, niche):

        strategy = self.get_strategy()

        context = get_niche_context(niche)

        prompt = build_prompt(
            company_name=company_name,
            niche=niche,
            context=context,
            strategy=strategy,
        )

        message = self.ai.generate(prompt)

        return strategy, message

    def get_strategy(self):
        return random.choice([
            "curiosity",
            "diagnostic",
            "pain",
            "comparison"
        ])