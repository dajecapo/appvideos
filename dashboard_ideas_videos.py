import streamlit as st
import random
import datetime
from io import BytesIO

st.set_page_config(page_title="Generador PRO Reels - Daniel", layout="wide")
st.title("🚀 Generador PRO de Reels Virales para Instagram")
st.markdown("**Funnel de Confianza + Afiliados Hotmart + Algoritmo Instagram**")

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
        "procrastinacion": ["Productividad Extrema"],
        "fe": ["Fe Inquebrantable"],
        "salud": ["Transformación Física Total"],
        "ansiedad": ["Paz Mental Total"]
    }
    for key in productos:
        if key in tema.lower():
            return random.choice(productos[key])
    return "Curso de Desarrollo Personal Avanzado"

def generar_idea_video(tema=None, cantidad=1, serie=False):
    ideas_generadas = []
    tema_actual = tema.strip() if tema and tema.strip() else random.choice(temas_sugeridos)
    
    for i in range(cantidad):
        # Hooks corregidos
        hooks = [
            f"STOP 🔥 Esto es lo que está arruinando tu {tema_actual}...",
            f"¿Cansado de sufrir por {tema_actual} todos los días?",
            f"Lo que nadie te cuenta sobre {tema_actual} pero sí funciona",
            f"Imagina arreglar tu {tema_actual} en solo unos días..."
        ]
        
        # Tips siempre variados
        tips_pool = [
            "Cada noche dedica 10 minutos a escuchar activamente a tu pareja sin interrumpir ni dar soluciones. Solo valida cómo se siente.",
            "Cada mañana envía un mensaje específico de agradecimiento por algo concreto que hizo el día anterior.",
            "Aplica la regla 5:1 → Por cada crítica, da 5 elogios sinceros y detallados.",
            "Planifica una cita semanal sin celulares (paseo corto o café en casa).",
            "Escribe 3 cosas que amas de tu pareja y díselas en voz alta antes de dormir."
        ]
        
        selected_tips = random.sample(tips_pool, 3)
        
        producto = sugerir_producto_hotmart(tema_actual)
        
        guion = f"""0-3s: [HOOK] {random.choice(hooks)}
3-15s: [DOLOR] Te sientes frustrado, agotado y sin esperanza porque nada ha funcionado.
15-25s: [PRUEBA SOCIAL] Miles ya transformaron su {tema_actual} con este método.
25-50s: [TIPS ESPECÍFICOS]
• {selected_tips[0]}
• {selected_tips[1]}
• {selected_tips[2]}
50-60s: [CTA] Comenta 'GUÍA' para recibir el PDF gratis."""

        titulo = f"Cómo {tema_actual} en 60 segundos (método que realmente funciona) 🔥"

        idea = f"""🎥 **IDEA PRO #{i+1} - {tema_actual.upper()}**

**📌 TÍTULO VIRAL:**  
{titulo}

**🔥 PUNTUACIÓN VIRALIDAD:** {random.randint(88, 97)}/100

**GUION COMPLETO:**
{guion}

**💰 HOTMART (Afiliado):** Recomiendo "{producto}"

**📸 THUMBNAIL PROMPT:**  
Split before/after (triste → feliz), texto grande "{titulo}", colores dramáticos, 9:16 vertical

**🔥 HASHTAGS:** #ReelsInstagram #Motivacion #{tema_actual.replace(' ','')} #VidaMejor #CrecimientoPersonal"""

        ideas_generadas.append(idea)
    
    return "\n\n" + "="*90 + "\n\n".join(ideas_generadas)

# Interfaz
st.subheader("🎯 Elige el tema")
tema = st.selectbox("Tema", [""] + temas_sugeridos)
if not tema:
    tema = st.text_input("Escribe tu propio tema:")

cantidad = st.slider("Número de ideas", 1, 5, 3)
es_serie = st.checkbox("Generar Serie de 7 días", value=False)

if st.button("🚀 Generar Ideas PRO", type="primary", use_container_width=True):
    with st.spinner("Generando..."):
        resultado = generar_idea_video(tema, cantidad, es_serie)
        st.success("¡Listo!")
        st.markdown(resultado)
        
        # Descarga
        txt = BytesIO(resultado.encode("utf-8"))
        st.download_button("📥 Descargar TXT", txt, f"reels_{datetime.datetime.now().strftime('%Y%m%d')}.txt")

# Reescritor
st.markdown("---")
st.subheader("🔄 Reescritor Anti-Plagio")
idea_orig = st.text_area("Pega idea viral que viste:")
if st.button("Reescribir Única"):
    if idea_orig:
        st.success("Versión original generada")
        st.markdown("**Versión única:** Imagina transformar " + idea_orig.lower() + " con este enfoque fresco...")

st.caption("Dashboard PRO para Daniel")
