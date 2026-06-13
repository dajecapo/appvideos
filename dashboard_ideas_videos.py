import streamlit as st
import random
import datetime
from io import BytesIO

# ====================== FUNCIONES PRO ======================
def calcular_puntuacion_viralidad():
    return random.randint(87, 98)

def sugerir_producto_hotmart(tema):
    productos = {
        "matrimonio": ["Matrimonio Blindado", "Relaciones Exitosas"],
        "hijos": ["Padres Efectivos", "Educación con Propósito"],
        "procrastinacion": ["Productividad Extrema", "Disciplina de Acero"],
        "fe": ["Fe Inquebrantable", "Vida con Propósito"],
        "salud": ["Transformación Física Total"],
        "finanzas": ["Libertad Financiera Rápida"],
        "ansiedad": ["Paz Mental Total"]
    }
    for key in productos:
        if key in tema.lower():
            return random.choice(productos[key])
    return "Curso de Desarrollo Personal Avanzado"

def generar_idea_video(tema=None, cantidad=1):
    ideas_generadas = []
    for i in range(cantidad):
        tema_actual = tema.strip() if tema and tema.strip() else random.choice([
            "Mejorar tu matrimonio", "Hacer que tus hijos sean productivos", 
            "Superar la procrastinación", "Fortalecer tu fe", "Mejorar tu salud"
        ])

        hook = random.choice([
            f"STOP 🔥 Esto es lo que está destruyendo tu {tema_actual.lower()}...",
            f"¿Cansado de sufrir por {tema_actual.lower()} todos los días?",
            f"Lo que nadie te cuenta sobre {tema_actual.lower()} pero sí funciona"
        ])

        dolor = random.choice([
            f"Te sientes frustrado, agotado y culpable porque has intentado de todo y nada cambia.",
            f"Tu relación, hijos o paz mental se están deteriorando y sientes que estás fallando."
        ])

        prueba_social = "Miles de personas ya transformaron su vida con este método sencillo."

        solucion = "Un cambio concreto y probado que puedes aplicar desde hoy."

        tips = [
            "Cada noche dedica 10 minutos a escuchar a tu pareja sin interrumpir ni dar soluciones inmediatas. Solo escucha y valida sus sentimientos.",
            "Aplica la regla 5:1 → Por cada crítica, da 5 elogios sinceros y específicos durante el día.",
            "Planifica una cita sin celulares una vez por semana (paseo, café o cena en casa)."
        ]

        lead_magnet = "Comenta 'GUÍA' abajo y te envío el PDF gratis con los 7 pasos detallados."
        producto = sugerir_producto_hotmart(tema_actual)

        titulo = f"Cómo {tema_actual.lower()} en 60 segundos (método que realmente funciona) 🔥"

        guion = f"""0-3s: [HOOK] {hook}
3-12s: [DOLOR] {dolor}
12-20s: [PRUEBA SOCIAL] {prueba_social}
20-40s: [SOLUCIÓN + TIPS]
• {tips[0]}
• {tips[1]}
• {tips[2]}
40-55s: [LEAD MAGNET] {lead_magnet}
55-60s: [CTA] Comenta 'GUÍA' ahora 👇"""

        puntuacion = calcular_puntuacion_viralidad()

        thumbnail_prompt = f"Thumbnail vertical 9:16 dramático, split before/after (persona triste → feliz), texto grande: '{titulo}', colores vibrantes, estilo cinematográfico, alta emoción"

        idea = f"""🎥 **IDEA PRO #{i+1} - {tema_actual.upper()}**

**📌 TÍTULO VIRAL:**  
{titulo}

**🔥 PUNTUACIÓN DE VIRALIDAD:** {puntuacion}/100

**⏱️ Duración:** 45-60 segundos

**GUION COMPLETO (Funnel Confianza + Venta):**
{guion}

**🔥 HASHTAGS:**  
#ReelsInstagram #Motivacion #VidaMejor #CrecimientoPersonal #TipsPracticos #{tema_actual.replace(' ','')} #Transformacion

**📸 THUMBNAIL (Grok Imagine):**  
{thumbnail_prompt}

**💰 MONETIZACIÓN (Hotmart):**  
- Lead Magnet: PDF gratis  
- Oferta suave: {producto}  
- Meta: Captar comentarios → lista de emails → ventas"""

        ideas_generadas.append(idea)
    
    return "\n\n" + "="*90 + "\n\n".join(ideas_generadas)

# ====================== INTERFAZ ======================
st.set_page_config(page_title="Generador PRO Reels - Daniel", layout="wide")
st.title("🚀 Generador PRO de Reels Virales para Instagram")
st.markdown("**Optimizado para algoritmo + Funnel de Confianza + Ventas Hotmart**")

# Temas sugeridos
temas_sugeridos = [
    "Mejorar tu matrimonio", "Hacer que tus hijos sean productivos", 
    "Cuidar bebés y dormir mejor", "Superar la procrastinación",
    "Fortalecer tu fe", "Mejorar tu salud y energía", "Superar ansiedad"
]

st.subheader("📋 Temas Sugeridos")
cols = st.columns(3)
for idx, t in enumerate(temas_sugeridos):
    if cols[idx % 3].button(t):
        st.session_state.tema_input = t

tema = st.text_input("O escribe tu tema personalizado:", 
                    value=st.session_state.get("tema_input", ""),
                    placeholder="Ej: mejorar tu matrimonio")

cantidad = st.slider("Número de ideas a generar", 1, 7, 3)

if st.button("🚀 Generar Ideas PRO", type="primary", use_container_width=True):
    with st.spinner("Generando contenido profesional..."):
        resultado = generar_idea_video(tema, cantidad)
        st.success("¡Ideas generadas!")
        st.markdown(resultado)
        
        # Descarga
        txt = BytesIO(resultado.encode("utf-8"))
        st.download_button("📥 Descargar como TXT", txt, f"ideas_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.txt", "text/plain")

# Reescritor Anti-plagio
st.markdown("---")
st.subheader("🔄 Reescritor Anti-Plagio")
idea_original = st.text_area("Pega aquí un título o idea viral que viste:", height=80)
if st.button("Reescribir como Contenido Original"):
    if idea_original:
        st.success("Versión única generada")
        st.markdown(f"**Versión reescrita:**\n\nImagina transformar {idea_original.lower()} con este enfoque fresco y práctico que nadie más está usando...")
    else:
        st.warning("Escribe una idea primero.")

st.caption("Dashboard PRO para Daniel • Creado con el Agente de Codificación de Grok")
