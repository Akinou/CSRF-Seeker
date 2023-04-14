import requests
import re

# Remplacez l'URL ci-dessous par le site Web que vous souhaitez tester
url = "https://example.com"

# Obtenir le contenu de la page Web
r = requests.get(url)

# Utiliser des expressions régulières pour trouver tous les balises d'entrée avec un attribut "name"
matches = re.findall(r'<input.*?name="(.*?)".*?>', r.text)

# Parcourir chaque balise d'entrée et vérifier si elle a un attribut "value"
for match in matches:
    data = {}
    data[match] = "test_value"
    r = requests.post(url, data=data)
    
    # Vérifier si la réponse contient des erreurs liées à la protection CSRF
    if "CSRF" in r.text or "csrf" in r.text or "Cross-Site Request Forgery" in r.text:
        print("Vulnérabilité CSRF trouvée pour le champ d'entrée: " + match)
