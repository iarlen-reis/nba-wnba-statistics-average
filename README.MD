Rotowire wnba scraper (Players)

Essse é um script de scraping de dados de jogadoras de WNBA no site Rotowire. Para usar esse script, basta criar uma lista de urls de jogadoras que você deseja scrapear e passar para o script.

## Como executar o script

```bash
pip install -r requirements.txt

python3 index.py
```

## Exemplo de saída

```json
[
  {
    "name": "Aja Wilson",
    "stats": [
      {
        "name": "PTS",
        "value": "27.2"
      },
      {
        "name": "REB",
        "value": "12.0"
      },
      {
        "name": "AST",
        "value": "2.4"
      },
      {
        "name": "STL",
        "value": "1.9"
      },
      {
        "name": "BLK",
        "value": "2.9"
      }
    ]
  }
]
```

## Bibliotecas utilizadas

- BeautifulSoup4
- requests
- json

## Observações

Esse script foi desenvolvido para fins de aprendizado e não é recomendado para uso em produção. É importante lembrar que para utilizar dados de terceiros é necessário obter permissão.

## Observations

This script was developed for educational purposes and should not be used in production. It is important to remember that to use data from third parties, you need to obtain permission.
