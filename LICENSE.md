<!DOCTYPE html>
<html lang="mn" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MKVISA - Албан ёсны танилцуулга</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#f0f4f8',
                            100: '#dbe3ed',
                            200: '#bdcbdc',
                            300: '#90a9c5',
                            400: '#5e82aa',
                            500: '#3e638e',
                            600: '#2f4e73',
                            700: '#273f5f',
                            800: '#233650',
                            900: '#142031',
                            gold: '#D4AF37',
                            goldHover: '#C59B27',
                            crimson: '#9E1B32'
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .gradient-bg {
            background: radial-gradient(circle at 10% 20%, rgb(20, 32, 49) 0%, rgb(39, 63, 95) 100%);
        }
        .gold-border-glow:hover {
            box-shadow: 0 0 15px rgba(212, 175, 55, 0.4);
            border-color: #D4AF37;
        }
    </style>
</head>
<body class="bg-slate-50 text-brand-900 overflow-x-hidden antialiased">

    <!-- Header / Navigation -->
    <header class="sticky top-0 z-50 backdrop-blur-md bg-brand-900/90 border-b border-brand-800 text-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-20">
                <div class="flex items-center space-x-3">
                    <div class="w-12 h-12 rounded-xl bg-gradient-to-tr from-brand-gold to-brand-crimson flex items-center justify-center font-bold text-2xl tracking-wider text-white shadow-lg">
                        MK
                    </div>
                    <div>
                        <span class="text-xl font-extrabold tracking-tight bg-gradient-to-r from-white via-slate-200 to-brand-gold bg-clip-text text-transparent">MKVISA</span>
                        <p class="text-[9px] tracking-widest text-slate-300 uppercase font-semibold">Global Consulting Group</p>
                    </div>
                </div>
                <!-- Desktop Nav -->
                <nav class="hidden md:flex space-x-8 text-sm font-medium">
                    <a href="#about" class="hover:text-brand-gold transition-colors duration-200">Тойм</a>
                    <a href="#services" class="hover:text-brand-gold transition-colors duration-200">Үйл ажиллагаа</a>
                    <a href="#team" class="hover:text-brand-gold transition-colors duration-200">Манай Баг</a>
                    <a href="#ai-hub" class="hover:text-brand-gold transition-colors duration-200">✨ AI Зөвлөх</a>
                    <a href="#why-us" class="hover:text-brand-gold transition-colors duration-200">Давуу тал</a>
                    <a href="#interactive-consult" class="hover:text-brand-gold transition-colors duration-200">Ухаалаг зөвлөх</a>
                </nav>
                <div>
                    <a href="#contact" class="inline-flex items-center justify-center px-5 py-2.5 rounded-xl text-xs font-bold uppercase tracking-wider bg-gradient-to-r from-brand-gold to-amber-500 hover:from-brand-goldHover hover:to-amber-600 text-brand-900 shadow-md transform hover:-translate-y-0.5 transition-all duration-150">
                        Холбоо барих
                    </a>
                </div>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="relative overflow-hidden text-white py-24 lg:py-32 gradient-bg">
        <!-- Background Elements -->
        <div class="absolute inset-0 bg-[linear-gradient(to_right,#1f293710_1px,transparent_1px),linear-gradient(to_bottom,#1f293710_1px,transparent_1px)] bg-[size:4rem_4rem]"></div>
        <div class="absolute -top-40 -right-40 w-96 h-96 rounded-full bg-brand-gold/10 blur-3xl"></div>
        <div class="absolute -bottom-40 -left-40 w-96 h-96 rounded-full bg-brand-crimson/10 blur-3xl"></div>

        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
                <!-- Left Content -->
                <div class="lg:col-span-7 space-y-6 text-center lg:text-left">
                    <span class="inline-flex items-center gap-1.5 py-1 px-3 rounded-full text-xs font-semibold bg-brand-crimson/30 text-rose-300 border border-brand-crimson/40">
                        <span class="w-2 h-2 rounded-full bg-rose-400 animate-pulse"></span>
                        Глобал Консалтинг Групп
                    </span>
                    <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight leading-tight">
                        БНСУ-д оршин суугчдын <br>
                        <span class="bg-gradient-to-r from-brand-gold via-yellow-200 to-white bg-clip-text text-transparent">Найдвартай Туслах</span>
                    </h1>
                    <p class="text-base sm:text-lg text-slate-300 max-w-2xl mx-auto lg:mx-0 font-light leading-relaxed">
                        БНСУ-ын хууль тогтоомжийг чандлан мөрдөж, гадаад иргэдэд тулгардаг хууль эрх зүй, захиргааны саад бэрхшээлийг шуурхай шийдвэрлэн, хоёр орныг холбосон хамгийн найдвартай бизнесийн гүүр болон ажиллаж байна.
                    </p>
                    
                    <!-- Quick Info Badges -->
                    <div class="flex flex-wrap justify-center lg:justify-start gap-4 pt-4">
                        <div class="flex items-center space-x-2 bg-brand-800/60 backdrop-blur border border-brand-700/50 py-2 px-4 rounded-xl">
                            <svg class="w-5 h-5 text-brand-gold" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                            <span class="text-xs font-semibold text-slate-200">Үүсгэн байгуулагдсан: 2022</span>
                        </div>
                        <div class="flex items-center space-x-2 bg-brand-800/60 backdrop-blur border border-brand-700/50 py-2 px-4 rounded-xl">
                            <svg class="w-5 h-5 text-brand-gold" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
                            <span class="text-xs font-semibold text-slate-200">Бүртгэл: 408-34-91980</span>
                        </div>
                    </div>

                    <div class="pt-6 flex flex-col sm:flex-row justify-center lg:justify-start gap-4">
                        <a href="#services" class="inline-flex items-center justify-center px-8 py-3.5 rounded-xl font-bold bg-white text-brand-900 hover:bg-slate-100 shadow-lg hover:shadow-xl transition-all duration-150">
                            Үйлчилгээ үзэх
                        </a>
                        <a href="#ai-hub" class="inline-flex items-center justify-center px-8 py-3.5 rounded-xl font-bold bg-gradient-to-r from-brand-gold to-amber-400 text-brand-900 hover:shadow-lg hover:scale-[1.02] transition-all duration-150">
                            ✨ AI Зөвлөх Ашиглах
                        </a>
                    </div>
                </div>

                <!-- Right Visual -->
                <div class="lg:col-span-5 relative flex justify-center">
                    <div class="relative w-72 h-96 sm:w-80 sm:h-[420px] rounded-3xl overflow-hidden shadow-2xl border-4 border-brand-800 bg-brand-800/40 p-1">
                        <!-- Simulated modern profile display with premium abstract gradients representing MKVISA -->
                        <div class="w-full h-full rounded-2xl bg-gradient-to-br from-brand-700 via-brand-900 to-black p-6 flex flex-col justify-between relative overflow-hidden">
                            <div class="absolute -top-20 -right-20 w-48 h-48 rounded-full bg-brand-gold/20 blur-2xl"></div>
                            
                            <!-- Header Info -->
                            <div class="flex justify-between items-start z-10">
                                <span class="text-xs font-bold tracking-widest text-brand-gold uppercase">Company Profile</span>
                                <span class="bg-brand-crimson py-1 px-2.5 rounded text-[10px] font-bold tracking-wider">SEOUL, KOREA</span>
                            </div>

                            <!-- Abstract Graphic -->
                            <div class="my-auto py-6 flex flex-col items-center justify-center space-y-4 z-10">
                                <div class="w-24 h-24 rounded-full bg-gradient-to-tr from-brand-gold via-amber-400 to-brand-crimson p-1 shadow-lg flex items-center justify-center">
                                    <span class="text-3xl font-black text-brand-900">MK</span>
                                </div>
                                <div class="text-center">
                                    <h4 class="text-xl font-extrabold text-white">MKVISA CO., LTD.</h4>
                                    <p class="text-xs text-brand-gold font-medium mt-1">엠케이비за</p>
                                </div>
                            </div>

                            <!-- Interactive Card Footer -->
                            <div class="border-t border-slate-700/60 pt-4 z-10 space-y-2">
                                <p class="text-[11px] text-slate-300 italic text-center">
                                    "БНСУ-д оршин суугч гадаад иргэдийн найдвартай туслах төв, Глобал бизнесийн гүүр"
                                </p>
                                <div class="flex justify-center space-x-1.5 text-[9px] text-slate-400">
                                    <span>Виз</span><span>•</span>
                                    <span>Хөдөлмөр</span><span>•</span>
                                    <span>Боловсрол</span><span>•</span>
                                    <span>Эрүүл Мэнд</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Overview Stat Counter Section -->
    <section id="about" class="py-12 bg-white border-b border-slate-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 text-center">
                <div class="p-6 bg-slate-50 rounded-2xl border border-slate-100">
                    <span class="block text-4xl font-extrabold text-brand-700">2022</span>
                    <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mt-1">Үүсгэн байгуулагдсан</span>
                </div>
                <div class="p-6 bg-slate-50 rounded-2xl border border-slate-100">
                    <span class="block text-4xl font-extrabold text-brand-700">100%</span>
                    <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mt-1">Хууль тогтоомжийн мөрдөлт</span>
                </div>
                <div class="p-6 bg-slate-50 rounded-2xl border border-slate-100">
                    <span class="block text-4xl font-extrabold text-brand-700">5+</span>
                    <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mt-1">Үндсэн чиглэл</span>
                </div>
                <div class="p-6 bg-slate-50 rounded-2xl border border-slate-100">
                    <span class="block text-4xl font-extrabold text-brand-700">Олон зуун</span>
                    <span class="block text-xs font-bold uppercase tracking-wider text-slate-400 mt-1">Шийдвэрлэсэн маргаан</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Company Overview -->
    <section class="py-20 lg:py-24 bg-slate-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="bg-white rounded-3xl shadow-xl overflow-hidden border border-slate-100">
                <div class="grid grid-cols-1 lg:grid-cols-12">
                    <div class="lg:col-span-5 bg-gradient-to-br from-brand-900 to-brand-700 p-8 sm:p-12 text-white flex flex-col justify-between relative">
                        <!-- Abstract Design -->
                        <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#fff_1px,transparent_1px)] [background-size:16px_16px]"></div>
                        <div class="relative z-10 space-y-6">
                            <h3 class="text-xs font-bold tracking-widest text-brand-gold uppercase">Компанийн зорилго</h3>
                            <h2 class="text-3xl font-extrabold tracking-tight">Бид хэн бэ?</h2>
                            <p class="text-slate-300 font-light leading-relaxed text-sm sm:text-base">
                                MKVISA нь БНСУ-д оршин сууж буй гадаад иргэдийн эрх ашгийг хамгаалах, виз болон захиргааны асуудлыг шийдвэрлэх, олон улсын боловсрол, эрүүл мэндийн аялал жуулчлал, гадаад худалдааны чиглэлээр цогц үйлчилгээ үзүүлдэг Глобал Консалтинг Групп юм.
                            </p>
                        </div>
                        <div class="mt-8 pt-8 border-t border-brand-800 relative z-10">
                            <p class="text-brand-gold font-bold text-sm italic">"БНСУ болон Монгол Улсыг холбосон хамгийн найдвартай бизнесийн гүүр"</p>
                        </div>
                    </div>
                    
                    <div class="lg:col-span-7 p-8 sm:p-12 space-y-8 bg-white">
                        <h3 class="text-2xl font-bold tracking-tight text-brand-900">Бидний баримталдаг зарчим</h3>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                            <!-- Principle 1 -->
                            <div class="flex items-start space-x-4">
                                <div class="p-3 bg-brand-50 rounded-xl text-brand-600 shrink-0">
                                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
                                </div>
                                <div>
                                    <h4 class="font-bold text-brand-800">Хуулийн дээд боловсрол</h4>
                                    <p class="text-xs text-slate-500 mt-1">БНСУ-ын хууль тогтоомжийн хүрээнд бүх ажиллагаа албан ёсны дагуу явагдана.</p>
                                </div>
                            </div>
                            <!-- Principle 2 -->
                            <div class="flex items-start space-x-4">
                                <div class="p-3 bg-brand-50 rounded-xl text-brand-600 shrink-0">
                                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                </div>
                                <div>
                                    <h4 class="font-bold text-brand-800">Шуурхай шийдвэрлэлт</h4>
                                    <p class="text-xs text-slate-500 mt-1">Тулгарсан саад бэрхшээл, захиргааны болон визний асуудалд цаг алдалгүй хариу өгнө.</p>
                                </div>
                            </div>
                            <!-- Principle 3 -->
                            <div class="flex items-start space-x-4">
                                <div class="p-3 bg-brand-50 rounded-xl text-brand-600 shrink-0">
                                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                                </div>
                                <div>
                                    <h4 class="font-bold text-brand-800">Салбарын мэргэжилтнүүд</h4>
                                    <p class="text-xs text-slate-500 mt-1">Худалдаа, боловсрол, эрүүл мэнд болон хуулийн чиглэлээр мэргэшсэн баг хамт олон.</p>
                                </div>
                            </div>
                            <!-- Principle 4 -->
                            <div class="flex items-start space-x-4">
                                <div class="p-3 bg-brand-50 rounded-xl text-brand-600 shrink-0">
                                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                                </div>
                                <div>
                                    <h4 class="font-bold text-brand-800">Орчин үеийн дижитал шийдэл</h4>
                                    <p class="text-xs text-slate-500 mt-1">Онлайн маркетинг болон дэвшилтэт контент ашиглан бизнесийг шинэ шатанд гаргана.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Main Activities Section (Interactive Tabs) -->
    <section id="services" class="py-20 lg:py-24 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto space-y-4 mb-16">
                <span class="text-xs font-extrabold uppercase tracking-widest text-brand-crimson">Хийж буй ажил</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-brand-900">Үйл ажиллагааны үндсэн чиглэлүүд</h2>
                <p class="text-slate-500 font-light">Визний дэмжлэгээс эхлээд бизнесийн глобал түншлэл хүртэлх бүх төрлийн цогц үйлчилгээ</p>
            </div>

            <!-- Mobile Select Dropdown for Tabs -->
            <div class="sm:hidden mb-8">
                <label for="TabSelect" class="sr-only">Үйлчилгээ сонгох</label>
                <select id="TabSelect" onchange="switchTab(this.value)" class="w-full rounded-xl border-slate-200 bg-white p-3 font-semibold shadow-sm text-brand-800">
                    <option value="tab-labor">1. Хөдөлмөр, хууль эрх зүй & Виз</option>
                    <option value="tab-medical">2. Эрүүл мэндийн аялал жуулчлал</option>
                    <option value="tab-education">3. Гадаад оюутан зуучлал</option>
                    <option value="tab-trade">4. Гадаад худалдаа & Бизнес</option>
                    <option value="tab-marketing">5. Дижитал контент маркетинг</option>
                </select>
            </div>

            <!-- Desktop Tabs Navigation -->
            <div class="hidden sm:block border-b border-slate-100 mb-12">
                <nav class="flex justify-between -mb-px overflow-x-auto space-x-2">
                    <button onclick="switchTab('tab-labor')" id="btn-tab-labor" class="tab-btn border-b-2 border-brand-gold py-4 px-4 text-sm font-bold text-brand-900 focus:outline-none flex items-center space-x-2">
                        <span>⚖️ Хөдөлмөр & Виз</span>
                    </button>
                    <button onclick="switchTab('tab-medical')" id="btn-tab-medical" class="tab-btn border-b-2 border-transparent py-4 px-4 text-sm font-bold text-slate-400 hover:text-slate-600 focus:outline-none flex items-center space-x-2">
                        <span>🏥 Эрүүл мэнд</span>
                    </button>
                    <button onclick="switchTab('tab-education')" id="btn-tab-education" class="tab-btn border-b-2 border-transparent py-4 px-4 text-sm font-bold text-slate-400 hover:text-slate-600 focus:outline-none flex items-center space-x-2">
                        <span>🎓 Боловсрол / Оюутан</span>
                    </button>
                    <button onclick="switchTab('tab-trade')" id="btn-tab-trade" class="tab-btn border-b-2 border-transparent py-4 px-4 text-sm font-bold text-slate-400 hover:text-slate-600 focus:outline-none flex items-center space-x-2">
                        <span>🤝 Худалдаа & Бизнес</span>
                    </button>
                    <button onclick="switchTab('tab-marketing')" id="btn-tab-marketing" class="tab-btn border-b-2 border-transparent py-4 px-4 text-sm font-bold text-slate-400 hover:text-slate-600 focus:outline-none flex items-center space-x-2">
                        <span>📱 Дижитал Маркетинг</span>
                    </button>
                </nav>
            </div>

            <!-- Tabs Content -->
            <div id="tab-container" class="bg-slate-50 rounded-3xl p-6 sm:p-10 border border-slate-100">
                
                <!-- Tab 1: Labor & Visa -->
                <div id="tab-labor" class="tab-content block space-y-8 animate-fade-in">
                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                        <div class="lg:col-span-7 space-y-6">
                            <span class="inline-block py-1 px-3 rounded-full text-xs font-bold bg-brand-500 text-white">ҮНДСЭН ЧИГЛЭЛ 01</span>
                            <h3 class="text-2xl sm:text-3xl font-extrabold text-brand-900">Хөдөлмөрийн хууль эрх зүйн зөвлөх үйлчилгээ</h3>
                            <p class="text-slate-600 leading-relaxed font-light">
                                Гадаадын иргэдийн хэлний бэрхшээл болон мэдээлэл дутмаг байдлаас үүдэн зөрчигдсөн эрх ашгийг БНСУ-ын Хөдөлмөрийн хууль тогтоомжийн хүрээнд албан ёсоор хамгаална.
                            </p>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
                                <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm">
                                    <h4 class="font-bold text-brand-800 text-sm flex items-center gap-2">
                                        <span class="text-brand-gold">💰</span> Цалингийн маргаан шийдвэрлэлт
                                    </h4>
                                    <p class="text-xs text-slate-500 mt-1">Үндэслэлгүй дутуу олгосон эсвэл саатуулсан цалинг Хөдөлмөрийн яаманд гомдол гаргах замаар бүрэн барагдуулна.</p>
                                </div>
                                <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm">
                                    <h4 class="font-bold text-brand-800 text-sm flex items-center gap-2">
                                        <span class="text-brand-gold">📑</span> Тэтгэмж нэхэмжлэх
                                    </h4>
                                    <p class="text-xs text-slate-500 mt-1">1-ээс дээш жил ажилласан иргэдийн олгогдоогүй тэтгэмжийг хуулийн дагуу гаргуулж өгнө.</p>
                                </div>
                            </div>
                        </div>
                        <div class="lg:col-span-5 bg-white p-6 rounded-2xl border border-slate-100 shadow-md">
                            <h4 class="font-bold text-brand-900 border-b pb-3 mb-4">Визний цогц үйлчилгээний шилжилтүүд:</h4>
                            <ul class="space-y-3 text-xs sm:text-sm text-slate-600">
                                <li class="flex items-center space-x-2">
                                    <span class="text-green-500">✔</span>
                                    <span><strong>D-4 / D-2 -оос D-10</strong> (Ажил хайх виз)</span>
                                </li>
                                <li class="flex items-center space-x-2">
                                    <span class="text-green-500">✔</span>
                                    <span><strong>D-10 -аас E-7</strong> (Мэргэжилтний хөдөлмөр эрхлэлт)</span>
                                </li>
                                <li class="flex items-center space-x-2">
                                    <span class="text-green-500">✔</span>
                                    <span><strong>F-2</strong> (Оршин суух), <strong>F-6</strong> (Гэрлэлт)</span>
                                </li>
                                <li class="flex items-center space-x-2">
                                    <span class="text-green-500">✔</span>
                                    <span><strong>F-5</strong> (Байнгын оршин суух) болон Иргэншил</span>
                                </li>
                            </ul>
                            <div class="mt-6">
                                <a href="#ai-hub" class="block text-center py-2 px-4 rounded-xl text-xs font-bold uppercase bg-brand-gold text-brand-900 hover:bg-brand-goldHover transition-colors duration-150">Миний визийг шалгах</a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Tab 2: Medical Tourism -->
                <div id="tab-medical" class="tab-content hidden space-y-8 animate-fade-in">
                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                        <div class="lg:col-span-7 space-y-6">
                            <span class="inline-block py-1 px-3 rounded-full text-xs font-bold bg-brand-500 text-white">ҮНДСЭН ЧИГЛЭЛ 02</span>
                            <h3 class="text-2xl sm:text-3xl font-extrabold text-brand-900">Эрүүл мэндийн аялал жуулчлал</h3>
                            <p class="text-slate-600 leading-relaxed font-light">
                                БНСУ-ын эрүүл мэндийн өндөр технологи, шилдэг нарийн мэргэжлийн эмнэлгүүдийн үйлчилгээг Монголчууддаа хамгийн амар, шуурхай хэлбэрээр хүргэдэг.
                            </p>
                            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-2">
                                <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm">
                                    <div class="text-2xl mb-2">✨</div>
                                    <h4 class="font-bold text-brand-800 text-sm">Гоо сайхан & Арьс</h4>
                                    <p class="text-[11px] text-slate-500 mt-1">Тэргүүлэгч клиникүүдийн гоо сайхны мэс засал, арьс арчилгааны үйлчилгээ.</p>
                                </div>
                                <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm">
                                    <div class="text-2xl mb-2">👁️</div>
                                    <h4 class="font-bold text-brand-800 text-sm">Хараа засал</h4>
                                    <p class="text-[11px] text-slate-500 mt-1">Солонгосын шилдэг лазер болон линз суулгах нүдний эмчилгээ.</p>
                                </div>
                                <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm">
                                    <div class="text-2xl mb-2">🩺</div>
                                    <h4 class="font-bold text-brand-800 text-sm">Оношилгоо & Хүнд өвчин</h4>
                                    <p class="text-[11px] text-slate-500 mt-1">Багц шинжилгээ, хүнд хэлбэрийн өвчний төрөлжсөн нарийн эмчилгээ.</p>
                                </div>
                            </div>
                        </div>
                        <div class="lg:col-span-5 bg-white p-6 rounded-2xl border border-slate-100 shadow-md">
                            <h4 class="font-bold text-brand-900 border-b pb-3 mb-4">Нэг цэгийн үйлчилгээ (One-stop Medical):</h4>
                            <div class="space-y-4">
                                <div class="flex items-start space-x-3">
                                    <span class="flex items-center justify-center w-6 h-6 rounded-full bg-brand-100 text-brand-700 text-xs font-bold shrink-0">1</span>
                                    <p class="text-xs text-slate-600">Солонгос явахаас өмнөх анхан шатны зөвлөгөө, эмнэлгийн цаг захиалга</p>
                                </div>
                                <div class="flex items-start space-x-3">
                                    <span class="flex items-center justify-center w-6 h-6 rounded-full bg-brand-100 text-brand-700 text-xs font-bold shrink-0">2</span>
                                    <p class="text-xs text-slate-600">БНСУ-д ирсний дараа эмнэлэгт мэргэжлийн орчуулагч дагалдах үйлчилгээ</p>
                                </div>
                                <div class="flex items-start space-x-3">
                                    <span class="flex items-center justify-center w-6 h-6 rounded-full bg-brand-100 text-brand-700 text-xs font-bold shrink-0">3</span>
                                    <p class="text-xs text-slate-600">Эмчилгээний дараах хяналт болон зааварчилгаа, зөвлөгөө</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Tab 3: Education & Students -->
                <div id="tab-education" class="tab-content hidden space-y-8 animate-fade-in">
                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                        <div class="lg:col-span-7 space-y-6">
                            <span class="inline-block py-1 px-3 rounded-full text-xs font-bold bg-brand-500 text-white">ҮНДСЭН ЧИГЛЭЛ 03</span>
                            <h3 class="text-2xl sm:text-3xl font-extrabold text-brand-900">Гадаад оюутан зуучлал, боловсролын консалтинг</h3>
                            <p class="text-slate-600 leading-relaxed font-light">
                                БНСУ-ын их дээд сургуулиудтай тогтоосон шууд түншлэлд тулгуурлан, суралцагчдад өөрийнх нь зорилго, нөхцөл байдалд тохирсон хөтөлбөрийг санал болгодог.
                            </p>
                            <div class="bg-amber-50 border-l-4 border-amber-400 p-4 rounded-r-xl">
                                <h4 class="font-bold text-amber-800 text-sm">⚠️ ОНЦЛОХ ДАВУУ ТАЛ:</h4>
                                <p class="text-xs text-amber-900 mt-1">Оюутан зуучлалын хөтөлбөрт насны хязгаар шаардахгүйгээр бүртгэж байна.</p>
                            </div>
                        </div>
                        <div class="lg:col-span-5 bg-white p-6 rounded-2xl border border-slate-100 shadow-md">
                            <h4 class="font-bold text-brand-900 border-b pb-3 mb-4">Боловсролын чиглэлүүд:</h4>
                            <div class="space-y-3 text-xs sm:text-sm text-slate-600">
                                <div class="flex justify-between items-center py-1 border-b border-slate-100">
                                    <span>Хэлний бэлтгэл сургалт</span>
                                    <span class="bg-blue-100 text-blue-800 text-[10px] font-bold px-2 py-0.5 rounded">D-4 виз</span>
                                </div>
                                <div class="flex justify-between items-center py-1 border-b border-slate-100">
                                    <span>Бакалавр, Магистр, Докторын зэрэг</span>
                                    <span class="bg-purple-100 text-purple-800 text-[10px] font-bold px-2 py-0.5 rounded">D-2 виз</span>
                                </div>
                                <div class="flex justify-between items-center py-1 border-b border-slate-100">
                                    <span>Тэтгэлэгт хамрагдах зааварчилгаа</span>
                                    <span class="bg-green-100 text-green-800 text-[10px] font-bold px-2 py-0.5 rounded">70-100% тэтгэлэг</span>
                                </div>
                                <div class="flex justify-between items-center py-1">
                                    <span>Гэр бүл урих урилгын бичиг баримт</span>
                                    <span class="bg-rose-100 text-rose-800 text-[10px] font-bold px-2 py-0.5 rounded">F-3 виз</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Tab 4: Trade & Brokerage -->
                <div id="tab-trade" class="tab-content hidden space-y-8 animate-fade-in">
                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                        <div class="lg:col-span-7 space-y-6">
                            <span class="inline-block py-1 px-3 rounded-full text-xs font-bold bg-brand-500 text-white">ҮНДСЭН ЧИГЛЭЛ 04</span>
                            <h3 class="text-2xl sm:text-3xl font-extrabold text-brand-900">Гадаад худалдаа ба Бизнесийн зуучлал</h3>
                            <p class="text-slate-600 leading-relaxed font-light">
                                БНСУ-ын чанартай бөгөөд олон улсад хүлээн зөвшөөрөгдсөн бараа бүтээгдэхүүнийг Монгол Улсын зах зээлд шууд болон шууд бус сувгаар нийлүүлэх найдвартай гүүр болдог.
                            </p>
                            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-2">
                                <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm text-center">
                                    <span class="text-2xl">💄</span>
                                    <h4 class="font-bold text-brand-800 text-xs mt-2">Гоо сайхны бараа</h4>
                                </div>
                                <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm text-center">
                                    <span class="text-2xl">🧥</span>
                                    <h4 class="font-bold text-brand-800 text-xs mt-2">Брэнд хувцас</h4>
                                </div>
                                <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm text-center">
                                    <span class="text-2xl">🍜</span>
                                    <h4 class="font-bold text-brand-800 text-xs mt-2">Эрүүл хүнс</h4>
                                </div>
                            </div>
                        </div>
                        <div class="lg:col-span-5 bg-white p-6 rounded-2xl border border-slate-100 shadow-md">
                            <h4 class="font-bold text-brand-900 border-b pb-3 mb-4">Бизнес Түншлэлд үзүүлэх тусламж:</h4>
                            <ul class="space-y-3 text-xs sm:text-sm text-slate-600">
                                <li class="flex items-start space-x-2">
                                    <span class="text-brand-gold">✦</span>
                                    <span>Монгол, Солонгосын аж ахуйн нэгжүүдийг холбох</span>
                                </li>
                                <li class="flex items-start space-x-2">
                                    <span class="text-brand-gold">✦</span>
                                    <span>Экспорт, импортын албан ёсны гэрээ хэлцэл байгуулах</span>
                                </li>
                                <li class="flex items-start space-x-2">
                                    <span class="text-brand-gold">✦</span>
                                    <span>Зах зээлийн нарийвчилсан судалгаа болон түгээлтийн сүлжээг төлөвлөх</span>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Tab 5: Content Marketing -->
                <div id="tab-marketing" class="tab-content hidden space-y-8 animate-fade-in">
                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                        <div class="lg:col-span-7 space-y-6">
                            <span class="inline-block py-1 px-3 rounded-full text-xs font-bold bg-brand-500 text-white">ҮНДСЭН ЧИГЛЭЛ 05</span>
                            <h3 class="text-2xl sm:text-3xl font-extrabold text-brand-900">Олон нийттэй харилцах, дижитал контент маркетинг</h3>
                            <p class="text-slate-600 leading-relaxed font-light">
                                Хоёр орны соёлын онцлогийг хамгийн сайн ойлгосон бүтээлч баг сошиал медиа сувгуудыг ашиглан түнш байгууллагуудын брэндийг өндөр түвшинд хөгжүүлж байна.
                            </p>
                            <div class="flex flex-wrap gap-2 pt-2">
                                <span class="bg-rose-500 text-white text-xs px-3 py-1 rounded-full font-bold">YouTube</span>
                                <span class="bg-black text-white text-xs px-3 py-1 rounded-full font-bold">TikTok</span>
                                <span class="bg-gradient-to-r from-purple-500 to-pink-500 text-white text-xs px-3 py-1 rounded-full font-bold">Instagram</span>
                                <span class="bg-blue-600 text-white text-xs px-3 py-1 rounded-full font-bold">Facebook</span>
                            </div>
                        </div>
                        <div class="lg:col-span-5 bg-white p-6 rounded-2xl border border-slate-100 shadow-md">
                            <h4 class="font-bold text-brand-900 border-b pb-3 mb-4">Төрөлжсөн маркетингийн үйлчилгээнүүд:</h4>
                            <div class="space-y-3 text-xs sm:text-sm text-slate-600">
                                <p class="flex items-center gap-2">🎥 Их сургуулиудын элсэлтийн видео</p>
                                <p class="flex items-center gap-2">🏥 Эмнэлгийн танилцуулга ба сурталчилгаа</p>
                                <p class="flex items-center gap-2">🛍️ Бүтээгдэхүүний шууд борлуулалт (Live)</p>
                                <p class="flex items-center gap-2">⚡ Богино хэмжээний тренд контентууд (Reels/Shorts)</p>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Meet Our Team -->
    <section id="team" class="py-20 lg:py-24 bg-slate-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto space-y-4 mb-16">
                <span class="text-xs font-extrabold uppercase tracking-widest text-brand-crimson">Мэргэжилтнүүд</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-brand-900">Удирдлагын баг & Зөвлөхүүд</h2>
                <p class="text-slate-500 font-light">Өндөр ур чадвар бүхий манай мэргэжлийн баг хамт олонтой танилцана уу</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 justify-center">
                <!-- CEO Card -->
                <div class="bg-white rounded-3xl overflow-hidden shadow-md border border-slate-200/60 hover:shadow-xl transition-all duration-200 flex flex-col justify-between md:col-span-2 lg:col-span-3 lg:max-w-4xl lg:mx-auto">
                    <div class="grid grid-cols-1 md:grid-cols-12">
                        <div class="md:col-span-5 bg-brand-900 relative flex items-center justify-center p-8 text-white min-h-[300px]">
                            <div class="absolute inset-0 bg-gradient-to-br from-brand-800 to-black opacity-90"></div>
                            <!-- Styled Profile Avatar representing M. Urtnasan (CEO) -->
                            <div class="relative z-10 text-center space-y-4">
                                <div class="w-32 h-32 rounded-full border-4 border-brand-gold mx-auto overflow-hidden bg-brand-800 flex items-center justify-center text-5xl font-bold text-white shadow-xl">
                                    МУ
                                </div>
                                <div>
                                    <h4 class="text-xl font-bold tracking-tight">М. Уртнасан</h4>
                                    <p class="text-xs text-brand-gold font-semibold uppercase tracking-wider mt-1">CEO / Ерөнхий захирал</p>
                                </div>
                            </div>
                        </div>
                        <div class="md:col-span-7 p-8 flex flex-col justify-between">
                            <div class="space-y-4">
                                <span class="bg-brand-gold/20 text-brand-800 text-xs font-bold px-2.5 py-1 rounded">Strategic Leader</span>
                                <h4 class="text-lg font-bold text-brand-900">Багаас өгөх чиглүүлэг ба үйл ажиллагаа</h4>
                                <p class="text-xs sm:text-sm text-slate-600 leading-relaxed font-light">
                                    Компанийн нэгдсэн стратеги болон үйл ажиллагааг удирдахын сацуу Цагаачлалын албаны виз, захиргааны маргаан, Хөдөлмөр эрхлэлт, хөдөлмөрийн яамны харьяа цалин хөлс, тэтгэмжийн асуудал зэрэг хууль эрх зүйн онцгой нөхцөлүүд дээр шууд ажиллана.
                                </p>
                                <div class="border-t pt-3 border-slate-100">
                                    <p class="text-xs text-brand-800 font-semibold">🎓 Боловсрол & Судалгаа:</p>
                                    <p class="text-xs text-slate-500 mt-1">Солонгос хэлний орчуулагч бакалавр, БНСУ-д магистр, докторын зэрэг горилон суралцсан, эрдэм шинжилгээний 2 томоохон бүтээлтэй.</p>
                                </div>
                            </div>
                            <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
                                <span>📞 010-7651-1616</span>
                                <span class="font-medium text-brand-900">📧 mkvisa1616@gmail.com</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Consultant 1 -->
                <div class="bg-white rounded-2xl overflow-hidden shadow-sm border border-slate-100 hover:shadow-md transition-all duration-150 p-6 flex flex-col justify-between">
                    <div class="space-y-4">
                        <div class="flex items-center space-x-4">
                            <div class="w-16 h-16 rounded-full bg-indigo-50 flex items-center justify-center text-xl font-bold text-indigo-700">ЭР</div>
                            <div>
                                <h4 class="font-extrabold text-brand-900">Эрдэнэчимэг</h4>
                                <p class="text-xs text-slate-400 font-semibold uppercase mt-0.5">Ахлах Зөвлөх</p>
                            </div>
                        </div>
                        <span class="inline-block bg-indigo-50 text-indigo-800 text-[10px] font-bold px-2 py-0.5 rounded">Гадаад худалдаа</span>
                        <p class="text-xs text-slate-500 leading-relaxed font-light">
                            Монгол, Солонгосын аж ахуйн нэгжүүдийг холбох, импорт, экспортын гэрээ хэлцэл байгуулах, зах зээлийн судалгаа хийх болон олон улсын худалдаа хариуцна.
                        </p>
                    </div>
                    <div class="mt-6 pt-4 border-t border-slate-100 text-xs space-y-1">
                        <p class="text-slate-500">📞 <span class="font-semibold text-brand-900">+976 9931-4766</span></p>
                        <p class="text-slate-500">📧 <span class="font-semibold text-brand-900">mkvisa1919@gmail.com</span></p>
                    </div>
                </div>

                <!-- Consultant 2 -->
                <div class="bg-white rounded-2xl overflow-hidden shadow-sm border border-slate-100 hover:shadow-md transition-all duration-150 p-6 flex flex-col justify-between">
                    <div class="space-y-4">
                        <div class="flex items-center space-x-4">
                            <div class="w-16 h-16 rounded-full bg-emerald-50 flex items-center justify-center text-xl font-bold text-emerald-700">ДО</div>
                            <div>
                                <h4 class="font-extrabold text-brand-900">Доржханд</h4>
                                <p class="text-xs text-slate-400 font-semibold uppercase mt-0.5">Ахлах Зөвлөх</p>
                            </div>
                        </div>
                        <span class="inline-block bg-emerald-50 text-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded">Боловсрол & Оюутан</span>
                        <p class="text-xs text-slate-500 leading-relaxed font-light">
                            Гадаад оюутан элсүүлэх, сургуулиудын түншлэлийг хариуцна. Хэлний бэлтгэл (D-4)-ээс үндсэн анги (D-2)-д шилжих, тэтгэлэгт хамрагдах асуудлыг хариуцна.
                        </p>
                    </div>
                    <div class="mt-6 pt-4 border-t border-slate-100 text-xs space-y-1">
                        <p class="text-slate-500">📧 <span class="font-semibold text-brand-900">mkvisa1818@gmail.com</span></p>
                    </div>
                </div>

                <!-- Consultant 3 -->
                <div class="bg-white rounded-2xl overflow-hidden shadow-sm border border-slate-100 hover:shadow-md transition-all duration-150 p-6 flex flex-col justify-between">
                    <div class="space-y-4">
                        <div class="flex items-center space-x-4">
                            <div class="w-16 h-16 rounded-full bg-rose-50 flex items-center justify-center text-xl font-bold text-rose-700">МА</div>
                            <div>
                                <h4 class="font-extrabold text-brand-900">Марал-Эрдэнэ</h4>
                                <p class="text-xs text-slate-400 font-semibold uppercase mt-0.5">Ахлах Зөвлөх</p>
                            </div>
                        </div>
                        <span class="inline-block bg-rose-50 text-rose-800 text-[10px] font-bold px-2 py-0.5 rounded">Эрүүл мэнд аялал жуулчлал</span>
                        <p class="text-xs text-slate-500 leading-relaxed font-light">
                            БНСУ-ын тэргүүлэх их сургуулийн болон нарийн мэргэжлийн эмнэлгүүдтэй түншлэл үүсгэж, эмчилгээ, шинжилгээний цогц үйлчилгээ болон маркетингийг хариуцна.
                        </p>
                    </div>
                    <div class="mt-6 pt-4 border-t border-slate-100 text-xs space-y-1">
                        <p class="text-slate-500">📧 <span class="font-semibold text-brand-900">mkvisa1313@gmail.com</span></p>
                    </div>
                </div>

                <!-- Consultant 4 -->
                <div class="bg-white rounded-2xl overflow-hidden shadow-sm border border-slate-100 hover:shadow-md transition-all duration-150 p-6 flex flex-col justify-between md:col-span-2 lg:col-span-1">
                    <div class="space-y-4">
                        <div class="flex items-center space-x-4">
                            <div class="w-16 h-16 rounded-full bg-amber-50 flex items-center justify-center text-xl font-bold text-amber-700">ЖА</div>
                            <div>
                                <h4 class="font-extrabold text-brand-900">Жамух</h4>
                                <p class="text-xs text-slate-400 font-semibold uppercase mt-0.5">Контент Маркетинг</p>
                            </div>
                        </div>
                        <span class="inline-block bg-amber-50 text-amber-800 text-[10px] font-bold px-2 py-0.5 rounded">Олон нийттэй харилцах</span>
                        <p class="text-xs text-slate-500 leading-relaxed font-light">
                            YouTube, TikTok, Instagram, Facebook зэрэг сошиал платформд зориулсан video контент, төлөвлөлт, брэндинг болон глобал маркетингийг гүйцэтгэнэ.
                        </p>
                    </div>
                    <div class="mt-6 pt-4 border-t border-slate-100 text-xs space-y-1">
                        <p class="text-slate-500">📧 <span class="font-semibold text-brand-900">mkvisa1717@gmail.com</span></p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ✨ AI HUB INTEGRATION SECTION ✨ -->
    <section id="ai-hub" class="py-20 lg:py-24 bg-gradient-to-br from-brand-900 via-brand-800 to-slate-900 text-white relative overflow-hidden">
        <div class="absolute inset-0 bg-grid-pattern opacity-5"></div>
        <div class="absolute top-1/4 right-0 w-80 h-80 rounded-full bg-brand-gold/10 blur-3xl"></div>
        <div class="absolute bottom-1/4 left-0 w-80 h-80 rounded-full bg-brand-crimson/10 blur-3xl"></div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-3xl mx-auto space-y-4 mb-12">
                <span class="inline-flex items-center gap-1.5 py-1 px-3 rounded-full text-xs font-bold bg-brand-gold/20 text-brand-gold border border-brand-gold/30">
                    ✨ Gemini LLM Систем
                </span>
                <h2 class="text-3xl sm:text-5xl font-black tracking-tight">MKVISA Ухаалаг AI Зөвлөх Хаб</h2>
                <p class="text-slate-300 font-light text-sm sm:text-base">
                    БНСУ-ын цагаачлалын хууль тогтоомж болон хөдөлмөрийн харилцааны талаар манай хиймэл оюунаас ухаалаг зөвлөгөө аваарай.
                </p>
            </div>

            <!-- Tabs selector for AI functions -->
            <div class="flex justify-center mb-10">
                <div class="inline-flex p-1 bg-brand-900/60 backdrop-blur rounded-2xl border border-brand-700/60">
                    <button id="btn-ai-chat" onclick="switchAiTab('chat')" class="px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold transition-all duration-150 bg-brand-gold text-brand-900">
                        ✨ Шууд Чатлах
                    </button>
                    <button id="btn-ai-analyzer" onclick="switchAiTab('analyzer')" class="px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold text-slate-300 hover:text-white transition-all duration-150">
                        ✨ Виз & Хөдөлмөр Шинжлүүр
                    </button>
                </div>
            </div>

            <div class="max-w-4xl mx-auto">
                <!-- AI Feature 1: Chat interface -->
                <div id="ai-chat-container" class="bg-brand-900/40 backdrop-blur border border-brand-700/50 rounded-3xl overflow-hidden shadow-2xl flex flex-col h-[550px] animate-fade-in">
                    <!-- Chat Header -->
                    <div class="bg-brand-900/80 p-4 border-b border-brand-800 flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                            <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-brand-gold to-yellow-500 flex items-center justify-center font-black text-brand-900">AI</div>
                            <div>
                                <h4 class="font-bold text-sm text-white">MKVISA Хиймэл оюуны туслах</h4>
                                <span class="text-[10px] text-emerald-400 flex items-center gap-1">
                                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Идэвхтэй зөвлөж байна
                                </span>
                            </div>
                        </div>
                        <button onclick="clearChat()" class="text-xs text-slate-400 hover:text-white transition-colors">Шинэ чат эхлэх 🔄</button>
                    </div>

                    <!-- Chat Message Area -->
                    <div id="ai-chat-messages" class="flex-1 p-6 overflow-y-auto space-y-4 text-xs sm:text-sm">
                        <!-- Bot intro -->
                        <div class="flex items-start space-x-3">
                            <div class="w-8 h-8 rounded-lg bg-brand-gold text-brand-900 flex items-center justify-center font-bold text-xs shrink-0">MK</div>
                            <div class="bg-brand-800/80 border border-brand-700/40 p-4 rounded-2xl rounded-tl-none max-w-[85%] text-slate-100">
                                <p class="font-semibold text-brand-gold mb-1">Сайн байна уу! Намайг MK智能 (MK-AI) гэдэг.</p>
                                <p class="leading-relaxed">Би танд БНСУ-д ажиллаж, амьдрах, суралцахтай холбоотой визний зөвлөгөө, цалин хөлс, тэтгэмж (severance pay)-ийн маргааны талаар мэдээлэл өгч чадна. Асуух зүйлээ доор бичээрэй!</p>
                            </div>
                        </div>
                    </div>

                    <!-- Input bar -->
                    <div class="p-4 bg-brand-900/80 border-t border-brand-800 flex items-center space-x-3">
                        <input id="ai-user-input" type="text" placeholder="Энд асуултаа бичнэ үү (жишээ нь: Severance pay-ийг хэрхэн нэхэмжлэх вэ?)..." 
                               onkeydown="if(event.key === 'Enter') sendAiChatMessage()"
                               class="flex-1 bg-brand-800/60 border border-brand-700/60 rounded-xl px-4 py-3 text-xs sm:text-sm text-white placeholder-slate-400 focus:outline-none focus:border-brand-gold transition-colors">
                        <button onclick="sendAiChatMessage()" class="bg-gradient-to-r from-brand-gold to-amber-500 hover:from-brand-goldHover hover:to-amber-600 text-brand-900 font-extrabold px-5 py-3 rounded-xl text-xs uppercase tracking-wider flex items-center gap-1 transition-all">
                            ✨ Илгээх
                        </button>
                    </div>
                </div>

                <!-- AI Feature 2: Analyzer Interface -->
                <div id="ai-analyzer-container" class="hidden bg-brand-900/40 backdrop-blur border border-brand-700/50 rounded-3xl p-6 sm:p-8 shadow-2xl space-y-6 animate-fade-in">
                    <div class="border-b border-brand-800 pb-4">
                        <h3 class="text-lg sm:text-xl font-bold text-white flex items-center gap-1.5">
                            ⚖️ ✨ Ухаалаг виз & Хөдөлмөрийн хэрэг хуулийн зөвлөгч
                        </h3>
                        <p class="text-xs text-slate-400 mt-1">
                            Та өөрийн нөхцөл байдлыг оруулснаар визний статус болон хөдөлмөрийн эрх зүйн асуудлыг AI ашиглан шинжилнэ.
                        </p>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs font-semibold text-slate-300 mb-1.5">Одоогийн Визний статус (жишээ нь: E-9, D-4, D-2, D-10):</label>
                            <input id="analyzer-current-visa" type="text" placeholder="E-9" class="w-full bg-brand-800 border border-brand-700/60 rounded-xl px-3 py-2 text-xs sm:text-sm text-white focus:outline-none focus:border-brand-gold">
                        </div>
                        <div>
                            <label class="block text-xs font-semibold text-slate-300 mb-1.5">Хүрэхийг зорьж буй виз (жишээ нь: E-7, F-2, F-5, эсвэл Маргаан):</label>
                            <input id="analyzer-target-visa" type="text" placeholder="E-7-4" class="w-full bg-brand-800 border border-brand-700/60 rounded-xl px-3 py-2 text-xs sm:text-sm text-white focus:outline-none focus:border-brand-gold">
                        </div>
                        <div>
                            <label class="block text-xs font-semibold text-slate-300 mb-1.5">БНСУ-д амьдарсан хугацаа (жил, сараар):</label>
                            <input id="analyzer-stay-duration" type="text" placeholder="3 жил 5 сар" class="w-full bg-brand-800 border border-brand-700/60 rounded-xl px-3 py-2 text-xs sm:text-sm text-white focus:outline-none focus:border-brand-gold">
                        </div>
                        <div>
                            <label class="block text-xs font-semibold text-slate-300 mb-1.5">Боловсролын зэрэг / Солонгос хэлний түвшин (TOPIK):</label>
                            <input id="analyzer-education" type="text" placeholder="Бакалавр, TOPIK 3 түвшин" class="w-full bg-brand-800 border border-brand-700/60 rounded-xl px-3 py-2 text-xs sm:text-sm text-white focus:outline-none focus:border-brand-gold">
                        </div>
                    </div>

                    <div>
                        <label class="block text-xs font-semibold text-slate-300 mb-1.5">Бусад тулгарсан асуудал эсвэл дэлгэрэнгүй тодорхойлолт (цалингаа аваагүй, тэтгэмж өгөхгүй байгаа гэх мэт):</label>
                        <textarea id="analyzer-details" rows="3" placeholder="Сүүлийн компанидаа 2 жил ажиллаад гарсан боловч ажил олгогч тэтгэмж (severance pay) болон сүүлийн сарын цалинг өгөхгүй саатуулж байна..." 
                                  class="w-full bg-brand-800 border border-brand-700/60 rounded-xl p-3 text-xs sm:text-sm text-white focus:outline-none focus:border-brand-gold"></textarea>
                    </div>

                    <div class="flex justify-center pt-2">
                        <button onclick="runAiAnalysis()" class="bg-gradient-to-r from-brand-gold to-amber-500 hover:from-brand-goldHover hover:to-amber-600 text-brand-900 font-extrabold px-8 py-3.5 rounded-xl text-xs sm:text-sm uppercase tracking-wider flex items-center gap-1.5 transition-all transform hover:scale-[1.01]">
                            ✨ Анализ хийх & Төлөвлөгөө гаргах
                        </button>
                    </div>

                    <!-- Analyzer Result display -->
                    <div id="ai-analyzer-result-card" class="hidden bg-brand-950/80 border border-brand-700 rounded-2xl p-6 space-y-4">
                        <div class="flex justify-between items-center border-b border-brand-800 pb-3">
                            <h4 class="font-bold text-sm text-brand-gold flex items-center gap-1">📋 ✨ AI Шинжилгээний үр дүн</h4>
                            <button onclick="copyAnalyzerResult()" class="text-xs bg-brand-800 hover:bg-brand-700 px-3 py-1 rounded border border-brand-700 transition-colors">Хуулж авах</button>
                        </div>
                        <!-- Markdown text content parsed elegantly inside UI -->
                        <div id="ai-analyzer-output-text" class="text-xs sm:text-sm leading-relaxed text-slate-100 space-y-2 whitespace-pre-line font-light">
                        </div>
                    </div>
                </div>

                <!-- Central Alert system (Replaces browser alert) -->
                <div id="ai-hub-alert" class="hidden mt-4 bg-rose-900/60 border border-rose-500/50 text-rose-200 p-4 rounded-xl text-xs font-semibold animate-pulse text-center">
                    Алдаа гарлаа. Та дахин оролдоно уу.
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose MKVISA -->
    <section id="why-us" class="py-20 lg:py-24 bg-slate-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto space-y-4 mb-16">
                <span class="text-xs font-extrabold uppercase tracking-widest text-brand-crimson">Өрсөлдөх давуу тал</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-brand-900">Яагаад MKVISA-ийг сонгох хэрэгтэй вэ?</h2>
                <p class="text-slate-500 font-light">Сүүлийн жилүүдэд бид олон зуун иргэдийн итгэлийг хүлээж, баталгаат үр дүн гаргасаар байна</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Advantage 1 -->
                <div class="bg-white rounded-2xl p-8 border border-slate-100 shadow-sm space-y-4 hover:shadow-md transition-shadow duration-150">
                    <span class="text-3xl">🧩</span>
                    <h3 class="font-extrabold text-brand-900 text-lg">Мэргэшсэн Удирдлага</h3>
                    <p class="text-xs sm:text-sm text-slate-500 leading-relaxed font-light">
                        Ерөнхий захирлын шууд удирдлага дор Худалдаа, Боловсрол, Эрүүл мэнд, Контент маркетинг гэсэн 4 үндсэн чиглэлээр салбарлаж, нягт уялдаатай ажилладаг өндөр бүтээмжтэй бүтэц.
                    </p>
                </div>
                <!-- Advantage 2 -->
                <div class="bg-white rounded-2xl p-8 border border-slate-100 shadow-sm space-y-4 hover:shadow-md transition-shadow duration-150">
                    <span class="text-3xl">🌟</span>
                    <h3 class="font-extrabold text-brand-900 text-lg">Баталгаат Үр Дүн</h3>
                    <p class="text-xs sm:text-sm text-slate-500 leading-relaxed font-light">
                        Сүүлийн жилүүдэд Монголчуудын хөдөлмөр эрхлэлт болон визний маш олон ээдрээтэй асуудлуудыг хуулийн хүрээнд амжилттай шийдвэрлэж, үйлчлүүлэгчдийн өндөр итгэлийг хүлээсэн туршлага.
                    </p>
                </div>
                <!-- Advantage 3 -->
                <div class="bg-white rounded-2xl p-8 border border-slate-100 shadow-sm space-y-4 hover:shadow-md transition-shadow duration-150">
                    <span class="text-3xl">🚀</span>
                    <h3 class="font-extrabold text-brand-900 text-lg">Хосолсон Маркетинг</h3>
                    <p class="text-xs sm:text-sm text-slate-500 leading-relaxed font-light">
                        Мэргэжлийн видео контент бүтээгчдийн багтай тул хамтран ажиллагч их дээд сургууль, эмнэлэг, брэндүүдийн зах зээлд эзлэх байр суурь, борлуулалтын үр дүнг бодитоор нэмэгдүүлдэг.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Vision Section -->
    <section class="py-24 relative overflow-hidden text-white gradient-bg">
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent"></div>
        <div class="relative max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-8">
            <span class="text-xs font-bold tracking-widest text-brand-gold uppercase">Алсын хараа</span>
            <blockquote class="text-2xl sm:text-4xl font-extrabold italic tracking-tight leading-normal">
                "БНСУ-д оршин сууж буй гадаад иргэдийн хамгийн сайн хөтөч, Глобал бизнесийн Тэргүүлэгч (First Mover)"
            </blockquote>
            <p class="text-slate-300 font-light max-w-3xl mx-auto text-sm sm:text-base leading-relaxed">
                MKVISA нь гадаад иргэдэд тулгардаг хууль эрх зүй, эрүүл мэндийн саад тотгорыг арилган, боловсрол, худалдаа, орчин үеийн дижитал контентоор дамжуулан хоёр орны хооронд эдийн засаг, соёлын шинэ үнэ цэнийг бүтээгч найдвартай түнш байх болно.
            </p>
            <div class="w-16 h-1 bg-brand-gold mx-auto rounded-full"></div>
        </div>
    </section>

    <!-- Contact & Footer Hub -->
    <footer id="contact" class="bg-brand-900 text-slate-300 pt-20 pb-12 border-t border-brand-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 pb-16 border-b border-brand-800">
                
                <!-- Brand Profile -->
                <div class="lg:col-span-4 space-y-6">
                    <div class="flex items-center space-x-3 text-white">
                        <div class="w-10 h-10 rounded-lg bg-brand-gold flex items-center justify-center font-bold text-lg text-brand-900">MK</div>
                        <span class="text-lg font-bold tracking-tight">MKVISA</span>
                    </div>
                    <p class="text-xs text-slate-400 font-light leading-relaxed">
                        БНСУ-ын Сөүл хотод төвтэй, гадаад иргэдийн эрх ашгийг хамгаалах болон олон улсын зуучлал, бизнесийн цогц консалтинг групп юм.
                    </p>
                    <div class="text-xs space-y-1.5 text-slate-400">
                        <p>📍 Сөүл хот, Гангбук-гү, СҮЮҮ (Suyu) метроны буудал (4-р шугам), 3-р гарцын ойролцоо</p>
                        <p>📞 Утас: 010-7651-1616</p>
                        <p>📧 Имэйл: mkvisa1616@gmail.com</p>
                    </div>
                </div>

                <!-- Individual Hub Contacts -->
                <div class="lg:col-span-8 grid grid-cols-1 sm:grid-cols-2 gap-6">
                    <!-- Unit 1 -->
                    <div class="bg-brand-800/40 p-5 rounded-2xl border border-brand-700/40 space-y-2">
                        <h4 class="text-sm font-bold text-white tracking-wide uppercase">Худалдаа, бизнесийн хамтын ажиллагаа</h4>
                        <p class="text-xs text-brand-gold">Холбогдох хүн: Эрдэнэчимэг</p>
                        <p class="text-xs text-slate-400">📞 +976 9931-4766 (Монгол руу шууд залгах)</p>
                        <p class="text-xs text-slate-400">📧 mkvisa1919@gmail.com</p>
                    </div>
                    <!-- Unit 2 -->
                    <div class="bg-brand-800/40 p-5 rounded-2xl border border-brand-700/40 space-y-2">
                        <h4 class="text-sm font-bold text-white tracking-wide uppercase">Боловсрол, гадаад оюутан зуучлал</h4>
                        <p class="text-xs text-brand-gold">Холбогдох хүн: Доржханд</p>
                        <p class="text-xs text-slate-400">📧 mkvisa1818@gmail.com</p>
                    </div>
                    <!-- Unit 3 -->
                    <div class="bg-brand-800/40 p-5 rounded-2xl border border-brand-700/40 space-y-2">
                        <h4 class="text-sm font-bold text-white tracking-wide uppercase">Эрүүл мэнд, эмнэлгийн зуучлал</h4>
                        <p class="text-xs text-brand-gold">Холбогдох хүн: Марал-Эрдэнэ</p>
                        <p class="text-xs text-slate-400">📧 mkvisa1313@gmail.com</p>
                    </div>
                    <!-- Unit 4 -->
                    <div class="bg-brand-800/40 p-5 rounded-2xl border border-brand-700/40 space-y-2">
                        <h4 class="text-sm font-bold text-white tracking-wide uppercase">Маркетинг, контентын хамтын ажиллагаа</h4>
                        <p class="text-xs text-brand-gold">Холбогдох хүн: Жамух</p>
                        <p class="text-xs text-slate-400">📧 mkvisa1717@gmail.com</p>
                    </div>
                </div>

            </div>

            <div class="pt-8 flex flex-col sm:flex-row justify-between items-center gap-4 text-xs text-slate-500 text-center sm:text-left">
                <p>© 2026 MKVISA Co., Ltd. Бүх эрх хуулиар хамгаалагдсан.</p>
                <div class="flex space-x-4">
                    <a href="#" class="hover:underline">Үйлчилгээний нөхцөл</a>
                    <span>•</span>
                    <a href="#" class="hover:underline">Нууцлалын бодлого</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- JS Logic for Tabs and Interactive Consultant Feature -->
    <script>
        // Logica de navigare intre taburile de servicii clasice
        function switchTab(tabId) {
            const contents = document.querySelectorAll('.tab-content');
            contents.forEach(el => el.classList.add('hidden'));

            const activeContent = document.getElementById(tabId);
            if (activeContent) {
                activeContent.classList.remove('hidden');
            }

            const buttons = document.querySelectorAll('.tab-btn');
            buttons.forEach(btn => {
                btn.classList.remove('border-brand-gold', 'text-brand-900');
                btn.classList.add('border-transparent', 'text-slate-400');
            });

            const activeBtn = document.getElementById('btn-' + tabId);
            if (activeBtn) {
                activeBtn.classList.remove('border-transparent', 'text-slate-400');
                activeBtn.classList.add('border-brand-gold', 'text-brand-900');
            }

            const select = document.getElementById('TabSelect');
            if (select) {
                select.value = tabId;
            }
        }

        // Baza de date statica pentru selectia consultantului rapid
        const advisorDb = {
            labor_visa: {
                name: "М. Уртнасан",
                role: "CEO / Ерөнхий захирал",
                avatar: "МУ",
                desc: "Визний чиглэлийн шилжилт, сунгалт (D, E, F ангилал), хөдөлмөрийн маргаан, цалин хөлс болон тэтгэмж нэхэмжлэх асуудлаар шууд чиглүүлэлт хийнэ.",
                email: "mkvisa1616@gmail.com"
            },
            student_recruitment: {
                name: "Доржханд",
                role: "Боловсрол, оюутан солилцооны ахлах зөвлөх",
                avatar: "ДО",
                desc: "БНСУ-ын их сургуулиудын хэлний бэлтгэл (D-4), үндсэн анги (D-2) элсэлт болон тэтгэлэгт хамруулах бүх шатны үйл ажиллагааг удирдан зохион байгуулна.",
                email: "mkvisa1818@gmail.com"
            },
            medical_tourism: {
                name: "Марал-Эрдэнэ",
                role: "Эрүүл мэнд аялал жуулчлалын албаны ахлах зөвлөх",
                avatar: "МА",
                desc: "Тэргүүлэх нарийн мэргэжлийн болон гоо сайхны эмнэлгүүдийн хамтын ажиллагаа, уулзалт захиалга болон нэг цэгийн эмчилгээний орчуулгыг зохион байгуулна.",
                email: "mkvisa1313@gmail.com"
            },
            global_trade: {
                name: "Эрдэнэчимэг",
                role: "Гадаад худалдааны ахлах зөвлөх",
                avatar: "ЭР",
                desc: "Монгол-Солонгосын аж ахуйн нэгжийн хамтын ажиллагаа, импорт, экспортын албан ёсны гэрээ, зах зээлийн судалгаа болон олон улсын тээвэр түгээлт хариуцна.",
                email: "mkvisa1919@gmail.com"
            },
            marketing_pr: {
                name: "Жамух",
                role: "Олон нийттэй харилцах, дижитал маркетингийн зөвлөх",
                avatar: "ЖА",
                desc: "Медиа брэндинг, ухаалаг сурталчилгаа, богино болон урт хэмжээний сошиал видео контент төлөвлөлт болон маркетинг хариуцна.",
                email: "mkvisa1717@gmail.com"
            }
        };

        // Generator pentru interactiunea clasica de selectie
        function generateContactPlan(value) {
            const card = document.getElementById('dynamicConsultCard');
            const successNotice = document.getElementById('copySuccessNotice');
            
            successNotice.classList.add('hidden');

            if (!value || !advisorDb[value]) {
                card.classList.add('hidden');
                return;
            }

            const advisor = advisorDb[value];
            
            document.getElementById('advisorAvatar').innerText = advisor.avatar;
            document.getElementById('advisorName').innerText = advisor.name;
            document.getElementById('advisorRole').innerText = advisor.role;
            document.getElementById('advisorDesc').innerText = advisor.desc;
            document.getElementById('advisorContactEmail').innerText = advisor.email;

            card.classList.remove('hidden');
        }

        // Copiere securizata a adreselor de email
        function copyToClipboardEmail() {
            const emailElement = document.getElementById('advisorContactEmail');
            if (!emailElement) return;

            const emailText = emailElement.innerText;
            const tempTextArea = document.createElement('textarea');
            tempTextArea.value = emailText;
            document.body.appendChild(tempTextArea);
            tempTextArea.select();
            
            try {
                const successful = document.execCommand('copy');
                if (successful) {
                    const successNotice = document.getElementById('copySuccessNotice');
                    successNotice.classList.remove('hidden');
                    setTimeout(() => {
                        successNotice.classList.add('hidden');
                    }, 3500);
                }
            } catch (err) {
                console.error('Eroare la copiere: ', err);
            }
            document.body.removeChild(tempTextArea);
        }

        /* =========================================================
           LOGICA DE INTEGRARE PENTRU HUB-UL DE INTELIGENTA ARTIFICIALA (GEMINI API)
           =========================================================
        */

        // Comutarea taburilor in modulul AI Hub
        function switchAiTab(tab) {
            const chatContainer = document.getElementById('ai-chat-container');
            const analyzerContainer = document.getElementById('ai-analyzer-container');
            const btnChat = document.getElementById('btn-ai-chat');
            const btnAnalyzer = document.getElementById('btn-ai-analyzer');

            if (tab === 'chat') {
                chatContainer.classList.remove('hidden');
                analyzerContainer.classList.add('hidden');
                
                btnChat.className = "px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold transition-all duration-150 bg-brand-gold text-brand-900";
                btnAnalyzer.className = "px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold text-slate-300 hover:text-white transition-all duration-150";
            } else {
                chatContainer.classList.add('hidden');
                analyzerContainer.classList.remove('hidden');

                btnChat.className = "px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold text-slate-300 hover:text-white transition-all duration-150";
                btnAnalyzer.className = "px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold transition-all duration-150 bg-brand-gold text-brand-900";
            }
        }

        // Functia de apel a API-ului Gemini cu reincercare si backoff exponential
        async function callGemini(userQuery, systemPrompt) {
            const apiKey = ""; // Lasat gol conform specificatiilor pentru mediu securizat runtime
            const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key=${apiKey}`;
            
            const payload = {
                contents: [{ parts: [{ text: userQuery }] }],
                systemInstruction: { parts: [{ text: systemPrompt }] }
            };

            let delay = 1000;
            // Incercam de maxim 5 ori cu intarzieri de: 1s, 2s, 4s, 8s, 16s
            for (let i = 0; i < 5; i++) {
                try {
                    const response = await fetch(url, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });
                    
                    if (response.ok) {
                        const data = await response.json();
                        const resultText = data.candidates?.[0]?.content?.parts?.[0]?.text;
                        if (resultText) {
                            return resultText;
                        }
                    }
                } catch (e) {
                    // Nu inregistram in consola esecurile temporare pentru a evita flood-ul
                }
                
                await new Promise(resolve => setTimeout(resolve, delay));
                delay *= 2;
            }
            throw new Error("Холболт амжилтгүй боллоо. Та дахин оролдоно уу.");
        }

        // Prompt de sistem pentru Asistentul de chat MKVISA
        const chatSystemPrompt = `
Sunteți "MK智能" (MK-AI), asistentul oficial inteligent de consultanță al MKVISA (fondat în 2022). 
Director executiv (CEO): М.Уртнасан.
Compania oferă suport pentru vize și drepturile muncii în Coreea de Sud (BНСУ).
Adresați-vă în limba mongolă (Mongolian), cu excepția cazului în care utilizatorul utilizează o altă limbă precum engleza sau româna. 
Fiți extrem de profesionist, politicos și cald. 
Cunoștințele dvs. cheie:
1. Виз сунгалт, өөрчлөлт (D-4, D-2 -оос D-10 ажил хайх, E-7 мэргэжилтний виз, F-2 оршин суух, F-6 гэрлэлт, F-5 байнгын оршин суух).
2. Хөдөлмөрийн маргаан (Цалингийн маргаан, тэтгэмж нэхэмжлэх/severance pay). Orice angajat care a lucrat peste 1 an (chiar și fără viză validă) are dreptul legal la severance pay (тэтгэмж) conform legilor coreene.
3. Оюутан зуучлал (D-4 хэлний бэлтгэл, D-2 үндсэн анги). Тэтгэлэг 70-100%, насны хязгааргүй! Гэр бүл урих (F-3 виз).
4. Гадаад худалдаа (Солонгос гоо сайхан, хувцас, хүнс импорт, экспорт).
Dacă utilizatorul dorește consultanță oficială directă, oferiți-le contactele:
- Төв утас: 010-7651-1616
- Имэйл: mkvisa1616@gmail.com
- Хаяг: Сөүл хот, Сүюү (Suyu) метроны буудал, 3-р гарц.
Fiti concis și structurați răspunsurile cu marcatori.
`;

        // Generarea si trimiterea unui mesaj in Chat-ul AI
        async function sendAiChatMessage() {
            const inputElement = document.getElementById('ai-user-input');
            const messagesContainer = document.getElementById('ai-chat-messages');
            const alertElement = document.getElementById('ai-hub-alert');
            
            const userText = inputElement.value.trim();
            if (!userText) return;

            alertElement.classList.add('hidden'); // Ascundem alertele anterioare

            // Adaugam mesajul utilizatorului in interfata
            const userMsgDiv = document.createElement('div');
            userMsgDiv.className = "flex items-start space-x-3 justify-end";
            userMsgDiv.innerHTML = `
                <div class="bg-brand-gold text-brand-900 font-semibold p-4 rounded-2xl rounded-tr-none max-w-[85%]">
                    <p class="leading-relaxed">${userText}</p>
                </div>
                <div class="w-8 h-8 rounded-lg bg-brand-gold text-brand-900 flex items-center justify-center font-bold text-xs shrink-0">Та</div>
            `;
            messagesContainer.appendChild(userMsgDiv);
            
            // Golim campul de input si scrollam jos
            inputElement.value = "";
            messagesContainer.scrollTop = messagesContainer.scrollHeight;

            // Adaugam indicatorul de incarcare/typing al botului
            const typingDiv = document.createElement('div');
            typingDiv.id = "ai-typing-indicator";
            typingDiv.className = "flex items-start space-x-3";
            typingDiv.innerHTML = `
                <div class="w-8 h-8 rounded-lg bg-brand-gold text-brand-900 flex items-center justify-center font-bold text-xs shrink-0">MK</div>
                <div class="bg-brand-800/50 border border-brand-700/40 p-4 rounded-2xl rounded-tl-none max-w-[85%] text-slate-400">
                    <span class="animate-pulse">✨ AI бодож байна...</span>
                </div>
            `;
            messagesContainer.appendChild(typingDiv);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;

            try {
                // Generam istoricul simplificat de chat bazat pe ultimele mesaje din UI
                const botResponse = await callGemini(userText, chatSystemPrompt);
                
                // Eliminam indicatorul de incarcare
                const typingIndicator = document.getElementById('ai-typing-indicator');
                if (typingIndicator) typingIndicator.remove();

                // Adaugam raspunsul oficial al botului
                const botMsgDiv = document.createElement('div');
                botMsgDiv.className = "flex items-start space-x-3";
                botMsgDiv.innerHTML = `
                    <div class="w-8 h-8 rounded-lg bg-brand-gold text-brand-900 flex items-center justify-center font-bold text-xs shrink-0">MK</div>
                    <div class="bg-brand-800/80 border border-brand-700/40 p-4 rounded-2xl rounded-tl-none max-w-[85%] text-slate-100">
                        <p class="font-semibold text-brand-gold mb-1">MK智能 Зөвлөх:</p>
                        <div class="leading-relaxed whitespace-pre-line">${botResponse}</div>
                    </div>
                `;
                messagesContainer.appendChild(botMsgDiv);
            } catch (err) {
                // Gestionare erori fara dialoguri natiove blocate (alert)
                const typingIndicator = document.getElementById('ai-typing-indicator');
                if (typingIndicator) typingIndicator.remove();
                
                alertElement.innerText = "Уучлаарай, холболтын алдаа гарлаа. Та дахин оролдоно уу.";
                alertElement.classList.remove('hidden');
            }

            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }

        // Reseteaza fereastra de chat
        function clearChat() {
            const messagesContainer = document.getElementById('ai-chat-messages');
            messagesContainer.innerHTML = `
                <div class="flex items-start space-x-3">
                    <div class="w-8 h-8 rounded-lg bg-brand-gold text-brand-900 flex items-center justify-center font-bold text-xs shrink-0">MK</div>
                    <div class="bg-brand-800/80 border border-brand-700/40 p-4 rounded-2xl rounded-tl-none max-w-[85%] text-slate-100">
                        <p class="font-semibold text-brand-gold mb-1">Сайн байна уу! Намайг MK智能 (MK-AI) гэдэг.</p>
                        <p class="leading-relaxed">Би танд БНСУ-д ажиллаж, амьдрах, суралцахтай холбоотой визний зөвлөгөө, цалин хөлс, тэтгэмж (severance pay)-ийн маргааны талаар мэдээлэл өгч чадна. Асуух зүйлээ доор бичээрэй!</p>
                    </div>
                </div>
            `;
            document.getElementById('ai-hub-alert').classList.add('hidden');
        }

        // Prompt de sistem pentru modulul de analiza strategica de vize/munca
        const analyzerSystemPrompt = `
Sunteți expertul juridic de vize și dreptul muncii din Coreea de Sud al MKVISA.
Sarcina dvs. este să analizați detaliile furnizate de utilizator și să generați un raport de consultanță structurat în limba mongolă:
1. ✨ НОХЦӨЛ БАЙДЛЫН ҮНЭЛГЭЭ (Evaluarea situației actuale).
2. ✨ БОЛОМЖИТ ШИЙДЭЛ & СТРАТЕГИ (Soluții posibile și strategie de tranziție recomandată).
3. ✨ БҮРДҮҮЛЭХ БИЧИГ БАРИМТЫН ХЯНАЛТЫН ХУУДАС (Listă detaliată de verificare a documentelor necesare).
4. ✨ MKVISA-Д ИЛГЭЭХ ХҮСЭЛТИЙН ТӨСӨЛ (O schiță de mesaj/e-mail scrisă profesional în mongolă și coreeană pe care clientul o poate trimite către MKVISA).

Informații de context:
- Viza E-9 la E-7-4 necesită îndeplinirea unui punctaj (experiență, vărstă, TOPIK, economii, diplomă).
- Toți lucrătorii care lucrează minim 1 an au dreptul la severance pay (тэтгэмж). Chiar dacă sunt neînregistrați (хар иргэн).
- Viza D-10 este pentru căutarea unui loc de muncă după finalizarea studiilor (D-2).
Fiți extrem de precis, realist și încurajați clientul să își rezerve o consultanță telefonică la 010-7651-1616.
`;

        // Executarea analizei strategice cu datele introduse
        async function runAiAnalysis() {
            const currentVisa = document.getElementById('analyzer-current-visa').value.trim() || 'Тодорхойгүй';
            const targetVisa = document.getElementById('analyzer-target-visa').value.trim() || 'Тодорхойгүй';
            const stayDuration = document.getElementById('analyzer-stay-duration').value.trim() || 'Тодорхойгүй';
            const education = document.getElementById('analyzer-education').value.trim() || 'Тодорхойгүй';
            const details = document.getElementById('analyzer-details').value.trim() || 'Тодорхойгүй';

            const alertElement = document.getElementById('ai-hub-alert');
            const resultCard = document.getElementById('ai-analyzer-result-card');
            const outputText = document.getElementById('ai-analyzer-output-text');

            alertElement.classList.add('hidden');
            resultCard.classList.add('hidden');

            // Formularea query-ului complet
            const userQuery = `
Хэрэглэгчийн мэдээлэл:
- Одоогийн визний статус: ${currentVisa}
- Хүрэх зорилтот виз / асуудал: ${targetVisa}
- БНСУ-д байсан хугацаа: ${stayDuration}
- Боловсрол, хэлний түвшин: ${education}
- Тулгарсан нэмэлт асуудлын дэлгэрэнгүй: ${details}

Дээрх өгөгдөлд дүн шинжилгээ хийж, мэргэжлийн түвшинд зөвлөмж төлөвлөгөөг боловсруулна уу.
`;

            // Afisam o stare temporara de incarcare
            outputText.innerHTML = `<div class="flex items-center justify-center py-8 space-x-2 text-slate-400">
                <span class="animate-spin text-xl">⏳</span>
                <span>Таны мэдээлэлд дүн шинжилгээ хийж, стратегийн төлөвлөгөө боловсруулж байна... Түр хүлээнэ үү!</span>
            </div>`;
            resultCard.classList.remove('hidden');

            // Scrollam pana la rezultate
            resultCard.scrollIntoView({ behavior: 'smooth' });

            try {
                const analysisResult = await callGemini(userQuery, analyzerSystemPrompt);
                outputText.innerText = analysisResult;
            } catch (err) {
                resultCard.classList.add('hidden');
                alertElement.innerText = "Шинжилгээ хийхэд алдаа гарлаа. Та мэдээллээ шалгаад дахин оролдоно уу.";
                alertElement.classList.remove('hidden');
            }
        }

        // Copierea in clipboard a strategiei generate
        function copyAnalyzerResult() {
            const outputText = document.getElementById('ai-analyzer-output-text').innerText;
            if (!outputText) return;

            const tempTextArea = document.createElement('textarea');
            tempTextArea.value = outputText;
            document.body.appendChild(tempTextArea);
            tempTextArea.select();
            
            try {
                const successful = document.execCommand('copy');
                if (successful) {
                    const alertElement = document.getElementById('ai-hub-alert');
                    alertElement.innerText = "Шинжилгээний тайланг амжилттай хууллаа!";
                    alertElement.className = "mt-4 bg-green-900/60 border border-green-500/50 text-green-200 p-4 rounded-xl text-xs font-semibold animate-pulse text-center";
                    alertElement.classList.remove('hidden');
                    setTimeout(() => {
                        alertElement.classList.add('hidden');
                        // Resetam clasa originala de alerta rosie
                        alertElement.className = "hidden mt-4 bg-rose-900/60 border border-rose-500/50 text-rose-200 p-4 rounded-xl text-xs font-semibold animate-pulse text-center";
                    }, 3500);
                }
            } catch (err) {
                console.error('Copiere nereusita: ', err);
            }
            document.body.removeChild(tempTextArea);
        }
    </script>
</body>
</html>
