#Script de Coleta de Informações de NFTs

Este script Python coleta informações de NFTs disponíveis para venda na plataforma MIR4 Global. Ele faz isso enviando requisições periódicas a uma API e exibindo os resultados no console. Abaixo está uma explicação detalhada sobre o funcionamento do script.

#Requisitos

Python 3
Biblioteca requests
Você pode instalar a biblioteca requests usando o pip: pip install requests

#Como o Script Funciona

URL da API: O script faz uma requisição GET para https://webapi.mir4global.com/nft/lists.
Parâmetros de Consulta: Definem os critérios de busca para NFTs à venda, incluindo tipo de lista, classe, nível, poder, preço, ordenação e idioma.

Cabeçalhos: Incluem informações sobre o agente de usuário e outras configurações de segurança.
Tratamento de Exceções: Lida com erros que possam ocorrer durante a requisição HTTP.
Loop Infinito: O script entra em um loop infinito, onde ele:
Chama a função obter_informacoes para buscar os dados.
Exibe as informações dos NFTs se houver dados disponíveis.
Aguarda um minuto antes de repetir o processo.

#Notas
Certifique-se de ter uma conexão com a internet estável, pois o script depende de requisições HTTP.
Modifique os parâmetros de consulta conforme necessário para ajustar os critérios de busca de NFTs.
Este script é uma ferramenta útil para monitorar NFTs disponíveis para venda na plataforma MIR4 Global e pode ser adaptado para diferentes necessidades de monitoramento ou coleta de dados.
