# Rives Intérieures — site vitrine

Site de **Rives Intérieures**, décoration d'intérieur premium accessible sur les
deux rives du Léman (Évian · Thonon · Genève · Lausanne), par Samantha.

**Bilingue FR/EN · 32 pages · 100 % statique · zéro dépendance · zéro tracking**

## Démarrer en local

```bash
python3 -m http.server 8090
# → http://localhost:8090
```

(Le site utilise des chemins absolus `/assets/...` : servir depuis la racine du dépôt.)

## Structure

```
/                       Accueil FR          /en/           Accueil EN
/prestations/           Offre & tarifs      /en/services/
/projets/               Avant/après (6)     /en/projects/
/a-propos/              Bio & zone          /en/about/
/journal/  (+8 articles)                    /en/journal/  (+8 articles)
/contact/               WhatsApp & FAQ      /en/contact/
/mentions-legales/  /confidentialite/       /en/legal/  /en/privacy/
assets/css|js|img|fonts    docs/            tools/build_journal.py
```

## Documents clés

- **`docs/GUIDE-IMAGES.md`** — produire le portrait IA de Samantha et les
  12 images avant/après (prompts complets), puis les intégrer.
- **`docs/BRAND.md`** — positionnement, palette, typos, ton, règles.
- **`docs/CHECKLIST-LANCEMENT.md`** — tout ce qu'il reste à faire avant/après
  la mise en ligne (domaine, INPI, WhatsApp, Google Business…).

## Éléments à remplacer avant mise en ligne publique

1. Numéro WhatsApp placeholder `33600000000` (voir check-list §4)
2. Portrait + images avant/après (SVG d'attente actuellement en place)
3. Champs `[À COMPLÉTER]` des pages légales
4. Bio réelle de Samantha sur /a-propos/

## Ajouter un article au journal

Éditer `tools/build_journal.py` (liste `ARTICLES`, contenu FR + EN), puis :

```bash
python3 tools/build_journal.py
```

Les 18+ pages du journal sont régénérées avec un gabarit identique.
Ajouter ensuite l'URL au `sitemap.xml` (ou régénérer, voir git log).

## Déploiement

Prêt pour **Netlify** (`netlify.toml` : publication racine, en-têtes de sécurité,
cache long sur `/assets`). Brancher le dépôt ou glisser-déposer le dossier.
