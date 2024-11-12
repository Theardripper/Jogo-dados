import random

# Classe Dado
class Dado:
    def __init__(self, faces):
        self.faces = faces

    def rolar(self):
        return random.randint(1, self.faces)

# Classes de Dados específicos
class Dado4(Dado):
    def __init__(self):
        super().__init__(4)

class Dado8(Dado):
    def __init__(self):
        super().__init__(8)

class Dado10(Dado):
    def __init__(self):
        super().__init__(10)

class Dado12(Dado):
    def __init__(self):
        super().__init__(12)

# Classe Jogador
class Jogador:
    def __init__(self, nome, dado):
        self.nome = nome
        self.dado = dado
        self.pontuacao_total = 0

    def jogar_dado(self):
        return self.dado.rolar()

    def atualizar_pontuacao(self, pontos):
        self.pontuacao_total += pontos

# Classe Rodada
class Rodada:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def jogar(self):
        pontos_jogador1 = self.jogador1.jogar_dado()
        pontos_jogador2 = self.jogador2.jogar_dado()

        self.jogador1.atualizar_pontuacao(pontos_jogador1)
        self.jogador2.atualizar_pontuacao(pontos_jogador2)

        return pontos_jogador1, pontos_jogador2

# Classe Batalha
class Batalha:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.rodadas = random.randint(1, 5)  # Número de rodadas aleatório entre 1 e 5

    def iniciar(self):
        for _ in range(self.rodadas):
            rodada = Rodada(self.jogador1, self.jogador2)
            pontos_jogador1, pontos_jogador2 = rodada.jogar()
            print(f"Rodada: {self.jogador1.nome} obteve {pontos_jogador1}, {self.jogador2.nome} obteve {pontos_jogador2}")

        if self.jogador1.pontuacao_total > self.jogador2.pontuacao_total:
            vencedor = self.jogador1
        elif self.jogador2.pontuacao_total > self.jogador1.pontuacao_total:
            vencedor = self.jogador2
        else:
            vencedor = None  # Empate

        return vencedor

# Classe Torneio
class Torneio:
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.vencedor = None

    def iniciar(self):
        while len(self.jogadores) > 1:
            proxima_fase = []

            for i in range(0, len(self.jogadores), 2):
                if i + 1 < len(self.jogadores):
                    batalha = Batalha(self.jogadores[i], self.jogadores[i+1])
                    vencedor = batalha.iniciar()

                    if vencedor:
                        print(f"Vencedor da batalha entre {self.jogadores[i].nome} e {self.jogadores[i+1].nome}: {vencedor.nome}")
                        proxima_fase.append(vencedor)
                    else:
                        print(f"Empate entre {self.jogadores[i].nome} e {self.jogadores[i+1].nome}. Ambos estão eliminados.")
            self.jogadores = proxima_fase

        if len(self.jogadores) == 1:
            self.vencedor = self.jogadores[0]
            print(f"O vencedor do torneio é {self.vencedor.nome}!")
        else:
            print("O torneio terminou sem um vencedor definitivo.")

# Exemplo de uso
if __name__ == "__main__":
    # Criando jogadores com dados variados
    jogadores = [
        Jogador("Jogador 1", Dado4()),
        Jogador("Jogador 2", Dado8()),
        Jogador("Jogador 3", Dado10()),
        Jogador("Jogador 4", Dado12())
    ]

    torneio = Torneio(jogadores)
    torneio.iniciar()