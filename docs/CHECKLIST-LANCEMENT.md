# Check-list de lancement — Rives Intérieures

## 1. Vérifications du nom (avant toute dépense)

- [ ] **INPI** (base marques, inpi.fr) : vérifier qu'aucune marque « Rives Intérieures »
      n'est déposée en classes 35/37/42 (déco/conseil). Dépôt conseillé : ~190 €.
- [ ] **Infogreffe / Annuaire des entreprises** : aucune société homonyme en activité déco.
- [ ] **Suisse (zefix.ch)** : pas d'homonyme gênant côté registre du commerce suisse.
- [ ] **Réseaux** : disponibilité du handle `@rives.interieures` (Instagram, Pinterest).

## 2. Domaines & e-mail

- [ ] Acheter **rives-interieures.fr** (~7 €/an, ex. OVH/Gandi) — le site est configuré
      pour `https://www.rives-interieures.fr`.
- [ ] Recommandé : **rives-interieures.ch** (~15 CHF/an) en redirection vers le .fr
      (crédibilité côté suisse).
- [ ] Créer l'adresse **contact@rives-interieures.fr** (offerte avec le domaine chez
      la plupart des registrars) et la rediriger vers la boîte de Samantha.

## 3. Statut & légal

- [ ] Immatriculation en **micro-entreprise** (choix acté) via le guichet unique :
      formalites.entreprises.gouv.fr. Activité : conseil en décoration d'intérieur
      (pas de maîtrise d'œuvre). Reporter ensuite le SIRET dans les mentions légales
      (FR + EN) — la TVA non applicable (art. 293 B) y est déjà indiquée.
- [ ] Assurance RC professionnelle (indispensable, ~150–300 €/an).
- [ ] Compléter **tous les champs `[À COMPLÉTER]`** dans `/mentions-legales/` et
      `/confidentialite/` (+ versions EN) : SIRET, adresse, nom complet, hébergeur, médiateur.
- [ ] Interventions en Suisse : se renseigner sur l'annonce des prestataires étrangers
      (procédure en ligne, gratuite, pour les prestations de service < 90 jours/an).
- [ ] CGV simples à faire relire (acompte, délais, ajustements inclus, annulation).

## 4. Contenus à remplacer dans le site

- [x] **Numéro WhatsApp** : +33 6 80 99 52 07 intégré partout dans le site
      → reste à activer **WhatsApp Business** sur ce numéro (profil avec logo,
      horaires, message d'absence, réponses rapides).
- [ ] **Portrait de Samantha** : suivre `docs/GUIDE-IMAGES.md` §1, puis intégration §5.
- [ ] **12 images avant/après** : suivre `docs/GUIDE-IMAGES.md` §2–5.
- [ ] Personnaliser la bio (`/a-propos/` et `/en/about/`) avec les vrais détails du parcours.
- [ ] Compte Instagram : créer `@rives.interieures` ou corriger le lien dans les footers.

## 5. Mise en ligne

- [ ] Hébergement : **Netlify** (gratuit, `netlify.toml` déjà prêt) — brancher le dépôt
      GitHub, dossier de publication `.` (racine). Alternatives : Vercel, OVH.
- [ ] Connecter le domaine + HTTPS automatique.
- [ ] Vérifier chaque page sur mobile après mise en ligne.

## 6. Référencement & visibilité locale (semaine 1)

- [ ] **Google Business Profile** « Rives Intérieures » (catégorie : décorateur
      d'intérieur, zone desservie : Évian, Thonon, Genève, Lausanne) — levier n° 1
      de clientèle locale.
- [ ] Google Search Console : soumettre `sitemap.xml`.
- [ ] Profils annuaires : Houzz, StarOfService (FR + CH) — cohérence nom/adresse/téléphone.
- [ ] Publier 2 des 8 articles du journal sur LinkedIn/Instagram pour amorcer.

## 7. Prospection agences (home staging)

- [ ] Lister 10 agences immobilières Évian/Thonon + 5 côté suisse.
- [ ] Leur proposer la formule Flash à conditions partenaires (volume).
- [ ] Objectif : 2 agences partenaires = flux régulier de missions courtes.

## 8. Plus tard (v2)

- [ ] Vrais projets clients → remplacer progressivement la galerie de visualisations
      (avec autorisation écrite des clients pour les photos).
- [ ] Témoignages clients réels (jamais fictifs).
- [ ] Nouveaux articles du journal : ajouter dans `tools/build_journal.py` et relancer.
- [ ] Réservation en ligne (Calendly) pour la Visite Conseil.
