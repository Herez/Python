class no:
    def __init__(self, num):
        self.valor = num
        self.esquerda = None
        self.direita = None
        self.Altura = 1

class Arvore:
    def Altura(self, no):
        if no is None:
            return 0
        else:
            return no.Altura

    def Balanceado(self, no):
        if no is None:
            return 0
        else:
            return self.Altura(no.esquerda) - self.Altura(no.direita)

    def RotacaoDireita(self, no):
        #armazenando os nos em variaveis
        a = no.esquerda
        b = a.direita
        #atribuindo os nos nas novas variaveis
        a.direita = no
        no.esquerda = b
        #ajusta a nova altura do no
        no.Altura = 1 + max(self.Altura(no.esquerda), self.Altura(no.direita))
        a.Altura = 1 + max(self.Altura(a.esquerda), self.Altura(a.direita))
        return a

    def RotacaoEsquerda(self, no):
        #armazena os nos em variaveis
        a = no.direita
        b = a.esquerda
        #atribui os nos nas novas variaveis
        a.esquerda = no
        no.direita = b
        #ajusta a nova altura do no
        no.Altura = 1 + max(self.Altura(no.esquerda), self.Altura(no.direita))
        a.Altura = 1 + max(self.Altura(a.esquerda), self.Altura(a.direita))
        return a

    def Inserir(self, val, raiz):
        #Se o no for o inicial
        if raiz is None:
            return no(val)
        #Se o valor do no for menor ou igual que o valor da raiz
        elif val <= raiz.valor:
            #O no sera inserido na esquerda do no raiz
            raiz.esquerda = self.Inserir(val, raiz.esquerda)
        #Se o valor do no for maior que o valor da raiz
        elif val > raiz.valor:
            #O no sera inserido na direita do no raiz
            raiz.direita = self.Inserir(val, raiz.direita)
        #Seta uma nova altura no no (pega a maior e adiciona 1)
        raiz.Altura = 1 + max(self.Altura(raiz.esquerda), self.Altura(raiz.direita))
        #Chama a funcao Balanceado
        Balanceado = self.Balanceado(raiz)
        #Se o retorno da funcao Balanceado for maior que 1 e o valor do no esquerdo dele for maior que o no a ser inserido
        if Balanceado > 1 and raiz.esquerda.valor > val:
            #O no a ser inserido rotaciona para a direita
            return self.RotacaoDireita(raiz)
        #Se o retorno da funcao Balanceado for menor que -1 e o valor do no direito dele for menor que o no a ser inserido
        if Balanceado < -1 and val > raiz.direita.valor:
            #O no a ser inserido rotaciona para a esquerda
            return self.RotacaoEsquerda(raiz)
        #Se o retordo da funcao Balanceado for maior que 1 e o valor do no esquerdo dele for menor que a do no a ser inserido
        if Balanceado > 1 and val > raiz.esquerda.valor:
            #O no da esquerda rotaciona para a esquerda
            raiz.esquerda = self.RotacaoEsquerda(raiz.esquerda)
            #O no a ser inserido rotaciona para a esquerda
            return self.RotacaoDireita(raiz)
        #Se o retorno da funcao Balanceado for menor que -1 e o valor do no direito dele for maior que o no a ser inserido
        if Balanceado < -1 and val < raiz.direita.valor:
            #O no da direita rotaciona para a direita
            raiz.direita = self.RotacaoDireita(raiz.direita)
            #O no a ser inserido rotaciona para a esquerda
            return self.RotacaoEsquerda(raiz)
        return raiz

    def InFixa(self, raiz):
        if raiz is None:
            return
        self.InFixa(raiz.esquerda)
        print(raiz.valor)
        self.InFixa(raiz.direita)

    def PreFixa(self, raiz):

        if raiz is None:
            return
        print(raiz.valor)
        self.PreFixa(raiz.esquerda)
        self.PreFixa(raiz.direita)

    def PosFixa(self, raiz):

        if raiz is None:
            return
        self.PosFixa(raiz.esquerda)
        self.PosFixa(raiz.direita)
        print(raiz.valor)

Arvore = Arvore()

R = None
R = Arvore.Inserir(3, R)
R = Arvore.Inserir(5, R)
R = Arvore.Inserir(7, R)
R = Arvore.Inserir(2, R)
R = Arvore.Inserir(4, R)
R = Arvore.Inserir(6, R)
R = Arvore.Inserir(8, R)
R = Arvore.Inserir(10, R)

print("---Varredura InFixa---")
Arvore.InFixa(R)
print("---Varredura PreFixa")
Arvore.PreFixa(R)
print("---Varredura PosFixa")
Arvore.PosFixa(R)
print("---Altura")
print(Arvore.Altura(R))
print("---Fator Balanceamento")
print(Arvore.Balanceado(R))

