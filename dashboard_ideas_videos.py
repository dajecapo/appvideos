import streamlit as st
import random
import datetime

# --- Funciones del generador ---
def generar_idea_video(tema=None, cantidad=1):
    ideas_generadas = []
    
    for i in range(cantidad):
        if not tema:
            temas_comunes = [
                "mejorar tu matrimonio", "hacer que tus hijos sean productivos", 
                "cuidar bebés y dormir mejor", "superar la procrastinación", 
                "mejorar tu salud y energía", "lograr metas financieras", 
                "encontrar paz mental", "fortalecer tu fe"
            ]
            tema_actual = random.choice(temas_comunes)
        else:
            tema_actual = tema.lower().strip()
        
        # Hooks optimizados para Instagram
        hooks = [
            f"STOP: Esto es lo que está destruyendo tu {tema_actual}...",
            f"¿Sabías que el 87% falla en {tema_actual} por ESTO?",
            f"Imagina arreglar {tema_actual} en solo 30 días...",
            f"El secreto que nadie te cuenta sobre {tema_actual}...",
            f"Si sigues así con {tema_actual}, vas a perderlo todo...",
            f"Una decisión de 60 segundos que cambió mi {tema_actual}...",
        ]
        
        dolores = [
            f"Te sientes frustrado, agotado y sin esperanza porque {tema_actual} parece imposible de arreglar.",
            f"Cada día es una lucha: discusiones, cansancio y culpa te consumen.",
            f"Intentaste todo y nada funciona. Sientes que fallas como pareja/padre.",
            f"Ver a tu familia sufrir mientras luchas con {tema_actual} te destroza por dentro.",
        ]
        
        soluciones = [
            "La clave está en un cambio simple pero poderoso que puedes empezar HOY.",
            "Existe un método probado que miles han usado para transformar esto rápidamente.",
            f"Estrategia práctica basada en psicología que resuelve la raíz de {tema_actual}.",
        ]
        
        # Tips específicos por tema
        tips_base = {
            "mejorar tu matrimonio": [
                "Cada noche dedica 10 minutos a escuchar activamente sin interrumpir ni dar soluciones.",
                "Envía un mensaje específico de agradecimiento cada mañana.",
                "Practica la regla 5:1 (5 elogios por cada crítica).",
                "Planifica una 'cita sin pantallas' una vez por semana.",
            ],
            "hacer que tus hijos sean productivos": [
                "Regla 'primero lo importante': tareas antes de pantallas.",
                "Usa Pomodoro de 15 min estudio + 5 min descanso.",
                "Crea tablero visual de responsabilidades con recompensas.",
                "Trabaja junto a ellos 20 minutos al día modelando el comportamiento.",
            ],
            "cuidar bebés y dormir mejor": [
                "Rutina fija: baño, masaje, canción a la misma hora.",
                "Método 5S para calmar al bebé rápidamente.",
                "Duerme cuando el bebé duerme (ignora tareas).",
                "Ambiente oscuro + ruido blanco consistente.",
            ],
            "superar la procrastinación": [
                "Regla de los 2 minutos: si tarda menos, hazlo YA.",
                "Divide tareas en pasos de máximo 5 minutos.",
                "Eat the frog: haz lo más difícil primero.",
                "Bloquea distracciones con modo avión.",
            ],
            "fortalecer tu fe": [
                "Dedica 10 minutos diarios a leer un versículo y meditarlo.",
                "Ora en voz alta por 5 minutos cada mañana.",
                "Únete a un grupo de estudio bíblico semanal.",
                "Lleva un diario de gratitud espiritual.",
            ],
        }
        
        if tema_actual in tips_base:
            tips = tips_base[tema_actual]
        else:
            tips = [
                f"Dedica 10 minutos diarios a una acción concreta para {tema_actual}.",
                f"Implementa un cambio pequeño y mide resultados en 7 días.",
                f"Busca alguien que te rinda cuentas semanalmente.",
            ]
        
        ctas = [
            "Comenta 'SÍ' si vas a probarlo hoy 👇",
            "Etiqueta a quien necesita ver esto ❤️",
            "Guarda y comparte este Reel",
            "Comenta 'GUÍA' para el PDF completo gratis",
            "¡Escribe tu mayor obstáculo abajo!",
        ]
        
        hook = random.choice(hooks)
        dolor = random.choice(dolores)
        solucion = random.choice(soluciones)
        selected_tips = random.sample(tips, min(3, len(tips)))
        cta = random.choice(ctas)
        
        titulo = f"Cómo {tema_actual} en 60 segundos (funciona de verdad) 🔥"
        
        guion = f"""GUION LISTO PARA GRABAR (Instagram Reel):

0-3s: [HOOK - voz intensa] {hook}

3-15s: [DOLOR - voz empática] {dolor}

15-25s: [SOLUCIÓN - voz esperanzadora] {solucion}

25-50s: [TIPS - voz clara y pausada]
• {selected_tips[0]}
• {selected_tips[1]}
• {selected_tips[2] if len(selected_tips)>2 else ''}

50-60s: [CTA fuerte] {cta}"""
        
        hashtags = ["#ReelsInstagram", "#MotivacionDiaria", "#VidaMejor", f"#{tema_actual.replace(' ','')}", "#TipsPracticos", "#CrecimientoPersonal", "#ViralReels", "#TransformacionPersonal"]
        hashtags_str = " ".join(random.sample(hashtags + ["#Shorts", "#Mindset", "#Exito"], 8))
        
        prompt_imagine = f"Video vertical Reel Instagram 9:16, estilo cinematico dramático, voz en off masculina grave y convincente español latino neutro, {tema_actual}, transiciones rápidas cada 3 segundos, texto en pantalla grande con emojis, antes y después, alta calidad 4K, música motivacional trending"
        
        thumbnail_prompts = [
            f"Thumbnail vertical 9:16, estilo cinematico dramático, cara expresiva split before/after dolor-esperanza, texto grande negrita: '{titulo}', emojis 🔥💔➡️❤️, alta calidad 4K",
            f"Thumbnail impactante vertical, pareja/familia antes vs después, overlay texto grande: 'Cómo {tema_actual} en 60 seg' 🔥, flechas, colores vibrantes",
            f"Close-up ojos lágrimas a sonrisa, fondo motivacional, gran texto: '{titulo}', iluminación cinematográfica 9:16",
        ]
        thumbnail_prompt = random.choice(thumbnail_prompts)
        
        idea = f"""🎥 **IDEA #{i+1} - {tema_actual.upper()}**

**📌 TÍTULO VIRAL:**
{titulo}

**⏱️ Duración:** 45-60 segundos

**GUION COMPLETO:**
{guion}

**🔥 HASHTAGS:**
{hashtags_str}

**📸 THUMBNAIL PROMPTS (Grok Imagine):**
{thumbnail_prompt}

**🎙️ PROMPT GROK IMAGINE (video):**
{prompt_imagine}

**🔍 ALGORITMO INSTAGRAM:**
- Hook <3 seg clave
- Cortes rápidos + texto en pantalla
- CTA fuerte para comentarios

**💰 MONETIZACIÓN:**
- Comenta 'GUÍA' → lead magnet
- Funnel a curso/ebook
- Afiliados"""
        
        ideas_generadas.append(idea)
    
    return "\n\n" + "="*80 + "\n\n".join(ideas_generadas)

# --- Interfaz del Dashboard ---
st.set_page_config(page_title="Generador de Reels Virales", layout="wide")
st.title("🚀 Generador de Ideas para Reels Virales - Instagram")
st.markdown("**Creado para Daniel** - Optimizado para algoritmo de Instagram Reels + Grok Imagine")

col1, col2 = st.columns([3,1])

with col1:
    tema = st.text_input("🎯 Tema del video", 
                        placeholder="mejorar tu matrimonio, fortalecer tu fe, etc.")
    
    cantidad = st.slider("Número de ideas a generar", 1, 10, 3)

with col2:
    st.markdown("### Cómo usarlo")
    st.write("1. Escribe el tema")
    st.write("2. Elige cuántas ideas")
    st.write("3. Pulsa Generar")

if st.button("🚀 Generar Ideas", type="primary", use_container_width=True):
    with st.spinner("Generando ideas virales..."):
        resultado = generar_idea_video(tema, cantidad)
        
        st.success(f"¡{cantidad} ideas generadas exitosamente!")
        st.markdown(resultado)
        
        # Guardado automático
        try:
            with open("ideas_videos_motivacionales.txt", "a", encoding="utf-8") as f:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"\n{'='*90}\nDASHBOARD - {timestamp} | Tema: {tema or 'Aleatorio'}\n")
                f.write(resultado)
            st.info("✅ Guardado automáticamente en ideas_videos_motivacionales.txt")
        except:
            pass

st.markdown("---")
st.caption("Dashboard creado con ❤️ por Grok • Listo para producción")
