banco_lista = ['samuellissandra@gmail.com', 'elissandra914@gmail.com','braca']

email_digitado = input("Digite seu email: ").strip().lower()
tem_email_banco_de_dados = email_digitado in [e.strip().lower() for e in banco_lista]

if tem_email_banco_de_dados:
    print(f"Acesso permitido! {email_digitado}")
else:
    print("Email não cadastrado.")
    cadastrar = input("Deseja cadastrar? (s/n): ").strip().lower()

    if cadastrar == "s":
        banco_lista.append(email_digitado)
        print(f"Email {email_digitado} cadastrado com sucesso!")
        print(f"Lista atualizada: {banco_lista}")
    else:
        print("Cadastro cancelado.")
        