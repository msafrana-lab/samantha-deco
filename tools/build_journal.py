#!/usr/bin/env python3
"""Génère les pages du Journal (FR + EN) de rives-interieures.

Usage :  python3 tools/build_journal.py
Ajouter un article : compléter ARTICLES ci-dessous puis relancer le script.
Les pages générées sont committées telles quelles (site 100 % statique).
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://www.rives-interieures.fr"

WA_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.07-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.5 0 1.47 1.07 2.9 1.22 3.1.15.2 2.1 3.2 5.1 4.49.71.3 1.27.49 1.7.63.72.23 1.37.2 1.88.12.57-.09 1.76-.72 2.01-1.42.25-.7.25-1.3.17-1.42-.07-.12-.27-.2-.57-.35M12.05 21.79h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.9-9.88a9.83 9.83 0 0 1 7 2.9 9.83 9.83 0 0 1 2.89 7c0 5.45-4.44 9.88-9.9 9.88m8.42-18.3A11.8 11.8 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.9c0 2.1.55 4.14 1.59 5.94L.06 24l6.3-1.65a11.9 11.9 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.34 11.89-11.9 0-3.18-1.24-6.16-3.47-8.4"/></svg>'

LOGO_DARK = '<svg viewBox="0 0 430 88" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M141 16 C 161 8, 181 24, 201 16 S 241 8, 261 16 S 289 22, 289 16" fill="none" stroke="#B08D57" stroke-width="2" stroke-linecap="round"/><path d="M161 25 C 177 19, 193 31, 209 25 S 241 19, 257 25" fill="none" stroke="#8A9B8E" stroke-width="1.4" stroke-linecap="round" opacity=".8"/><text x="215" y="59" text-anchor="middle" style="font-family:\'Cormorant Garamond\',serif;font-weight:600;font-size:30px;letter-spacing:6.5px;fill:#1F2A38">RIVES INTÉRIEURES</text><text x="215" y="79" text-anchor="middle" style="font-family:\'Jost\',sans-serif;font-size:9.5px;letter-spacing:4.2px;fill:#B08D57">DÉCORATION D\'INTÉRIEUR · LÉMAN</text></svg>'
LOGO_LIGHT = LOGO_DARK.replace('#1F2A38">RIVES', '#F7F4EF">RIVES').replace('stroke="#B08D57"', 'stroke="#C9A96A"').replace('fill:#B08D57', 'fill:#C9A96A')

I18N = {
    "fr": dict(
        lang="fr", other="en", locale="fr_FR",
        home="/", nav=[("/prestations/", "Prestations"), ("/projets/", "Projets"), ("/a-propos/", "À propos"), ("/journal/", "Journal"), ("/contact/", "Contact")],
        journal_href="/journal/", read="Lire l'article", back="Tout le journal",
        fin_titre="Envie d'aller plus loin que la lecture ?",
        fin_texte="Deux photos de votre pièce sur WhatsApp, et je vous donne un premier avis personnel sous 24 h ouvrées.",
        fin_btn="Écrire à Samantha", fin_presta="Voir les prestations &amp; tarifs",
        foot_desc="Décoration d'intérieur premium et accessible, sur les deux rives du Léman. Basée à Évian-les-Bains, interventions de Thonon à Lausanne.",
        foot_nav="Navigation", foot_presta="Prestations", foot_contact="Contact",
        foot_p=[("/prestations/#visite", "Visite Conseil — 240 €"), ("/prestations/#projet", "Projet Complet — dès 890 €"), ("/prestations/#staging", "Home Staging — dès 390 €")],
        legal=[("/mentions-legales/", "Mentions légales"), ("/confidentialite/", "Confidentialité")],
        copyright="© 2026 Rives Intérieures — Samantha, décoratrice d'intérieur, Évian-les-Bains.",
        other_label="English",
        j_overline="Le journal", j_h1="Idées &amp; conseils, côté Léman",
        j_lead="Des articles concrets, nourris du terrain : aménager, rénover sans travaux, valoriser un bien — avec les spécificités de notre région, du Chablais à Lausanne.",
        j_title="Journal — Idées &amp; conseils déco côté Léman | Rives Intérieures",
        j_desc="Conseils de décoration pour le bassin lémanique : vue lac, télétravail, home staging, couleurs, budget. Le journal de Rives Intérieures, décoratrice à Évian.",
        wa_aria="Écrire à Samantha sur WhatsApp",
    ),
    "en": dict(
        lang="en", other="fr", locale="en_GB",
        home="/en/", nav=[("/en/services/", "Services"), ("/en/projects/", "Projects"), ("/en/about/", "About"), ("/en/journal/", "Journal"), ("/en/contact/", "Contact")],
        journal_href="/en/journal/", read="Read the article", back="All articles",
        fin_titre="Ready to go beyond reading?",
        fin_texte="Send two photos of your room on WhatsApp and you'll get my honest first thoughts within one business day.",
        fin_btn="Message Samantha", fin_presta="See services &amp; pricing",
        foot_desc="Premium yet accessible interior design on both shores of Lake Geneva. Based in Évian-les-Bains, working from Thonon to Lausanne.",
        foot_nav="Navigation", foot_presta="Services", foot_contact="Contact",
        foot_p=[("/en/services/#visite", "Advice Visit — €240"), ("/en/services/#projet", "Full Project — from €890"), ("/en/services/#staging", "Home Staging — from €390")],
        legal=[("/en/legal/", "Legal notice"), ("/en/privacy/", "Privacy")],
        copyright="© 2026 Rives Intérieures — Samantha, interior decorator, Évian-les-Bains, France.",
        other_label="Français",
        j_overline="The journal", j_h1="Ideas &amp; advice, Lake Geneva style",
        j_lead="Hands-on articles rooted in local experience: layouts, no-renovation makeovers, preparing a property for sale — with the specifics of our region, from the Chablais to Lausanne.",
        j_title="Journal — Interior design ideas for Lake Geneva | Rives Intérieures",
        j_desc="Interior design advice for the Lake Geneva basin: lake views, home offices, home staging, colour palettes, budgets. By Rives Intérieures, decorator in Évian.",
        wa_aria="Message Samantha on WhatsApp",
    ),
}

# ---------------------------------------------------------------- articles --
ARTICLES = [
dict(
  slug_fr="reveler-la-vue-lac", slug_en="reveal-the-lake-view",
  cat_fr="Aménagement", cat_en="Layout",
  img="/assets/img/projets/salon-apres.svg",
  title_fr="Appartement au bord du Léman : révéler (enfin) la vue lac",
  title_en="Living by Lake Geneva: how to (finally) reveal the view",
  desc_fr="La vue est votre plus belle pièce de mobilier. Cinq principes concrets pour la mettre en majesté dans un salon du bord du Léman.",
  desc_en="The view is your finest piece of furniture. Five practical principles to give it centre stage in a Lake Geneva living room.",
  lead_fr="Des appartements avec vue lac qui vivent rideaux tirés, j'en visite toutes les semaines. C'est le paradoxe régional par excellence : on paie la vue au prix fort, puis on installe le salon comme si elle n'existait pas.",
  lead_en="Every week I walk into lake-view apartments that live with their curtains drawn. It is the great regional paradox: people pay a premium for the view, then arrange the living room as if it did not exist.",
  body_fr="""
<h2>1. Orientez les assises vers la lumière, pas vers l'écran</h2>
<p>Dans la plupart des salons que je visite, le canapé fait face au téléviseur et tourne le dos à la baie. Première décision, la plus rentable : pivoter le plan. Le canapé perpendiculaire à la fenêtre, un fauteuil qui regarde le lac, et l'écran sur le mur secondaire. On ne renonce pas à la télévision — on cesse simplement de lui offrir la place d'honneur.</p>
<h2>2. Déshabillez la fenêtre</h2>
<p>Les doubles rideaux épais, hérités d'une époque où le vitrage isolait mal, mangent 20 à 30 cm de vue de chaque côté. Remplacez-les par un voilage qui filtre sans obstruer, posé sur une tringle qui déborde largement du cadre : ouverts, les rideaux libèrent la totalité du vitrage.</p>
<blockquote>La règle que je donne à mes clients : depuis le canapé, on doit voir l'eau — pas le tissu.</blockquote>
<h2>3. Travaillez en teintes minérales</h2>
<p>Le Léman impose sa palette : gris bleutés le matin, acier à midi, presque doré au couchant. Les murs qui l'encadrent doivent l'accompagner, pas rivaliser. Crème chaud, grège, sauge très doux — et les teintes vives en petites touches (coussins, céramiques) qu'on peut déplacer au fil des saisons.</p>
<h2>4. Méfiez-vous des meubles hauts près de la baie</h2>
<p>Une bibliothèque ou un buffet haut à moins d'un mètre de la fenêtre crée un tunnel visuel. La zone qui borde la baie doit rester basse : enfilade, banc, ou rien du tout. La vue a besoin d'une piste d'atterrissage.</p>
<h2>5. Le miroir, votre deuxième fenêtre</h2>
<p>Placé sur le mur perpendiculaire à la baie, un grand miroir attrape le lac et le renvoie dans la pièce. Effet garanti dans les séjours en profondeur, où le fond de pièce ne voit jamais l'eau. C'est l'astuce la moins chère de cette liste — et souvent la plus spectaculaire.</p>
<h2>Et concrètement ?</h2>
<p>Ces cinq principes forment la colonne vertébrale de la plupart de mes projets « vue lac ». La difficulté n'est pas de les connaître, c'est de les appliquer à VOS volumes : où pivoter le canapé quand le radiateur bloque le mur idéal, comment habiller une baie de 4 mètres sans budget pharaonique. C'est exactement ce qu'on résout en <a href="/prestations/#visite">Visite Conseil</a> — deux heures chez vous, et le plan d'action est posé.</p>
""",
  body_en="""
<h2>1. Point the seating at the light, not the screen</h2>
<p>In most living rooms I visit, the sofa faces the television and turns its back on the window. The first and most profitable decision: rotate the plan. Sofa perpendicular to the glazing, one armchair looking at the lake, the screen on a secondary wall. You are not giving up television — you are simply no longer giving it the best seat in the house.</p>
<h2>2. Undress the window</h2>
<p>Heavy double curtains, inherited from the days of poor glazing, eat 20 to 30 cm of view on each side. Replace them with a sheer that filters without blocking, hung on a rail that extends well beyond the frame: once open, the curtains free the entire pane.</p>
<blockquote>The rule I give my clients: from the sofa, you should see water — not fabric.</blockquote>
<h2>3. Work with mineral tones</h2>
<p>Lake Geneva dictates its own palette: blue-greys in the morning, steel at noon, almost golden at sunset. The walls framing it should accompany it, not compete. Warm cream, greige, the softest sage — and bright colours in small, movable touches such as cushions and ceramics.</p>
<h2>4. Beware of tall furniture near the glazing</h2>
<p>A bookcase or tall sideboard within a metre of the window creates a visual tunnel. The zone along the glazing should stay low: a low sideboard, a bench, or nothing at all. A view needs a landing strip.</p>
<h2>5. The mirror: your second window</h2>
<p>Placed on the wall perpendicular to the glazing, a large mirror catches the lake and throws it back into the room. It works wonders in deep living rooms whose far end never sees the water. The cheapest trick on this list — and often the most spectacular.</p>
<h2>Putting it into practice</h2>
<p>These five principles are the backbone of most of my lake-view projects. The difficulty is not knowing them — it is applying them to <em>your</em> volumes: where to rotate the sofa when a radiator blocks the ideal wall, how to dress a four-metre window without a monumental budget. That is precisely what an <a href="/en/services/#visite">Advice Visit</a> solves: two hours at your home, and the action plan is set.</p>
""",
),
dict(
  slug_fr="home-staging-vendre-plus-vite", slug_en="home-staging-sell-faster",
  cat_fr="Home staging", cat_en="Home staging",
  img="/assets/img/projets/studio-apres.svg",
  title_fr="Vendre à Thonon ou Évian : ce que le home staging change vraiment",
  title_en="Selling around Thonon or Évian: what home staging really changes",
  desc_fr="Des visites qui s'enchaînent aux offres qui montent : le mécanisme réel du home staging, sans promesses magiques ni pourcentages fantaisistes.",
  desc_en="From busier viewings to better offers: how home staging actually works, without magic promises or fanciful percentages.",
  lead_fr="Le home staging souffre de ses vendeurs de rêve : « +15 % sur le prix de vente ! », « vendu en 48 h ! ». La réalité est plus sobre — et bien plus intéressante pour qui vend un bien dans la région.",
  lead_en="Home staging suffers from its own hype: “+15% on the sale price!”, “sold in 48 hours!”. The reality is more sober — and far more interesting if you are selling in this region.",
  body_fr="""
<h2>Ce que le home staging fait vraiment</h2>
<p>Il ne transforme pas un bien surestimé en bonne affaire. Il fait trois choses, toutes mesurables :</p>
<ul>
<li><strong>Il élargit l'entonnoir.</strong> Sur les portails d'annonces, la photo décide en une seconde. Un bien désencombré, lumineux et lisible génère plus de clics, donc plus de visites, donc plus de chances de rencontrer « son » acheteur.</li>
<li><strong>Il neutralise les objections.</strong> Un séjour trop meublé paraît petit ; une chambre-bureau-débarras n'a pas de fonction claire ; une déco très typée oblige l'acheteur à « défaire » mentalement. Chaque objection levée, c'est un argument de négociation en moins.</li>
<li><strong>Il raccourcit le délai.</strong> Et dans une vente, le temps, c'est de l'argent : chaque mois de délai supplémentaire, ce sont des charges, des intérêts, et la tentation croissante de baisser le prix.</li>
</ul>
<h2>La spécificité lémanique</h2>
<p>Notre marché a une particularité : une partie des acheteurs vient de loin — frontaliers qui se rapprochent de Genève, familles suisses cherchant le prix français, néo-arrivants. Ces acheteurs visitent peu et vite, souvent sur un week-end. Ils n'ont ni le temps ni l'envie de « se projeter avec des travaux » : le bien doit être lisible immédiatement. C'est exactement le travail du home staging.</p>
<blockquote>Un acheteur local pardonne le bazar, il connaît le quartier. Un acheteur qui a fait deux heures de route juge tout, tout de suite.</blockquote>
<h2>Avec l'existant d'abord</h2>
<p>Le home staging tel que je le pratique commence par soustraire, pas par acheter : désencombrer radicalement, dépersonnaliser sans stériliser, réagencer avec le mobilier en place, soigner la lumière de chaque pièce. La location de mobilier n'intervient qu'en dernier recours — un logement vide, en revanche, mérite presque toujours quelques pièces clés : les volumes nus semblent paradoxalement plus petits.</p>
<h2>Combien ça coûte, combien ça rapporte</h2>
<p>Ma <a href="/prestations/#staging">formule Flash à 390 €</a> livre un diagnostic priorisé et un plan d'action que vous exécutez vous-même ; la <a href="/prestations/#staging">formule Complète dès 990 €</a> ajoute une journée de mise en œuvre. À l'échelle d'un bien à 350 000 € ou 500 000 €, l'enjeu n'est pas le coût de la prestation : c'est le mois de mise en vente gagné et la marge de négociation préservée. Je laisse les pourcentages spectaculaires aux plaquettes commerciales — les agences avec qui je travaille, elles, comptent en visites et en délais.</p>
""",
  body_en="""
<h2>What home staging actually does</h2>
<p>It does not turn an overpriced property into a bargain. It does three things, all measurable:</p>
<ul>
<li><strong>It widens the funnel.</strong> On listing portals, the photo decides within a second. A decluttered, luminous, legible home generates more clicks, therefore more viewings, therefore more chances of meeting <em>the</em> buyer.</li>
<li><strong>It neutralises objections.</strong> An overfurnished living room reads as small; a bedroom-office-storage room has no clear function; a highly personal décor forces buyers to mentally “undo” it. Every objection removed is one negotiation argument fewer.</li>
<li><strong>It shortens the timeline.</strong> And in a sale, time is money: every extra month means charges, interest, and the growing temptation to drop the price.</li>
</ul>
<h2>The Lake Geneva specificity</h2>
<p>Our market has a particularity: many buyers come from afar — cross-border workers moving closer to Geneva, Swiss families seeking French prices, newcomers to the region. They view few properties, quickly, often in a single weekend. They have neither the time nor the inclination to “imagine it after works”: the home must be legible instantly. That is precisely the job of home staging.</p>
<blockquote>A local buyer forgives clutter — they know the neighbourhood. A buyer who has driven two hours judges everything, immediately.</blockquote>
<h2>Start with what is already there</h2>
<p>Home staging as I practise it begins by subtracting, not buying: radical decluttering, depersonalising without sterilising, rearranging the existing furniture, working the light in every room. Furniture rental is a last resort — though an empty property almost always deserves a few key pieces: bare volumes paradoxically look smaller.</p>
<h2>What it costs, what it returns</h2>
<p>My <a href="/en/services/#staging">Flash package at €390</a> delivers a prioritised diagnosis and an action plan you execute yourself; the <a href="/en/services/#staging">Full package from €990</a> adds a day of hands-on implementation. Against a €350,000 or €500,000 property, the stake is not the fee: it is the month of marketing time saved and the negotiation margin preserved. I leave the spectacular percentages to sales brochures — the agencies I work with count in viewings and in weeks.</p>
""",
),
dict(
  slug_fr="coin-teletravail-chambre", slug_en="home-office-in-the-bedroom",
  cat_fr="Télétravail", cat_en="Home office",
  img="/assets/img/projets/chambre-apres.svg",
  title_fr="Télétravail frontalier : un vrai bureau dans la chambre, sans sacrifier le sommeil",
  title_en="Working from home: a real desk in the bedroom without sacrificing sleep",
  desc_fr="Deux jours de télétravail par semaine et pas de pièce en plus : comment intégrer un poste de travail digne de ce nom dans la chambre — et l'oublier le soir.",
  desc_en="Two remote days a week and no spare room: how to fit a proper workstation into the bedroom — and forget it at night.",
  lead_fr="C'est LA demande qui a explosé dans la région : les frontaliers télétravaillent désormais une partie de la semaine, et la table pliante calée entre le lit et l'armoire a fait son temps.",
  lead_en="It is THE request that has soared in this region: cross-border workers now work from home part of the week, and the folding table wedged between bed and wardrobe has had its day.",
  body_fr="""
<h2>Le vrai problème n'est pas la place, c'est la frontière</h2>
<p>Un bureau dans la chambre pose une question de territoire : comment empêcher le travail de coloniser le sommeil ? Les études sur le sujet convergent — un espace de travail visible depuis le lit dégrade l'endormissement. La réponse n'est pas de renoncer, c'est de <strong>marquer la frontière</strong>.</p>
<h2>Trois dispositifs qui fonctionnent</h2>
<h3>La niche assumée</h3>
<p>Plutôt que de fondre le bureau dans le décor, on lui donne un écrin : un pan de mur peint dans une teinte profonde (encre, vert forêt), une tablette toute largeur, deux étagères. Le soir, un rideau ou un paravent referme la parenthèse. Le contraste chromatique dit au cerveau : ici, c'est un autre lieu.</p>
<h3>Le bureau-armoire</h3>
<p>Les « cloffices » bien conçus se referment complètement : portes closes, le travail disparaît, littéralement. Solution idéale dans les chambres de moins de 14 m², à condition de câbler proprement l'intérieur (multiprise fixée, passe-câbles) pour que la fermeture ne soit pas un rituel pénible.</p>
<h3>La tête de lit épaissie</h3>
<p>Dans les chambres en longueur, une tête de lit-cloison de 35 cm d'épaisseur cache un plan de travail dans son dos. On dort d'un côté, on travaille de l'autre — et depuis l'oreiller, l'écran n'existe pas.</p>
<blockquote>Le test infaillible : allongé dans le lit, si vous voyez l'écran, la frontière n'existe pas encore.</blockquote>
<h2>Les détails qui changent tout</h2>
<ul>
<li><strong>La chaise :</strong> une vraie assise de travail n'est pas négociable, mais elle peut être belle — le marché regorge de fauteuils ergonomiques qui n'ont plus rien de bureautique.</li>
<li><strong>La lumière :</strong> une lampe de tâche orientable à 4000 K pour travailler, des ampoules chaudes à 2700 K partout ailleurs. Deux mondes lumineux, une seule pièce.</li>
<li><strong>Le fond de visio :</strong> pensez-y dès la conception — un pan de mur soigné derrière le fauteuil vaut tous les arrière-plans flous.</li>
</ul>
<p>Ce projet est l'un de mes classiques en <a href="/prestations/#projet">Projet Complet</a> : c'est typiquement le cas où la visualisation préalable évite l'erreur coûteuse — on voit tout de suite si la niche écrase la pièce ou si elle l'organise.</p>
""",
  body_en="""
<h2>The real problem is not space — it is the boundary</h2>
<p>A desk in the bedroom raises a question of territory: how do you stop work from colonising sleep? Research converges on this — a workstation visible from the bed degrades sleep onset. The answer is not to give up; it is to <strong>mark the boundary</strong>.</p>
<h2>Three set-ups that work</h2>
<h3>The assumed niche</h3>
<p>Rather than blending the desk into the décor, give it a stage: one wall section painted in a deep tone (ink blue, forest green), a full-width worktop, two shelves. In the evening, a curtain or screen closes the parenthesis. The colour contrast tells the brain: this is another place.</p>
<h3>The closet office</h3>
<p>A well-designed “cloffice” closes completely: doors shut, work literally disappears. Ideal in bedrooms under 14 m², provided the inside is properly wired (fixed power strip, cable grommets) so that closing it is not a nightly chore.</p>
<h3>The thickened headboard</h3>
<p>In elongated bedrooms, a 35 cm-deep partition headboard hides a worktop on its back. You sleep on one side, work on the other — and from the pillow, the screen does not exist.</p>
<blockquote>The infallible test: lying in bed, if you can see the screen, the boundary does not yet exist.</blockquote>
<h2>The details that change everything</h2>
<ul>
<li><strong>The chair:</strong> a genuine task chair is non-negotiable, but it can be beautiful — the market is full of ergonomic armchairs with nothing “office” about them.</li>
<li><strong>The light:</strong> an adjustable 4000 K task lamp for work, warm 2700 K bulbs everywhere else. Two lighting worlds, one room.</li>
<li><strong>The video-call backdrop:</strong> plan it from the start — one well-styled wall behind the chair beats any blurred background.</li>
</ul>
<p>This project is one of my classics as a <a href="/en/services/#projet">Full Project</a>: it is exactly the case where visualising beforehand avoids the costly mistake — you see at once whether the niche crushes the room or organises it.</p>
""",
),
dict(
  slug_fr="relooker-sans-travaux", slug_en="restyle-without-renovation",
  cat_fr="Relooking", cat_en="Makeover",
  img="/assets/img/projets/cuisine-apres.svg",
  title_fr="Relooker sans travaux : ce que la peinture, la lumière et le textile savent faire",
  title_en="A makeover without building work: what paint, light and textiles can do",
  desc_fr="Pas de démolition, pas de poussière, pas de permis : trois leviers qui transforment une pièce en profondeur — et dans quel ordre les actionner.",
  desc_en="No demolition, no dust, no permits: three levers that transform a room in depth — and the order in which to pull them.",
  lead_fr="« On pensait devoir tout casser. » C'est la phrase que j'entends le plus souvent en fin de projet. La vérité du métier : la plupart des pièces tristes ne souffrent pas de leurs murs, mais de ce qu'on a posé dessus et devant.",
  lead_en="“We thought we would have to gut everything.” It is the sentence I hear most often at the end of a project. The trade's truth: most sad rooms do not suffer from their walls, but from what has been put on and in front of them.",
  body_fr="""
<h2>Levier n° 1 : la peinture, mais stratégique</h2>
<p>Repeindre en blanc n'est pas un projet, c'est un réflexe. La peinture devient un levier quand elle est stratégique : un soubassement qui rehausse les plafonds, une teinte profonde qui donne un fond aux meubles clairs, des boiseries et cadres de portes traités en contraste. Dans une cuisine, repeindre les façades (avec la bonne préparation et la bonne laque) change davantage la pièce que remplacer les meubles — pour un dixième du prix.</p>
<h2>Levier n° 2 : la lumière, le levier le plus sous-estimé</h2>
<p>Le plafonnier unique au centre de la pièce est le meilleur allié de la tristesse. La règle des trois sources change tout : une lumière d'ambiance (indirecte, chaude), une lumière de tâche (liseuse, plan de travail), une lumière d'accent (qui caresse un mur, une œuvre, une matière). Comptez le nombre de sources dans une chambre d'hôtel qui vous a plu : rarement moins de cinq.</p>
<blockquote>On ne voit jamais la lumière — on ne voit que ce qu'elle veut bien montrer.</blockquote>
<h2>Levier n° 3 : le textile, l'acoustique et la chaleur</h2>
<p>Un salon « froid » l'est souvent au sens propre : trop de surfaces dures qui renvoient le son et la lumière. Rideaux toute hauteur, tapis généreux (l'erreur classique : trop petit — les pieds avant du canapé doivent être dessus), coussins et plaids en matières naturelles. Le textile est ce qui sépare une pièce meublée d'une pièce habitée.</p>
<h2>Dans quel ordre ?</h2>
<ul>
<li><strong>D'abord soustraire.</strong> Avant d'ajouter quoi que ce soit, retirer ce qui encombre. C'est gratuit et ça remet les volumes à zéro.</li>
<li><strong>Ensuite la peinture</strong> — elle définit le décor dans lequel tout le reste s'inscrit.</li>
<li><strong>Puis la lumière</strong>, pensée pièce par pièce, usage par usage.</li>
<li><strong>Enfin le textile et les accessoires</strong>, qui signent l'ambiance.</li>
</ul>
<p>Budget indicatif pour un salon complet ainsi traité : souvent moins que le prix d'un canapé de milieu de gamme. C'est tout l'esprit de mes <a href="/prestations/">formules</a> : le maximum d'effet par euro engagé, et zéro dépense avant d'avoir vu le résultat en visualisation.</p>
""",
  body_en="""
<h2>Lever 1: paint — but strategic paint</h2>
<p>Repainting everything white is not a project, it is a reflex. Paint becomes a lever when it is strategic: a painted lower wall that visually lifts the ceiling, a deep tone that gives light furniture a backdrop, woodwork and door frames treated in contrast. In a kitchen, repainting the fronts (with proper preparation and the right lacquer) changes the room more than replacing the units — at a tenth of the price.</p>
<h2>Lever 2: light, the most underrated lever</h2>
<p>The single ceiling light in the middle of the room is sadness's best friend. The three-source rule changes everything: ambient light (indirect, warm), task light (reading lamp, worktop), accent light (grazing a wall, a picture, a texture). Count the light sources in a hotel room you loved: rarely fewer than five.</p>
<blockquote>You never see light itself — only what it chooses to show you.</blockquote>
<h2>Lever 3: textiles — acoustics and warmth</h2>
<p>A “cold” living room is often literally cold: too many hard surfaces bouncing sound and light. Full-height curtains, a generous rug (the classic mistake: too small — the sofa's front feet must sit on it), cushions and throws in natural fibres. Textile is what separates a furnished room from an inhabited one.</p>
<h2>In what order?</h2>
<ul>
<li><strong>Subtract first.</strong> Before adding anything, remove what clutters. It is free, and it resets the volumes.</li>
<li><strong>Then paint</strong> — it defines the stage on which everything else sits.</li>
<li><strong>Then light</strong>, designed room by room, use by use.</li>
<li><strong>Finally textiles and accessories</strong>, which sign the atmosphere.</li>
</ul>
<p>Indicative budget for a full living room treated this way: often less than a mid-range sofa. That is the whole spirit of my <a href="/en/services/">services</a>: maximum effect per euro spent, and no spending at all before you have seen the result visualised.</p>
""",
),
dict(
  slug_fr="esprit-chalet-contemporain", slug_en="modern-chalet-spirit",
  cat_fr="Esprit alpin", cat_en="Alpine spirit",
  img="/assets/img/projets/chalet-apres.svg",
  title_fr="Moderniser un chalet sans le trahir",
  title_en="Modernising a chalet without betraying it",
  desc_fr="Entre le tout-lambris qui étouffe et le blanc clinique qui efface : la voie du chalet alpin contemporain, expliquée choix par choix.",
  desc_en="Between all-over timber that suffocates and clinical white that erases: the contemporary alpine path, explained choice by choice.",
  lead_fr="Des hauteurs de Thonon à la vallée d'Abondance, le parc de chalets des années 70-90 pose la même question : comment sortir de la pénombre boisée sans transformer un chalet en appartement de ville ?",
  lead_en="From the heights above Thonon to the Abondance valley, the 1970s-90s chalet stock poses the same question: how do you escape the timbered gloom without turning a chalet into a city flat?",
  body_fr="""
<h2>Le diagnostic : pourquoi un chalet paraît sombre</h2>
<p>Ce n'est pas (seulement) une affaire de petites fenêtres. Le bois vernis orangé absorbe une part importante de la lumière et la teinte de ce qu'il en rend. Sol, murs et plafond dans le même bois : l'œil ne trouve aucun repère de luminosité, et la pièce entière semble fermer les yeux.</p>
<h2>La règle du tiers conservé</h2>
<p>Ma méthode sur ces projets : conserver le bois là où il a le plus de valeur — au plafond, avec ses poutres, là où il raconte l'architecture — et libérer les murs, peints dans un blanc chaud légèrement crémeux. Le sol suit en bois clair naturel, mat. Un tiers de bois assumé, deux tiers de respiration : l'âme reste, l'étouffement part.</p>
<blockquote>Un chalet réussi, c'est celui où l'on sent la montagne sans avoir besoin de la mimer.</blockquote>
<h2>Les matières qui remplacent le folklore</h2>
<p>Exit les rideaux à carreaux et les skis croisés au mur. L'esprit alpin contemporain passe par les matières, pas par les symboles : laine bouclée, lin lavé, pierre locale, cuir patiné, céramique artisanale. Un poêle contemporain — noir graphite, ligne simple — réchauffe davantage l'ambiance que n'importe quelle panoplie décorative.</p>
<h2>La lumière d'altitude</h2>
<p>En montagne, la lumière naturelle est violente à midi, très faible en fin de journée. D'où l'importance des éclairages en couches basses : appliques qui lèchent les murs, lampes posées, guirlande de braises dans l'âtre du poêle. Le soir, un chalet doit s'éclairer comme un refuge — par îlots chauds, jamais par plafond inondé.</p>
<h2>Ce qu'on ne touche pas</h2>
<ul>
<li>Les poutres structurelles et leur patine — irremplaçables ;</li>
<li>Les planchers massifs qui peuvent être poncés et huilés clair ;</li>
<li>Tout ce qui porte l'histoire du lieu : une porte ancienne, une niche, un linteau gravé.</li>
</ul>
<p>Moderniser un chalet est un exercice d'équilibriste — c'est précisément le genre de projet où mes <a href="/prestations/#projet">visualisations préalables</a> rassurent : on voit le chalet transformé avant le premier coup de pinceau, et on garde la main sur le curseur « caractère ».</p>
""",
  body_en="""
<h2>The diagnosis: why a chalet feels dark</h2>
<p>It is not (only) a matter of small windows. Orange-varnished timber absorbs a large share of the light and tints whatever it returns. Floor, walls and ceiling in the same wood: the eye finds no luminosity reference, and the whole room seems to close its eyes.</p>
<h2>The one-third rule</h2>
<p>My method on these projects: keep the timber where it carries most value — on the ceiling, with its beams, where it tells the architecture's story — and free the walls, painted in a warm, slightly creamy white. The floor follows in pale, matt natural wood. One third of assumed timber, two thirds of breathing space: the soul stays, the suffocation goes.</p>
<blockquote>A successful chalet is one where you feel the mountain without needing to mimic it.</blockquote>
<h2>Materials instead of folklore</h2>
<p>Out with the checked curtains and crossed skis on the wall. Contemporary alpine spirit works through materials, not symbols: bouclé wool, washed linen, local stone, patinated leather, artisan ceramics. A contemporary stove — graphite black, simple lines — warms the atmosphere more than any decorative panoply.</p>
<h2>Altitude light</h2>
<p>In the mountains, natural light is harsh at noon and very weak by late afternoon. Hence the importance of low, layered lighting: wall lights grazing the surfaces, table lamps, the ember glow of the stove. In the evening, a chalet should light up like a refuge — in warm islands, never under a flooded ceiling.</p>
<h2>What we never touch</h2>
<ul>
<li>Structural beams and their patina — irreplaceable;</li>
<li>Solid floors, which can be sanded and oiled pale;</li>
<li>Anything carrying the history of the place: an old door, a niche, a carved lintel.</li>
</ul>
<p>Modernising a chalet is a balancing act — exactly the kind of project where my <a href="/en/services/#projet">advance visualisations</a> reassure: you see the transformed chalet before the first brushstroke, and you keep your hand on the “character” dial.</p>
""",
),
dict(
  slug_fr="entree-premiere-impression", slug_en="entryway-first-impression",
  cat_fr="Petits espaces", cat_en="Small spaces",
  img="/assets/img/projets/entree-apres.svg",
  title_fr="L'entrée, la pièce qu'on oublie (et que tout le monde voit en premier)",
  title_en="The entryway: the room everyone forgets (and everyone sees first)",
  desc_fr="Six mètres carrés qui décident de la première impression : méthode complète pour une entrée belle ET fonctionnelle, même étroite.",
  desc_en="Six square metres that decide the first impression: a complete method for an entryway both beautiful AND functional, even a narrow one.",
  lead_fr="On soigne le salon pour les invités et la cuisine pour soi — et on laisse l'entrée se débrouiller avec les manteaux de toute la famille. Pourtant, c'est elle qui donne le ton, deux fois par jour, à ceux qui vivent là.",
  lead_en="We polish the living room for guests and the kitchen for ourselves — and leave the entryway to cope with the whole family's coats. Yet it sets the tone, twice a day, for the people who live there.",
  body_fr="""
<h2>Commencer par l'inventaire, pas par Pinterest</h2>
<p>Une entrée échoue quand elle est dimensionnée pour une famille imaginaire. Avant tout choix esthétique, comptez : combien de manteaux par saison ? De paires de chaussures en rotation ? Casques, sacs d'école, laisse du chien, courrier ? L'entrée est un problème de flux avant d'être un problème de style — la déco vient récompenser la logistique résolue.</p>
<h2>La hiérarchie du rangement</h2>
<ul>
<li><strong>Fermé pour le volume :</strong> une armoire toute hauteur, portes affleurantes, peinte comme le mur — elle avale 80 % du chaos et disparaît visuellement.</li>
<li><strong>Ouvert pour le quotidien :</strong> quatre à six patères (pas plus !) pour les manteaux du jour, un banc pour se chausser, un vide-poche pour les clés.</li>
<li><strong>Caché pour les chaussures :</strong> les meubles à abattant minces (15 cm) rentrent dans presque tous les couloirs.</li>
</ul>
<blockquote>La règle d'or : ce qui sert tous les jours à portée de main, tout le reste derrière une porte.</blockquote>
<h2>Les trois gestes déco qui paient</h2>
<h3>Le sol assume</h3>
<p>C'est LA pièce où le sol graphique se justifie : carreaux à motifs ou tapis à dessin fort. Petite surface, coût contenu, effet immédiat — et les traces de pas s'y voient moins que sur un sol uni clair.</p>
<h3>Le miroir travaille double</h3>
<p>Vérification avant de sortir + lumière doublée + profondeur visuelle. Grand, rond de préférence dans les entrées anguleuses, face ou perpendiculaire à la source de lumière.</p>
<h3>La lumière accueille</h3>
<p>Une suspension à hauteur généreuse (2,10 m sous le point bas) en ambiance chaude, plutôt qu'un spot blafard. L'entrée est le sas de décompression entre le dehors et le dedans : sa lumière doit dire « bienvenue », pas « contrôle d'identité ».</p>
<h2>Le budget réaliste</h2>
<p>Une entrée complète ainsi traitée — rangement sur mesure ou semi-mesure, banc, patères, miroir, luminaire, sol ou tapis — se joue le plus souvent entre 1 500 et 4 000 € selon le niveau de sur-mesure. Rapporté au nombre de passages quotidiens, c'est probablement l'investissement déco le plus rentable de la maison. C'est aussi un format parfait pour découvrir ma façon de travailler en <a href="/prestations/#projet">Projet Complet</a>.</p>
""",
  body_en="""
<h2>Start with the inventory, not with Pinterest</h2>
<p>An entryway fails when it is sized for an imaginary family. Before any aesthetic choice, count: how many coats per season? Pairs of shoes in rotation? Helmets, school bags, the dog's lead, the post? An entryway is a flow problem before it is a style problem — décor comes as the reward for solved logistics.</p>
<h2>The storage hierarchy</h2>
<ul>
<li><strong>Closed for volume:</strong> a full-height cupboard, flush doors, painted like the wall — it swallows 80% of the chaos and visually disappears.</li>
<li><strong>Open for the everyday:</strong> four to six hooks (no more!) for today's coats, a bench for shoes, a tray for keys.</li>
<li><strong>Hidden for shoes:</strong> slim tilt-out cabinets (15 cm deep) fit almost any hallway.</li>
</ul>
<blockquote>The golden rule: what serves daily within arm's reach; everything else behind a door.</blockquote>
<h2>The three décor moves that pay</h2>
<h3>The floor makes a statement</h3>
<p>This is THE room where a graphic floor earns its keep: patterned tiles or a bold rug. Small surface, contained cost, immediate effect — and footprints show less than on a plain pale floor.</p>
<h3>The mirror works double shifts</h3>
<p>Last check before leaving + doubled light + visual depth. Large, preferably round in angular entryways, facing or perpendicular to the light source.</p>
<h3>The light welcomes</h3>
<p>A pendant at generous height (2.10 m under its lowest point) in a warm tone, rather than a wan spotlight. The entryway is the airlock between outside and inside: its light should say “welcome”, not “identity check”.</p>
<h2>A realistic budget</h2>
<p>A complete entryway treated this way — made-to-measure or semi-custom storage, bench, hooks, mirror, light fixture, floor or rug — usually lands between €1,500 and €4,000 depending on the level of customisation. Divided by the number of daily passages, it is probably the most profitable design investment in the house. It is also a perfect format to discover how I work on a <a href="/en/services/#projet">Full Project</a>.</p>
""",
),
dict(
  slug_fr="palette-leman-sauge-laiton", slug_en="lake-geneva-palette",
  cat_fr="Couleurs", cat_en="Colours",
  img="/assets/img/journal-palette.svg",
  title_fr="Sauge, laiton, bleu profond : la palette qui va si bien au Léman",
  title_en="Sage, brass, deep blue: the palette that suits Lake Geneva so well",
  desc_fr="Pourquoi ces trois teintes fonctionnent dans presque toutes les pièces de la région — et comment les doser sans tomber dans le catalogue.",
  desc_en="Why these three tones work in almost every room in the region — and how to dose them without falling into catalogue clichés.",
  lead_fr="Toutes les régions ont une lumière, et toutes les lumières ont leurs couleurs alliées. Celle du Léman — douce, changeante, réfléchie par l'eau — a les siennes. Ce n'est pas un hasard si trois teintes reviennent sans cesse dans mes projets.",
  lead_en="Every region has its light, and every light has its allied colours. Lake Geneva's — soft, changing, reflected by the water — has its own. It is no accident that three tones keep returning in my projects.",
  body_fr="""
<h2>Comprendre la lumière d'ici</h2>
<p>La lumière lémanique est une lumière réfléchie : l'eau lui ajoute une composante froide et mouvante, les montagnes la coupent tôt le soir. Résultat : les blancs purs virent au gris triste dès 17 h, et les teintes très saturées paraissent criardes à midi. La palette qui fonctionne ici doit encaisser ces variations avec grâce.</p>
<h2>Le vert sauge : le neutre qui n'est pas gris</h2>
<p>Le sauge se comporte comme un neutre — il s'accorde avec tout — mais il vit : verdâtre au soleil, presque gris-bleu au crépuscule. C'est la teinte parfaite des cuisines et des chambres de la région, en soubassement, en façades de meubles ou en linge de lit. Il rappelle les rives sans jamais les singer.</p>
<h2>Le laiton : la lumière solide</h2>
<p>Quand les journées raccourcissent, le laiton — patères, cadres, robinetterie, pieds de lampe — fait ce que l'argenté ne sait pas faire : il réchauffe. Dosage strict : c'est un condiment, pas un plat. Trois à cinq points de laiton par pièce suffisent ; au-delà, on bascule dans le lobby d'hôtel.</p>
<blockquote>Le laiton dans une pièce, c'est le soleil couchant qu'on aurait mis en bouteille.</blockquote>
<h2>Le bleu profond : l'écho du lac</h2>
<p>Encre, pétrole ou nuit — le bleu profond donne ce que le beige ne donnera jamais : de la gravité. Un mur de niche, une tête de lit, un dressing, un cabinet de toilette entier : il excelle dans les usages délimités, en dialogue avec du bois clair et du crème. Face à une fenêtre côté lac, il crée une continuité intérieure-extérieur troublante de justesse.</p>
<h2>La formule de dosage</h2>
<ul>
<li><strong>70 %</strong> de fond clair et chaud (crème, grège, blanc cassé) ;</li>
<li><strong>20 %</strong> de teintes d'ancrage (sauge et/ou bleu profond, bois) ;</li>
<li><strong>10 %</strong> d'accents (laiton, céramiques, textiles).</li>
</ul>
<p>Cette règle 70/20/10 n'a rien d'original — c'est son application locale qui change tout : ici, le 70 % doit être chaud (jamais blanc pur), et le 20 % gagne à faire écho au paysage. C'est exactement le genre de calibrage qu'on règle ensemble en <a href="/prestations/#visite">Visite Conseil</a>, échantillons en main, dans VOTRE lumière.</p>
""",
  body_en="""
<h2>Understanding the light here</h2>
<p>Lake Geneva light is reflected light: the water adds a cool, shifting component; the mountains cut it early in the evening. As a result, pure whites turn sad-grey from 5 pm, and highly saturated tones look garish at noon. The palette that works here must absorb these variations with grace.</p>
<h2>Sage green: the neutral that is not grey</h2>
<p>Sage behaves like a neutral — it goes with everything — but it is alive: greenish in sunlight, almost grey-blue at dusk. It is the perfect tone for the region's kitchens and bedrooms, on lower walls, cabinet fronts or bed linen. It echoes the shores without ever imitating them.</p>
<h2>Brass: solid light</h2>
<p>As the days shorten, brass — hooks, frames, taps, lamp bases — does what chrome cannot: it warms. Strict dosage: it is a condiment, not a dish. Three to five brass points per room are enough; beyond that, you tip into hotel lobby.</p>
<blockquote>Brass in a room is bottled sunset.</blockquote>
<h2>Deep blue: the lake's echo</h2>
<p>Ink, petrol or midnight — deep blue gives what beige never will: gravity. A niche wall, a headboard, a dressing room, an entire cloakroom: it excels in defined uses, in dialogue with pale wood and cream. Facing a lake-side window, it creates an indoor-outdoor continuity that is uncannily right.</p>
<h2>The dosing formula</h2>
<ul>
<li><strong>70%</strong> warm light background (cream, greige, off-white);</li>
<li><strong>20%</strong> anchoring tones (sage and/or deep blue, wood);</li>
<li><strong>10%</strong> accents (brass, ceramics, textiles).</li>
</ul>
<p>This 70/20/10 rule is nothing original — its local application is what changes everything: here, the 70% must be warm (never pure white), and the 20% benefits from echoing the landscape. It is exactly the kind of calibration we settle together during an <a href="/en/services/#visite">Advice Visit</a>, samples in hand, in YOUR light.</p>
""",
),
dict(
  slug_fr="combien-coute-decoratrice", slug_en="interior-decorator-cost",
  cat_fr="Budget", cat_en="Budget",
  img="/assets/img/journal-budget.svg",
  title_fr="Combien coûte une décoratrice d'intérieur ? La vraie réponse",
  title_en="How much does an interior decorator cost? The honest answer",
  desc_fr="Honoraires, budget d'achat, économies évitées : le vrai calcul du coût d'une décoratrice, chiffres du marché à l'appui.",
  desc_en="Fees, purchase budget, avoided mistakes: the real arithmetic of hiring a decorator, with market figures to back it up.",
  lead_fr="C'est la question que tout le monde se pose et que personne n'ose poser en premier. Alors posons-la franchement — avec de vrais chiffres, les miens comme ceux du marché.",
  lead_en="It is the question everyone has and nobody dares ask first. So let us ask it squarely — with real figures, mine as well as the market's.",
  body_fr="""
<h2>Les deux budgets qu'il ne faut jamais confondre</h2>
<p>Le coût d'un projet déco, ce sont deux enveloppes distinctes : <strong>les honoraires</strong> (la conception, l'accompagnement) et <strong>le budget d'achat</strong> (mobilier, peinture, artisans). Chez moi, la frontière est étanche : vous achetez tout aux prix publics, directement, sans marge cachée. Mes honoraires sont ma seule rémunération — c'est la condition d'un conseil réellement libre.</p>
<h2>Ce que coûte le conseil, sur le marché et chez moi</h2>
<p>En France, une consultation de décorateur se facture généralement entre 100 et 300 €, et les projets par pièce démarrent autour de 500 € pour grimper au-delà de 1 500 € selon l'accompagnement. En Suisse romande, comptez 100 à 250 CHF de l'heure et souvent 1 500 à 3 000 CHF la pièce. Mes formules s'inscrivent délibérément entre les deux : <a href="/prestations/#visite">Visite Conseil à 240 €</a>, <a href="/prestations/#projet">Projet Complet dès 890 € la pièce</a> — la rigueur du travail sur mesure, sans les loyers genevois dans l'addition.</p>
<h2>Le coût que personne ne calcule : l'erreur</h2>
<p>Le canapé trop grand commandé sur un coup de tête : 2 000 €. La teinte « comme sur Instagram » qui vire au gris morgue dans votre salon : un week-end et 300 € de repeinte. Le tapis trop petit, la suspension trop basse, la table qui bloque la circulation… La vraie question n'est pas « combien coûte une décoratrice » mais « combien coûtent les erreurs qu'elle empêche ». Sur un projet de pièce à 8 000 € d'achats, une seule erreur majeure évitée finance l'essentiel des honoraires.</p>
<blockquote>Mon travail, au fond : que chaque euro de votre budget d'achat tombe juste du premier coup.</blockquote>
<h2>Pourquoi je visualise tout avant</h2>
<p>C'est ma réponse structurelle à la peur de l'erreur : vous voyez votre pièce transformée — vos volumes, votre lumière — avant le premier achat. Deux allers-retours d'ajustements sont inclus. Le jour où la liste shopping part en commande, il n'y a plus d'inconnue, seulement un plan qu'on exécute.</p>
<h2>Les trois questions à poser avant de signer (avec n'importe qui)</h2>
<ul>
<li>« Vos honoraires sont-ils votre seule rémunération, ou touchez-vous des commissions sur ce que vous me faites acheter ? »</li>
<li>« Que se passe-t-il si la proposition ne me plaît pas ? » (Les allers-retours inclus doivent être écrits noir sur blanc.)</li>
<li>« Qui achète, qui réceptionne, qui gère un retour ? » — la logistique est le vrai révélateur du sérieux.</li>
</ul>
<p>Un professionnel à l'aise avec ces trois questions est généralement un professionnel avec qui tout se passera bien. Et si vous voulez me les poser à moi : <a href="/contact/">j'y réponds sur WhatsApp</a>, sans détour.</p>
""",
  body_en="""
<h2>The two budgets you must never confuse</h2>
<p>A design project has two distinct envelopes: <strong>the fees</strong> (design, guidance) and <strong>the purchase budget</strong> (furniture, paint, tradespeople). With me the border is watertight: you buy everything at public prices, directly, with no hidden margin. My fees are my only remuneration — the precondition for genuinely independent advice.</p>
<h2>What advice costs — on the market and with me</h2>
<p>In France, a decorator's consultation generally runs €100–300, and per-room projects start around €500 and climb past €1,500 depending on the level of support. In French-speaking Switzerland, expect CHF 100–250 per hour and often CHF 1,500–3,000 per room. My packages sit deliberately between the two: <a href="/en/services/#visite">Advice Visit at €240</a>, <a href="/en/services/#projet">Full Project from €890 per room</a> — bespoke rigour, without Geneva rents baked into the bill.</p>
<h2>The cost nobody calculates: mistakes</h2>
<p>The oversized sofa ordered on impulse: €2,000. The “just like Instagram” shade that turns morgue-grey in your living room: a weekend and €300 of repainting. The too-small rug, the too-low pendant, the table that blocks the walkway… The real question is not “how much does a decorator cost” but “how much do the mistakes she prevents cost”. On a room with an €8,000 purchase budget, a single major mistake avoided funds most of the fees.</p>
<blockquote>My job, at its core: making sure every euro of your purchase budget lands right the first time.</blockquote>
<h2>Why I visualise everything first</h2>
<p>It is my structural answer to the fear of error: you see your transformed room — your volumes, your light — before the first purchase. Two rounds of adjustments are included. By the day the shopping list goes to order, there are no unknowns left, only a plan to execute.</p>
<h2>Three questions to ask before signing (with anyone)</h2>
<ul>
<li>“Are your fees your only remuneration, or do you earn commissions on what you have me buy?”</li>
<li>“What happens if I dislike the proposal?” (Included revision rounds should be in writing.)</li>
<li>“Who orders, who receives deliveries, who handles a return?” — logistics is the true test of professionalism.</li>
</ul>
<p>A professional at ease with these three questions is generally a professional with whom everything will go well. And if you would like to ask me directly: <a href="/en/contact/">I answer on WhatsApp</a>, plainly.</p>
""",
),
]

# ---------------------------------------------------------------- gabarits --
def header(lang, active, self_fr, self_en):
    t = I18N[lang]
    cur = ' aria-current="page"'
    nav = "\n".join(
        f'      <a href="{h}"{cur if h == active else ""}>{label}</a>'
        for h, label in t["nav"])
    fr_cur = ' aria-current="true"' if lang == "fr" else ""
    en_cur = ' aria-current="true"' if lang == "en" else ""
    return f'''<header class="header">
  <div class="wrap header__inner">
    <a class="header__logo" href="{t['home']}" aria-label="Rives Intérieures">
      {LOGO_DARK}
    </a>
    <nav class="nav" aria-label="Navigation">
{nav}
    </nav>
    <div class="lang-switch" aria-label="Language">
      <a href="{self_fr}"{fr_cur} lang="fr">FR</a>
      <a href="{self_en}"{en_cur} lang="en">EN</a>
    </div>
    <button class="burger" aria-label="Menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>'''

def footer(lang, other_href):
    t = I18N[lang]
    nav = "\n".join(f'          <li><a href="{h}">{label}</a></li>' for h, label in t["nav"])
    presta = "\n".join(f'          <li><a href="{h}">{label}</a></li>' for h, label in t["foot_p"])
    legal = " · ".join(f'<a href="{h}">{label}</a>' for h, label in t["legal"])
    return f'''<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <div class="footer__logo">
          {LOGO_LIGHT}
        </div>
        <p>{t['foot_desc']}</p>
      </div>
      <div>
        <h4>{t['foot_nav']}</h4>
        <ul>
{nav}
        </ul>
      </div>
      <div>
        <h4>{t['foot_presta']}</h4>
        <ul>
{presta}
        </ul>
      </div>
      <div>
        <h4>{t['foot_contact']}</h4>
        <ul>
          <!-- TODO : coordonnées réelles -->
          <li><a href="https://wa.me/33680995207" rel="noopener">WhatsApp</a></li>
          <li><a href="mailto:contact@rives-interieures.fr">contact@rives-interieures.fr</a></li>
          <li><a href="https://instagram.com/rives.interieures" rel="noopener">Instagram</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bas">
      <p>{t['copyright']}</p>
      <p>{legal} · <a href="{other_href}">{t['other_label']}</a></p>
    </div>
  </div>
</footer>'''

def head(lang, title, desc, canonical, alt_fr, alt_en, ogimg, ogtype="article"):
    t = I18N[lang]
    return f'''<meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="fr" href="{alt_fr}">
  <link rel="alternate" hreflang="en" href="{alt_en}">
  <link rel="alternate" hreflang="x-default" href="{alt_fr}">
  <meta property="og:type" content="{ogtype}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{BASE}{ogimg}">
  <meta property="og:locale" content="{t['locale']}">
  <link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg">
  <script>document.documentElement.classList.add('js');if(location.search.indexOf('noanim')!==-1)document.documentElement.classList.add('no-anim');</script>
  <link rel="stylesheet" href="/assets/css/fonts.css">
  <link rel="stylesheet" href="/assets/css/style.css">'''

def wa_float(lang):
    return f'''<a class="wa-flottant" href="https://wa.me/33680995207" rel="noopener" aria-label="{I18N[lang]['wa_aria']}">
  {WA_ICON}
</a>'''

def article_page(a, lang):
    t = I18N[lang]
    slug = a["slug_" + lang]
    twin = a["slug_" + t["other"]]
    if lang == "fr":
        self_href, twin_href = f"/journal/{slug}/", f"/en/journal/{twin}/"
        self_fr, self_en = self_href, twin_href
        canonical = BASE + self_href
        alt_fr, alt_en = BASE + self_href, BASE + twin_href
        presta_href = "/prestations/"
    else:
        self_href, twin_href = f"/en/journal/{slug}/", f"/journal/{twin}/"
        self_fr, self_en = twin_href, self_href
        canonical = BASE + self_href
        alt_fr, alt_en = BASE + twin_href, BASE + self_href
        presta_href = "/en/services/"
    title = a["title_" + lang]
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  {head(lang, f"{title} | Rives Intérieures", a["desc_" + lang], canonical, alt_fr, alt_en, a["img"])}
</head>
<body>

{header(lang, t["journal_href"], self_fr, self_en)}

<main>

  <article>
    <div class="article-hero">
      <div class="wrap--narrow">
        <p class="overline rvl">{a["cat_" + lang]}</p>
        <h1 class="rvl">{title}</h1>
        <p class="lead rvl rvl-2">{a["lead_" + lang]}</p>
      </div>
    </div>

    <div class="wrap--narrow rvl rvl-2" style="margin-bottom:3rem">
      <img src="{a["img"]}" alt="" width="1200" height="900" style="border-radius:4px;box-shadow:var(--ombre)">
    </div>

    <div class="wrap--narrow prose">
{a["body_" + lang]}
    </div>

    <div class="wrap--narrow">
      <div class="article-fin">
        <div>
          <h3 class="t-serif" style="font-size:1.5rem">{t["fin_titre"]}</h3>
          <p style="font-size:.95rem;color:var(--encre-70);margin-top:.5rem">{t["fin_texte"]}</p>
        </div>
        <div style="display:flex;flex-direction:column;gap:.7rem;align-items:flex-start">
          <!-- TODO : numéro WhatsApp réel -->
          <a class="btn btn--plein" href="https://wa.me/33680995207" rel="noopener">{WA_ICON} {t["fin_btn"]}</a>
          <a href="{presta_href}" style="font-size:.82rem;letter-spacing:.12em;text-transform:uppercase;color:var(--laiton);font-weight:500">{t["fin_presta"]} →</a>
        </div>
      </div>
      <p style="margin:2.2rem 0 4rem"><a href="{t["journal_href"]}" style="color:var(--laiton);font-weight:500">← {t["back"]}</a></p>
    </div>
  </article>

</main>

{wa_float(lang)}

{footer(lang, twin_href)}

<script src="/assets/js/main.js" defer></script>
</body>
</html>
'''

def journal_index(lang):
    t = I18N[lang]
    if lang == "fr":
        self_href, twin_href = "/journal/", "/en/journal/"
        self_fr, self_en = self_href, twin_href
    else:
        self_href, twin_href = "/en/journal/", "/journal/"
        self_fr, self_en = twin_href, self_href
    cards = []
    for i, a in enumerate(ARTICLES):
        slug = a["slug_" + lang]
        href = (f"/journal/{slug}/" if lang == "fr" else f"/en/journal/{slug}/")
        delay = "" if i % 3 == 0 else (" rvl-2" if i % 3 == 1 else " rvl-3")
        cards.append(f'''        <a class="jcard rvl{delay}" href="{href}">
          <div class="jcard__img"><img src="{a["img"]}" alt="" width="1200" height="900" loading="lazy"></div>
          <div class="jcard__corps">
            <p class="jcard__theme">{a["cat_" + lang]}</p>
            <h3>{a["title_" + lang]}</h3>
            <p>{a["desc_" + lang]}</p>
            <span class="jcard__lire">{t["read"]}</span>
          </div>
        </a>''')
    cards_html = "\n".join(cards)
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  {head(lang, t["j_title"], t["j_desc"], BASE + self_href, BASE + self_fr, BASE + self_en, "/assets/img/journal-palette.svg", "website")}
</head>
<body>

{header(lang, t["journal_href"], self_fr, self_en)}

<main>

  <section class="page-hero">
    <div class="wrap">
      <p class="overline rvl">{t["j_overline"]}</p>
      <h1 class="rvl">{t["j_h1"]}</h1>
      <p class="lead rvl rvl-2">{t["j_lead"]}</p>
    </div>
  </section>

  <section style="padding-top:1rem">
    <div class="wrap">
      <div class="journal-grid">
{cards_html}
      </div>
    </div>
  </section>

</main>

{wa_float(lang)}

{footer(lang, twin_href)}

<script src="/assets/js/main.js" defer></script>
</body>
</html>
'''

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(content)
    print("  •", path)

if __name__ == "__main__":
    print("Génération du journal…")
    write("journal/index.html", journal_index("fr"))
    write("en/journal/index.html", journal_index("en"))
    for a in ARTICLES:
        write(f"journal/{a['slug_fr']}/index.html", article_page(a, "fr"))
        write(f"en/journal/{a['slug_en']}/index.html", article_page(a, "en"))
    print(f"Terminé : {2 + 2 * len(ARTICLES)} pages.")
