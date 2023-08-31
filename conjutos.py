#Ayumi Sato Brizola, Ian Gabriel Fagundes,  Letícia Izabelly Melnick Garsztka

#Enunciado
#Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de operações que serão realizadas entre dois conjuntos de dados.
#O programa que você desenvolverá irá receber como entrada um arquivo de texto (txt)
#contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão
#representadas em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas segundo a
#seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de operações que estão descritas no
#arquivo, este número de operações será um inteiro; as linhas seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha
#apresenta o código da operação (U para união, l para interseção, D para diferença e C produto cartesiano), a segunda e terceira linhas conterão
#os elementos dos conjuntos separados por virgulas.


with open("conjuntos1.txt", "r") as arquivo:
    linhas = arquivo.readlines()


uniao1 = set(linhas[1].strip().split(", "))
uniao2 = set(linhas[2].strip().split(", "))
inter1 = set(linhas[4].strip().split(", "))
inter2 = set(linhas[5].strip().split(", "))
difer1 = set(linhas[7].strip().split(", "))
difer2 = set(linhas[8].strip().split(", "))
cartesiano1 = set(linhas[10].strip().split(", "))
cartesiano2 = set(linhas[11].strip().split(", "))


interseccao = inter1 & inter2
uniao = uniao1 | uniao2
diferenca = difer1 - difer2
cartesiano = [(a, b) for a in cartesiano1 for b in cartesiano2]



print(f"União: conjunto 1 {uniao1}, conjunto 2 {uniao2}. Resultado: {uniao}")

print(f"Intersecção: conjunto 1 {inter1}, conjunto 2 {inter2}. Resultado: {interseccao}")

print(f"Diferença: conjunto 1 {difer1}, conjunto 2 {difer2}. Resultado: {diferenca}")

print(f"Produto Catesiano: conjunto 1 {cartesiano1}, conjunto 2 {cartesiano2}. Resultado: {cartesiano}")