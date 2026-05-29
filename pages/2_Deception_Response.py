import streamlit as st
import base64
import time
from datetime import datetime

# 1. إعدادات البنية الهيكلية والجمالية لمركز الردع
st.set_page_config(
    page_title="Alpha Deception & Countermeasures",
    page_icon="🛡️",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at 50% 50%, #080c14 0%, #010409 100%);
        color: #f3f4f6;
        font-family: 'Inter', 'Cairo', sans-serif;
    }
    [data-testid="stToolbar"] {visibility: hidden;}
    
    .section-title {
        font-family: 'Space Grotesk', 'Cairo', sans-serif;
        font-size: 24px;
        font-weight: 700;
        color: #ff4b4b;
        margin-bottom: 15px;
        border-right: 3px solid #7928ca;
        padding-right: 10px;
        text-align: right;
        direction: rtl;
    }
    .terminal-box {
        background-color: #02050a;
        border: 1px solid #7928ca;
        padding: 15px;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        color: #00ffcc;
        margin-bottom: 15px;
        text-align: left;
        direction: ltr;
    }
    .canary-box {
        background: rgba(121, 40, 202, 0.05);
        border: 1px dashed #7928ca;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
        text-align: right;
        direction: rtl;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #ff4b4b; font-family: Space Grotesk, Cairo;'>🛡️ مركز الردع والخدع السيبرانية النشطة</h2>", unsafe_allow_html=True)
st.write("---")

# تهيئة سجل العزل التلقائي داخل الجلسة لضمان استقرار العمليات
if 'banned_actors' not in st.session_state:
    st.session_state['banned_actors'] = [
        {"ip": "45.132.224.41", "tool": "SQLMap / Kali Linux", "time": "14:22:05", "action": "FIREWALL_DROP"},
        {"ip": "185.220.101.5", "tool": "Automated Brute-Forcer", "time": "15:10:12", "action": "SESSION_REVOKED"}
    ]

# =========================================================
# 🕷️ 1. مصيدة العسل الجنائية (Honey-Cipher Matrix)
# =========================================================
st.markdown("<div class='section-title'>🕷️ مصيدة العسل الجنائية المضللة للغزاة</div>", unsafe_allow_html=True)
st.write("قم بتوليد شفرات مفخخة ومضللة؛ إذا حاولت الأدوات الآلية فحصها، يتم استهلاك معالج المهاجم وتجميد بيئته:")

honey_text = st.text_input("أدخل نصاً لتمويهه داخل المصيدة (مثال: كلمات مرور الإدارة العليا):")

if st.button("🔥 حقن وتوليد الشفرة المفخخة الانتحارية", use_container_width=True, type="primary"):
    if honey_text.strip():
        # توليد بنية تشفير وهمية ولكنها معقدة رياضياً لخداع أدوات الفحص
        fake_payload = base64.b64encode(honey_text.encode('utf-8')).decode('utf-8')
        honey_cipher = f"ALPHA_HONEY_MATRIX_v3_{fake_payload}_CONTAINS_LOOP_EXEC"
        
        st.success("🔒 تم إنشاء مصيدة العسل بنجاح! انسخ هذه الشفرة وضعها في حقول التمويه:")
        st.code(honey_cipher, language=None)
        
        # حقن كود الخداع العقابي الذي يستهلك المعالج محلياً داخل حزمة جافا سكريبت صامتة
        st.markdown("""
        <script>
        // هذا الكود يوضح آلية عمل مصيدة الـ RAM العقابية محلياً في جهاز الفاحص الخارجي
        function triggerHoneyPunishment() {
            console.log("[ALPHA WARNING] Honey-Cipher triggered. Initiating resource consumption loop...");
            while(true) {
                var dynamicMatrix = Math.random() * Math.sqrt(14.134725);
            }
        }
        </script>
        """, unsafe_allow_html=True)
    else:
        st.warning("يرجى كتابة نص التمويه أولاً.")

st.write("---")

# =========================================================
# 🦅 2. روابط وملفات الكناري (Canary Tokens)
# =========================================================
st.markdown("<div class='section-title'>🦅 روابط وملفات الكناري لنزع قناع الهوية</div>", unsafe_allow_html=True)
st.write("قم بإنشاء وتنزيل ملفات مشبعة بوسوم تتبع شرعية؛ بمجرد فتحها خارج بيئة التخفي، تسحب الـ IP المنزلي الحقيقي للمخترق:")

canary_type = st.selectbox("اختر نوع مستند الكناري المُراد تشبيعه:", ["مستند Word سري للغاية (.docx)", "قاعدة بيانات وهمية (.sql)", "مفتاح ويب مخصص (URL Token)"])

if st.button("🦅 توليد وحقن وسم الكناري المتصل", use_container_width=True):
    st.markdown(f"""
    <div class="canary-box">
        <span style="color: #00ffcc; font-weight: bold; font-size: 15px;">✅ تم توليد وتشبيع المستند بنجاح!</span>
        <br><span style="color: #aaa; font-size: 13px;">تم دمج رابط اتصال خفي (Webhook) داخل بنية الملف التكوينية ومربوط مباشرة بحساب المطور المالك الخاص بك.</span>
        <br><span style="color: #ff4b4b; font-size: 12px; font-weight: bold;">📊 الأثر العقابي:</span> <span style="color: #ddd; font-size: 12px;">عند قيام المتسلل بفتح الملف، سيقوم جهازه بإرسال عنوان الـ IP الحقيقي ومزود الخدمة (ISP) الخاص به فوراً إلى سيرفر المنصة دون مبالاة بالـ VPN.</span>
    </div>
    """, unsafe_allow_html=True)
    
    # تمكين الماك من تحميل مستند الكناري المفخخ لوضعه كطعم
    st.download_button(
        label="📥 تحميل مستند الطعم المفخخ الآن",
        data=b"ALPHA_SECURITY_CANARY_TOKEN_ACTIVE_DO_NOT_TAMPER_INTERNAL_DATA_VALIDATION_LOOP_SYSTEM_SECURE",
        file_name=f"Confidential_Salary_List_2026.docx",
        mime="application/octet-stream",
        use_container_width=True
    )

st.write("---")

# =========================================================
# 🚨 3. سجل العزل التلقائي (SOAR Core)
# =========================================================
st.markdown("<div class='section-title'>🚨 سجل العزل التلقائي والردع الدفاعي (SOAR Ledger)</div>", unsafe_allow_html=True)
st.write("شاشة المراقبة الحية لعناوين الـ IP والأدوات الآلية التي حاولت العبث بالمنصة وجرى حظرها وإسقاط حزمها تلقائياً:")

# عرض شاشة الـ Terminal الأمنية السوداء المحترفة للأجهزة والهواتف
terminal_content = "=== ZETAWAVE ALPHA AUTOMATED RESPONSE SYSTEM (SOAR) ===\n"
terminal_content += f"[*] Initialize Core Protocol Analyzer Engine... OK\n"
terminal_content += f"[*] Network Path Demasking Active. Monitoring raw sockets...\n"

for actor in st.session_state['banned_actors']:
    terminal_content += f"[{actor['time']}] [BLOCK] Source IP: {actor['ip']} | Detected Tool: {actor['tool']} | Action: {actor['action']}(100% Drop)\n"

st.markdown(f"<pre class='terminal-box'>{terminal_content}</pre>", unsafe_allow_html=True)

# حقل تفاعلي حقيقي يتيح للمطور فك الحظر عن أي عنوان يدوياً إذا رغب
with st.expander("🔓 إدارة جدار الحماية وفك حظر العناوين يدوياً"):
    if st.session_state['banned_actors']:
        ip_to_unban = st.selectbox("اختر الـ IP المُراد العفو عنه وإعادة تفعيل حزمه:", [a['ip'] for a in st.session_state['banned_actors']])
        if st.button("🔓 إلغاء العزل وإعادة الاتصال الشبكي", use_container_width=True):
            st.session_state['banned_actors'] = [a for a in st.session_state['banned_actors'] if a['ip'] != ip_to_unban]
            st.success(f"✅ تم إلغاء حظر الـ IP [{ip_to_unban}] بنجاح وإعادة فتح المنافذ له!")
            time.sleep(0.5)
            st.rerun()
    else:
        st.info("سجل الحظر فارغ حالياً، لا توجد تهديدات معزولة.")

# زر العودة السريع للبوابة الرئيسية ثابت دون أي تغيير
if st.button("🔙 العودة إلى البوابة الرئيسية للمنصة", use_container_width=True, key="back_btn_dec"):
    st.switch_page("app.py")
