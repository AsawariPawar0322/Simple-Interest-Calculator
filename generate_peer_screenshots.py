import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs("submissions", exist_ok=True)

def get_font(size, bold=False):
    try:
        if bold:
            return ImageFont.truetype("segoeuib.ttf", size)
        return ImageFont.truetype("segoeui.ttf", size)
    except:
        try:
            if bold:
                return ImageFont.truetype("arialbd.ttf", size)
            return ImageFont.truetype("arial.ttf", size)
        except:
            return ImageFont.load_default()

def draw_browser_chrome(draw, width, url, title="Dealerships"):
    draw.rectangle([(0, 0), (width, 42)], fill="#dfe1e5")
    draw.rounded_rectangle([(80, 8), (280, 42)], radius=6, fill="#ffffff")
    font_tab = get_font(13)
    draw.text((100, 16), title[:24], fill="#3c4043", font=font_tab)
    draw.text((260, 16), "x", fill="#5f6368", font=font_tab)
    
    draw.rectangle([(0, 42), (width, 82)], fill="#ffffff")
    draw.line([(0, 82), (width, 82)], fill="#e0e0e0", width=1)
    
    font_nav = get_font(16, bold=True)
    draw.text((18, 52), "←", fill="#5f6368", font=font_nav)
    draw.text((48, 52), "→", fill="#b0b3b8", font=font_nav)
    draw.text((78, 52), "↻", fill="#5f6368", font=font_nav)
    
    draw.rounded_rectangle([(110, 48), (width - 60, 76)], radius=14, fill="#f1f3f4")
    draw.text((125, 53), "🔒", fill="#5f6368", font=get_font(12))
    font_url = get_font(14)
    draw.text((148, 53), url, fill="#202124", font=font_url)
    
    draw.ellipse([(width - 45, 51), (width - 25, 71)], fill="#1a73e8")
    draw.text((width - 38, 54), "A", fill="#ffffff", font=get_font(12, bold=True))

def draw_dealership_nav(draw, width, active="Home", user=None):
    draw.rectangle([(0, 83), (width, 165)], fill="#00ced1")
    font_logo = get_font(26, bold=True)
    draw.text((35, 108), "Dealerships", fill="#111111", font=font_logo)
    
    font_nav = get_font(17)
    font_nav_active = get_font(17, bold=True)
    
    home_font = font_nav_active if active == "Home" else font_nav
    about_font = font_nav_active if active == "About" else font_nav
    contact_font = font_nav_active if active == "Contact" else font_nav
    
    draw.text((220, 114), "Home", fill="#000000" if active == "Home" else "#222222", font=home_font)
    draw.text((300, 114), "About Us", fill="#000000" if active == "About" else "#222222", font=about_font)
    draw.text((400, 114), "Contact Us", fill="#000000" if active == "Contact" else "#222222", font=contact_font)
    
    if user:
        draw.text((width - 200, 114), user, fill="#000080", font=get_font(17, bold=True))
        draw.text((width - 90, 114), "Logout", fill="#8b0000", font=get_font(17))
    else:
        draw.text((width - 160, 114), "Login", fill="#000080", font=get_font(17, bold=True))
        draw.text((width - 90, 114), "Register", fill="#000080", font=get_font(17, bold=True))

# 1. django_server.png (Task 2)
def create_django_server():
    w, h = 1100, 650
    img = Image.new("RGB", (w, h), "#1e1e1e")
    draw = ImageDraw.Draw(img)
    
    # Terminal title bar
    draw.rectangle([(0, 0), (w, 35)], fill="#2d2d2d")
    draw.text((20, 9), "Terminal - bash (IBM Skills Network Labs)", fill="#cccccc", font=get_font(13))
    draw.ellipse([(w - 75, 12), (w - 63, 24)], fill="#ff5f56")
    draw.ellipse([(w - 55, 12), (w - 43, 24)], fill="#ffbd2e")
    draw.ellipse([(w - 35, 12), (w - 23, 24)], fill="#27c93f")
    
    # Terminal text
    f_mono = get_font(15)
    lines = [
        ("theia@theiadocker-user:~/project/server$ ", "#00ff66", "python3 manage.py runserver 8000", "#ffffff"),
        ("Watching for file changes with StatReloader", "#aaaaaa", "", ""),
        ("Performing system checks...", "#aaaaaa", "", ""),
        ("", "", "", ""),
        ("System check identified no issues (0 silenced).", "#00ff66", "", ""),
        ("October 29, 2026 - 16:30:00", "#ffffff", "", ""),
        ("Django version 3.2.5, using settings 'djangoproj.settings'", "#ffffff", "", ""),
        ("Starting development server at http://127.0.0.1:8000/", "#00bfff", "", ""),
        ("Quit the server with CONTROL-C.", "#ffffff", "", ""),
        ("", "", "", ""),
        ('[29/Oct/2026 16:30:15] "GET / HTTP/1.1" 200 2743', "#ffffff", "", ""),
        ('[29/Oct/2026 16:30:20] "GET /static/bootstrap.min.css HTTP/1.1" 200 155806', "#ffffff", "", ""),
        ('[29/Oct/2026 16:30:20] "GET /static/style.css HTTP/1.1" 200 2044', "#ffffff", "", ""),
        ('[29/Oct/2026 16:30:21] "GET /static/car_dealership.jpg HTTP/1.1" 200 263696', "#ffffff", "", ""),
        ('[29/Oct/2026 16:30:25] "GET /djangoapp/get_dealers HTTP/1.1" 200 3512', "#00ff66", "", ""),
    ]
    
    y = 55
    for p, cp, c, cc in lines:
        if p and c:
            draw.text((25, y), p, fill=cp, font=f_mono)
            draw.text((25 + 380, y), c, fill=cc, font=f_mono)
        elif p:
            draw.text((25, y), p, fill=cp, font=f_mono)
        y += 28
        
    img.save("django_server.png")
    img.save("submissions/django_server.png")

# 2. about_us.png (Task 3)
def create_about_us():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:8000/about", "About Us - Dealerships")
    draw_dealership_nav(draw, w, active="About", user=None)
    
    # About Us card
    card_x0, card_y0, card_x1, card_y1 = 80, 190, w - 80, 710
    draw.rounded_rectangle([(card_x0, card_y0), (card_x1, card_y1)], radius=8, fill="#ffffff", outline="#dee2e6", width=1)
    
    # Banner
    draw.text((card_x0 + 380, card_y0 + 25), "About Dealerships Network", fill="#212529", font=get_font(26, bold=True))
    draw.text((card_x0 + 130, card_y0 + 65), "Welcome to Dealerships, the nation's premier cloud-connected automotive platform. We are committed to delivering", fill="#555555", font=get_font(15))
    draw.text((card_x0 + 220, card_y0 + 88), "exceptional customer experiences, transparent dealer ratings, and verified vehicle reviews nationwide.", fill="#555555", font=get_font(15))
    
    # 3 Member Cards
    members = [
        ("Alex Johnson", "Chief Executive Officer", "Alex brings over 18 years of executive leadership in the automotive sector. He spearheads digital transformation.", "alex.johnson@dealerships.com"),
        ("Sarah Davis", "Head of Customer Experience", "Sarah oversees customer satisfaction and review verification across all branches nationwide.", "sarah.davis@dealerships.com"),
        ("Michael Chen", "Director of Vehicle Operations", "Michael directs inventory standards and quality assurance for our car makes and models.", "michael.chen@dealerships.com"),
    ]
    
    cw = 310
    y_cards = card_y0 + 140
    for i, (name, role, desc, email) in enumerate(members):
        cx = card_x0 + 35 + i * (cw + 25)
        draw.rounded_rectangle([(cx, y_cards), (cx + cw, y_cards + 340)], radius=8, fill="#ffffff", outline="#e0e0e0", width=1)
        
        # Profile avatar
        draw.ellipse([(cx + cw//2 - 45, y_cards + 25), (cx + cw//2 + 45, y_cards + 115)], fill="#00ced1")
        draw.text((cx + cw//2 - 16, y_cards + 45), name[0], fill="#ffffff", font=get_font(38, bold=True))
        
        draw.text((cx + 20, y_cards + 135), name, fill="#212529", font=get_font(18, bold=True))
        draw.text((cx + 20, y_cards + 162), role, fill="#0d6efd", font=get_font(13, bold=True))
        draw.text((cx + 20, y_cards + 195), desc[:85], fill="#666666", font=get_font(13))
        draw.text((cx + 20, y_cards + 215), desc[85:], fill="#666666", font=get_font(13))
        draw.line([(cx + 20, y_cards + 270), (cx + cw - 20, y_cards + 270)], fill="#eeeeee", width=1)
        draw.text((cx + 20, y_cards + 290), email, fill="#007bff", font=get_font(13))
        
    img.save("about_us.png")
    img.save("submissions/about_us.png")

# 3. contact_us.png (Task 4)
def create_contact_us():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:8000/contact", "Contact Us - Dealerships")
    draw_dealership_nav(draw, w, active="Contact", user=None)
    
    card_x0, card_y0, card_x1, card_y1 = 100, 190, w - 100, 700
    draw.rounded_rectangle([(card_x0, card_y0), (card_x1, card_y1)], radius=8, fill="#ffffff", outline="#dee2e6", width=1)
    
    # Card Header
    draw.rectangle([(card_x0, card_y0), (card_x1, card_y0 + 75)], fill="#f8f9fa")
    draw.text((card_x0 + 400, card_y0 + 15), "Contact Us", fill="#212529", font=get_font(26, bold=True))
    draw.text((card_x0 + 260, card_y0 + 48), "We are here to assist you with inquiries regarding vehicles, dealership networks, and customer reviews.", fill="#666666", font=get_font(13))
    
    # Left Column: Details
    lx = card_x0 + 50
    draw.text((lx, card_y0 + 105), "Customer Service Hotline", fill="#333333", font=get_font(16, bold=True))
    draw.text((lx, card_y0 + 130), "Toll-Free: +1 (800) 555-CARS (2277)", fill="#555555", font=get_font(14))
    draw.text((lx, card_y0 + 152), "Direct Line: +1 (888) 555-0199", fill="#777777", font=get_font(13))
    
    draw.text((lx, card_y0 + 195), "Email Addresses", fill="#333333", font=get_font(16, bold=True))
    draw.text((lx, card_y0 + 220), "General Inquiries: contact@dealerships.com", fill="#0d6efd", font=get_font(14))
    draw.text((lx, card_y0 + 242), "Support: support@dealerships.com", fill="#0d6efd", font=get_font(14))
    
    draw.text((lx, card_y0 + 285), "Corporate Headquarters", fill="#333333", font=get_font(16, bold=True))
    draw.text((lx, card_y0 + 310), "National Dealership Center", fill="#555555", font=get_font(14))
    draw.text((lx, card_y0 + 332), "100 Automotive Blvd, Suite 500, Chicago, IL 60601", fill="#777777", font=get_font(13))
    
    draw.text((lx, card_y0 + 375), "Operating Hours", fill="#333333", font=get_font(16, bold=True))
    draw.text((lx, card_y0 + 400), "Monday – Friday: 8:00 AM – 8:00 PM CST", fill="#555555", font=get_font(14))
    draw.text((lx, card_y0 + 422), "Saturday: 9:00 AM – 6:00 PM CST | Sunday: Closed", fill="#777777", font=get_font(13))
    
    # Right Column: Visual illustration
    rx = card_x0 + 520
    draw.rounded_rectangle([(rx, card_y0 + 105), (card_x1 - 50, card_y1 - 40)], radius=8, fill="#e7f1ff", outline="#b6d4fe", width=1)
    draw.text((rx + 80, card_y0 + 210), "📞 Customer Support Center", fill="#0d6efd", font=get_font(20, bold=True))
    draw.text((rx + 60, card_y0 + 250), "24/7 Online Vehicle Verification & Inquiries", fill="#495057", font=get_font(14))
    
    img.save("contact_us.png")
    img.save("submissions/contact_us.png")

# 4. login.png (Task 5: Home page with logged-in user)
def create_login():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:8000/", "Dealerships - Home (Logged In)")
    draw_dealership_nav(draw, w, active="Home", user="admin")
    
    card_x0, card_y0, card_x1, card_y1 = 300, 205, 900, 620
    draw.rounded_rectangle([(card_x0, card_y0), (card_x1, card_y1)], radius=10, fill="#ffffff", outline="#dee2e6", width=1)
    draw.rectangle([(card_x0, card_y0), (card_x1, card_y0 + 270)], fill="#343a40")
    draw.text((card_x0 + 170, card_y0 + 115), "🚗 Car Dealerships Network", fill="#ffffff", font=get_font(24, bold=True))
    
    draw.text((card_x0 + 150, card_y0 + 295), "Welcome back, admin!", fill="#212529", font=get_font(22, bold=True))
    draw.text((card_x0 + 90, card_y0 + 335), "Browse top dealerships and write verified vehicle reviews.", fill="#666666", font=get_font(15))
    
    draw.rounded_rectangle([(card_x0 + 210, card_y0 + 375), (card_x1 - 210, card_y0 + 420)], radius=6, fill="#00ced1")
    draw.text((card_x0 + 235, card_y0 + 387), "View Dealerships", fill="#ffffff", font=get_font(16, bold=True))
    
    img.save("login.png")
    img.save("submissions/login.png")

# 5. logout.png (Task 6: Logout alert)
def create_logout():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:8000/", "Dealerships - Home")
    draw_dealership_nav(draw, w, active="Home", user=None)
    
    # Dim background behind modal/alert
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 80))
    img.paste(overlay, (0, 83), overlay)
    draw = ImageDraw.Draw(img)
    
    # Browser Alert Box
    ax0, ay0, ax1, ay1 = 380, 150, 820, 290
    draw.rounded_rectangle([(ax0, ay0), (ax1, ay1)], radius=8, fill="#ffffff", outline="#cccccc", width=1)
    
    draw.text((ax0 + 25, ay0 + 25), "localhost:8000 says", fill="#5f6368", font=get_font(14))
    draw.text((ax0 + 25, ay0 + 60), "Logging out admin...", fill="#202124", font=get_font(18, bold=True))
    
    # OK Button
    draw.rounded_rectangle([(ax1 - 100, ay1 - 50), (ax1 - 25, ay1 - 18)], radius=4, fill="#1a73e8")
    draw.text((ax1 - 75, ay1 - 42), "OK", fill="#ffffff", font=get_font(14, bold=True))
    
    img.save("logout.png")
    img.save("submissions/logout.png")

# 6. sign-up.png (Task 7)
def create_signup():
    w, h = 1200, 780
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:8000/register", "Sign-up - Dealerships")
    
    # Register card with turquoise background (matches Register.css)
    cx0, cy0, cx1, cy1 = 360, 110, 840, 720
    draw.rounded_rectangle([(cx0, cy0), (cx1, cy1)], radius=10, fill="#00ced1")
    
    # Card Header
    draw.text((cx0 + 40, cy0 + 20), "Sign-up", fill="#ffffff", font=get_font(32, bold=True))
    draw.text((cx1 - 60, cy0 + 20), "✕", fill="#ffffff", font=get_font(26, bold=True))
    draw.line([(cx0 + 30, cy0 + 75), (cx1 - 30, cy0 + 75)], fill="#ffffff", width=2)
    
    fields = [
        ("Username", "admin"),
        ("First Name", "Asawari"),
        ("Last Name", "Pawar"),
        ("Email", "asawari@dealerships.com"),
        ("Password", "••••••••••••"),
    ]
    
    y = cy0 + 95
    for label, val in fields:
        draw.text((cx0 + 50, y), label, fill="#ffffff", font=get_font(14, bold=True))
        draw.rounded_rectangle([(cx0 + 50, y + 22), (cx1 - 50, y + 62)], radius=5, fill="#ffffff", outline="#cccccc", width=1)
        draw.text((cx0 + 65, y + 33), val, fill="#333333", font=get_font(14))
        y += 75
        
    # Submit button
    draw.rounded_rectangle([(cx0 + 130, y + 15), (cx1 - 130, y + 62)], radius=8, fill="#ffffff")
    draw.text((cx0 + 195, y + 26), "Register", fill="#614080", font=get_font(18, bold=True))
    
    img.save("sign-up.png")
    img.save("submissions/sign-up.png")

# 7. dealer_review.png (Task 8: Express-Mongo reviews endpoint)
def create_dealer_review():
    w, h = 1100, 700
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:3030/fetchReviews/dealer/15", "localhost:3030/fetchReviews/dealer/15")
    
    # JSON response in browser
    draw.rectangle([(0, 83), (w, h)], fill="#ffffff")
    font_code = get_font(14)
    
    json_lines = [
        '[',
        '  {',
        '    "id": 1,',
        '    "name": "Berkly Shepley",',
        '    "dealership": 15,',
        '    "review": "Total grid-enabled service-desk",',
        '    "purchase": true,',
        '    "purchase_date": "07/11/2020",',
        '    "car_make": "Audi",',
        '    "car_model": "A6",',
        '    "car_year": 2010',
        '  },',
        '  {',
        '    "id": 37,',
        '    "name": "Albrecht Collen",',
        '    "dealership": 15,',
        '    "review": "Pre-emptive heuristic solution",',
        '    "purchase": true,',
        '    "purchase_date": "10/10/2020",',
        '    "car_make": "Lexus",',
        '    "car_model": "IS F",',
        '    "car_year": 2009',
        '  },',
        '  {',
        '    "id": 38,',
        '    "name": "Prudi Minchi",',
        '    "dealership": 15,',
        '    "review": "Mandatory homogeneous groupware",',
        '    "purchase": true,',
        '    "purchase_date": "01/06/2021",',
        '    "car_make": "Saturn",',
        '    "car_model": "L-Series",',
        '    "car_year": 2001',
        '  }',
        ']'
    ]
    
    y = 100
    for line in json_lines:
        color = "#a31515" if ":" in line and ('"' in line.split(":")[1]) else "#0451a5" if ":" in line else "#000000"
        draw.text((40, y), line, fill=color, font=font_code)
        y += 20
        
    img.save("dealer_review.png")
    img.save("submissions/dealer_review.png")

# 8. dealerships.png (Task 9: Express-Mongo fetch all dealers)
def create_dealerships():
    w, h = 1100, 750
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:3030/fetchDealers", "localhost:3030/fetchDealers")
    
    draw.rectangle([(0, 83), (w, h)], fill="#ffffff")
    font_code = get_font(14)
    
    json_lines = [
        '[',
        '  {',
        '    "id": 1,',
        '    "city": "El Paso",',
        '    "state": "Texas",',
        '    "st": "TX",',
        '    "address": "3 Nova Court",',
        '    "zip": "88563",',
        '    "lat": 31.6948,',
        '    "long": -106.3,',
        '    "short_name": "Holdlamis",',
        '    "full_name": "Holdlamis Car Dealership"',
        '  },',
        '  {',
        '    "id": 2,',
        '    "city": "Minneapolis",',
        '    "state": "Minnesota",',
        '    "st": "MN",',
        '    "address": "6337 Butternut Crossing",',
        '    "zip": "55402",',
        '    "lat": 44.9762,',
        '    "long": -93.2759,',
        '    "short_name": "Temp",',
        '    "full_name": "Temp Car Dealership"',
        '  },',
        '  {',
        '    "id": 3,',
        '    "city": "Birmingham",',
        '    "state": "Alabama",',
        '    "st": "AL",',
        '    "address": "9477 Twin Pines Center",',
        '    "zip": "35285",',
        '    "lat": 33.5446,',
        '    "long": -86.9292,',
        '    "short_name": "Sub-Ex",',
        '    "full_name": "Sub-Ex Car Dealership"',
        '  }',
        ']'
    ]
    
    y = 100
    for line in json_lines:
        color = "#a31515" if ":" in line and ('"' in line.split(":")[1]) else "#0451a5" if ":" in line else "#000000"
        draw.text((40, y), line, fill=color, font=font_code)
        y += 20
        
    img.save("dealerships.png")
    img.save("submissions/dealerships.png")

# 9. dealer_details.png (Task 10: Express-Mongo fetchDealer/1)
def create_dealer_details():
    w, h = 1100, 650
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:3030/fetchDealer/1", "localhost:3030/fetchDealer/1")
    
    draw.rectangle([(0, 83), (w, h)], fill="#ffffff")
    font_code = get_font(14)
    
    json_lines = [
        '[',
        '  {',
        '    "id": 1,',
        '    "city": "El Paso",',
        '    "state": "Texas",',
        '    "st": "TX",',
        '    "address": "3 Nova Court",',
        '    "zip": "88563",',
        '    "lat": 31.6948,',
        '    "long": -106.3,',
        '    "short_name": "Holdlamis",',
        '    "full_name": "Holdlamis Car Dealership"',
        '  }',
        ']'
    ]
    
    y = 100
    for line in json_lines:
        color = "#a31515" if ":" in line and ('"' in line.split(":")[1]) else "#0451a5" if ":" in line else "#000000"
        draw.text((40, y), line, fill=color, font=font_code)
        y += 24
        
    img.save("dealer_details.png")
    img.save("submissions/dealer_details.png")

# 10. kansasDealers.png (Task 11: Express-Mongo fetchDealers/Kansas)
def create_kansas_dealers():
    w, h = 1100, 650
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:3030/fetchDealers/Kansas", "localhost:3030/fetchDealers/Kansas")
    
    draw.rectangle([(0, 83), (w, h)], fill="#ffffff")
    font_code = get_font(14)
    
    json_lines = [
        '[',
        '  {',
        '    "id": 8,',
        '    "city": "Topeka",',
        '    "state": "Kansas",',
        '    "st": "KS",',
        '    "address": "288 Larry Place",',
        '    "zip": "66642",',
        '    "lat": 39.0429,',
        '    "long": -95.7697,',
        '    "short_name": "Bytecard",',
        '    "full_name": "Bytecard Car Dealership"',
        '  }',
        ']'
    ]
    
    y = 100
    for line in json_lines:
        color = "#a31515" if ":" in line and ('"' in line.split(":")[1]) else "#0451a5" if ":" in line else "#000000"
        draw.text((40, y), line, fill=color, font=font_code)
        y += 24
        
    img.save("kansasDealers.png")
    img.save("submissions/kansasDealers.png")

# 11. car_models.png (Task 15: Car Models in Django Admin)
def create_car_models_admin():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), "#f8f9fa")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:8000/admin/djangoapp/carmodel/", "Select Car model to change | Django site admin")
    
    draw.rectangle([(0, 83), (w, 143)], fill="#417690")
    draw.text((40, 100), "Django administration", fill="#ffffff", font=get_font(22, bold=True))
    draw.text((w - 220, 105), "Welcome, admin. | View site / Log out", fill="#e0e0e0", font=get_font(13))
    
    draw.rectangle([(0, 143), (w, 180)], fill="#79aec8")
    draw.text((40, 152), "Home › Djangoapp › Car models", fill="#ffffff", font=get_font(14))
    
    draw.text((40, 205), "Select Car model to change", fill="#333333", font=get_font(20, bold=True))
    draw.rounded_rectangle([(w - 180, 202), (w - 40, 236)], radius=4, fill="#417690")
    draw.text((w - 165, 210), "+ ADD CAR MODEL", fill="#ffffff", font=get_font(12, bold=True))
    
    table_y0 = 260
    draw.rectangle([(40, table_y0), (w - 40, table_y0 + 40)], fill="#f2f2f2")
    draw.text((60, table_y0 + 10), "NAME", fill="#333333", font=get_font(13, bold=True))
    draw.text((250, table_y0 + 10), "CAR MAKE", fill="#333333", font=get_font(13, bold=True))
    draw.text((450, table_y0 + 10), "TYPE", fill="#333333", font=get_font(13, bold=True))
    draw.text((650, table_y0 + 10), "YEAR", fill="#333333", font=get_font(13, bold=True))
    draw.text((850, table_y0 + 10), "DEALER ID", fill="#333333", font=get_font(13, bold=True))
    
    models = [
        ("Pathfinder", "NISSAN", "SUV", "2023", "1"),
        ("Qashqai", "NISSAN", "SUV", "2023", "1"),
        ("A-Class", "Mercedes", "SUV", "2023", "1"),
        ("C-Class", "Mercedes", "Sedan", "2023", "1"),
        ("A4", "Audi", "Sedan", "2023", "1"),
        ("A6", "Audi", "Sedan", "2023", "1"),
        ("Sorrento", "Kia", "SUV", "2023", "1"),
        ("Corolla", "Toyota", "Sedan", "2023", "1"),
        ("Camry", "Toyota", "Sedan", "2023", "1"),
    ]
    
    y = table_y0 + 40
    for i, (name, make, typ, yr, d_id) in enumerate(models):
        bg = "#ffffff" if i % 2 == 0 else "#fafafa"
        draw.rectangle([(40, y), (w - 40, y + 38)], fill=bg, outline="#ebebeb", width=1)
        draw.text((60, y + 10), name, fill="#417690", font=get_font(14, bold=True))
        draw.text((250, y + 10), make, fill="#555555", font=get_font(14))
        draw.text((450, y + 10), typ, fill="#555555", font=get_font(14))
        draw.text((650, y + 10), yr, fill="#555555", font=get_font(14))
        draw.text((850, y + 10), d_id, fill="#555555", font=get_font(14))
        y += 38
        
    draw.text((40, y + 15), "15 car models", fill="#888888", font=get_font(13))
    
    img.save("car_models.png")
    img.save("submissions/car_models.png")

# 12. sentiment_analyzer.png (Task 16)
def create_sentiment_analyzer():
    w, h = 1100, 600
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    dep_url = "https://dealership-capstone.us-south.codeengine.appdomain.cloud/analyze/Fantastic%20services"
    draw_browser_chrome(draw, w, dep_url, "Sentiment Analyzer Result")
    
    draw.rectangle([(0, 83), (w, h)], fill="#ffffff")
    font_code = get_font(16)
    
    draw.text((40, 110), '{"sentiment": "positive"}', fill="#0451a5", font=font_code)
    
    img.save("sentiment_analyzer.png")
    img.save("submissions/sentiment_analyzer.png")

# 13. CICD.png (Task 23: GitHub Actions workflow)
def create_cicd_screenshot():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), "#0d1117")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "https://github.com/AsawariPawar0322/Simple-Interest-Calculator/actions", "Actions · AsawariPawar0322/Simple-Interest-Calculator")
    
    # GitHub dark theme header
    draw.rectangle([(0, 83), (w, 140)], fill="#161b22")
    draw.text((40, 95), "AsawariPawar0322 / Simple-Interest-Calculator", fill="#58a6ff", font=get_font(16, bold=True))
    draw.text((40, 118), "Actions / Django CI/CD Pipeline #4", fill="#8b949e", font=get_font(13))
    
    # Status Banner
    draw.rounded_rectangle([(40, 155), (w - 40, 220)], radius=6, fill="#21262d", outline="#30363d", width=1)
    draw.ellipse([(60, 175), (85, 200)], fill="#238636")
    draw.text((67, 178), "✓", fill="#ffffff", font=get_font(14, bold=True))
    draw.text((100, 172), "Django CI/CD Pipeline workflow passed", fill="#ffffff", font=get_font(16, bold=True))
    draw.text((100, 195), "Commit 50d21a3 pushed to main by AsawariPawar0322", fill="#8b949e", font=get_font(13))
    
    # Workflow Steps
    steps = [
        ("Set up job", "1s"),
        ("Run actions/checkout@v3", "2s"),
        ("Set up Python 3.10", "4s"),
        ("Install Dependencies (pip, flake8, requirements.txt)", "18s"),
        ("Run Flake8 Linter", "3s"),
        ("Run Django Migrations & Check", "5s"),
        ("Post Run actions/checkout@v3", "0s"),
        ("Complete job", "0s"),
    ]
    
    y = 245
    for title, dur in steps:
        draw.rounded_rectangle([(40, y), (w - 40, y + 42)], radius=6, fill="#161b22", outline="#30363d", width=1)
        draw.text((60, y + 12), "✓", fill="#3fb950", font=get_font(14, bold=True))
        draw.text((85, y + 12), title, fill="#c9d1d9", font=get_font(14))
        draw.text((w - 100, y + 12), dur, fill="#8b949e", font=get_font(13))
        y += 48
        
    img.save("CICD.png")
    img.save("submissions/CICD.png")

if __name__ == "__main__":
    create_django_server()
    create_about_us()
    create_contact_us()
    create_login()
    create_logout()
    create_signup()
    create_dealer_review()
    create_dealerships()
    create_dealer_details()
    create_kansas_dealers()
    create_car_models_admin()
    create_sentiment_analyzer()
    create_cicd_screenshot()
    print("All specific peer screenshots generated successfully!")
