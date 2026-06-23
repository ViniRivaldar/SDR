from orchestrators.opening_orchestrator import Orchestrator

orchestrator = Orchestrator()

company = input("Empresa: ")
niche = input("Nicho: ")

strategy, message = orchestrator.start_conversation(
    company_name=company,
    niche=niche,
)

print("\n=== ESTRATÉGIA ===\n")
print(strategy)

print("\n=== PRIMEIRA ABORDAGEM ===\n")
print(message)