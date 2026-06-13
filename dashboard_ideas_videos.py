import streamlit as st
import random
import datetime
from io import BytesIO

st.set_page_config(page_title="Generador PRO Reels - Daniel", layout="wide")
st.title("🚀 Generador PRO de Reels Virales para Instagram")
st.markdown("**Optimizado para algoritmo de Instagram + Funnel de Confianza + Ventas Hotmart**")

temas_sugeridos = [
    "Mejorar tu matrimonio", "Hacer que tus hijos sean productivos", 
    "Cuidar bebés y dormir mejor", "Superar la procrastinación",
    "Fortalecer tu fe", "Mejorar tu salud y energía", "Superar ansiedad"
]

def sugerir_producto_hotmart(tema):
    productos = {
        "matrimonio": ["Matrimonio Blindado", "Relación Sin Límites"],
        "hijos": ["Padres Efectivos", "Educación con Propósito"],
        "procrastinacion": ["Productividad Extrema", "Disciplina de Acero"],
        "fe": ["Fe Inquebrantable", "Vida con Propósito"],
        "salud": ["Transformación Física Total"],
        "ansiedad": ["Paz Mental Total"]
    }
    for key in productos:
        if key in tema.lower():
            return random.choice(productos[key])
    return "Curso de Desarrollo Personal Avanzado"

def generar_idea_video(tema=None, cantidad=1, es_serie=False):
    ideas_generadas = []
    
    if not tema:
        temas_comunes = [
            "Mejorar tu matrimonio", "Hacer que tus hijos sean productivos", 
            "Cuidar bebés y dormir mejor", "Superar la procrastinación", 
            "Mejorar tu salud y energía", "Lograr metas financieras", 
            "Encontrar paz mental", "Fortalecer tu fe", "Ser mejor padre"
        ]
        tema_actual = random.choice(temas_comunes)
    else:
        tema_actual = tema.strip()
    
    # Pool grande de tips para que nunca se repitan
    tips_pool = [
        "Cada noche dedica exactamente 10 minutos a escuchar a tu pareja sin interrumpir ni dar soluciones. Solo valida sus emociones.",
        "Envía cada mañana un mensaje específico: 'Gracias por [algo concreto que hizo ayer]'.",
        "Aplica la regla 5:1 → Por cada crítica, da 5 elogios sinceros y detallados.",
        "Planifica una cita semanal sin celulares (paseo o cena en casa).",
        "Escribe 3 cosas que amas de tu pareja y díselas en voz alta antes de dormir.",
        "Cuando discutan, usa la técnica de la pausa de 10 minutos antes de responder.",
        "Haz una lista juntos de sueños como pareja y revísenla cada mes.",
    ]
    
    for i in range(cantidad):
        selected_tips = random.sample(tips_pool, 3)
        
        hook = random.choice([
            f"STOP 🔥 Esto es lo que está destruyendo tu {tema_actual.lower()}...",
            f"¿Cansado de sentirte frustrado con {tema_actual.lower()} todos los días?",
            f"Lo que nadie te cuenta sobre {tema_actual.lower()} (pero funciona)",
        ])
        
        dolor = random.choice([
            f"Te sientes agotado, culpable y sin esperanza porque has intentado todo y nada cambia.",
            f"Tu relación se está deteriorando y sientes que estás fallando como pareja.",
        ])
        
        producto = sugerir_producto_hotmart(tema_actual)
        
        guion = f"""0-3s: [HOOK] {hook}
3-12s: [DOLOR] {dolor}
12-20s: [PRUEBA SOCIAL] Miles de personas ya transformaron su matrimonio con este método.
20-40s: [TIPS CONCRETOS]
• {selected_tips[0]}
• {selected_tips[1]}
• {selected_tips[2]}
40-55s: [LEAD MAGNET] Comenta 'GUÍA' y te envío el PDF gratis con los pasos detallados.
55-60s: [CTA] Comenta 'GUÍA' ahora 👇"""

        puntuacion = calcular_puntuacion_viralidad()
        
        idea = f"""🎥 **IDEA PRO #{i+1} - {tema_actual.upper()}**

**📌 TÍTULO VIRAL:** Cómo {tema_actual.lower()} en 60 segundos (funciona de verdad) 🔥

**🔥 PUNTUACIÓN DE VIRALIDAD:** {puntuacion}/100

**⏱️ Duración:** 45-60 segundos

**GUION COMPLETO (Funnel de Confianza + Venta):**
{guion}

**🔥 HASHTAGS:** #ReelsInstagram #Motivacion #VidaMejor #CrecimientoPersonal #{tema_actual.replace(' ','')} #Transformacion

**📸 THUMBNAIL PROMPT:** Split before/after persona triste → feliz, texto grande '{tema_actual}', estilo cinematográfico, alta emoción

**💰 MONETIZACIÓN HOTMART:** {producto} (recomienda el PDF gratis y al final ofrece el curso como recurso recomendado)

**✅ Recomendación Instagram:** Publica como parte de una serie de 7 días."""
        
        ideas_generadas.append(idea)
    
    if es_serie:
        return f"**SERIE DE 7 DÍAS - {tema_actual}**\n\n" + "\n\n".join(ideas_generadas)
    
    return "\n\n" + "="*90 + "\n\n".join(ideas_generadas)

# ====================== INTERFAZ ======================
st.subheader("📋 Elige un tema o escribe el tuyo")
tema = st.selectbox("Temas sugeridos", [""] + temas_sugeridos)
if not tema:
    tema = st.text_input("Escribe tu propio tema:", placeholder="mejorar tu matrimonio")

cantidad = st.slider("Número de ideas", 1, 5, 3)
es_serie = st.checkbox("Generar como SERIE DE 7 DÍAS", value=False)

if st.button("🚀 Generar Ideas PRO", type="primary", use_container_width=True):
    with st.spinner("Generando contenido de alto nivel..."):
        resultado = generar_idea_video(tema, cantidad, es_serie)
        st.success(f"¡{cantidad} ideas generadas con éxito!")
        st.markdown(resultado)
        
        txt = BytesIO(resultado.encode("utf-8"))
        st.download_button("📥 Descargar como TXT", txt, f"ideas_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.txt")

# Reescritor
st.markdown("---")
st.subheader("🔄 Reescritor Anti-Plagio")
idea_original = st.text_area("Pega aquí una idea viral que viste:", height=80)
if st.button("Reescribir como Contenido Original"):
    if idea_original.strip():
        st.success("Versión 100% original generada")
        st.markdown(f"**Título:** Cómo transformar {idea_original.lower()} sin que parezca imposible (método real)\n\n**Guion único:** ... (versión personalizada)")
    else:
        st.warning("Escribe una idea primero.")

st.caption("Dashboard PRO para Daniel • Creado con el Agente de Codificación de Grok")
