import json
import re

# Load complete scraped DB
with open('full_detailed_spotlight_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# Curated metadata & dates for each item
dates = [
    "يناير 2026 / January 2026",
    "ديسمبر 2025 / December 2025",
    "أكتوبر 2025 / October 2025",
    "مايو 2025 / May 2025",
    "ديسمبر 2024 / December 2024",
    "ديسمبر 2024 / December 2024",
    "أكتوبر 2024 / October 2024",
    "سبتمبر 2024 / September 2024",
    "نوفمبر 2024 / November 2024",
    "مايو 2024 / May 2024",
    "يونيو 2025 / June 2025",
    "مارس 2024 / March 2024",
    "فبراير 2025 / February 2025",
    "يناير 2024 / January 2024",
    "سبتمبر 2023 / September 2023",
    "مايو 2023 / May 2023",
    "فبراير 2024 / February 2024",
    "مايو 2022 / May 2022"
]

categories = [
    {"en": "JOY AWARDS", "ar": "جوائز صنّاع الترفيه"},
    {"en": "RED SEA FILM FESTIVAL", "ar": "مهرجان البحر الأحمر"},
    {"en": "RIYADH FASHION WEEK", "ar": "أسبوع الموضة بالرياض"},
    {"en": "CANNES FILM FESTIVAL", "ar": "مهرجان كان السينمائي"},
    {"en": "HARPER'S BAZAAR", "ar": "هاربرز بازار العربية"},
    {"en": "RED SEA FILM FESTIVAL", "ar": "مهرجان البحر الأحمر"},
    {"en": "RIYADH FASHION WEEK", "ar": "أسبوع الموضة بالرياض"},
    {"en": "VOGUE ARABIA", "ar": "فوغ العربية"},
    {"en": "BILLBOARD ARABIA", "ar": "بيلبورد عربية"},
    {"en": "CANNES FILM FESTIVAL", "ar": "مهرجان كان السينمائي"},
    {"en": "HIA MAGAZINE", "ar": "مجلة هي"},
    {"en": "THE OSCARS", "ar": "جوائز الأوسكار"},
    {"en": "SAUDI CUP", "ar": "كأس السعودية للخيل"},
    {"en": "JOY AWARDS", "ar": "جوائز صنّاع الترفيه"},
    {"en": "VENICE FILM FESTIVAL", "ar": "مهرجان فينيسيا السينمائي"},
    {"en": "CANNES FILM FESTIVAL", "ar": "مهرجان كان السينمائي"},
    {"en": "SAUDI CUP", "ar": "كأس السعودية للخيل"},
    {"en": "CANNES FILM FESTIVAL", "ar": "مهرجان كان السينمائي"}
]

# Exact Arabic & English titles and descriptions
titles_ar = [
    "الدورة السادسة لحفل جوائز صنّاع الترفيه (Joy Awards 2026)",
    "الدورة الخامسة لمهرجان البحر الأحمر السينمائي الدولي",
    "أسبوع الموضة بالرياض – الدورة الثالثة (مجموعة يمال SS26)",
    "الدورة الـ 78 لمهرجان كان السينمائي الدولي (2025)",
    "مجلة هاربرز بازار العربية – عدد ديسمبر 2024",
    "الدورة الرابعة لمهرجان البحر الأحمر السينمائي الدولي",
    "أسبوع الموضة بالرياض – الدورة الثانية (مجموعة SS25)",
    "مجلة فوغ العربية – غلاف سبتمبر 2024 مع كانديس سوانبويل",
    "السجادة الحمراء لحفل بيلبورد عربية (Billboard Arabia)",
    "الدورة الـ 77 لمهرجان كان السينمائي الدولي (2024)",
    "مجلة هي – غلاف شهر يونيو مع كارمن سليمان",
    "حفل جوائز الأوسكار الـ 96 (The 96th Academy Awards)",
    "كأس السعودية للخيل – الدورة السادسة (عام الحرف اليدوية)",
    "حفل جوائز صنّاع الترفيه (Joy Awards 2024)",
    "الدورة الـ 80 لمهرجان البندقية السينمائي الدولي (Venice)",
    "الدورة الـ 76 لمهرجان كان السينمائي الدولي (2023)",
    "كأس السعودية للخيل – الدورة الخامسة",
    "الدورة الـ 75 لمهرجان كان السينمائي الدولي (2022)"
]

titles_en = [
    "The 6th Edition of the Joy Awards",
    "The 5th Edition of the Red Sea Film Festival",
    "The Third Edition of Riyadh Fashion Week",
    "The 78th Edition of the Cannes Film Festival",
    "December 2024 Issue of Harper’s Bazaar Arabia",
    "The 4th Edition of the Red Sea Film Festival",
    "The Second Edition of Riyadh Fashion Week",
    "September 2024 Issue of Vogue Arabia",
    "Billboard Arabia Red Carpet",
    "The 77th Annual Cannes Film Festival",
    "June 2025 Issue of Hia Magazine",
    "The 96th Academy Awards (Oscars)",
    "The Sixth Edition of the Saudi Cup",
    "Joy Awards (2024)",
    "The 80th Venice International Film Festival",
    "The 76th Edition of the Cannes Film Festival",
    "The Fifth Edition of the Saudi Cup",
    "The 75th Edition of the Cannes Film Festival"
]

descs_ar = [
    "في الدورة السادسة من حفل جوائز Joy Awards، كشفت دار وعد العقيلي كوتور عن تصاميم استثنائية من مجموعة ربيع وصيف 2026 'يمال'، تميزت بالقصات المنحوتة والمزدانة بعرق اللؤلؤ الطبيعي على كوكبة من النجمات العالميات كالنجمة كاتي بيري وهدى المفتي ومريم الناصر.",
    "في قلب جدة التاريخية، تألقت إبداعات دار وعد العقيلي على السجادة الحمراء للدورة الخامسة لمهرجان البحر الأحمر بتصاميم كوتور ساحرة مستوحاة من أعماق البحر والأصداف على النجمة درة زروق وروز البندر وهمس بندر.",
    "عرض أزياء مذهل في أسبوع الموضة بالرياض لمجموعة كوتور ربيع وصيف 2026 'يمال'، مستعرضاً أرقى مهارات الحرفية السعودية وقصات الكوتور الانسيابية بحضور نخبة من أيقونات الموضة والضيوف المرموقين.",
    "على السجادة الحمراء لقصر المهرجانات في كان، خطفت دار وعد العقيلي الأنظار بإطلالات كوتور ملكية ارتدتها عارضة الأزياء العالمية غريس إليزابيث وهنا كروس ولو-آن.",
    "جلسة تصوير تحريرية واحتفاء خاص بحرفية الدار السعودية وتميزها في صناعة الهوت كوتور في عدد ديسمبر 2024 من مجلة هاربرز بازار العربية، متألقة بالريش الأسود الهندسي وتفاصيل الكريستال.",
    "في الدورة الرابعة لمهرجان البحر الأحمر، تألقت النجمة مي عمر بفستان زمردي أيقوني والإعلامية أجواء الجودي بتطريزات الزهور اليدوية الدقيقة من مجموعة 'حجاب التجدد' لربيع وصيف 2025.",
    "خلال الدورة الثانية لأسبوع الموضة بالرياض، قدمت دار وعد العقيلي مجموعتها لربيع وصيف 2025 بإطلالات مميزة ارتدتها روز البندر وخولة الشيبان وليان الحفار.",
    "تكريماً لأعماق وسحر البحر الأحمر والشعاب المرجانية، تألقت العارضة العالمية وسفيرة المحيطات كانديس سوانبويل على غلاف فوغ العربية بفستان كوتور استثنائي مكسر يدوياً من أقمشة صديقة للبيئة.",
    "تألقت ربا طرسون على سجادة بيلبورد عربية بفستان كوتور ساحر من دار وعد العقيلي لربيع وصيف 2025 'حجاب التجدد' المستوحى من نقاء زهرة اللوتس وحيوان اليعسوب.",
    "حضور لافت لدار وعد العقيلي على السجادة الحمراء لمهرجان كان الـ 77، بتصاميم هوت كوتور ارتدتها أليس عبد العزيز ونادين عبد العزيز وأوليفيا يانغ في عشاء لوريال باريس.",
    "الفنانة كارمن سليمان تتصدر غلاف مجلة هي لعدد يونيو احتفاءً بشهر الموسيقى بفستان 'السيمفونية' الفاخر من مجموعة حجاب التجدد لوعد العقيلي.",
    "حضور سعودي تاريخي في هوليوود على السجادة الحمراء لحفل الأوسكار الـ 96، حيث ارتدت النجمة العالمية آشلي فستان كوتور عاجي مطرزاً بالفراشات الفضية وذيل التول الملكي.",
    "احتفاءً بعام الحرف اليدوية، صممت دار وعد العقيلي إطلالة استثنائية من 132 متراً من القماش المشبع باللافندر الطبيعي للجوف وست درجات بنفسجية بديعة تعكس التراث والأصالة.",
    "في حفل Joy Awards، تألقت أسيل محمد وأجواء الجودي ونيكول سعفان بتصاميم كوتور خاصة بتطريزات الفراشات والكريستال والقفازات المخملية الفاخرة.",
    "شهد مهرجان البندقية السينمائي الثمانين تألق فرح عبد العزيز بالفستان الأحمر من مجموعة 'خارج الشرنقة' ونادين عبد العزيز بفستان كوتور أسود مذهل.",
    "في مهرجان كان السينمائي الـ 76، سحرت مجموعة 'خارج الشرنقة' الحضور بتصاميم ارتدتها جيسيكا دي أوليفيرا، داريا كيريليوك، إيلينا بدري، وصوفيا سعيدي بفستان الفراشة 'بابيون'.",
    "في أتيليه وعد العقيلي بالرياض، تم صياغة ثوب ملكي بديع يعكس العراقة والأصالة التراثية لسباقات كأس السعودية للخيل.",
    "البداية التاريخية لتألق الدار في مهرجان كان الـ 75 بمجموعة 'إيلان فيتال' مع مهلاقا جابري، كلاوديا بوزا، جوزفين سكرايفر، وريبيكا كونيكوفسكي."
]

descs_en = [
    "At the 6th edition of the Joy Awards, Waad Aloqaili Couture unveiled standout creations from its SS26 ‘YAMAL’ collection, defined by sculpted forms and mother-of-pearl craftsmanship worn by international pop icon Katy Perry, Huda El Mufti, Maryam Alnasser, Lama Abdullwahab, and Nicole Saafan.",
    "For the 5th Red Sea Film Festival in historic Jeddah, Waad Aloqaili Couture presented standout creations from its SS26 ‘YAMAL’ collection, celebrated by Dorra Zarrouk, Rose Al Bandar, and Hams Bandar.",
    "A breathtaking runway showcase by Waad Aloqaili featuring the Spring/Summer 2026 Yamal couture collection, paying homage to Saudi Arabia's heritage with guests of honor Nour Elboboo, Ruba Tursun, Lara Alamri, and Khawlah Alshyban.",
    "At the 78th Annual Cannes Film Festival, Waad Aloqaili Couture unveiled exquisite creations worn on the world's most prestigious red carpet by top model Grace Elizabeth, Hana Cross, and Lou-ann.",
    "A dedicated editorial tribute celebrating the artisanal craftsmanship and haute couture architecture of designer Waad Aloqaili in the December 2024 issue of Harper’s Bazaar Arabia.",
    "For the 4th Red Sea Film Festival, Waad Aloqaili Couture presented standout creations from its SS25 ‘Veil of Renewal’ collection worn by Egyptian star Mai Omar and TV presenter Ajwa Aljoudi.",
    "During the second edition of Riyadh Fashion Week, Waad Aloqaili Couture presented its Spring/Summer 2025 collection, modeled by Rose Albander, Khawlah Alshyban, and Layan Alhaffar.",
    "A tribute to the enchanting depths of the Red Sea, supermodel and ocean advocate Candice Swanepoel graces the cover of Vogue Arabia wearing a custom gown by Waad Aloqaili Couture.",
    "Ruba Tursun captivated the Billboard Arabia red carpet in Waad Aloqaili Couture SS25 ‘Veil of Renewal’, inspired by the elegance of the lotus flower and iridescent dragonflies.",
    "Waad Aloqaili Couture made a distinguished appearance at the 77th Annual Cannes Film Festival, dressing Alice Abdelaziz, Nadine Abdelaziz, and Olivia Yang for the L’Oréal Paris gala.",
    "Carmen Soliman graces the June cover of Hia Magazine celebrating Music Month in the breathtaking 'Symphony' gown by Waad Aloqaili Couture.",
    "On the prestigious red carpet of the 96th Academy Awards in Hollywood, international celebrity Ashley was draped in an exquisite ivory bespoke gown by Waad Aloqaili Couture.",
    "Celebrating Saudi Arabia's Year of Handicrafts, an iconic ensemble crafted from 132 meters of Al-Jouf lavender-dyed fabric with six violet gradients and geometric heritage weaving.",
    "At the Joy Awards, Waad Aloqaili Couture adorned celebrated figures Asail Mohammed, Ajwa Aljoudi, and Nicole Saafan in bespoke crystal and velvet couture gowns.",
    "The 80th Venice Film Festival bore witness to the mesmerizing presence of Waad Aloqaili Couture, featuring Farah Abdelaziz in scarlet red and Nadine Abdelaziz at the Dali premiere.",
    "The 76th Annual Cannes Film Festival witnessed the presence of Waad Aloqaili's 'Out of the Chrysalis' collection, worn by Jessica de Oliveira, Daria Kyryliuk, Elena Badri, and Sofia Saidi in the 'Papillon' crystal gown.",
    "In the ateliers of Waad Aloqaili Couture, an iconic gown was exquisitely crafted, mirroring the cultural majesty of the Saudi Cup.",
    "Waad Aloqaili Couture House made a stunning impact at the star-studded 75th Annual Cannes Film Festival with the 'Élan Vital' collection worn by Mahlagha Jaberi, Cláudia Bouza, Josephine Skriver, and Rebecca Kunikowski."
]

# Build JSON payload for client-side modal data
client_events_data = []

# Generate Grid Cards HTML
cards_html = []

for idx, ev in enumerate(db):
    i = idx
    ev_obj = {
        "id": f"story_{i+1}",
        "index": i + 1,
        "title_ar": titles_ar[i],
        "title_en": titles_en[i],
        "category_ar": categories[i]["ar"],
        "category_en": categories[i]["en"],
        "date_badge": dates[i],
        "desc_ar": descs_ar[i],
        "desc_en": descs_en[i],
        "hero_img": ev["main_image"],
        "sub_items": ev.get("sub_items", [])
    }
    client_events_data.append(ev_obj)
    
    card = f'''
    <!-- Story Card {i+1} -->
    <article class="spotlight-story-card scroll-reveal" data-story-id="story_{i+1}" onclick="window.openStoryModal('story_{i+1}')">
      <div class="spotlight-img-wrap">
        <img src="{ev['main_image']}" alt="{titles_en[i]}" class="spotlight-main-img" loading="lazy">
        <span class="spotlight-date-badge">{dates[i].split('/')[0].strip()}</span>
        <div class="spotlight-overlay-hover">
          <span class="spotlight-quick-view-btn">
            <i data-feather="eye" style="width:16px;height:16px; margin-inline-end:6px;"></i>
            <span class="txt-ar">عرض تفاصيل التغطية الكاملة</span>
            <span class="txt-en">View Full Coverage & Gallery</span>
          </span>
        </div>
      </div>
      <div class="spotlight-story-content">
        <div class="spotlight-card-top-meta">
          <span class="spotlight-category-tag">
            <span class="txt-ar">{categories[i]['ar']}</span>
            <span class="txt-en">{categories[i]['en']}</span>
          </span>
          <span class="spotlight-photo-count">
            <i data-feather="image" style="width:13px;height:13px; margin-inline-end:4px; vertical-align:middle;"></i>
            {len(ev.get('sub_items', [])) or 1} <span class="txt-ar">صور</span><span class="txt-en">Photos</span>
          </span>
        </div>
        <h3 class="spotlight-story-title">
          <span class="txt-ar">{titles_ar[i]}</span>
          <span class="txt-en">{titles_en[i]}</span>
        </h3>
        <p class="spotlight-story-desc">
          <span class="txt-ar">{descs_ar[i]}</span>
          <span class="txt-en">{descs_en[i]}</span>
        </p>
        <div class="spotlight-story-footer">
          <span class="spotlight-brand-badge">WAAD ALOQAILI COUTURE</span>
          <button type="button" class="spotlight-open-btn" onclick="event.stopPropagation(); window.openStoryModal('story_{i+1}')" aria-label="Open Story Details">
            <span class="txt-ar">استكشاف القصة &larr;</span>
            <span class="txt-en">Explore Story &rarr;</span>
          </button>
        </div>
      </div>
    </article>
    '''
    cards_html.append(card)

grid_all_html = "\n".join(cards_html)
json_events_dump = json.dumps(client_events_data, ensure_ascii=False)

full_html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Waad Aloqaili | Under The Spotlight (تحت الأضواء)</title>
  <meta name="description" content="التغطية الرسمية لإطلالات السجادة الحمراء وأغلفة المجلات العالمية لدار وعد العقيلي كوتور: كان، الأوسكار، البندقية، Joy Awards، فوغ، وهاربرز بازار.">
  <meta name="theme-color" content="#2C1A48">
  
  <meta property="og:title" content="Waad Aloqaili – Under The Spotlight | تحت الأضواء">
  <meta property="og:description" content="Red carpet moments and global press features from Cannes, Venice, and the Oscars to Vogue and Harper's Bazaar.">
  <meta property="og:image" content="https://waadaloqaili.com/cdn/shop/files/Photo_17-01-2026_8_08_06_PM.jpg?width=1800">
  
  <link rel="icon" type="image/svg+xml" href="logo.svg">
  <script src="https://unpkg.com/feather-icons"></script>
  <link rel="stylesheet" href="styles.css">
  
  <style>
    /* Language visibility handlers */
    body[data-lang="ar"] .txt-en {{ display: none !important; }}
    body[data-lang="ar"] .txt-ar {{ display: inline !important; }}
    body[data-lang="ar"] span.txt-ar, body[data-lang="ar"] p.txt-ar, body[data-lang="ar"] div.txt-ar, body[data-lang="ar"] h1.txt-ar, body[data-lang="ar"] h2.txt-ar, body[data-lang="ar"] h3.txt-ar, body[data-lang="ar"] h4.txt-ar {{ display: block !important; }}

    body[data-lang="en"] .txt-ar {{ display: none !important; }}
    body[data-lang="en"] .txt-en {{ display: inline !important; }}
    body[data-lang="en"] span.txt-en, body[data-lang="en"] p.txt-en, body[data-lang="en"] div.txt-en, body[data-lang="en"] h1.txt-en, body[data-lang="en"] h2.txt-en, body[data-lang="en"] h3.txt-en, body[data-lang="en"] h4.txt-en {{ display: block !important; }}

    .spotlight-hero-header {{
      background: linear-gradient(135deg, #1D0E32 0%, #2C1A48 60%, #160B26 100%);
      color: #FFFFFF;
      padding: 6.5rem 2rem 5.5rem;
      text-align: center;
      position: relative;
      overflow: hidden;
      border-bottom: 1px solid var(--color-border-dark);
    }}
    .spotlight-hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.8rem;
      font-weight: 800;
      letter-spacing: 0.25em;
      color: var(--color-accent-gold);
      background: rgba(223, 186, 115, 0.12);
      border: 1px solid rgba(223, 186, 115, 0.35);
      padding: 0.5rem 1.4rem;
      margin-bottom: 1.8rem;
      border-radius: 2px;
      text-transform: uppercase;
    }}
    .spotlight-hero-title {{
      font-family: var(--font-couture);
      font-size: clamp(2rem, 5vw, 4.5rem);
      font-weight: 900;
      letter-spacing: 0.08em;
      margin-bottom: 1.2rem;
      text-transform: uppercase;
      line-height: 1.2;
      color: #FFFFFF;
    }}
    .spotlight-hero-subtitle {{
      font-size: clamp(0.95rem, 2vw, 1.2rem);
      color: var(--color-accent-gold-light);
      max-width: 900px;
      margin: 0 auto;
      line-height: 1.8;
      font-weight: 400;
    }}

    .spotlight-filter-bar {{
      background: #FAF8F5;
      border-bottom: 1px solid var(--color-border);
      padding: 1.2rem 2rem;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 1.5rem;
      flex-wrap: wrap;
      position: sticky;
      top: 70px;
      z-index: 40;
      backdrop-filter: blur(10px);
    }}
    body.velvet-dark .spotlight-filter-bar {{
      background: #190F2C;
      border-bottom-color: var(--color-border-dark);
    }}
    .spotlight-filter-chip {{
      background: transparent;
      border: 1px solid var(--color-border);
      color: var(--color-text-primary);
      padding: 0.5rem 1.2rem;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.3s ease;
      letter-spacing: 0.05em;
    }}
    .spotlight-filter-chip:hover, .spotlight-filter-chip.active {{
      background: var(--color-brand-purple);
      color: #FFFFFF;
      border-color: var(--color-brand-purple);
      box-shadow: 0 4px 12px rgba(44, 26, 72, 0.2);
    }}
    body.velvet-dark .spotlight-filter-chip {{
      border-color: rgba(223, 186, 115, 0.2);
      color: var(--color-accent-gold-light);
    }}
    body.velvet-dark .spotlight-filter-chip:hover, body.velvet-dark .spotlight-filter-chip.active {{
      background: var(--color-accent-gold);
      color: #120820;
      border-color: var(--color-accent-gold);
    }}

    .spotlight-feed-container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 4.5rem 2.5rem;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
      gap: 3rem;
    }}
    @media (max-width: 850px) {{
      .spotlight-feed-container {{
        grid-template-columns: 1fr;
        padding: 2rem 1.2rem;
        gap: 2rem;
      }}
      .spotlight-filter-bar {{
        gap: 0.8rem;
        padding: 0.9rem 1rem;
        top: 60px;
      }}
      .spotlight-filter-chip {{
        font-size: 0.75rem;
        padding: 0.4rem 0.9rem;
      }}
    }}

    .spotlight-story-card {{
      background: #FFFFFF;
      border: 1px solid var(--color-border);
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      cursor: pointer;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      border-radius: 2px;
      overflow: hidden;
    }}
    body.velvet-dark .spotlight-story-card {{
      background: #190F2C;
      border-color: rgba(223, 186, 115, 0.15);
    }}
    .spotlight-story-card:hover {{
      transform: translateY(-8px);
      box-shadow: 0 16px 36px rgba(44, 26, 72, 0.18);
      border-color: var(--color-accent-gold);
    }}
    body.velvet-dark .spotlight-story-card:hover {{
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5);
      border-color: var(--color-accent-gold);
    }}

    .spotlight-img-wrap {{
      position: relative;
      width: 100%;
      aspect-ratio: 3 / 4;
      overflow: hidden;
      background: #140B24;
    }}
    .spotlight-main-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .spotlight-story-card:hover .spotlight-main-img {{
      transform: scale(1.05);
    }}

    .spotlight-overlay-hover {{
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(20, 11, 36, 0.85) 0%, rgba(20, 11, 36, 0.2) 60%, transparent 100%);
      display: flex;
      align-items: flex-end;
      justify-content: center;
      padding-bottom: 2rem;
      opacity: 0;
      transition: opacity 0.35s ease;
    }}
    .spotlight-story-card:hover .spotlight-overlay-hover {{
      opacity: 1;
    }}
    .spotlight-quick-view-btn {{
      background: rgba(223, 186, 115, 0.95);
      color: #120820;
      font-size: 0.8rem;
      font-weight: 800;
      letter-spacing: 0.05em;
      padding: 0.65rem 1.4rem;
      border-radius: 2px;
      display: inline-flex;
      align-items: center;
      box-shadow: 0 6px 16px rgba(0,0,0,0.3);
      transform: translateY(10px);
      transition: transform 0.3s ease;
    }}
    .spotlight-story-card:hover .spotlight-quick-view-btn {{
      transform: translateY(0);
    }}

    .spotlight-date-badge {{
      position: absolute;
      top: 16px;
      right: 16px;
      background: rgba(20, 11, 36, 0.88);
      backdrop-filter: blur(8px);
      color: var(--color-accent-gold);
      font-size: 0.75rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      padding: 0.4rem 0.9rem;
      border: 1px solid rgba(223, 186, 115, 0.35);
      z-index: 2;
    }}
    [dir="ltr"] .spotlight-date-badge {{
      right: auto;
      left: 16px;
    }}

    .spotlight-story-content {{
      padding: 2.2rem;
      display: flex;
      flex-direction: column;
      flex: 1;
    }}
    .spotlight-card-top-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.8rem;
    }}
    .spotlight-category-tag {{
      font-size: 0.75rem;
      font-weight: 900;
      letter-spacing: 0.15em;
      color: var(--color-accent-gold);
      text-transform: uppercase;
    }}
    .spotlight-photo-count {{
      font-size: 0.75rem;
      color: var(--color-text-muted);
      font-weight: 600;
    }}
    .spotlight-story-title {{
      font-family: var(--font-serif);
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--color-brand-purple);
      margin-bottom: 0.9rem;
      line-height: 1.4;
      word-break: break-word;
    }}
    body.velvet-dark .spotlight-story-title {{
      color: #FFFFFF;
    }}
    .spotlight-story-desc {{
      font-size: 0.92rem;
      color: var(--color-text-secondary);
      line-height: 1.75;
      margin-bottom: 1.8rem;
      flex: 1;
    }}
    body.velvet-dark .spotlight-story-desc {{
      color: #C8BFD4;
    }}
    .spotlight-story-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid var(--color-border);
      padding-top: 1.2rem;
    }}
    body.velvet-dark .spotlight-story-footer {{
      border-top-color: rgba(223, 186, 115, 0.15);
    }}
    .spotlight-brand-badge {{
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--color-accent-gold);
      letter-spacing: 0.1em;
    }}
    .spotlight-open-btn {{
      background: transparent;
      border: none;
      color: var(--color-brand-purple);
      font-weight: 800;
      font-size: 0.85rem;
      cursor: pointer;
      padding: 0.4rem 0.6rem;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: color 0.3s ease;
    }}
    body.velvet-dark .spotlight-open-btn {{
      color: var(--color-accent-gold-light);
    }}
    .spotlight-open-btn:hover {{
      color: var(--color-accent-gold);
    }}

    /* Detail Modal Styles */
    .story-modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(10, 5, 20, 0.82);
      backdrop-filter: blur(12px);
      z-index: 9999;
      opacity: 0;
      visibility: hidden;
      transition: all 0.35s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2rem;
    }}
    .story-modal-backdrop.open {{
      opacity: 1;
      visibility: visible;
    }}
    .story-modal-container {{
      background: #FFFFFF;
      width: 100%;
      max-width: 1050px;
      max-height: 90vh;
      border-radius: 4px;
      overflow-y: auto;
      border: 1px solid rgba(223, 186, 115, 0.4);
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.5);
      position: relative;
      transform: scale(0.95) translateY(20px);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    body.velvet-dark .story-modal-container {{
      background: #180D2C;
      color: #FFFFFF;
    }}
    .story-modal-backdrop.open .story-modal-container {{
      transform: scale(1) translateY(0);
    }}
    .story-modal-close-btn {{
      position: absolute;
      top: 18px;
      left: 20px;
      background: rgba(20, 11, 36, 0.75);
      color: var(--color-accent-gold);
      border: 1px solid rgba(223, 186, 115, 0.3);
      width: 38px;
      height: 38px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 10;
      transition: all 0.3s ease;
    }}
    [dir="ltr"] .story-modal-close-btn {{
      left: auto;
      right: 20px;
    }}
    .story-modal-close-btn:hover {{
      background: var(--color-accent-gold);
      color: #120820;
      transform: rotate(90deg);
    }}
    .story-modal-header-hero {{
      position: relative;
      height: 380px;
      width: 100%;
      background: #120820;
      overflow: hidden;
    }}
    .story-modal-hero-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      filter: brightness(0.7);
    }}
    .story-modal-header-content {{
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 2.5rem 3rem;
      background: linear-gradient(to top, rgba(18, 8, 32, 0.95) 0%, rgba(18, 8, 32, 0.6) 70%, transparent 100%);
      color: #FFFFFF;
    }}
    .story-modal-title {{
      font-family: var(--font-serif);
      font-size: clamp(1.4rem, 3vw, 2.2rem);
      font-weight: 800;
      margin-bottom: 0.5rem;
      color: #FFFFFF;
    }}
    .story-modal-meta {{
      display: flex;
      gap: 1.5rem;
      align-items: center;
      font-size: 0.85rem;
      color: var(--color-accent-gold);
      font-weight: 700;
    }}
    .story-modal-body {{
      padding: 2.8rem 3rem;
    }}
    .story-modal-lead-text {{
      font-size: 1.1rem;
      line-height: 1.85;
      color: var(--color-text-primary);
      margin-bottom: 2.5rem;
      padding-bottom: 2rem;
      border-bottom: 1px solid var(--color-border);
    }}
    body.velvet-dark .story-modal-lead-text {{
      color: #EDE8F2;
      border-bottom-color: rgba(223, 186, 115, 0.15);
    }}
    .story-modal-looks-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 2rem;
    }}
    .story-look-card {{
      background: #FAF8F5;
      border: 1px solid var(--color-border);
      border-radius: 2px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}
    body.velvet-dark .story-look-card {{
      background: #1F1238;
      border-color: rgba(223, 186, 115, 0.15);
    }}
    .story-look-img-wrap {{
      width: 100%;
      aspect-ratio: 3 / 4;
      overflow: hidden;
      background: #140B24;
    }}
    .story-look-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
    }}
    .story-look-card:hover .story-look-img {{
      transform: scale(1.04);
    }}
    .story-look-caption {{
      padding: 1.2rem;
      font-size: 0.88rem;
      line-height: 1.65;
      color: var(--color-text-secondary);
      flex: 1;
    }}
    body.velvet-dark .story-look-caption {{
      color: #D6CFE0;
    }}
    @media (max-width: 650px) {{
      .story-modal-backdrop {{
        padding: 0;
      }}
      .story-modal-container {{
        max-height: 100vh;
        border-radius: 0;
      }}
      .story-modal-header-hero {{
        height: 260px;
      }}
      .story-modal-header-content {{
        padding: 1.5rem 1.2rem;
      }}
      .story-modal-body {{
        padding: 1.8rem 1.2rem;
      }}
      .story-modal-looks-grid {{
        grid-template-columns: 1fr;
      }}
    }}
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

  <!-- Header -->
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

    <!-- Center Brand Logo -->
    <div class="brand-logo-container">
      <a href="index.html" class="brand-logo-link">
        <img src="logo.svg" alt="Waad Aloqaili Emblem" style="height:32px; width:auto; margin-bottom:2px;">
        <span class="brand-logo-text" id="brandLogo">Waad Aloqaili</span>
      </a>
    </div>

    <!-- Right Header Actions -->
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
  <header class="spotlight-hero-header">
    <div class="spotlight-hero-badge">
      <i data-feather="star" style="width:14px;height:14px;"></i>
      <span class="txt-ar">الأرشيف الصحفي وعروض السجادة الحمراء</span>
      <span class="txt-en">Red Carpet Archive & Press Features</span>
    </div>
    <h1 class="spotlight-hero-title">
      <span class="txt-ar">تحت الأضواء</span>
      <span class="txt-en">Under The Spotlight</span>
    </h1>
    <p class="spotlight-hero-subtitle">
      <span class="txt-ar">رحلة توثيقية ترصد تألق إبداعات دار وعد العقيلي للأزياء الراقية على كبرى المحافل العالمية من مهرجان كان السينمائي والبندقية إلى الأوسكار، وأغلفة كبرى المجلات الدولية.</span>
      <span class="txt-en">A curated retrospective of Waad Aloqaili Haute Couture illuminating the world's most prestigious stages from Cannes, Venice, and the Oscars to the covers of Vogue and Harper's Bazaar.</span>
    </p>
  </header>

  <!-- Filter Bar -->
  <div class="spotlight-filter-bar">
    <button class="spotlight-filter-chip active" onclick="window.filterSpotlight('all', this)">
      <span class="txt-ar">الكل (18 مناسبة)</span>
      <span class="txt-en">All (18 Stories)</span>
    </button>
    <button class="spotlight-filter-chip" onclick="window.filterSpotlight('CANNES', this)">
      <span class="txt-ar">مهرجان كان</span>
      <span class="txt-en">Cannes Festival</span>
    </button>
    <button class="spotlight-filter-chip" onclick="window.filterSpotlight('JOY AWARDS', this)">
      <span class="txt-ar">جوائز Joy Awards</span>
      <span class="txt-en">Joy Awards</span>
    </button>
    <button class="spotlight-filter-chip" onclick="window.filterSpotlight('RED SEA', this)">
      <span class="txt-ar">مهرجان البحر الأحمر</span>
      <span class="txt-en">Red Sea Festival</span>
    </button>
    <button class="spotlight-filter-chip" onclick="window.filterSpotlight('RIYADH', this)">
      <span class="txt-ar">أسبوع الموضة بالرياض</span>
      <span class="txt-en">Riyadh Fashion Week</span>
    </button>
    <button class="spotlight-filter-chip" onclick="window.filterSpotlight('MAGAZINE', this)">
      <span class="txt-ar">أغلفة المجلات العالمية</span>
      <span class="txt-en">Editorial & Covers</span>
    </button>
    <button class="spotlight-filter-chip" onclick="window.filterSpotlight('SAUDI CUP', this)">
      <span class="txt-ar">كأس السعودية</span>
      <span class="txt-en">Saudi Cup</span>
    </button>
  </div>

  <!-- Editorial Story Grid (18 Official Events) -->
  <main class="spotlight-feed-container" id="spotlightContainer">
{grid_all_html}
  </main>

  <!-- Rich Modal for Story Detail & Full Gallery -->
  <div class="story-modal-backdrop" id="storyModal" onclick="window.closeStoryModal(event)">
    <div class="story-modal-container" onclick="event.stopPropagation()">
      <button type="button" class="story-modal-close-btn" onclick="window.closeStoryModalDirect()" aria-label="Close Modal">
        <i data-feather="x"></i>
      </button>
      <div class="story-modal-header-hero">
        <img src="" alt="Story Hero" class="story-modal-hero-img" id="modalHeroImg">
        <div class="story-modal-header-content">
          <div class="story-modal-meta">
            <span id="modalCategory">RED CARPET</span>
            <span>&bull;</span>
            <span id="modalDate">2026</span>
          </div>
          <h2 class="story-modal-title" id="modalTitle">Event Title</h2>
        </div>
      </div>
      <div class="story-modal-body">
        <p class="story-modal-lead-text" id="modalDesc"></p>
        <h4 style="font-family:var(--font-serif); font-size:1.3rem; margin-bottom:1.5rem; color:var(--color-accent-gold);">
          <span class="txt-ar">إطلالات وتفاصيل الحضور الرسمي</span>
          <span class="txt-en">Celebrity Looks & Couture Details</span>
        </h4>
        <div class="story-modal-looks-grid" id="modalLooksGrid"></div>
      </div>
    </div>
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
    // Spotlight Events Database Injection
    window.SPOTLIGHT_EVENTS = {json_events_dump};

    // Filter Stories Function
    window.filterSpotlight = function(categoryKey, btnElem) {{
      document.querySelectorAll('.spotlight-filter-chip').forEach(c => c.classList.remove('active'));
      if (btnElem) btnElem.classList.add('active');

      const cards = document.querySelectorAll('.spotlight-story-card');
      cards.forEach(card => {{
        const storyId = card.getAttribute('data-story-id');
        const story = window.SPOTLIGHT_EVENTS.find(s => s.id === storyId);
        if (!story) return;

        if (categoryKey === 'all') {{
          card.style.display = 'flex';
        }} else if (categoryKey === 'MAGAZINE') {{
          const isMag = story.category_en.includes('HARPER') || story.category_en.includes('VOGUE') || story.category_en.includes('HIA') || story.category_en.includes('BILLBOARD');
          card.style.display = isMag ? 'flex' : 'none';
        }} else {{
          const matches = story.category_en.toUpperCase().includes(categoryKey) || story.title_en.toUpperCase().includes(categoryKey);
          card.style.display = matches ? 'flex' : 'none';
        }}
      }});
    }};

    // Open Interactive Story Modal
    window.openStoryModal = function(storyId) {{
      const story = window.SPOTLIGHT_EVENTS.find(s => s.id === storyId);
      if (!story) return;

      const isAr = (document.body.getAttribute('data-lang') || 'ar') === 'ar';
      document.getElementById('modalHeroImg').src = story.hero_img;
      document.getElementById('modalHeroImg').alt = isAr ? story.title_ar : story.title_en;
      document.getElementById('modalCategory').textContent = isAr ? story.category_ar : story.category_en;
      document.getElementById('modalDate').textContent = story.date_badge.split('/')[isAr ? 0 : 1].trim();
      document.getElementById('modalTitle').textContent = isAr ? story.title_ar : story.title_en;
      document.getElementById('modalDesc').textContent = isAr ? story.desc_ar : story.desc_en;

      // Populate Looks Grid
      const looksGrid = document.getElementById('modalLooksGrid');
      looksGrid.innerHTML = '';

      if (story.sub_items && story.sub_items.length > 0) {{
        story.sub_items.forEach((item, idx) => {{
          const card = document.createElement('div');
          card.className = 'story-look-card';
          card.innerHTML = `
            <div class="story-look-img-wrap">
              <img src="${{item.image}}" alt="Look ${{idx+1}}" class="story-look-img" loading="lazy">
            </div>
            ${{item.caption ? `<div class="story-look-caption">${{item.caption}}</div>` : ''}}
          `;
          looksGrid.appendChild(card);
        }});
      }} else {{
        looksGrid.innerHTML = `
          <div class="story-look-card">
            <div class="story-look-img-wrap">
              <img src="${{story.hero_img}}" alt="${{story.title_en}}" class="story-look-img">
            </div>
            <div class="story-look-caption">${{isAr ? story.desc_ar : story.desc_en}}</div>
          </div>
        `;
      }}

      document.getElementById('storyModal').classList.add('open');
      document.body.style.overflow = 'hidden';
      if (window.feather) feather.replace();
    }};

    window.closeStoryModalDirect = function() {{
      document.getElementById('storyModal').classList.remove('open');
      document.body.style.overflow = '';
    }};

    window.closeStoryModal = function(e) {{
      if (e.target.id === 'storyModal') {{
        window.closeStoryModalDirect();
      }}
    }};

    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') {{
        window.closeStoryModalDirect();
      }}
    }});

    document.addEventListener('DOMContentLoaded', () => {{
      if (window.feather) feather.replace();
    }});
  </script>
</body>
</html>
'''

with open('under-the-spotlight.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Saved updated under-the-spotlight.html successfully with all 18 official stories!")
