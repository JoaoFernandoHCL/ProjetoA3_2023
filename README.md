# Projeto A3

Repositório para entrega do Projeto A3 das Uc's de Inteligência Artificial, Análise de Dados e Big Data


# Entregas

### Base de dados escolhida: [Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)  
### Colunas do Dataset:

**ID da pessoa:** um identificador para cada indivíduo.  
Tipo guardado: quantitativo discreto  
  
**Gênero:** O gênero da pessoa (Masculino/Feminino).  
Tipo Guardado: qualitativo nominal  
  
**Idade:** A idade da pessoa em anos.  
Tipo Guardado: quantitativo discreto  
  
**Ocupação:** A ocupação ou profissão da pessoa.  
Tipo Guardado: qualitativo nominal  
  
**Duração do sono (horas):** O número de horas que a pessoa dorme por dia.   
Tipo Guardado: quantitativo contínuo  

**Qualidade do Sono (escala: 1-10):** Uma classificação subjetiva da qualidade do sono, variando de 1 a 10.  
Tipo Guardado: quantitativo discreto  
  
**Nível de atividade física (minutos/dia):** O número de minutos que a pessoa pratica atividade física diariamente.   
Tipo Guardado: quantitativo discreto  
  
**Nível de Estresse (escala: 1-10):** Uma classificação subjetiva do nível de estresse vivenciado pela pessoa, variando de 1 a 10.   
Tipo Guardado: quantitativo discreto  
  
**Categoria de IMC:** A categoria de IMC da pessoa (por exemplo, Abaixo do Peso, Normal, Sobrepeso).    
Tipo Guardado: qualitativo ordinal  
  
**Pressão Arterial (sistólica/diastólica):** A medição da pressão arterial da pessoa, indicada como pressão sistólica sobre pressão diastólica.   
Tipo Guardado: quantitativo discreto  
  
**Frequência cardíaca (bpm):** A frequência cardíaca em repouso da pessoa em batimentos por minuto.  
Tipo Guardado: quantitativo discreto  
  
**Passos Diários:** O número de passos que a pessoa dá por dia.  
Tipo Guardado: quantitativo discreto  
  
**Distúrbio do Sono:** A presença ou ausência de um distúrbio do sono na pessoa (Nenhum, Insônia, Apneia do Sono).  
Tipo Guardado: qualitativo nominal  

## Escolha da variável target 
**Qualidade do sono** foi escolhida como variável target devido ser um aspecto importante da saúde e do bem-estar. Uma Qualidade do sono alta indica um sono de boa qualidade, enquanto uma qualidade do sono baixa pode ter implicações para outras áreas da saúde, como o risco de doenças cardiovasculares, diabetes, obesidade, depressão, ansiedade, demência, entre outras. A qualidade do sono pode ser afetada por vários fatores, como a atividade física, o nível de estresse, o consumo de álcool, cafeína e nicotina, a exposição à luz, o horário de dormir e de acordar. 

## Para aplicar as técnicas de IA, algumas variáveis precisam ser transformadas. As variáveis que precisam ser transformadas são:  

  
**Duração do sono:** Essa variável está em formato de hora (hh:mm), mas para facilitar a análise, ela pode ser convertida em minutos ou horas decimais. Por exemplo, 7:30 pode ser convertido em 450 minutos ou 7.5 horas.
  
**IMC:** Essa variável tem alguns valores ausentes, que podem ser tratados de diferentes formas. Uma forma é excluir as observações que têm valores ausentes. Outra forma é imputar os valores ausentes com a média, a mediana ou a moda da variável. Uma terceira forma é usar um modelo de regressão para estimar os valores ausentes com base nas outras variáveis.
  
**Distúrbio do sono:** transformar essa variável em uma escala ordinal sendo 0= Nenhum, 1= Insônia, 2= Apneia do Sono  

Decidimos testar a hipótese de que a atividade física tem um efeito positivo na eficiência do sono, pois essa é uma questão relevante para a saúde do sono e o estilo de vida. A atividade física pode melhorar a qualidade do sono, reduzir o estresse, regular o ritmo circadiano, aumentar o gasto energético e promover o relaxamento muscular. A hipótese pode ser formulada da seguinte forma:
  
**H0:** A atividade física não tem efeito na eficiência do sono.  
**H1:** A atividade física tem um efeito positivo na eficiência do sono.
