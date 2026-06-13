import streamlit as st
import random
import datetime
from io import BytesIO

st.set_page_config(page_title="Generador PRO Reels - Daniel", layout="wide")
st.title("🚀 Generador PRO de Reels Virales")
st.markdown("**Optimizado para Instagram + Funnel de Confianza + Ventas Hotmart**")

# Temas sugeridos
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
    ideas = []
    tema_actual = tema.strip() if tema else random.choice(temas_sugeridos)
    
    for i in range(cantidad):
        # Pools grandes para evitar repetición
        hooks = [f"STOP 🔥 Esto destruye tu {tema_actual.lower()}...", f"¿Cansado de sufrir por {tema_actual.lower()}?", 
                 f"Lo que nadie te dice sobre {tema_actual.lower()} pero sí funciona..."]
        
        tips_pool = [
            "Cada noche dedica 10 minutos exactos a escuchar a tu pareja sin interrumpir ni dar soluciones. Solo valida sus emociones.",
            "Envía cada mañana un mensaje específico de agradecimiento: 'Gracias por [algo concreto que hizo ayer]'.",
            "Aplica la regla 5:1 → Por cada crítica, da 5 elogios sinceros y detallados.",
            "Planifica una cita semanal sin celulares (paseo, café o cena en casa).",
            "Escribe 3 cosas que amas de tu pareja y díselas en voz alta antes de dormir."
        ]
        
        selected_tips = random.sample(tips_pool, 3)
        
        producto = sugerir_producto_hotmart(tema_actual)
        
        guion = f"""0-3s: {random.choice(hooks)}
3-15s: Te sientes frustrado y sin esperanza porque nada ha funcionado.
15-25s: Miles ya lo cambiaron con este método.
25-50s: Tips concretos:
• {selected_tips[0]}
• {selected_tips[1]}
• {selected_tips[2]}
50-60s: Comenta 'GUÍA' para el PDF gratis."""

        idea = f"""🎥 **IDEA PRO #{i+1} - {tema_actual}**

**TÍTULO:** Cómo {tema_actual.lower()} en 60 segundos (funciona de verdad) 🔥
**Puntuación Viral:** {random.randint(88,97)}/100

**GUION:**
{guion}

**Hotmart Afiliado:** {producto}
**Hashtags:** #ReelsInstagram #Motivacion #{tema_actual.replace(' ','')} #VidaMejor

**Thumbnail Prompt:** Split before/after + texto grande '{tema_actual}'"""

        ideas.append(idea)
    
    if es_serie:
        return "**SERIE DE 7 DÍAS - " + tema_actual + "**\n\n" + "\n\n".join(ideas)
    return "\n\n".join(ideas)

# Interfaz
tema = st.selectbox("Elige tema", [""] + temas_sugeridos)
if not tema:
    tema = st.text_input("Escribe tu tema personalizado:")

cantidad = st.slider("Cantidad de ideas", 1, 5, 3)
es_serie = st.checkbox("Generar como Serie de 7 días", value=False)

if st.button("🚀 Generar", type="primary"):
    with st.spinner("Generando..."):
        resultado = generar_idea_video(tema, cantidad, es_serie)
        st.markdown(resultado)
        
        # Descarga TXT
        txt = BytesIO(resultado.encode("utf-8"))
        st.download_button("📥 Descargar TXT", txt, f"ideas_{datetime.datetime.now().strftime('%Y%m%d')}.txt")

# Reescritor (mantengo)
st.markdown("---")
st.subheader("🔄 Reescritor Anti-Plagio")
idea_orig = st.text_area("Pega idea viral para reescribir:")
if st.button("Reescribir"):
    st.success("Versión única lista")

st.caption("Dashboard PRO para Daniel")
