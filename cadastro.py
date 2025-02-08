class cadastro():
    def __init__ (self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def inputNome(self):
        self.nome = input('Digite seu nome: ')
    def inputEmail(self):
        self.email = input('Digite seu email: ')
    def inputSenha(self):
        self.senha = input('Digite sua senha: ')
    def mostrarCadastro(self):
        print(f'Nome: {self.nome}\nEmail: {self.email}\nSenha: {self.senha}')
        
print('Cadastro de Usuário')
usuario = cadastro('','','')
usuario.inputNome()
usuario.inputEmail()
usuario.inputSenha()
usuario.mostrarCadastro()


        
    