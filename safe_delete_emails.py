import imaplib

EMAIL = "silvioferro917@gmail.com"
PASSWORD = "xaxzrrduyyfpurhj"  
IMAP_SERVER = "imap.gmail.com"

mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(EMAIL, PASSWORD)

mail.select("inbox") 

result, data = mail.search(None, "ALL")
mail_ids = data[0].split()

print(f"Trovate {len(mail_ids)} email nella casella INBOX.")

# Vuoi procedere?
risposta = input("Vuoi davvero cancellarle? (S/N): ").strip().upper()

if risposta != "S":
    print("Annullato! Nessuna email è stata cancellata.")
    mail.logout()
    exit()

# Chiedi quante mail eliminare
quante = int(input(f"Quante email vuoi cancellare? (Max {len(mail_ids)}): "))
if quante > len(mail_ids):
    quante = len(mail_ids)

# Contrassegna per eliminazione solo quelle richieste
for idx, mail_id in enumerate(mail_ids):
    if idx >= quante:
        break
    mail.store(mail_id, '+FLAGS', '\\Deleted')
    print(f"[{idx+1}] Contrassegnata per l'eliminazione: {mail_id.decode()}")

# Chiedi conferma finale
risp_finale = input("Procedere con l'eliminazione definitiva? (S/N): ").strip().upper()

if risp_finale == "S":
    mail.expunge()
    print(f"{quante} email sono state eliminate definitivamente.")
else:
    print("Nessuna email è stata eliminata definitivamente.")

mail.logout()
print("Connessione chiusa.")
