import requests
import time

def obter_informacoes():
    url = "https://webapi.mir4global.com/nft/lists"

    querystring = {
        "listType": "sale",
        "class": "0",
        "levMin": "0",
        "levMax": "0",
        "powerMin": "0",
        "powerMax": "0",
        "priceMin": "0",
        "priceMax": "0",
        "sort": "pricelow",
        "page": "1",
        "languageCode": "pt"
    }

    headers = {
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua": '"Not A;Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "Android"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  
        data = response.json()

        if "data" in data and "lists" in data["data"] and data["data"]["lists"]:
            return data["data"]["lists"]
        else:
            print("Nenhuma informação disponível.")
            return []
    except requests.exceptions.RequestException as e:
        print("Erro ao fazer solicitação HTTP:", e)
        return []

def main():
    while True:
        print("Obtendo informações...")
        informacoes = obter_informacoes()
        if informacoes:
            print("\nInformações obtidas:")
            for item in informacoes:
                print(f"ID: {item['nftID']}, Nome do Personagem: {item['characterName']}, Nível: {item['lv']}, Pontuação de Poder: {item['powerScore']}, Preço: {item['price']}, MirageScore: {item['MirageScore']}, MiraX: {item['MiraX']}")
        print("Aguardando 1 minuto...")
        time.sleep(60)

if __name__ == "__main__":
    main()
