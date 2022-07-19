PROBLEMA:   Escreva instruções para exibir a moda de um determinado atributo. 

O nome do atributo (coluna) será informado pelo usuário. Utilize o seguinte rótulo : "Moda do atributo xxx = ", sendo xxx  a coluna informada.

Somente se a moda tiver dois valores deve-se exibir a mensagem "Bimodal".

[Atenção]:

mode() retorna a moda
mode().count() retorna a quantidade de elementos "da moda".
Utilize to_string(index=False)  no print para inibir a exibição dos índices do conjunto

SOLUÇÃO

import pandas as pd
pacientes = pd.read_csv("pacientes.csv", sep = ";", decimal=",")
coluna = input("Digite o título da coluna para exibir a moda:")
moda = pacientes[coluna].mode()
print("Moda do atributo ", coluna, " = ", moda.to_string(index=False))
if (moda.count() == 2):
    print("Bimodal")
