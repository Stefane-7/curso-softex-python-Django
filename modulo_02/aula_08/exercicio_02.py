"""2. Nível Médio: Sistema de Mídia

Crie uma classe base Midia com um construtor que recebe titulo e duracao_seg. Adicione um
método exibir() que imprime o título e a duração.

Crie duas classes filhas, Musica e Video, que herdam de Midia:

● Musica deve ter um atributo adicional artista e sobrescrever o método exibir() para
incluir o nome do artista.

● Video deve ter um atributo adicional resolucao e sobrescrever o método exibir() para
incluir a resolução.

No script principal, crie um dicionário para organizar sua coleção de mídias, usando as
chaves 'musicas' e 'videos'. Crie objetos de Musica e Video e os adicione a suas respectivas
listas dentro do dicionário. 
Por fim, itere sobre as listas e chame o método exibir() para cada item, demonstrando o polimorfismo de forma organizada."""

class Midia:
    def __init__(self, titulo, duracao_seg):
        self.titulo = titulo
        self.duracao_seg = duracao_seg

    def exibir(self):
        print(f"Titulo: {self.titulo} Duração: {self.duracao_seg} segundos")

class Musica(Midia):
    def __init__(self, titulo, duracao_seg, artista):
        super().__init__(titulo, duracao_seg)
        self.artista = artista

    def exibir(self):
        print(f"Titulo: {self.titulo} Duração: {self.duracao_seg} segundos. Artista: {self.artista}.") 

class Video(Midia):
    def __init__(self, titulo, duracao_seg, resolucao):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao

    def exibir(self):
        print(f"Titulo: {self.titulo} Duração: {self.duracao_seg} segundos. Resolução: {self.resolucao}")    

musica = Musica("mmmmm", 400, "alguém")
video = Video("AAAAAAAA", 5000, "3840x2160")

acervo = {"musicas": [musica], "video": [video]}

for i in acervo.values():
    for i in i:
        i.exibir()
