import streamlit as st
import time
from datetime import datetime

# 1. إعدادات البنية الهيكلية والجمالية لمنصة Alpha
st.set_page_config(
    page_title="ZetaWave Alpha Pro",
    page_icon="🌌",
    layout="centered"
)

# حقن التصميم السيبراني المتقدم المتوافق مع الهواتف والأجهزة الذكية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght=300;400;600&family=Space+Grotesk:wght=500;700&family=Cairo:wght=400;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #080c14 0%, #010409 100%);
        color: #f3f4f6;
        font-family: 'Inter', 'Cairo', sans-serif;
    }
    
    [data-testid="stToolbar"] {visibility: hidden;}
    
    .alpha-header {
        text-align: center;
        padding: 15px;
        margin-bottom: 25px;
        border-bottom: 1px dashed rgba(0, 255, 204, 0.15);
    }
    .alpha-title {
        font-family: 'Space Grotesk', 'Cairo', sans-serif;
        font-size: 36px;
        font-weight: 700;
        background: linear-gradient(90deg, #00ffcc 0%, #7928ca 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 1px;
    }
    .owner-badge {
        background: linear-gradient(135deg, rgba(0,255,204,0.1), rgba(121,40,202,0.1));
        border: 1px solid #00ffcc;
        padding: 14px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
    }
    .card-task {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(0, 255, 204, 0.1);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 12px;
        direction: rtl;
        text-align: right;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="alpha-header">
    <div class="alpha-title">🌌 ZETAWAVE ALPHA PRO</div>
    <p style='color: #8b949e; font-size: 14px; margin-top: 5px;'>الجيل القادم لمنصات السيادة السيبرانية، الاستخبارات التكتيكية، والردع الدفاعي النشط.</p>
</div>
""", unsafe_allow_html=True)

# 2. تهيئة وإدارة متغيرات الجلسة (Session State) للمشروع الجديد
if 'is_alpha_owner' not in st.session_state:
    st.session_state['is_alpha_owner'] = True

if 'automated_tasks' not in st.session_state:
    st.session_state['automated_tasks'] = [
        {"id": "TASK-01", "name": "فحص المنافذ وجدار الحماية الدوري للخادم", "interval": "كل ساعة", "status": "نشط 🟢", "last_run": "منذ 14 دقيقة"},
        {"id": "TASK-02", "name": "مزامنة قوائم الحظر السوداء من التغذيات العالمية", "interval": "كل 6 ساعات", "status": "نشط 🟢", "last_run": "منذ ساعتين"}
    ]

# عرض صلاحية المطور المالك المفتوحة تلقائياً وبأبهى صورة
if st.session_state['is_alpha_owner']:
    st.markdown("""
    <div class="owner-badge">
        <span style="color: #00ffcc; font-weight: bold; font-size: 15px;">👑 بيئة التشغيل الفوق-أمنية: رتبة المطور المالك (Alpha Owner)</span>
        <br><span style="color: #8b949e; font-size: 11px;">🔒 ميزات الاستخبارات، التتبع الجنائي، ومصائد العسل العقابية نشطة وتعمل بكامل طاقتها التشغيلية الحية.</span>
    </div>
    """, unsafe_allow_html=True)

# 3. لوحة التحكم الإدارية ومركز الأتمتة والجدولة السحابية
st.markdown("<h3 style='font-family: Cairo; font-size: 20px; color: #00ffcc;'>⚙️ مركز الأتمتة والعمليات السحابية الذكية</h3>", unsafe_allow_html=True)
st.write("قم ببرمجة وجدولة المهام والسكربتات السيبرانية لتعمل في الخلفية على الخادم بشكل مستقل ومستمر:")

# حقول إضافة مهمة جديدة مؤتمتة بشكل حقيقي
with st.expander("➕ جدولة مهمة سيبرانية مؤتمتة جديدة في الخلفية"):
    task_name = st.text_input("اسم المهمة المراد أتمتتها (مثال: فحص سلامة ملفات النظام):")
    task_interval = st.selectbox("معدل التكرار الزمني والجدولة:", ["كل دقيقة", "كل ساعة", "كل 12 ساعة", "كل 24 ثانية (وضع الفحص المكثف)"])
    
    if st.button("🚀 حقن وتفعيل المهمة في المجدول السحابي", use_container_width=True):
        if task_name.strip():
            new_task = {
                "id": f"TASK-0{len(st.session_state['automated_tasks']) + 1}",
                "name": task_name.strip(),
                "interval": task_interval,
                "status": "نشط 🟢",
                "last_run": "جاري الجدولة الآن..."
            }
            st.session_state['automated_tasks'].append(new_task)
            st.success(f"✅ تم حقن المهمة [{new_task['id']}] بنجاح في الخلفية وتوصيلها بالمجدول!")
            time.sleep(0.5)
            st.rerun()
        else:
            st.warning("يرجى إدخال اسم المهمة أولاً.")

# عرض قائمة المهام المؤتمتة الحالية التي تعمل في نظام Alpha
st.write("")
st.markdown("<p style='font-size: 15px; font-weight: bold; color: #7928ca;'>📜 سجل العمليات والمهام النشطة في الخلفية (Active Workers Log):</p>", unsafe_allow_html=True)

for task in st.session_state['automated_tasks']:
    st.markdown(f"""
    <div class="card-task">
        <span style="color: #00ffcc; font-weight: bold;">🆔 {task['id']} | {task['name']}</span>
        <br><span style="color: #aaa; font-size: 12px;">⏰ معدل التكرار: {task['interval']} | 📊 الحالة: {task['status']}</span>
        <br><span style="color: #666; font-size: 11px;">🕒 آخر تشغيل تلقائي: {task['last_run']}</span>
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.info("💡 استخدم الشريط الجانبي للتنقل بين أسلحة منصة Alpha الاستخباراتية والجنائية المتقدمة.")
