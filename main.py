from orchestrator import Orchestrator

orchestrator = Orchestrator()

company = input("Empresa: ")
niche = input("Nicho: ")

message = orchestrator.start_conversation(
    company_name=company,
    niche=niche,
)

print("\n--- PRIMEIRA MENSAGEM ---\n")
print(message)

history = ""

while True:
    lead_message = input("\nCliente: ")

    response = orchestrator.continue_conversation(
        company_name=company,
        niche=niche,
        conversation_history=history,
        lead_message=lead_message,
    )

    print("\nSDR:\n")
    print(response)

    history += f"\nLead: {lead_message}"
    history += f"\nSDR: {response}"