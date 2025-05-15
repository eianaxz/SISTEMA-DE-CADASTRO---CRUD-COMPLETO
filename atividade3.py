# Senha correta definida pelo sistema
senha_correta = "python123"

# Entrada inicial do usuário
senha_digitada = input("Digite a senha: ")

# Enquanto a senha estiver incorreta, continua pedindo
while senha_digitada != senha_correta:
    print("❌ Senha incorreta. Tente novamente.")
    senha_digitada = input("Digite a senha: ")

# Quando acerta, sai do laço
print("✅ Acesso permitido. Bem-vindo!")




