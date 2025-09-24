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