from orchestrator import Orchestrator

orchestrator = Orchestrator()

company = input("Empresa: ")
niche = input("Nicho: ")

message = orchestrator.start_conversation(
    company_name=company,
    niche=niche,
)

print("\n=== PRIMEIRA ABORDAGEM ===\n")
print(message)