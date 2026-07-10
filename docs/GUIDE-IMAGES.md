# Guide de production des images — Rives Intérieures

Ce guide contient tout ce qu'il faut pour produire les visuels définitifs du site :
le **portrait professionnel de Samantha** (à partir de ses vraies photos) et les
**12 images avant/après** (6 projets × 2). Les prompts sont rédigés en anglais
(les modèles d'image y répondent mieux) ; les explications sont en français.

Une fois les images générées, voir la section [Intégration dans le site](#5-intégration-dans-le-site).

---

## 1. Le portrait de Samantha

### Outil recommandé

**Gemini (modèle d'édition d'images, dit « Nano Banana »)** — gemini.google.com →
mode image. C'est aujourd'hui le meilleur outil grand public pour générer un
portrait professionnel **fidèle au visage réel** à partir de photos de référence.
Alternatives : Midjourney (`--oref` / Omni-Reference), ChatGPT (édition d'images).

### Les photos de référence à fournir (3 à 5)

| Exigence | Pourquoi |
|---|---|
| Visage net, bien éclairé, sans lunettes de soleil | Le modèle doit apprendre les traits exacts |
| Au moins 1 photo de face + 1 de trois-quarts | Fidélité sous plusieurs angles |
| Lumière naturelle, pas de filtre Instagram | Éviter que le modèle apprenne un « faux » teint |
| Coiffure proche de celle souhaitée sur le portrait | Cohérence avec son apparence actuelle |
| Résolution correcte (≥ 800 px de large sur le visage) | Détails des traits |

### Le prompt principal (à coller avec les photos jointes)

```
Using the attached photos as a strict facial reference, create an
ultra-realistic professional portrait photograph of this woman.

Scene: she is an interior decorator in her bright, elegant studio near
Lake Geneva. She stands slightly angled, arms relaxed, holding a fabric
swatch book. Warm, confident, approachable smile with natural teeth.

Wardrobe: elegant cream silk blouse, fine gold jewelry, effortlessly chic.

Setting (softly blurred background): cream wall, a hint of sage-green
cabinetry, brass wall light, a large window with soft daylight suggesting
a lake view.

Photography: shot on an 85mm lens at f/2.0, professional editorial
portrait, soft golden-hour window light from the left, gentle catchlights
in the eyes, realistic skin texture with visible pores (no beauty-filter
smoothing), natural color grading, warm tones (cream, brass, soft sage).

Vertical portrait, 3:4 aspect ratio.
The face must remain perfectly faithful to the reference photos.
```

### Variantes à générer (choisir la meilleure)

- **V2 — plan plus serré :** remplacer la 2ᵉ phrase par
  `Chest-up portrait, she looks directly at the camera, hands lightly crossed.`
- **V3 — en situation :** `She is pinning fabric samples on a moodboard,
  photographed in a candid documentary style, looking at her work.`
- **V4 — extérieur lac :** `She stands on a lakeside terrace at golden hour,
  Lake Geneva softly blurred behind her, hair gently moved by the breeze.`

### Contrôle qualité avant validation

- [ ] Le visage est-il **vraiment** le sien ? (montrer à un proche sans expliquer)
- [ ] Mains : 5 doigts, pas de déformation
- [ ] Dents / yeux naturels, pas de lissage plastique
- [ ] Bijoux et boutons cohérents (les IA ratent souvent ces détails)
- [ ] Arrière-plan crédible, sans objets fondus

**Astuce :** générer 6–8 versions, en retenir 2, puis demander
`same image, subtle variation, fix the hands` pour raffiner.

### Alternative sérieuse : le vrai shooting

Budget 200–400 €, une demi-journée. Brief à donner au photographe :
lumière dorée de fin de journée, intérieur crème/sauge/laiton OU terrasse
face au lac, 85 mm, ton éditorial chaleureux (pas corporate), tenues crème/lin.
Un vrai shooting reste plus crédible à long terme (presse locale, réseaux).

---

## 2. Les avant/après — méthode générale

**Objectif :** 6 paires d'images photoréalistes, chaque paire montrant
LA MÊME pièce (même cadrage, même objectif, même heure) avant et après
transformation. C'est la cohérence du cadrage qui rend l'avant/après crédible.

### La technique en 2 étapes (Gemini / Nano Banana ou Midjourney editor)

1. **Générer l'AVANT** avec le prompt « avant » ci-dessous.
2. **Éditer cette même image** (upload de l'avant + prompt de transformation) :
   `Keep the exact same room, camera angle, lens and window position.
   Transform it as follows: …` — le modèle conserve la géométrie et ne
   change que la décoration. **Ne jamais générer l'après “from scratch”.**

### Règles de réalisme (valables pour les 12 images)

- Ajouter aux prompts « avant » : `amateur real-estate photo, slightly
  imperfect framing, mixed lighting, realistic clutter` — un avant trop
  léché n'est pas crédible.
- Ajouter aux prompts « après » : `professional interior photography,
  editorial style, soft natural light, realistic materials and shadows`.
- Format : **4:3, minimum 1600×1200 px** (le site les affiche en 4:3).
- Palette de l'après, toujours : crème chaud, bois clair, vert sauge,
  laiton, touches bleu nuit — c'est la signature visuelle du site.

---

## 3. Les 6 projets — prompts détaillés

### Projet 1 — Salon vue lac (`salon-avant.jpg` / `salon-apres.jpg`)

**AVANT :**
```
Amateur real-estate photo of a dated 1990s French living room in Évian,
France. A narrow window with heavy brown velvet curtains half-closed,
partially hiding a lake view. Bulky dark-brown leather sofa facing an old
TV cabinet, massive dark oak coffee table, worn burgundy patterned rug,
beige-grey walls, dark parquet floor, single ceiling light, slightly
crooked picture frame. Cluttered shelves, dim mixed lighting, realistic,
slightly imperfect framing. 4:3.
```
**APRÈS (édition de l'image avant) :**
```
Keep the exact same room, camera angle and window position. Renovate the
decoration only: open the window fully with sheer white curtains on a
wide brass rail revealing Lake Geneva and mountains; cream walls; light
oak floor; beige linen sofa with sage-green and brass-gold cushions;
round light-wood coffee table with brass legs; large cream wool rug;
brass globe pendant light; arc floor lamp; one large green plant; two
framed abstract artworks in sage and brass tones. Professional interior
photography, soft golden daylight from the window, editorial style. 4:3.
```

### Projet 2 — Cuisine chablaisienne (`cuisine-avant.jpg` / `cuisine-apres.jpg`)

**AVANT :**
```
Amateur photo of a dark rustic 1980s kitchen in a French village house in
Haute-Savoie. Orange-varnished oak cabinets with ornate handles, dark
laminate worktop, small beige wall tiles, old extractor hood, gingham
curtain under the sink, fluorescent tube light, linoleum floor, cluttered
worktop with old appliances. Dim, slightly green-tinted lighting,
realistic, 4:3.
```
**APRÈS :**
```
Keep the exact same kitchen layout, camera angle and window. Renovate the
decoration only: cabinet fronts repainted in sage green with brass
handles, light oak worktop, handmade off-white zellige tile splashback,
minimalist cream extractor hood, open light-wood shelves with ceramics
and a small plant, two brass cone pendant lights, herringbone light oak
floor, black gooseneck tap, tidy styled worktop. Professional interior
photography, soft morning light, editorial style. 4:3.
```

### Projet 3 — Chambre + télétravail (`chambre-avant.jpg` / `chambre-apres.jpg`)

**AVANT :**
```
Amateur photo of a cluttered French bedroom: heavy dark wooden double bed
with a dark patterned duvet, striped beige dated wallpaper, massive dark
wardrobe, improvised desk made of a folding table with an old monitor and
tangled cables, folding chair, cardboard boxes, laundry pile, thick
closed curtains, bare ceiling bulb, grey carpet. Realistic, slightly
messy, mixed lighting, 4:3.
```
**APRÈS :**
```
Keep the exact same bedroom, camera angle and window position. Transform
the decoration only: cream walls with a sage-green lower panel, light
cane-and-oak headboard, crisp cream bedding with sage throw and brass-
toned cushions, two suspended brass reading lights, light-wood
nightstands, a built-in desk niche painted deep ink blue with an oak
desktop, slim black chair and small brass task lamp, sheer curtains on a
brass rail, soft cream rug, two framed artworks. Professional interior
photography, calm morning light, editorial style. 4:3.
```

### Projet 4 — Studio home-stagé (`studio-avant.jpg` / `studio-apres.jpg`)

**AVANT :**
```
Amateur real-estate photo of a cluttered 24 m² studio apartment for sale
in Thonon, France: unmade sofa bed with mismatched blankets, drying rack
with laundry, stacked cardboard boxes, table covered with objects, broken
crooked venetian blind, bare bulb, clothes pile on the floor, dull beige
walls, old tiled floor. Realistic messy interior, harsh flash-like
lighting, 4:3.
```
**APRÈS :**
```
Keep the exact same studio, camera angle and window. Home-stage it using
mostly the same furniture: sofa neatly made into a couch with cream and
sage cushions and a folded camel throw, laundry and boxes removed, small
round dining table with two chairs and a small plant, clear floor, light
rug defining the living zone, round mirror on the wall, sheer curtain,
simple brass pendant, one tall plant in the corner. Bright, airy,
professional real-estate photography, daylight, 4:3.
```

### Projet 5 — Entrée optimisée (`entree-avant.jpg` / `entree-apres.jpg`)

**AVANT :**
```
Amateur photo of a narrow cluttered entryway in a French apartment:
overloaded coat rack with piles of coats, shoes scattered on the floor,
overflowing shoe cabinet, umbrella leaning on the wall, stack of mail on
a ledge, bare bulb, dark brown front door, dull beige walls, old beige
tiled floor. Realistic, cramped feeling, dim light, 4:3.
```
**APRÈS :**
```
Keep the exact same entryway, camera angle and front door position.
Transform it: full-height built-in storage with flush cream doors and
small brass knobs, floating light-oak bench with two sage cushions and
woven baskets underneath, a row of four brass wall hooks with one elegant
coat, large round brass-framed mirror, graphic black-and-white cement
tile floor, deep-blue graphic runner rug, round paper-and-brass pendant
light. Professional interior photography, warm welcoming light, 4:3.
```

### Projet 6 — Chalet modernisé (`chalet-avant.jpg` / `chalet-apres.jpg`)

**AVANT :**
```
Amateur photo of a dark 1980s chalet living room in the French Alps:
orange-varnished pine panelling covering walls and ceiling, tartan
upholstered sofa, heavy stone fireplace, checkered curtains on a small
window, wagon-wheel chandelier, old skis on the wall, dark wooden floor,
worn brown rug. Cozy but suffocating and dark, realistic, 4:3.
```
**APRÈS :**
```
Keep the exact same chalet room, camera angle, beams and window position.
Renovate: wall panelling painted warm cream while keeping the natural
wood ceiling and beams, wide window enlarged view of snowy Alps, black
minimalist wood-burning stove instead of the stone fireplace, off-white
linen sofa with wool bouclé throws and camel leather cushion, light oak
tree-trunk coffee table, black metal and brass pendant lights, cream wool
rug, branches in a ceramic vase. Contemporary alpine style, professional
interior photography, bright natural mountain light, 4:3.
```

---

## 4. Contrôle qualité des paires

- [ ] Même cadrage exact entre avant et après (superposer les 2 images pour vérifier)
- [ ] Fenêtres, portes, radiateurs au même endroit
- [ ] L'avant paraît « vrai » (léger désordre, lumière moyenne)
- [ ] L'après reste crédible : pas de pièce de magazine irréaliste, pas d'objets fondus
- [ ] Palette de l'après cohérente avec le site (crème/sauge/laiton/bois clair)
- [ ] Export : JPEG qualité 85, 1600×1200 minimum, poids < 400 Ko (compresser sur squoosh.app)

---

## 5. Intégration dans le site

1. Nommer les fichiers exactement :
   `portrait.jpg`, `salon-avant.jpg`, `salon-apres.jpg`, `cuisine-avant.jpg`,
   `cuisine-apres.jpg`, `chambre-avant.jpg`, `chambre-apres.jpg`,
   `studio-avant.jpg`, `studio-apres.jpg`, `entree-avant.jpg`,
   `entree-apres.jpg`, `chalet-avant.jpg`, `chalet-apres.jpg`.
2. Les déposer dans `assets/img/projets/` (portrait : `assets/img/`).
3. Remplacer les références dans les pages HTML : chaque `<img>` du site pointe
   aujourd'hui vers les `.svg` d'attente du même nom — un rechercher/remplacer
   `salon-avant.svg` → `salon-avant.jpg` (etc.) suffit. Commande :
   ```bash
   # depuis la racine du projet
   for n in salon cuisine chambre studio entree chalet; do
     grep -rl "projets/$n-" --include='*.html' . | xargs sed -i "s|projets/$n-avant.svg|projets/$n-avant.jpg|g; s|projets/$n-apres.svg|projets/$n-apres.jpg|g"
   done
   grep -rl "portrait-placeholder.svg" --include='*.html' . | xargs sed -i "s|portrait-placeholder.svg|portrait.jpg|g"
   ```
4. Vérifier l'affichage, puis committer.

*(Ou me redonner la main : j'exécute l'intégration dès que les images sont dans le dépôt.)*
