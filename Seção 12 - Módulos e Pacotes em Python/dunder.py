"""
Dunder Name e Dunder Main

Dunder → Double Under

Dunder Name → __name__

Dunder Main → __main__

Em python, são utilziados dunder para criar funções, atributos/ propriedades dentre outras coisas,
utilizando Double Under para não gerar conflito com os nomes desses elementos na programação.

# Na linguagem C, temos um programa da seguinte forma:

int main(){

    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:

public static void main(Sring[] args){
}

# Em python, se executarmos um módulo Python diretamente na linha de comando, internamente o Python atribuírá
à variável __name__ o valor __main__ indicando que este é o módulo de execução principal
"""

from funcoes_com_parametro import soma_impares
import primeiro
import segundo
