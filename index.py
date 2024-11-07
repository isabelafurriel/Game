# Definindo a classe Heroi
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome        # guarda o nome do herói
        self.idade = idade      # guarda a idade do herói
        self.tipo = tipo        # guardao tipo do herói

    def atacar(self):
        # Definindo a mensagem de ataque com base no tipo do herói
        if self.tipo.lower() == "mago":
            ataque = "magia"
        elif self.tipo.lower() == "guerreiro":
            ataque = "espada"
        elif self.tipo.lower() == "monge":
            ataque = "artes marciais"
        elif self.tipo.lower() == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque desconhecido" 

        print(f"o {self.tipo} atacou usando {ataque}")


# Utilizando as clsses e criando instâncias da classe Heroi
heroi1 = Heroi("Gandalf", 100, "Mago")
heroi2 = Heroi("Conan", 30, "Guerreiro")
heroi3 = Heroi("Tigre", 25, "Monge")
heroi4 = Heroi("Shadow", 20, "Ninja")

# Chamando o método atacar para cada herói
# Saídas
heroi1.atacar()  
heroi2.atacar() 
heroi3.atacar()  
heroi4.atacar()  
