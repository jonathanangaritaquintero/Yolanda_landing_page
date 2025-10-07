# app.py - Landing Page Yolanda Quintero - Asesora de Seguros

from flask import Flask, render_template_string, jsonify
import urllib.parse
import os

app = Flask(__name__)

# ========================================
# CONFIGURACIÓN YOLANDA QUINTERO
# ========================================
ADVISOR_CONFIG = {
    "business_name": "+20 años de experiencia",
    "advisor_name": "Yolanda Quintero",
    "title": "ASESORA DE SEGUROS",
    "main_message": "¿Necesitas un seguro y al mejor precio?",
    "submessage": "OBTEN UNA ASESORÍA COMPLETAMENTE GRATIS",
    
    "hero_video": "https://res.cloudinary.com/dweqlnl1w/video/upload/v1759790299/4733687-uhd_2160_3840_25fps_nufezs.mp4",
    
    "hero_fallback_image": "https://res.cloudinary.com/dweqlnl1w/image/upload/v1759790052/pexels-oandremoura-6105553_a8f5yu.jpg",
    
    "instagram_handle": "@yolandaquinteroseguros",
    "instagram_url": "https://www.instagram.com/yolandaquinteroseguros",
    "whatsapp_number": "+573216484963",
    "email": "yolandaquinteroasesor@gmail.com",
    "location": "Bucaramanga, Santander",
    "about_text": "Soy Yolanda Quintero, asesora de seguros con más de 20 años de experiencia en el sector asegurador, trabajando con las principales compañías del país como SURA, AXA Colpatria, Liberty Seguros, Mapfre, Allianz, entre otras. Mi objetivo es brindar a cada cliente la mejor cobertura al mejor precio, comparando entre múltiples aseguradoras para encontrar la opción perfecta para sus necesidades. Ofrezco asesoría personalizada en seguros de vida, salud, vehículos, hogar, empresariales y ARL. Si buscas tranquilidad y protección real para ti y tu familia, agenda tu consultoría gratuita conmigo.",
    "google_maps_embed": "Bucaramanga Santander",
    "google_ads_id": "", # Reemplazar con ID real si se tiene
}

insurance_services = [
    {
        "name": "SEGUROS DE VIDA",
        "image": "https://res.cloudinary.com/dweqlnl1w/image/upload/v1756162454/cld-sample.jpg",
        "description": "Individual y familiar, colectivos vida grupo - Protección garantizada"
    },
    {
        "name": "VEHICULARES", 
        "image": "https://res.cloudinary.com/dweqlnl1w/image/upload/v1756162445/samples/ecommerce/car-interior-design.jpg",
        "description": "SOAT y Todo Riesgo, livianos, pesado, individual y colectivo - Mejor precio del mercado - Asistencia vial 24/7"
    },
    {
        "name": "HOGAR",
        "image": "https://res.cloudinary.com/dweqlnl1w/image/upload/v1756162444/samples/people/boy-snow-hoodie.jpg",
        "description": "Multiriesgo hogar y hogar deudor - Protección completa"
    },
    {
        "name": "EMPRESARIALES",
        "image": "https://res.cloudinary.com/dweqlnl1w/image/upload/v1756162445/samples/imagecon-group.jpg",
        "description": "ARL, Responsabilidad Civil y más - Protege tu negocio"
    },
    {
        "name": "POLIZAS DE SALUD",
        "image": "https://res.cloudinary.com/dweqlnl1w/image/upload/v1756162447/samples/two-ladies.jpg",
        "description": "Planes individuales y familiares, medicina prepagada y planes complementarios - Cobertura nacional e internacional"
    },
    {
        "name": "CREDITOS PARA VEHICULOS",
        "image": "https://res.cloudinary.com/dweqlnl1w/image/upload/v1756162444/samples/people/bicycle.jpg",
        "description": "Usados y nuevos, compra de cartera y leasing - Aprobación rápida"
    }
]

def generate_whatsapp_link(message="Hola! Me interesa cotizar un seguro y agendar una asesoría gratuita"):
    phone = ADVISOR_CONFIG["whatsapp_number"].replace("+", "").replace(" ", "")
    encoded_message = urllib.parse.quote(message)
    return f"https://wa.me/{phone}?text={encoded_message}"

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, 
                                config=ADVISOR_CONFIG,
                                services=insurance_services,
                                whatsapp_link=generate_whatsapp_link())

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ config.advisor_name }} - {{ config.title }}</title>
    
    <meta name="description" content="Asesora de seguros en {{ config.location }}. +20 años de experiencia. Cotización gratuita.">
    <meta name="keywords" content="seguros bucaramanga, asesora seguros, SURA, AXA Colpatria, Liberty, vida, vehicular, hogar">
    
    <meta property="og:title" content="Yolanda Quintero - Asesora de Seguros Bucaramanga">
    <meta property="og:description" content="Asesora de seguros con +20 años de experiencia. Cotización GRATIS.">
    <meta property="og:image" content="{{ config.hero_fallback_image }}">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
    :root {
        --primary-blue: #6B83D6;
        --primary-teal: #52D4D4;
        --primary-green: #47C4BC;
        --hover-blue: #5A72C4;
        --hover-teal: #41C0C0;
        --light-blue: #869AE8;
        --bg-cream: #FAFBFF;
        --cream: #E5D4FC;
        --yellow: #EE7402;
        --bg-light-cream: #F4F7FF;
        --bg-warm-white: #FBFCFF;
        --text-dark: #1F2D4A;
        --text-medium: #3D4A6B;
        --text-light: #5D6E8F;
        --border-light: #DEE6F7;
        --shadow-soft: 0 4px 6px -1px rgba(107, 131, 214, 0.12);
        --shadow-medium: 0 10px 15px -3px rgba(107, 131, 214, 0.18);
    }
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html {
        scroll-behavior: smooth;
    }
    
    body {
        font-family: 'Inter', sans-serif;
        line-height: 1.6;
        overflow-x: hidden;
        background-color: var(--bg-cream);
        color: var(--text-dark);
    }
    
    .header {
        background: var(--bg-warm-white);
        padding: 1rem 0;
        box-shadow: var(--shadow-soft);
        position: fixed;
        width: 100%;
        top: 0;
        z-index: 1000;
        border-bottom: 1px solid var(--border-light);
    }
    
    .nav-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .logo {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: var(--text-dark);
        text-decoration: none;
        letter-spacing: -0.5px;
    }
    
    .logo .highlight {
        color: var(--primary-blue);
    }
    
    .hamburger-menu {
        display: flex;
        flex-direction: column;
        cursor: pointer;
        padding: 10px;
        background: var(--primary-blue);
        border-radius: 8px;
        transition: all 0.3s ease;
        position: relative;
        z-index: 1001;
    }
    
    .hamburger-menu:hover {
        background: var(--hover-blue);
        transform: scale(1.05);
    }
    
    .hamburger-line {
        width: 25px;
        height: 3px;
        background: white;
        margin: 3px 0;
        transition: all 0.3s ease;
        border-radius: 2px;
    }
    
    .hamburger-menu.active .hamburger-line:nth-child(1) {
        transform: rotate(45deg) translate(6px, 6px);
    }
    
    .hamburger-menu.active .hamburger-line:nth-child(2) {
        opacity: 0;
    }
    
    .hamburger-menu.active .hamburger-line:nth-child(3) {
        transform: rotate(-45deg) translate(6px, -6px);
    }
    
    .mobile-menu {
        position: fixed;
        top: 0;
        right: -100%;
        width: 100%;
        height: 100vh;
        background: var(--bg-warm-white);
        transition: right 0.3s ease;
        z-index: 1000;
        display: flex;
        flex-direction: column;
        padding: 100px 2rem 2rem;
    }
    
    .mobile-menu.active {
        right: 0;
    }
    
    .mobile-menu-item {
        display: block;
        padding: 1.5rem 0;
        color: var(--primary-blue);
        text-decoration: none;
        font-size: 1.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        border-bottom: 2px solid var(--border-light);
        transition: all 0.3s ease;
    }
    
    .mobile-menu-item:hover {
        color: var(--hover-blue);
        padding-left: 1rem;
    }
    
    .mobile-menu-instagram {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-top: 2rem;
    }
    
    .mobile-menu-instagram i {
        font-size: 2rem;
        color: var(--text-dark);
    }
    
    .menu-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh;
        background: rgba(0, 0, 0, 0.5);
        z-index: 999;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
    }
    
    .menu-overlay.active {
        opacity: 1;
        visibility: visible;
    }
    
    .hero {
        min-height: 90vh;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: white;
        position: relative;
        padding-top: 70px;
        overflow: hidden;
        background:  
                    url('{{ config.hero_fallback_image }}') center/cover no-repeat;
    }
    
    .hero-video {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: 1;
        opacity: 0;
        transition: opacity 0.5s ease;
    }
    
    .hero-video.loaded {
        opacity: 1;
    }
    
    .hero::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        
        z-index: 2;
    }
    
    .hero-content {
        max-width: 800px;
        padding: 2rem;
        position: relative;
        z-index: 3;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        font-weight: 500;
        letter-spacing: 2px;
        margin-bottom: 1rem;
        color: var(--text-dark);
        text-transform: uppercase;
    }
    
    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(3rem, 8vw, 5rem);
        font-weight: 700;
        margin-bottom: 2rem;
        letter-spacing: -1px;
        line-height: 1.1;
    }
    
    .hero-message {
        font-size: 2.0rem;
        margin-bottom: 1rem;
        font-weight: 500;
        line-height: 1.2;
    }
    
    .hero-submessage {
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        color: var(--text-dark);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .hero-final {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 2rem;
        color: #ffffff;
    }
    
    .cta-button {
        background: linear-gradient(135deg, var(--primary-green), var(--primary-teal));
        color: white;
        padding: 1.2rem 3rem;
        border: none;
        border-radius: 8px;
        font-size: 1.2rem;
        font-weight: 700;
        text-transform: uppercase;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
        letter-spacing: 0.5px;
        box-shadow: var(--shadow-medium);
    }
    
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 20px -5px rgba(37, 99, 235, 0.4);
    }
    
    .services-section {
        padding: 5rem 2rem;
        background: var(--bg-cream);
    }
    
    .section-container {
        max-width: 1200px;
        margin: 0 auto;
        text-align: center;
    }
    
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        color: var(--text-dark);
        margin-bottom: 1rem;
        position: relative;
    }
    
    .section-subtitle {
        font-size: 1.2rem;
        color: var(--text-medium);
        margin-bottom: 3rem;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 3px;
        background: linear-gradient(135deg, var(--primary-blue), var(--primary-teal));
    }
    
    .services-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin-bottom: 3rem;
    }
    
    .service-card {
        background: white;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: var(--shadow-soft);
        transition: all 0.3s ease;
        border: 1px solid var(--border-light);
    }
    
    .service-card:hover {
        transform: translateY(-8px);
        box-shadow: var(--shadow-medium);
    }
    
    .service-image {
        width: 100%;
        height: 250px;
        object-fit: cover;
    }
    
    .service-content {
        padding: 2rem;
    }
    
    .service-name {
        font-size: 1.5rem;
        color: var(--text-dark);
        margin-bottom: 1rem;
        font-weight: 700;
        text-transform: uppercase;
    }
    
    .service-description {
        color: var(--text-medium);
        margin-bottom: 1.5rem;
        font-size: 1rem;
    }
    
    .service-button {
        background: var(--primary-teal);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 6px;
        font-weight: 600;
        text-transform: uppercase;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 0.9rem;
    }
    
    .service-button:hover {
        background: var(--hover-teal);
        transform: translateY(-2px);
    }
    
    .about-section {
        background: var(--primary-blue);
        padding: 5rem 2rem;
        color: white;
    }
    
    .about-container {
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 4rem;
        align-items: center;
    }
    
    .about-content h2 {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        margin-bottom: 2rem;
        color: white;
    }
    
    .about-text {
        font-size: 1.1rem;
        line-height: 1.8;
        margin-bottom: 2rem;
        text-align: justify;
        opacity: 0.95;
    }
    
    .credentials {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin-bottom: 2rem;
    }
    
    .credential-badge {
        background: var(--primary-blue);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .about-button {
        background: white;
        color: var(--text-dark);
        padding: 1rem 2rem;
        border: none;
        border-radius: 8px;
        font-weight: 700;
        text-transform: uppercase;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        font-size: 1rem;
    }
    
    .about-button:hover {
        background: var(--light-blue);
        transform: translateY(-2px);
    }
    
    .about-image {
        text-align: center;
    }
    
    .about-photo {
        width: 300px;
        height: 400px;
        object-fit: cover;
        border-radius: 15px;
        border: 4px solid white;
        box-shadow: var(--shadow-medium);
    }
    
    .companies-section {
        padding: 4rem 2rem;
        background: var(--bg-warm-white);
        text-align: center;
    }
    
    .companies-title {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        color: var(--primary-blue);
        margin-bottom: 1rem;
    }
    
    .companies-subtitle {
        color: var(--text-medium);
        margin-bottom: 3rem;
        font-size: 1.1rem;
    }
    
    .companies-logos {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        gap: 2rem;
        opacity: 0.7;
    }
    
    .company-logo {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text-medium);
        padding: 1rem 2rem;
        border: 2px solid var(--border-light);
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .company-logo:hover {
        border-color: var(--primary-blue);
        color: var(--primary-blue);
        opacity: 1;
    }
    
    .map-section {
        padding: 0;
        height: 400px;
    }
    
    .map-container {
        width: 100%;
        height: 100%;
    }
    
    .map-container iframe {
        width: 100%;
        height: 100%;
        border: none;
    }
    
    .testimonials-section {
        background: var(--bg-warm-white);
        color: var(--text-dark);
        padding: 5rem 2rem;
        text-align: center;
    }
    
    .testimonials-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        color: var(--text-dark);
        margin-bottom: 1rem;
    }
    
    .testimonials-subtitle {
        font-size: 1.2rem;
        margin-bottom: 1rem;
        font-weight: 600;
        color: var(--text-dark);
    }
    
    .testimonials-text {
        margin-bottom: 2rem;
        color: var(--text-medium);
        font-size: 1.1rem;
    }
    
    .stars {
        font-size: 2rem;
        color: #fbbf24;
        margin-bottom: 2rem;
        display: flex;
        justify-content: center;
        gap: 0.5rem;
    }
    
    .testimonials-button {
        background: linear-gradient(135deg, var(--primary-blue), var(--primary-teal));
        color: white;
        padding: 1rem 2rem;
        border: none;
        border-radius: 8px;
        font-weight: 700;
        text-transform: uppercase;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        font-size: 1rem;
        box-shadow: var(--shadow-soft);
    }
    
    .testimonials-button:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-medium);
    }
    
    .footer {
        background: var(--text-dark);
        color: white;
        padding: 3rem 2rem 2rem;
    }
    
    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 2fr 1fr 1fr;
        gap: 3rem;
        margin-bottom: 2rem;
    }
    
    .footer-section h3 {
        font-family: 'Playfair Display', serif;
        margin-bottom: 1rem;
        color: var(--light-blue);
    }
    
    .footer-links {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }
    
    .footer-links a {
        color: rgba(255, 255, 255, 0.8);
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    .footer-links a:hover {
        color: var(--light-blue);
    }
    
    .footer-social {
        display: flex;
        justify-content: center;
        gap: 2.5rem;
        margin-top: 1rem;
    }
    
    .footer-social a {
        color: rgba(255, 255, 255, 0.8);
        font-size: 1.5rem;
        transition: color 0.3s ease;
    }
    
    .footer-social a:hover {
        color: var(--primary-blue);
    }
    
    .footer-bottom {
        border-top: 1px solid rgba(255, 255, 255, 0.2);
        padding-top: 2rem;
        text-align: center;
        color: rgba(255, 255, 255, 0.6);
        font-size: 0.9rem;
    }
    
    .whatsapp-float {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        background: #25d366;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.8rem;
        text-decoration: none;
        box-shadow: var(--shadow-medium);
        z-index: 1000;
        transition: all 0.3s ease;
    }
    
    .whatsapp-float:hover {
        transform: scale(1.1);
        box-shadow: 0 8px 30px rgba(37, 211, 102, 0.4);
    }
    
    @media (max-width: 768px) {
        .nav-container {
            padding: 0 1rem;
        }
        
        .logo {
            font-size: 1.4rem;
        }
        
        .services-grid {
            grid-template-columns: 1fr;
        }
        
        .about-container {
            grid-template-columns: 1fr;
            text-align: center;
            gap: 2rem;
        }
        
        .about-photo {
            width: 250px;
            height: 320px;
        }
        
        .footer-content {
            grid-template-columns: 1fr;
            text-align: center;
        }
        
        .companies-logos {
            flex-direction: column;
        }
    }
    
    @media (max-width: 480px) {
        .hero-content {
            padding: 1rem;
        }
        
        .whatsapp-float {
            bottom: 1rem;
            right: 1rem;
            width: 50px;
            height: 50px;
            font-size: 1.5rem;
        }
    }
    
    .fade-in {
        opacity: 0;
        transform: translateY(30px);
        transition: all 0.8s ease;
    }
    
    .fade-in.active {
        opacity: 1;
        transform: translateY(0);
    }
    </style>
    
    <script async src="https://www.googletagmanager.com/gtag/js?id={{ config.google_ads_id }}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', '{{ config.google_ads_id }}');
    </script>
    
    <script>
        function gtagSendEvent(url) {
            var callback = function () {
                if (typeof url === 'string') {
                    window.location = url;
                }
            };
            gtag('event', 'whatsapp_contact', {
                'event_callback': callback,
                'event_timeout': 2000,
            });
            return false;
        }
    </script>
</head>
<body>
    <header class="header">
        <nav class="nav-container">
            <a href="#" class="logo">{{ config.business_name }}<span class="highlight">.</span></a>
            <div class="hamburger-menu" id="hamburgerMenu">
                <div class="hamburger-line"></div>
                <div class="hamburger-line"></div>
                <div class="hamburger-line"></div>
            </div>
        </nav>
    </header>

    <div class="menu-overlay" id="menuOverlay"></div>

    <nav class="mobile-menu" id="mobileMenu">
        <a href="#inicio" class="mobile-menu-item">Inicio</a>
        <a href="#servicios" class="mobile-menu-item">Servicios</a>
        <a href="#sobre-mi" class="mobile-menu-item">Mi Experiencia</a>
        <a href="#contacto" class="mobile-menu-item">Contacto</a>
        <a href="{{ config.instagram_url }}" target="_blank" class="mobile-menu-item mobile-menu-instagram">
            <i class="fab fa-instagram"></i>
            Instagram
        </a>
    </nav>

    <section class="hero" id="inicio">
        <video class="hero-video" id="heroVideo" muted loop playsinline preload="metadata">
            <source src="{{ config.hero_video }}" type="video/mp4">
        </video>
        
        <div class="hero-content">
            <div class="hero-subtitle">{{ config.title }}</div>
            <h1 class="hero-title">{{ config.advisor_name }}</h1>
            <p class="hero-message">{{ config.main_message }}</p>
            <p class="hero-submessage">{{ config.submessage }}</p>
            <p class="hero-final">{{ config.final_message }}</p>
            <a href="{{ whatsapp_link }}" class="cta-button" target="_blank" onclick="return gtagSendEvent('{{ whatsapp_link }}')">
                <i class="fas fa-calculator"></i> COTIZAR AHORA
            </a>
        </div>
    </section>

    <section class="services-section" id="servicios">
        <div class="section-container">
            <h2 class="section-title">Nuestros Servicios</h2>
            <p class="section-subtitle"></p>
            <div class="services-grid">
                {% for service in services %}
                <div class="service-card fade-in">
                    <img src="{{ service.image }}" alt="{{ service.name }}" class="service-image">
                    <div class="service-content">
                        <h3 class="service-name">{{ service.name }}</h3>
                        <p class="service-description">{{ service.description }}</p>
                        <button class="service-button" onclick="openWhatsApp('{{ service.name }}')">
                            <i class="fas fa-phone"></i> COTIZAR
                        </button>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <section class="companies-section">
        <div class="section-container">
            <h2 class="companies-title">Trabajamos con las mejores compañías para ofrecerte la mejor protección</h2>
            <p class="companies-subtitle">Comparamos precios entre múltiples compañías para conseguirte la mejor oferta posible en el mercado actual.</p>
            <p class="companies-note">NO ENCONTRARAS UN MEJOR PRECIO EN NINGUNA PARTE.</p>
        </div>
    </section>

    <section class="about-section" id="mi-experiencia">
        <div class="about-container">
            <div class="about-content">
                <h2>Mi Experiencia</h2>
                <div class="credentials">
                    <span class="credential-badge">✓ Licenciada SFC</span>
                    <span class="credential-badge">✓ +20 Años Experiencia</span>
                    <span class="credential-badge">✓ +2000 Clientes Satisfechos</span>
                </div>
                <p class="about-text">{{ config.about_text }}</p>
                <a href="{{ whatsapp_link }}" class="about-button" target="_blank" onclick="return gtagSendEvent('{{ whatsapp_link }}')">
                    <i class="fab fa-whatsapp"></i> AGENDAR CITA
                </a>
            </div>
            <div class="about-image">
                <img src="https://res.cloudinary.com/dweqlnl1w/image/upload/v1759786553/IMG_7267_ppikay.png" alt="{{ config.advisor_name }}" class="about-photo">
            </div>
        </div>
    </section>

    <section class="map-section" id="contacto">
        <div class="map-container">
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31715.648982!2d-73.13521!3d7.12539!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e683f408f6f6f67%3A0x6e5a5d4b8b8b8b8b!2sBucaramanga%2C%20Santander!5e0!3m2!1ses!2sco!4v1644542567890!5m2!1ses!2sco"
                width="100%" 
                height="100%" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade">
            </iframe>
        </div>
    </section>

    <section class="testimonials-section">
        <div class="section-container">
            <h2 class="testimonials-title">Lo Que Dicen Nuestros Clientes</h2>
            <p class="testimonials-subtitle">EXPERIENCIAS REALES DE FAMILIAS Y EMPRESAS</p>
            <p class="testimonials-text">Más de 2000 clientes satisfechos nos respaldan. Lee las opiniones reales de quienes ya protegen su patrimonio con nosotros.</p>
            <div class="stars">
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
            </div>
            <a href="https://g.page/reviews" target="_blank" class="testimonials-button">
                VER TODAS LAS OPINIONES
            </a>
        </div>
    </section>

    <footer class="footer">
        <div class="footer-content">
            <div class="footer-section">
                <h3>{{ config.business_name }}</h3>
                <p>Tu asesora de seguros de confianza. </p>
                <div class="footer-social">
                    <a href="{{ config.instagram_url }}" target="_blank">
                        <i class="fab fa-instagram"></i>
                    </a>
                    <a href="{{ whatsapp_link }}" target="_blank">
                        <i class="fab fa-whatsapp"></i>
                    </a>
                    <a href="mailto:{{ config.email }}">
                        <i class="fas fa-envelope"></i>
                    </a>
                </div>
            
            <div class="footer-section">
                <h3>Contacto</h3>
                <div class="footer-links">
                    <a href="tel:(+57) 321 648-4963">(+57) 321-648-4963</a>
                    <a href="mailto:{{ config.email }}">{{ config.email }}</a>
                    <a href="#contacto">{{ config.location }}</a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2025. Todos los derechos reservados. </p>
        </div>
    </footer>

    <a href="{{ whatsapp_link }}" class="whatsapp-float" target="_blank" aria-label="Contactar por WhatsApp" onclick="return gtagSendEvent('{{ whatsapp_link }}')">
        <i class="fab fa-whatsapp"></i>
    </a>

    <script>
    const hamburgerMenu = document.getElementById('hamburgerMenu');
    const mobileMenu = document.getElementById('mobileMenu');
    const menuOverlay = document.getElementById('menuOverlay');
    const mobileMenuItems = document.querySelectorAll('.mobile-menu-item');

    hamburgerMenu.addEventListener('click', toggleMenu);
    menuOverlay.addEventListener('click', closeMenu);

    mobileMenuItems.forEach(item => {
        item.addEventListener('click', (e) => {
            if (!item.hasAttribute('target')) {
                closeMenu();
            }
        });
    });

    function toggleMenu() {
        hamburgerMenu.classList.toggle('active');
        mobileMenu.classList.toggle('active');
        menuOverlay.classList.toggle('active');
        
        if (mobileMenu.classList.contains('active')) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = '';
        }
    }

    function closeMenu() {
        hamburgerMenu.classList.remove('active');
        mobileMenu.classList.remove('active');
        menuOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    const heroVideo = document.getElementById('heroVideo');
    
    if (heroVideo) {
        heroVideo.addEventListener('loadeddata', () => {
            tryPlayVideo();
        });
        
        function tryPlayVideo() {
            heroVideo.play()
                .then(() => {
                    heroVideo.classList.add('loaded');
                })
                .catch(error => {
                    console.log('Video fallback to image background');
                });
        }
        
        heroVideo.load();
    }
    
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.fade-in').forEach(el => {
        observer.observe(el);
    });
    
    function openWhatsApp(serviceName) {
        const message = `Hola! Me interesa cotizar ${serviceName}. ¿Podrías ayudarme?`;
        const phone = '{{ config.whatsapp_number }}'.replace("+", "").replace(" ", "");
        const encodedMessage = encodeURIComponent(message);
        const whatsappUrl = `https://wa.me/${phone}?text=${encodedMessage}`;
        
        window.open(whatsappUrl, '_blank');
        
        if (typeof gtag !== 'undefined') {
            gtag('event', 'service_inquiry', {
                'event_category': 'engagement',
                'event_label': serviceName
            });
        }
    }
    
    document.querySelectorAll('a[href*="wa.me"]').forEach(btn => {
        btn.addEventListener('click', () => {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'whatsapp_click', {
                    'event_category': 'conversion',
                    'event_label': 'contact_button'
                });
            }
        });
    });
    
    console.log('🛡️ {{ config.advisor_name }} - Asesora de Seguros');
    console.log('📱 Instagram: {{ config.instagram_handle }}');
    console.log('💬 WhatsApp: {{ config.whatsapp_number }}');
    console.log('📧 Email: {{ config.email }}');
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))