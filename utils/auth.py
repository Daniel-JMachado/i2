def check_authentication(username: str, password: str, user_type: str) -> bool:
    """
    Função básica de autenticação.
    Posteriormente, deve ser substituída por uma verificação real no banco de dados.
    """
    # Autenticação temporária para teste
    if user_type == "agente":
        return username == "admin" and password == "admin"
    elif user_type == "empreendedor":
        return username == "user" and password == "user"
    return False