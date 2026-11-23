# Dashboard de vendas Porsche

Projeto educacional independente baseado na planilha sanitizada do curso. O visual foi inspirado na [Porsche Brasil](https://www.porsche.com/brazil/pt/); não há vínculo com a marca.

## Perguntas de negócio

1. **Quais modelos concentram mais valor?** A soma por modelo evidencia a composição do valor registrado.
2. **Onde estão os registros?** A contagem por estado mostra a distribuição geográfica da amostra.
3. **Como os clientes pagam?** A contagem por método permite comparar as formas de pagamento.

Os filtros de modelo, estado, ano do veículo, pagamento e status afetam todos os indicadores. Os rankings de modelos e estados mostram os dez maiores resultados.

## Preparação dos dados

A planilha tem 100 registros. Foram selecionados somente os campos sanitizados necessários para a análise; nomes de clientes e vendedores não foram incluídos. Ano e preço foram convertidos para números e exportados como valores, sem fórmulas. A base apresenta 24 datas de venda `INVALID`, por isso não foi usada para análise temporal. Os valores estão em dólares americanos; a soma inclui todos os status, inclusive cancelados e pendentes, e não deve ser interpretada como receita realizada. A base preparada está em `dados_sanitizados.csv`, e o próprio `index.html` contém seus dados incorporados.

## Processo e prompt

O desafio foi implementado com o Codex, usando a planilha fornecida e uma página HTML independente. Não foram utilizados Canvas nem um agente próprio com skill criada para este projeto.

Pedido inicial: criar uma dashboard HTML de arquivo único com três perguntas de negócio, indicadores, filtros e identidade visual coerente a partir da planilha sanitizada.

Refinamento: usar o site oficial da Porsche Brasil como referência visual, esclarecer a moeda e a diferença entre valores registrados e receita realizada, e manter datas inválidas fora de análises temporais.

## Executar

Abra `index.html` em um navegador. Não há dependências externas para a dashboard. Para publicar no GitHub Pages, crie um repositório público, envie `index.html`, `dados_sanitizados.csv` e este README e habilite Pages a partir da branch principal. O endereço publicado ainda não foi definido.
