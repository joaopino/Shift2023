# Use Case 4.1

* Painel de Controlo para um utilizador do tipo "Produtor"

## ** Precondition** 

* O utilizador encontra-se logado
* O utilizador é do tipo "Produtor"

## ** Success Guarantee**

* O utilizador tem acesso a todas as encomendas ativas para os seus produtos

## ** Main Success Scenario**

1. O utilizado encontra-se na sua página inicial
2. O utilizador consegue observar linhas com as suas encomendas com a seguinte informação
   1. ID da encomenda
   2. Produto relacionado à encomenda
   3. Quantidade relacionada à encomenda
3. O utilizador clica na encomenda e vê um pop-up com a seguinte informação:
   1. Todos os 3 sub-pontos da alínea 2.
   2. Localização de entrega
   3. Data de Entrega máxima e horas
   4. Interação com a encomenda

## Alternative Path
4. (a) Encomenda por aceitar/recusar
   1. O utilizador tem 2 botões
      1. Aceitar em verde
      2. Recusar em vermelho
   2. O botão "Aceitar" é permido
      1. A encomenda é realizada
   3. O botão "Recusar" é permido
      1. O revendedor é notificado que o X produto foi deduzido da sua encomenda 

4. (b) A encomenda já foi aceite/recusada
   1. A encomenda foi aceite
      1. O utilizador consegue ver o estado da encomendo sendo
         1. Em curso
         2. Past due
         3. Realizada
         4. Cancelada
   2. A encomenda foi recusada
      1. O utilizador vê o estado apenas como recusada