# HFAU — Human Flow Analyzer Unit

Um sistema embarcado de baixo custo capaz de classificar o fluxo de pessoas em um ambiente como baixo, médio ou alto, tudo em tempo real.

## Como funciona

Dessa maneira: sensor HC-SR04 coleta leituras de distância continuamente. Esses dados alimentam um pipeline de ML rodando localmente na Raspberry Pi, onde um modelo K-means classifica o fluxo capturado em três categorias. A depender da classificação do modelo, a LED verde será acessa (fluxo baixo) ou a LED amarela (fluxo médio) ou a LED vermelha (fluxo alto).

Ademais, cada um dos 3 estados aciona de maneiras diferentes as *features* do aplicativo



**TO BE CONTINUED (NÃO ESTÁ PRONTO)**
 

