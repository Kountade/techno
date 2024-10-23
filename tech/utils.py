import re

def nettoyer_html(texte):
    # Utilise une expression régulière pour supprimer toutes les balises HTML
    return re.sub(r'<[^>]*>', '', texte)