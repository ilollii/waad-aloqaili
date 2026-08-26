import json
import re

# Load scraped DB
with open('full_detailed_spotlight_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

event_cards = []
all_looks_cards = []

celeb_ar_map = {
    "Katy Perry": "كاتي بيري",
    "Huda El Mufti": "هدى المفتي",
    "Maryam Alnasser": "مريم الناصر",
    "Lama Abdullwahab": "لمى عبد الوهاب",
    "Nicole Saafan": "نيكول سعفان",
    "Sahar Alnaser": "سحر الناصر",
    "Dorra Zarrouk": "درة زروق",
    "Rose Al Bandar": "روز البندر",
    "Rose Albander": "روز البندر",
    "Hams Bandar": "همس بندر",
    "Nour Elboboo": "نور البوبو",
    "Ruba Tursun": "ربا طرسون",
    "Lara Alamri": "لارا العامري",
    "Khawlah Alshyban": "خولة الشيبان",
    "Rasha Al-Rifaie": "رشا الرفاعي",
    "Alanoud Alfallaj": "العنود الفلاج",
    "Taraf Almutairi": "طرف المطيري",
    "Rabell Ejlali": "رابيل إجلالي",
    "Shouq": "شوق",
    "Maya Reaidy": "مايا رعيدي",
    "Reem Alsanea": "ريم الصانع",
    "Celine Abdallah": "سيلين عبد الله",
    "Rola AlQarni": "رولا القرني",
    "Ftoon Aljarallah": "فتون الجارالله",
    "Grace Elizabeth": "غريس إليزابيث",
    "Hana Cross": "هنا كروس",
    "Lou-ann": "لو-آن",
    "Mai Omar": "مي عمر",
    "Ajwa Aljoudi": "أجواء الجودي",
    "Layan Alhaffar": "ليان الحفار",
    "Candice Swanepoel": "كانديس سوانبويل",
    "Alice Abdelaziz": "أليس عبد العزيز",
    "Nadine Abdelaziz": "نادين عبد العزيز",
    "Olivia Yang": "أوليفيا يانغ",
    "Carmen Soliman": "كارمن سليمان",
    "Ashley": "آشلي",
    "Asail Mohammed": "أسيل محمد",
    "Farah Abdelaziz": "فرح عبد العزيز",
    "Jessica de Oliveira": "جيسيكا دي أوليفيرا",
    "Daria Kyryliuk": "داريا كيريليوك",
    "Elena Badri": "إيلينا بدري",
    "Sofia Saidi": "صوفيا سعيدي",
    "Dia Anitska": "ديا أنيتسكا",
    "Angelika Gribova": "أنجيليكا غريبوفا",
    "Mahlagha Jaberi": "مهلاقا جابري",
    "Cláudia Bouza": "كلاوديا بوزا",
    "Josephine Skriver": "جوزفين سكرايفر",
    "Rebecca Kunikowski": "ريبيكا كونيكوفسكي",
    "Anne-Sophie Tima": "آن صوفي تيما"
}

category_badges = [
    {"en": "Joy Awards", "ar": "جوائز صنّاع الترفيه", "filter": "JOY"},
    {"en": "Red Sea Film Festival", "ar": "مهرجان البحر الأحمر", "filter": "REDSEA"},
    {"en": "Riyadh Fashion Week", "ar": "أسبوع الموضة بالرياض", "filter": "RFW"},
    {"en": "Cannes Film Festival", "ar": "مهرجان كان السينمائي", "filter": "CANNES"},
    {"en": "Harper's Bazaar Arabia", "ar": "مجلة هاربرز بازار", "filter": "MAG"},
    {"en": "Red Sea Film Festival", "ar": "مهرجان البحر الأحمر", "filter": "REDSEA"},
    {"en": "Riyadh Fashion Week", "ar": "أسبوع الموضة بالرياض", "filter": "RFW"},
    {"en": "Vogue Arabia", "ar": "مجلة فوغ العربية", "filter": "MAG"},
    {"en": "Billboard Arabia", "ar": "بيلبورد عربية", "filter": "BILLBOARD"},
    {"en": "Cannes Film Festival", "ar": "مهرجان كان السينمائي", "filter": "CANNES"},
    {"en": "Hia Magazine", "ar": "مجلة هي", "filter": "MAG"},
    {"en": "The Oscars", "ar": "جوائز الأوسكار", "filter": "OSCARS"},
    {"en": "Saudi Cup", "ar": "كأس السعودية للخيل", "filter": "SAUDICUP"},
    {"en": "Joy Awards", "ar": "جوائز صنّاع الترفيه", "filter": "JOY"},
    {"en": "Venice Film Festival", "ar": "مهرجان فينيسيا السينمائي", "filter": "VENICE"},
    {"en": "Cannes Film Festival", "ar": "مهرجان كان السينمائي", "filter": "CANNES"},
    {"en": "Saudi Cup", "ar": "كأس السعودية للخيل", "filter": "SAUDICUP"},
    {"en": "Cannes Film Festival", "ar": "مهرجان كان السينمائي", "filter": "CANNES"}
]

# Generate Event Overview Cards
for idx, ev in enumerate(db):
    cat = category_badges[idx]
    sub_count = len(ev.get('sub_items', [])) or 1
    intro_txt = ev.get('intro_text', '') or ev.get('main_desc', '')
    
    card = f'''
    <article class="spotlight-event-card" data-category="{cat['filter']}" data-event-id="event_{idx+1}">
      <div class="event-card-media" onclick="window.openEventModal('event_{idx+1}')">
        <div class="media-aspect-wrap">
          <img src="{ev['main_image']}" alt="{ev['main_title']}" class="event-main-img" loading="lazy">
        </div>
        <span class="event-tag-badge">
          <span class="txt-ar">{cat['ar']}</span>
          <span class="txt-en">{cat['en']}</span>
        </span>
        <div class="media-hover-overlay">
          <span class="view-gallery-btn">
            <i data-feather="grid" style="width:14px;height:14px;margin-inline-end:6px;"></i>
            <span class="txt-ar">استعراض كافة الصور ({sub_count})</span>
            <span class="txt-en">View All ({sub_count}) Photos</span>
          </span>
        </div>
      </div>
      <div class="event-card-content">
        <div class="event-card-meta">
          <span class="event-brand-signature">WAAD ALOQAILI COUTURE</span>
          <span class="event-counter">#{idx+1:02d}</span>
        </div>
        <h3 class="event-card-title" onclick="window.openEventModal('event_{idx+1}')">
          {ev['main_title']}
        </h3>
        <p class="event-card-desc">
          {intro_txt}
        </p>
        <div class="event-card-footer">
          <button type="button" class="event-open-action-btn" onclick="window.openEventModal('event_{idx+1}')">
            <span class="txt-ar">عرض تفاصيل التغطية الكاملة &larr;</span>
            <span class="txt-en">Explore Full Coverage &rarr;</span>
          </button>
        </div>
      </div>
    </article>
    '''
    event_cards.append(card)

# Generate Individual Looks Cards
seen_sub_imgs = set()
look_counter = 0

for ev_idx, ev in enumerate(db):
    cat = category_badges[ev_idx]
    for sub_idx, sub in enumerate(ev.get('sub_items', [])):
        img = sub['image']
        cap = sub.get('caption', '')
        if not cap:
            cap = ev.get('intro_text', '') or ev.get('main_desc', '')
            
        if img in seen_sub_imgs:
            continue
        seen_sub_imgs.add(img)
        look_counter += 1
        
        detected_celeb = ""
        for name in celeb_ar_map.keys():
            if name.lower() in cap.lower():
                detected_celeb = name
                break
                
        celeb_badge_html = ""
        if detected_celeb:
            ar_celeb = celeb_ar_map[detected_celeb]
            celeb_badge_html = f'''
            <span class="celeb-pill">
              <i data-feather="star" style="width:12px;height:12px;margin-inline-end:4px;"></i>
              <span class="txt-ar">{ar_celeb}</span>
              <span class="txt-en">{detected_celeb}</span>
            </span>
            '''

        escaped_cap = cap.replace('"', '&quot;').replace("'", "&#39;")

        look_card = f'''
        <div class="look-gallery-card" data-category="{cat['filter']}">
          <div class="look-media-wrap" onclick="window.openLightbox('{img}', '{escaped_cap}')">
            <img src="{img}" alt="{detected_celeb or ev['main_title']}" class="look-img" loading="lazy">
            <div class="look-overlay-action">
              <span class="look-zoom-btn"><i data-feather="maximize-2"></i></span>
            </div>
          </div>
          <div class="look-info-body">
            <div class="look-tags-row">
              <span class="look-event-badge">
                <span class="txt-ar">{cat['ar']}</span>
                <span class="txt-en">{cat['en']}</span>
              </span>
              {celeb_badge_html}
            </div>
            <h4 class="look-event-heading">{ev['main_title']}</h4>
            <p class="look-exact-caption">{cap}</p>
          </div>
        </div>
        '''
        all_looks_cards.append(look_card)

print(f"Generated {len(event_cards)} event cards and {len(all_looks_cards)} individual look cards.")

events_grid_html = "\n".join(event_cards)
looks_grid_html = "\n".join(all_looks_cards)
db_json = json.dumps(db, ensure_ascii=False)

# Template using standard string format
template = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Under The Spotlight | Waad Aloqaili Haute Couture (تحت الأضواء)</title>
  <meta name="description" content="التوثيق الرسمي لإطلالات السجادة الحمراء وأغلفة المجلات العالمية لدار وعد العقيلي للأزياء الراقية.">
  <meta name="theme-color" content="#2C1A48">
  
  <meta property="og:title" content="Waad Aloqaili – Under The Spotlight">
  <meta property="og:description" content="Red carpet moments and global press features from Cannes, Venice, and the Oscars to Vogue and Harper's Bazaar.">
  <meta property="og:image" content="https://waadaloqaili.com/cdn/shop/files/Photo_17-01-2026_8_08_06_PM.jpg?width=1800">
  
  <link rel="icon" type="image/svg+xml" href="logo.svg">
  <script src="https://unpkg.com/feather-icons"></script>
  <link rel="stylesheet" href="styles.css">
  
  <style>
    /* Language switching classes */
    body[data-lang="ar"] .txt-en { display: none !important; }
    body[data-lang="ar"] .txt-ar { display: inline !important; }
    body[data-lang="ar"] span.txt-ar, body[data-lang="ar"] p.txt-ar, body[data-lang="ar"] div.txt-ar, body[data-lang="ar"] h1.txt-ar, body[data-lang="ar"] h2.txt-ar, body[data-lang="ar"] h3.txt-ar, body[data-lang="ar"] h4.txt-ar { display: block !important; }

    body[data-lang="en"] .txt-ar { display: none !important; }
    body[data-lang="en"] .txt-en { display: inline !important; }
    body[data-lang="en"] span.txt-en, body[data-lang="en"] p.txt-en, body[data-lang="en"] div.txt-en, body[data-lang="en"] h1.txt-en, body[data-lang="en"] h2.txt-en, body[data-lang="en"] h3.txt-en, body[data-lang="en"] h4.txt-en { display: block !important; }

    /* Spotlight Hero */
    .spotlight-hero-section {
      background: linear-gradient(135deg, #160B24 0%, #2A1744 50%, #120820 100%);
      color: #FFFFFF;
      padding: 5.5rem 2rem 4.5rem;
      text-align: center;
      position: relative;
      border-bottom: 1px solid var(--color-border-dark);
    }
    .spotlight-hero-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.25em;
      color: var(--color-accent-gold);
      background: rgba(223, 186, 115, 0.1);
      border: 1px solid rgba(223, 186, 115, 0.3);
      padding: 0.45rem 1.4rem;
      margin-bottom: 1.5rem;
      border-radius: 2px;
      text-transform: uppercase;
    }
    .spotlight-hero-title {
      font-family: var(--font-serif);
      font-size: clamp(2.2rem, 5vw, 4rem);
      font-weight: 800;
      color: #FFFFFF;
      letter-spacing: 0.04em;
      margin-bottom: 1rem;
      line-height: 1.25;
    }
    .spotlight-hero-description {
      font-size: clamp(0.95rem, 1.8vw, 1.15rem);
      color: var(--color-accent-gold-light);
      max-width: 860px;
      margin: 0 auto 2.5rem;
      line-height: 1.85;
    }

    /* View Switcher Tabs */
    .spotlight-view-switcher {
      display: inline-flex;
      background: rgba(20, 10, 32, 0.7);
      border: 1px solid rgba(223, 186, 115, 0.3);
      padding: 0.35rem;
      border-radius: 4px;
      gap: 0.4rem;
    }
    .view-switch-tab {
      background: transparent;
      border: none;
      color: var(--color-accent-gold-light);
      font-weight: 700;
      font-size: 0.85rem;
      padding: 0.6rem 1.5rem;
      cursor: pointer;
      border-radius: 2px;
      transition: all 0.3s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
    }
    .view-switch-tab.active {
      background: var(--color-accent-gold);
      color: #120820;
      box-shadow: 0 4px 14px rgba(0,0,0,0.3);
    }

    /* Filter Bar */
    .spotlight-filter-strip {
      background: #FAF8F5;
      border-bottom: 1px solid var(--color-border);
      padding: 1.1rem 2rem;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
      position: sticky;
      top: 70px;
      z-index: 40;
      backdrop-filter: blur(10px);
    }
    body.velvet-dark .spotlight-filter-strip {
      background: #180D2C;
      border-bottom-color: var(--color-border-dark);
    }
    .filter-btn-pill {
      background: transparent;
      border: 1px solid var(--color-border);
      color: var(--color-text-primary);
      padding: 0.45rem 1.1rem;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.3s ease;
      letter-spacing: 0.04em;
    }
    .filter-btn-pill:hover, .filter-btn-pill.active {
      background: var(--color-brand-purple);
      color: #FFFFFF;
      border-color: var(--color-brand-purple);
      box-shadow: 0 4px 12px rgba(44, 26, 72, 0.2);
    }
    body.velvet-dark .filter-btn-pill {
      border-color: rgba(223, 186, 115, 0.2);
      color: var(--color-accent-gold-light);
    }
    body.velvet-dark .filter-btn-pill:hover, body.velvet-dark .filter-btn-pill.active {
      background: var(--color-accent-gold);
      color: #120820;
      border-color: var(--color-accent-gold);
    }

    /* Main Container */
    .spotlight-main-container {
      max-width: 1440px;
      margin: 0 auto;
      padding: 4rem 2.5rem 6rem;
    }

    /* Event Overview Grid (18 Cards) */
    .events-grid-layout {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 3.5rem 2.5rem;
    }
    @media (max-width: 1100px) {
      .events-grid-layout {
        grid-template-columns: repeat(2, 1fr);
        gap: 2.5rem 1.8rem;
      }
    }
    @media (max-width: 720px) {
      .events-grid-layout {
        grid-template-columns: 1fr;
        gap: 2.5rem;
      }
      .spotlight-main-container {
        padding: 2.5rem 1.2rem 4rem;
      }
    }

    .spotlight-event-card {
      background: #FFFFFF;
      border: 1px solid var(--color-border);
      display: flex;
      flex-direction: column;
      border-radius: 2px;
      overflow: hidden;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    body.velvet-dark .spotlight-event-card {
      background: #190F2E;
      border-color: rgba(223, 186, 115, 0.15);
    }
    .spotlight-event-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 16px 36px rgba(44, 26, 72, 0.15);
      border-color: var(--color-accent-gold);
    }
    body.velvet-dark .spotlight-event-card:hover {
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
    }

    .event-card-media {
      position: relative;
      width: 100%;
      aspect-ratio: 2 / 3;
      overflow: hidden;
      background: #120820;
      cursor: pointer;
    }
    .media-aspect-wrap {
      width: 100%;
      height: 100%;
    }
    .event-main-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
      display: block;
    }
    .spotlight-event-card:hover .event-main-img {
      transform: scale(1.05);
    }
    .event-tag-badge {
      position: absolute;
      top: 14px;
      right: 14px;
      background: rgba(18, 8, 32, 0.88);
      backdrop-filter: blur(8px);
      color: var(--color-accent-gold);
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.1em;
      padding: 0.35rem 0.85rem;
      border: 1px solid rgba(223, 186, 115, 0.35);
      z-index: 2;
    }
    [dir="ltr"] .event-tag-badge {
      right: auto;
      left: 14px;
    }

    .media-hover-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(18, 8, 32, 0.9) 0%, rgba(18, 8, 32, 0.1) 60%, transparent 100%);
      display: flex;
      align-items: flex-end;
      justify-content: center;
      padding-bottom: 1.8rem;
      opacity: 0;
      transition: opacity 0.35s ease;
    }
    .spotlight-event-card:hover .media-hover-overlay {
      opacity: 1;
    }
    .view-gallery-btn {
      background: var(--color-accent-gold);
      color: #120820;
      font-size: 0.78rem;
      font-weight: 800;
      padding: 0.55rem 1.2rem;
      border-radius: 2px;
      display: inline-flex;
      align-items: center;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }

    .event-card-content {
      padding: 1.8rem 1.6rem 2rem;
      display: flex;
      flex-direction: column;
      flex: 1;
    }
    .event-card-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.75rem;
    }
    .event-brand-signature {
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.15em;
      color: var(--color-accent-gold);
    }
    .event-counter {
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--color-text-muted);
    }
    .event-card-title {
      font-family: var(--font-serif);
      font-size: 1.22rem;
      font-weight: 800;
      color: var(--color-brand-purple);
      margin-bottom: 0.8rem;
      line-height: 1.4;
      cursor: pointer;
      transition: color 0.3s ease;
    }
    body.velvet-dark .event-card-title {
      color: #FFFFFF;
    }
    .event-card-title:hover {
      color: var(--color-accent-gold);
    }
    .event-card-desc {
      font-size: 0.9rem;
      color: var(--color-text-secondary);
      line-height: 1.75;
      margin-bottom: 1.6rem;
      flex: 1;
    }
    body.velvet-dark .event-card-desc {
      color: #C8BFD4;
    }
    .event-card-footer {
      border-top: 1px solid var(--color-border);
      padding-top: 1.2rem;
    }
    body.velvet-dark .event-card-footer {
      border-top-color: rgba(223, 186, 115, 0.15);
    }
    .event-open-action-btn {
      background: transparent;
      border: none;
      color: var(--color-brand-purple);
      font-weight: 800;
      font-size: 0.84rem;
      cursor: pointer;
      padding: 0;
      display: inline-flex;
      align-items: center;
      transition: color 0.3s ease;
    }
    body.velvet-dark .event-open-action-btn {
      color: var(--color-accent-gold-light);
    }
    .event-open-action-btn:hover {
      color: var(--color-accent-gold);
    }

    /* Complete Individual Looks Grid View */
    .looks-gallery-layout {
      display: none;
      grid-template-columns: repeat(3, 1fr);
      gap: 3rem 2rem;
    }
    .looks-gallery-layout.active {
      display: grid;
    }
    .events-grid-layout.active {
      display: grid;
    }
    .events-grid-layout.hidden {
      display: none;
    }
    @media (max-width: 1024px) {
      .looks-gallery-layout {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    @media (max-width: 650px) {
      .looks-gallery-layout {
        grid-template-columns: 1fr;
      }
    }

    .look-gallery-card {
      background: #FFFFFF;
      border: 1px solid var(--color-border);
      display: flex;
      flex-direction: column;
      border-radius: 2px;
      overflow: hidden;
      transition: all 0.35s ease;
    }
    body.velvet-dark .look-gallery-card {
      background: #190F2E;
      border-color: rgba(223, 186, 115, 0.15);
    }
    .look-gallery-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 12px 30px rgba(0,0,0,0.15);
      border-color: var(--color-accent-gold);
    }
    .look-media-wrap {
      position: relative;
      width: 100%;
      aspect-ratio: 3 / 4;
      background: #120820;
      overflow: hidden;
      cursor: pointer;
    }
    .look-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s ease;
    }
    .look-gallery-card:hover .look-img {
      transform: scale(1.04);
    }
    .look-overlay-action {
      position: absolute;
      top: 12px;
      left: 12px;
      background: rgba(18, 8, 32, 0.8);
      color: var(--color-accent-gold);
      border: 1px solid rgba(223, 186, 115, 0.3);
      width: 34px;
      height: 34px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    .look-gallery-card:hover .look-overlay-action {
      opacity: 1;
    }

    .look-info-body {
      padding: 1.4rem 1.3rem 1.6rem;
      display: flex;
      flex-direction: column;
      flex: 1;
    }
    .look-tags-row {
      display: flex;
      gap: 0.5rem;
      align-items: center;
      margin-bottom: 0.6rem;
      flex-wrap: wrap;
    }
    .look-event-badge {
      font-size: 0.7rem;
      font-weight: 800;
      color: var(--color-accent-gold);
      text-transform: uppercase;
    }
    .celeb-pill {
      font-size: 0.72rem;
      font-weight: 800;
      color: #FFFFFF;
      background: var(--color-brand-purple);
      padding: 0.2rem 0.6rem;
      border-radius: 2px;
      display: inline-flex;
      align-items: center;
    }
    body.velvet-dark .celeb-pill {
      background: rgba(223, 186, 115, 0.2);
      color: var(--color-accent-gold-light);
    }
    .look-event-heading {
      font-family: var(--font-serif);
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--color-brand-purple);
      margin-bottom: 0.6rem;
      line-height: 1.35;
    }
    body.velvet-dark .look-event-heading {
      color: #FFFFFF;
    }
    .look-exact-caption {
      font-size: 0.85rem;
      color: var(--color-text-secondary);
      line-height: 1.65;
      flex: 1;
    }
    body.velvet-dark .look-exact-caption {
      color: #C8BFD4;
    }

    /* Event Detail Modal */
    .spotlight-modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(12, 6, 24, 0.88);
      backdrop-filter: blur(12px);
      z-index: 99999;
      opacity: 0;
      visibility: hidden;
      transition: all 0.35s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2rem;
    }
    .spotlight-modal-backdrop.active {
      opacity: 1;
      visibility: visible;
    }
    .spotlight-modal-box {
      background: #FFFFFF;
      width: 100%;
      max-width: 1100px;
      max-height: 92vh;
      border-radius: 4px;
      overflow-y: auto;
      border: 1px solid rgba(223, 186, 115, 0.35);
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6);
      position: relative;
      transform: scale(0.96) translateY(20px);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }
    body.velvet-dark .spotlight-modal-box {
      background: #180D2C;
      color: #FFFFFF;
    }
    .spotlight-modal-backdrop.active .spotlight-modal-box {
      transform: scale(1) translateY(0);
    }
    .spotlight-modal-close {
      position: absolute;
      top: 18px;
      left: 20px;
      background: rgba(20, 11, 36, 0.8);
      color: var(--color-accent-gold);
      border: 1px solid rgba(223, 186, 115, 0.3);
      width: 40px;
      height: 40px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 20;
      transition: all 0.3s ease;
    }
    [dir="ltr"] .spotlight-modal-close {
      left: auto;
      right: 20px;
    }
    .spotlight-modal-close:hover {
      background: var(--color-accent-gold);
      color: #120820;
      transform: rotate(90deg);
    }

    .modal-hero-cover {
      position: relative;
      height: 360px;
      background: #120820;
      overflow: hidden;
    }
    .modal-hero-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      filter: brightness(0.6);
    }
    .modal-hero-overlay {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 2.5rem 3rem;
      background: linear-gradient(to top, rgba(18, 8, 32, 0.95) 0%, rgba(18, 8, 32, 0.5) 70%, transparent 100%);
      color: #FFFFFF;
    }
    .modal-event-title {
      font-family: var(--font-serif);
      font-size: clamp(1.4rem, 3vw, 2.3rem);
      font-weight: 800;
      color: #FFFFFF;
      margin-bottom: 0.5rem;
    }
    .modal-body-content {
      padding: 2.8rem 3rem;
    }
    .modal-intro-text {
      font-size: 1.08rem;
      line-height: 1.85;
      color: var(--color-text-primary);
      margin-bottom: 2.5rem;
      padding-bottom: 2rem;
      border-bottom: 1px solid var(--color-border);
    }
    body.velvet-dark .modal-intro-text {
      color: #EDE8F2;
      border-bottom-color: rgba(223, 186, 115, 0.15);
    }

    .modal-sublooks-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 2rem;
    }
    .modal-look-item {
      background: #FAF8F5;
      border: 1px solid var(--color-border);
      border-radius: 2px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }
    body.velvet-dark .modal-look-item {
      background: #1F1238;
      border-color: rgba(223, 186, 115, 0.15);
    }
    .modal-look-img-wrap {
      width: 100%;
      aspect-ratio: 3 / 4;
      overflow: hidden;
      background: #120820;
      cursor: pointer;
    }
    .modal-look-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
    }
    .modal-look-item:hover .modal-look-img {
      transform: scale(1.04);
    }
    .modal-look-caption {
      padding: 1.2rem;
      font-size: 0.88rem;
      line-height: 1.65;
      color: var(--color-text-secondary);
      flex: 1;
    }
    body.velvet-dark .modal-look-caption {
      color: #D6CFE0;
    }

    /* Lightbox Modal */
    .lightbox-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(8, 4, 16, 0.95);
      z-index: 999999;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 2rem;
      opacity: 0;
      visibility: hidden;
      transition: all 0.3s ease;
    }
    .lightbox-backdrop.active {
      opacity: 1;
      visibility: visible;
    }
    .lightbox-img-wrap {
      max-width: 90vw;
      max-height: 75vh;
      margin-bottom: 1.5rem;
    }
    .lightbox-img {
      max-width: 100%;
      max-height: 75vh;
      object-fit: contain;
      box-shadow: 0 15px 40px rgba(0,0,0,0.8);
      border: 1px solid rgba(223, 186, 115, 0.3);
    }
    .lightbox-caption {
      color: #FFFFFF;
      max-width: 800px;
      text-align: center;
      font-size: 0.95rem;
      line-height: 1.7;
      background: rgba(26, 14, 44, 0.85);
      padding: 1rem 1.8rem;
      border: 1px solid rgba(223, 186, 115, 0.2);
    }
    .lightbox-close {
      position: absolute;
      top: 20px;
      right: 25px;
      background: rgba(223, 186, 115, 0.9);
      color: #120820;
      border: none;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
    }
  </style>
</head>
<body data-lang="ar">

  <div class="custom-cursor" id="customCursor"></div>

  <!-- Announcement Bar -->
  <div class="announcement-bar" id="announcementBar">
    <div class="announcement-meta">
      <span style="font-weight:800; color:var(--color-accent-gold);">
        <span class="txt-ar">المملكة العربية السعودية</span>
        <span class="txt-en">Saudi Arabia</span>
      </span>
      <select class="currency-select" id="currencySelect" aria-label="Select Currency" style="margin-inline-start:1rem;">
        <option value="SAR" selected>SAR (ر.س)</option>
        <option value="USD">USD ($)</option>
        <option value="EUR">EUR (€)</option>
        <option value="AED">AED (د.إ)</option>
        <option value="KWD">KWD (د.ك)</option>
        <option value="QAR">QAR (ر.ق)</option>
      </select>
    </div>

    <div class="announcement-slider" id="announcementSlider">
      <span class="announcement-item active">
        <span class="txt-ar">تحت الأضواء: إطلالات السجادة الحمراء وأغلفة المجلات العالمية لدار وعد العقيلي</span>
        <span class="txt-en">Under The Spotlight: Global Red Carpet Moments & International Press</span>
      </span>
      <span class="announcement-item">
        <span class="txt-ar">توصيل ملكي فاخر مجاني لجميع مناطق المملكة وكافة دول العالم</span>
        <span class="txt-en">Complimentary White-Glove Couture Delivery Across Saudi Arabia & Worldwide</span>
      </span>
    </div>

    <div class="announcement-meta" style="display:flex; align-items:center; gap:1.2rem;">
      <button class="theme-toggle-btn" id="themeToggleBtn" onclick="window.app.toggleVelvetTheme()" aria-label="Toggle Velvet Mode">
        <i data-feather="moon" id="themeIcon" style="width:14px;height:14px; color:var(--color-accent-gold);"></i>
        <span id="themeLabel">
          <span class="txt-ar">الوضع الملكي</span>
          <span class="txt-en">Velvet Mode</span>
        </span>
      </button>

      <button class="lang-btn" id="langToggleBtn" onclick="window.app.toggleLanguage()" aria-label="Switch Language">
        <i data-feather="globe" style="width:14px;height:14px;"></i>
        <span id="langLabel">
          <span class="txt-ar">English</span>
          <span class="txt-en">العربية</span>
        </span>
      </button>
    </div>
  </div>

  <!-- Site Header -->
  <header class="site-header" id="siteHeader">
    <div class="header-left">
      <button class="menu-toggle-btn" id="rightNavToggleBtn" onclick="window.app.openRightNav()" aria-label="Open Menu">
        <div class="hamburger-lines" aria-hidden="true">
          <span class="hamburger-bar"></span>
          <span class="hamburger-bar"></span>
          <span class="hamburger-bar"></span>
        </div>
        <span class="menu-btn-label">
          <span class="txt-ar">القائمة والتصنيفات</span>
          <span class="txt-en">Menu & Navigation</span>
        </span>
      </button>
    </div>

    <div class="brand-logo-container">
      <a href="index.html" class="brand-logo-link">
        <img src="logo.svg" alt="Waad Aloqaili Emblem" style="height:32px; width:auto; margin-bottom:2px;">
        <span class="brand-logo-text" id="brandLogo">Waad Aloqaili</span>
      </a>
    </div>

    <div class="header-right">
      <button class="icon-btn search-trigger-btn" onclick="window.app.openSearchModal()" aria-label="Search">
        <i data-feather="search"></i>
        <span class="action-btn-text">
          <span class="txt-ar">بحث</span>
          <span class="txt-en">Search</span>
        </span>
      </button>

      <a href="collections.html?filter=all" class="icon-btn" aria-label="Collections">
        <i data-feather="grid"></i>
        <span class="action-btn-text">
          <span class="txt-ar">المجموعات</span>
          <span class="txt-en">Collections</span>
        </span>
      </a>

      <button class="icon-btn cart-trigger-btn" onclick="window.app.openCartDrawer()" aria-label="Cart">
        <div class="cart-icon-wrap">
          <i data-feather="shopping-bag"></i>
          <span class="cart-badge" id="cartCountBadge">0</span>
        </div>
        <span class="action-btn-text">
          <span class="txt-ar">حقيبة التسوق</span>
          <span class="txt-en">Shopping Bag</span>
        </span>
      </button>
    </div>
  </header>

  <!-- Sticky Luxury Navigation -->
  <nav class="luxury-nav-bar" aria-label="Main Navigation">
    <ul class="nav-links-list">
      <li><a href="index.html" class="nav-link-item"><span class="txt-ar">الرئيسية</span><span class="txt-en">Home</span></a></li>
      <li><a href="collections.html?filter=all" class="nav-link-item"><span class="txt-ar">كافة المجموعات</span><span class="txt-en">All Collections</span></a></li>
      <li><a href="collections.html?filter=yamal" class="nav-link-item"><span class="txt-ar">مجموعة يمال SS26</span><span class="txt-en">Yamal SS26</span></a></li>
      <li><a href="collections.html?filter=veil-of-renewal" class="nav-link-item"><span class="txt-ar">حجاب التجدد SS25</span><span class="txt-en">Veil of Renewal</span></a></li>
      <li><a href="collections.html?filter=gowns" class="nav-link-item"><span class="txt-ar">فساتين السهرة</span><span class="txt-en">Evening Gowns</span></a></li>
      <li><a href="under-the-spotlight.html" class="nav-link-item active" style="color:var(--color-accent-gold);"><span class="txt-ar">تحت الأضواء</span><span class="txt-en">Under The Spotlight</span></a></li>
      <li><a href="about-us.html" class="nav-link-item"><span class="txt-ar">عن الدار</span><span class="txt-en">About The House</span></a></li>
      <li><a href="checkout.html" class="nav-link-item"><span class="txt-ar">إتمام الطلب</span><span class="txt-en">Checkout</span></a></li>
    </ul>
  </nav>

  <!-- Hero Header -->
  <header class="spotlight-hero-section">
    <div class="spotlight-hero-tag">
      <i data-feather="star" style="width:14px;height:14px;"></i>
      <span class="txt-ar">الأرشيف الصحفي وعروض السجادة الحمراء</span>
      <span class="txt-en">Red Carpet Archive & Press Features</span>
    </div>
    <h1 class="spotlight-hero-title">
      <span class="txt-ar">تحت الأضواء</span>
      <span class="txt-en">Under The Spotlight</span>
    </h1>
    <p class="spotlight-hero-description">
      <span class="txt-ar">رحلة توثيقية ترصد تألق إبداعات دار وعد العقيلي للأزياء الراقية على كبرى المحافل العالمية من مهرجان كان السينمائي والبندقية إلى الأوسكار، وأغلفة كبرى المجلات الدولية.</span>
      <span class="txt-en">A curated retrospective of Waad Aloqaili Haute Couture illuminating the world's most prestigious stages from Cannes, Venice, and the Oscars to the covers of Vogue and Harper's Bazaar.</span>
    </p>

    <!-- View Switcher -->
    <div class="spotlight-view-switcher">
      <button type="button" class="view-switch-tab active" id="tabEventsView" onclick="window.switchSpotlightView('events')">
        <i data-feather="grid" style="width:15px;height:15px;"></i>
        <span class="txt-ar">بطاقات المناسبات الرسمية (18 تغطية)</span>
        <span class="txt-en">Editorial Events (18 Stories)</span>
      </button>
      <button type="button" class="view-switch-tab" id="tabLooksView" onclick="window.switchSpotlightView('looks')">
        <i data-feather="image" style="width:15px;height:15px;"></i>
        <span class="txt-ar">معرض كافة الإطلالات والمشاهير (60+ صورة بالكابشن)</span>
        <span class="txt-en">All Celebrity Looks & Captions</span>
      </button>
    </div>
  </header>

  <!-- Filter Strip -->
  <div class="spotlight-filter-strip">
    <button class="filter-btn-pill active" onclick="window.filterAllSpotlight('ALL', this)">
      <span class="txt-ar">الكل</span>
      <span class="txt-en">All</span>
    </button>
    <button class="filter-btn-pill" onclick="window.filterAllSpotlight('CANNES', this)">
      <span class="txt-ar">مهرجان كان</span>
      <span class="txt-en">Cannes Festival</span>
    </button>
    <button class="filter-btn-pill" onclick="window.filterAllSpotlight('JOY', this)">
      <span class="txt-ar">جوائز Joy Awards</span>
      <span class="txt-en">Joy Awards</span>
    </button>
    <button class="filter-btn-pill" onclick="window.filterAllSpotlight('REDSEA', this)">
      <span class="txt-ar">مهرجان البحر الأحمر</span>
      <span class="txt-en">Red Sea Festival</span>
    </button>
    <button class="filter-btn-pill" onclick="window.filterAllSpotlight('RFW', this)">
      <span class="txt-ar">أسبوع الموضة بالرياض</span>
      <span class="txt-en">Riyadh Fashion Week</span>
    </button>
    <button class="filter-btn-pill" onclick="window.filterAllSpotlight('MAG', this)">
      <span class="txt-ar">المجلات (Vogue & Bazaar & Hia)</span>
      <span class="txt-en">Magazines</span>
    </button>
    <button class="filter-btn-pill" onclick="window.filterAllSpotlight('SAUDICUP', this)">
      <span class="txt-ar">كأس السعودية</span>
      <span class="txt-en">Saudi Cup</span>
    </button>
    <button class="filter-btn-pill" onclick="window.filterAllSpotlight('OSCARS', this)">
      <span class="txt-ar">حفل الأوسكار</span>
      <span class="txt-en">The Oscars</span>
    </button>
    <button class="filter-btn-pill" onclick="window.filterAllSpotlight('VENICE', this)">
      <span class="txt-ar">مهرجان البندقية</span>
      <span class="txt-en">Venice Festival</span>
    </button>
  </div>

  <!-- Main Content Grid -->
  <main class="spotlight-main-container">
    <!-- View 1: 18 Editorial Event Cards -->
    <div class="events-grid-layout active" id="eventsGridLayout">
""" + events_grid_html + """
    </div>

    <!-- View 2: Complete Looks Gallery (All photos + Captions) -->
    <div class="looks-gallery-layout" id="looksGalleryLayout">
""" + looks_grid_html + """
    </div>
  </main>

  <!-- Event Dossier Modal -->
  <div class="spotlight-modal-backdrop" id="spotlightModal" onclick="window.closeEventModal(event)">
    <div class="spotlight-modal-box" onclick="event.stopPropagation()">
      <button type="button" class="spotlight-modal-close" onclick="window.closeEventModalDirect()" aria-label="Close">
        <i data-feather="x"></i>
      </button>
      <div class="modal-hero-cover">
        <img src="" alt="" class="modal-hero-img" id="modalHeroImg">
        <div class="modal-hero-overlay">
          <div style="font-size:0.8rem; font-weight:800; color:var(--color-accent-gold); letter-spacing:0.15em; margin-bottom:0.4rem;">WAAD ALOQAILI COUTURE</div>
          <h2 class="modal-event-title" id="modalHeroTitle">Event Title</h2>
        </div>
      </div>
      <div class="modal-body-content">
        <p class="modal-intro-text" id="modalIntroText"></p>
        <h4 style="font-family:var(--font-serif); font-size:1.25rem; font-weight:800; color:var(--color-accent-gold); margin-bottom:1.5rem;">
          <span class="txt-ar">معرض الإطلالات وتفاصيل الحضور بالكابشن الكامل</span>
          <span class="txt-en">Celebrity Looks & Verified Captions</span>
        </h4>
        <div class="modal-sublooks-grid" id="modalSublooksGrid"></div>
      </div>
    </div>
  </div>

  <!-- Lightbox for Image Zoom -->
  <div class="lightbox-backdrop" id="lightboxModal" onclick="window.closeLightbox(event)">
    <button type="button" class="lightbox-close" onclick="window.closeLightboxDirect()">&times;</button>
    <div class="lightbox-img-wrap" onclick="event.stopPropagation()">
      <img src="" alt="" class="lightbox-img" id="lightboxImg">
    </div>
    <div class="lightbox-caption" id="lightboxCaption" onclick="event.stopPropagation()"></div>
  </div>

  <!-- Cart Drawer -->
  <div class="cart-drawer-backdrop" id="cartDrawerBackdrop" onclick="window.app.closeCartDrawer()"></div>
  <aside class="cart-drawer" id="cartDrawer" aria-label="Shopping Cart">
    <div class="cart-drawer-header">
      <h3 class="cart-drawer-title">
        <span class="txt-ar">حقيبة المقتنيات الملكية</span>
        <span class="txt-en">Your Luxury Bag</span>
      </h3>
      <button class="cart-drawer-close" onclick="window.app.closeCartDrawer()" aria-label="Close Cart">
        <i data-feather="x"></i>
      </button>
    </div>
    <div class="cart-drawer-items" id="cartDrawerItems"></div>
    <div class="cart-drawer-footer">
      <div class="cart-subtotal-row">
        <span><span class="txt-ar">المجموع الإجمالي</span><span class="txt-en">Subtotal</span></span>
        <span class="cart-subtotal-amount" id="cartSubtotalAmount">0 SAR</span>
      </div>
      <button class="primary-btn checkout-btn" onclick="window.location.href='checkout.html'">
        <span class="txt-ar">متابعة إتمام الطلب</span>
        <span class="txt-en">Proceed to Checkout</span>
      </button>
    </div>
  </aside>

  <!-- Right Navigation Drawer -->
  <div class="nav-drawer-backdrop" id="rightNavBackdrop" onclick="window.app.closeRightNav()"></div>
  <aside class="nav-drawer" id="rightNavDrawer" aria-label="Site Navigation">
    <div class="nav-drawer-header">
      <span class="nav-drawer-title">
        <span class="txt-ar">القائمة الرئيسية</span>
        <span class="txt-en">Menu & Categories</span>
      </span>
      <button class="nav-drawer-close" onclick="window.app.closeRightNav()" aria-label="Close Navigation">
        <i data-feather="x"></i>
      </button>
    </div>
    <ul class="drawer-nav-list">
      <li><a href="index.html" class="drawer-nav-item"><span class="txt-ar">الرئيسية</span><span class="txt-en">Home</span></a></li>
      <li><a href="collections.html?filter=all" class="drawer-nav-item"><span class="txt-ar">كافة المجموعات</span><span class="txt-en">All Collections</span></a></li>
      <li><a href="collections.html?filter=yamal" class="drawer-nav-item"><span class="txt-ar">مجموعة يمال SS26</span><span class="txt-en">Yamal SS26</span></a></li>
      <li><a href="collections.html?filter=veil-of-renewal" class="drawer-nav-item"><span class="txt-ar">حجاب التجدد SS25</span><span class="txt-en">Veil of Renewal SS25</span></a></li>
      <li><a href="collections.html?filter=out-of-the-chrysalis" class="drawer-nav-item"><span class="txt-ar">خارج الشرنقة</span><span class="txt-en">Out of the Chrysalis</span></a></li>
      <li><a href="collections.html?filter=elan-vital" class="drawer-nav-item"><span class="txt-ar">إيلان فيتال</span><span class="txt-en">Élan Vital</span></a></li>
      <li><a href="under-the-spotlight.html" class="drawer-nav-item active" style="color:var(--color-accent-gold);"><span class="txt-ar">تحت الأضواء (Red Carpet)</span><span class="txt-en">Under The Spotlight</span></a></li>
      <li><a href="about-us.html" class="drawer-nav-item"><span class="txt-ar">عن الدار والحرفية</span><span class="txt-en">About The House</span></a></li>
      <li><a href="checkout.html" class="drawer-nav-item"><span class="txt-ar">إتمام الطلب الملكي</span><span class="txt-en">Checkout</span></a></li>
    </ul>
  </aside>

  <!-- Search Modal -->
  <div class="search-modal-backdrop" id="searchModalBackdrop" onclick="window.app.closeSearchModal()">
    <div class="search-modal-box" onclick="event.stopPropagation()">
      <div class="search-input-wrap">
        <i data-feather="search" style="color:var(--color-accent-gold);"></i>
        <input type="text" id="globalSearchInput" placeholder="ابحثي عن فستان، مجموعة، أو مناسبة..." oninput="window.app.handleSearchInput(this.value)">
        <button class="search-close-btn" onclick="window.app.closeSearchModal()" aria-label="Close search">
          <i data-feather="x"></i>
        </button>
      </div>
      <div class="search-results-list" id="searchResultsList"></div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="footer-grid">
      <div class="footer-col">
        <div class="footer-logo">
          <img src="logo.svg" alt="Waad Aloqaili Emblem" style="height:36px; width:auto; margin-bottom:8px;">
          <span style="font-family:var(--font-serif); font-size:1.3rem; font-weight:800; color:var(--color-accent-gold); display:block;">Waad Aloqaili</span>
        </div>
        <p style="color:var(--color-accent-gold-light); font-size:0.88rem; line-height:1.8; margin-top:1rem;">
          <span class="txt-ar">دار أزياء سعودية راقية تجسد فخامة الهوت كوتور والحرفية الملكية، مستلهمة من التراث الأصيل لتتألق على أكبر المحافل العالمية.</span>
          <span class="txt-en">A distinguished Saudi Haute Couture house exemplifying regal craftsmanship, architectural tailoring, and timeless elegance on the world stage.</span>
        </p>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading"><span class="txt-ar">المجموعات</span><span class="txt-en">Collections</span></h4>
        <ul class="footer-links">
          <li><a href="collections.html?filter=yamal"><span class="txt-ar">مجموعة يمال SS26</span><span class="txt-en">Yamal SS26</span></a></li>
          <li><a href="collections.html?filter=veil-of-renewal"><span class="txt-ar">حجاب التجدد SS25</span><span class="txt-en">Veil of Renewal SS25</span></a></li>
          <li><a href="collections.html?filter=out-of-the-chrysalis"><span class="txt-ar">خارج الشرنقة</span><span class="txt-en">Out of the Chrysalis</span></a></li>
          <li><a href="collections.html?filter=elan-vital"><span class="txt-ar">إيلان فيتال</span><span class="txt-en">Élan Vital</span></a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading"><span class="txt-ar">تحت الأضواء</span><span class="txt-en">Under The Spotlight</span></h4>
        <ul class="footer-links">
          <li><a href="under-the-spotlight.html"><span class="txt-ar">مهرجان كان السينمائي</span><span class="txt-en">Cannes Film Festival</span></a></li>
          <li><a href="under-the-spotlight.html"><span class="txt-ar">جوائز Joy Awards</span><span class="txt-en">Joy Awards</span></a></li>
          <li><a href="under-the-spotlight.html"><span class="txt-ar">أسبوع الموضة بالرياض</span><span class="txt-en">Riyadh Fashion Week</span></a></li>
          <li><a href="under-the-spotlight.html"><span class="txt-ar">حفل الأوسكار ومهرجان فينيسيا</span><span class="txt-en">Oscars & Venice</span></a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading"><span class="txt-ar">خدمة العملاء</span><span class="txt-en">Client Relations</span></h4>
        <ul class="footer-links">
          <li><a href="about-us.html"><span class="txt-ar">عن الدار والحرفية</span><span class="txt-en">About The House</span></a></li>
          <li><a href="about-us.html#atelier"><span class="txt-ar">حجز موعد بالأوتيليه</span><span class="txt-en">Book Atelier Appointment</span></a></li>
          <li><a href="checkout.html"><span class="txt-ar">الشحن والتوصيل الملكي</span><span class="txt-en">White-Glove Shipping</span></a></li>
          <li><a href="about-us.html#contact"><span class="txt-ar">تواصل معنا</span><span class="txt-en">Contact Concierge</span></a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Waad Aloqaili Haute Couture. All Rights Reserved. جميع الحقوق محفوظة لدار وعد العقيلي للأزياء الراقية.</p>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="data.js"></script>
  <script src="app.js"></script>
  
  <script>
    // Spotlight Events Database
    window.SPOTLIGHT_DATABASE = """ + db_json + """;

    // View Switcher (Events vs All Looks)
    window.switchSpotlightView = function(viewType) {
      const eventsGrid = document.getElementById('eventsGridLayout');
      const looksGrid = document.getElementById('looksGalleryLayout');
      const tabEvents = document.getElementById('tabEventsView');
      const tabLooks = document.getElementById('tabLooksView');

      if (viewType === 'events') {
        eventsGrid.classList.add('active');
        eventsGrid.classList.remove('hidden');
        looksGrid.classList.remove('active');
        tabEvents.classList.add('active');
        tabLooks.classList.remove('active');
      } else {
        eventsGrid.classList.remove('active');
        eventsGrid.classList.add('hidden');
        looksGrid.classList.add('active');
        tabEvents.classList.remove('active');
        tabLooks.classList.add('active');
      }
      if (window.feather) feather.replace();
    };

    // Filter Function
    window.filterAllSpotlight = function(categoryKey, btnElem) {
      document.querySelectorAll('.filter-btn-pill').forEach(b => b.classList.remove('active'));
      if (btnElem) btnElem.classList.add('active');

      const eventCards = document.querySelectorAll('.spotlight-event-card');
      const lookCards = document.querySelectorAll('.look-gallery-card');

      eventCards.forEach(c => {
        const cat = c.getAttribute('data-category');
        if (categoryKey === 'ALL' || cat === categoryKey) {
          c.style.display = 'flex';
        } else {
          c.style.display = 'none';
        }
      });

      lookCards.forEach(c => {
        const cat = c.getAttribute('data-category');
        if (categoryKey === 'ALL' || cat === categoryKey) {
          c.style.display = 'flex';
        } else {
          c.style.display = 'none';
        }
      });
    };

    // Open Event Modal
    window.openEventModal = function(eventId) {
      const idx = parseInt(eventId.replace('event_', '')) - 1;
      const eventData = window.SPOTLIGHT_DATABASE[idx];
      if (!eventData) return;

      document.getElementById('modalHeroImg').src = eventData.main_image;
      document.getElementById('modalHeroTitle').textContent = eventData.main_title;
      document.getElementById('modalIntroText').textContent = eventData.intro_text || eventData.main_desc;

      const looksGrid = document.getElementById('modalSublooksGrid');
      looksGrid.innerHTML = '';

      if (eventData.sub_items && eventData.sub_items.length > 0) {
        eventData.sub_items.forEach((item, i) => {
          const el = document.createElement('div');
          el.className = 'modal-look-item';
          const safeCap = (item.caption || '').replace(/'/g, "\\'");
          el.innerHTML = `
            <div class="modal-look-img-wrap" onclick="window.openLightbox('${item.image}', '${safeCap}')">
              <img src="${item.image}" alt="Look ${i+1}" class="modal-look-img" loading="lazy">
            </div>
            ${item.caption ? `<div class="modal-look-caption">${item.caption}</div>` : ''}
          `;
          looksGrid.appendChild(el);
        });
      } else {
        looksGrid.innerHTML = `
          <div class="modal-look-item">
            <div class="modal-look-img-wrap" onclick="window.openLightbox('${eventData.main_image}', '${(eventData.intro_text || eventData.main_desc).replace(/'/g, "\\'")}')">
              <img src="${eventData.main_image}" alt="${eventData.main_title}" class="modal-look-img">
            </div>
            <div class="modal-look-caption">${eventData.intro_text || eventData.main_desc}</div>
          </div>
        `;
      }

      document.getElementById('spotlightModal').classList.add('active');
      document.body.style.overflow = 'hidden';
      if (window.feather) feather.replace();
    };

    window.closeEventModalDirect = function() {
      document.getElementById('spotlightModal').classList.remove('active');
      document.body.style.overflow = '';
    };

    window.closeEventModal = function(e) {
      if (e.target.id === 'spotlightModal') {
        window.closeEventModalDirect();
      }
    };

    // Lightbox Functionality
    window.openLightbox = function(imgSrc, captionText) {
      document.getElementById('lightboxImg').src = imgSrc;
      document.getElementById('lightboxCaption').textContent = captionText || '';
      document.getElementById('lightboxModal').classList.add('active');
    };

    window.closeLightboxDirect = function() {
      document.getElementById('lightboxModal').classList.remove('active');
    };

    window.closeLightbox = function(e) {
      if (e.target.id === 'lightboxModal') {
        window.closeLightboxDirect();
      }
    };

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        window.closeLightboxDirect();
        window.closeEventModalDirect();
      }
    });

    document.addEventListener('DOMContentLoaded', () => {
      if (window.feather) feather.replace();
    });
  </script>
</body>
</html>
"""

with open('under-the-spotlight.html', 'w', encoding='utf-8') as f:
    f.write(template)

print("Saved under-the-spotlight.html successfully with dual mode and all verified looks & captions!")
