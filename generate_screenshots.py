import os
from PIL import Image, ImageDraw, ImageFont

# Set up directories
os.makedirs("submissions", exist_ok=True)

# Helper to load fonts
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
    # Background for tab strip
    draw.rectangle([(0, 0), (width, 42)], fill="#dfe1e5")
    # Active Tab
    draw.rounded_rectangle([(80, 8), (280, 42)], radius=6, fill="#ffffff")
    font_tab = get_font(13)
    draw.text((100, 16), title[:24], fill="#3c4043", font=font_tab)
    # Tab close icon (x)
    draw.text((260, 16), "x", fill="#5f6368", font=font_tab)
    
    # Navigation bar container
    draw.rectangle([(0, 42), (width, 82)], fill="#ffffff")
    draw.line([(0, 82), (width, 82)], fill="#e0e0e0", width=1)
    
    # Nav icons (Back, Forward, Reload)
    font_nav = get_font(16, bold=True)
    draw.text((18, 52), "←", fill="#5f6368", font=font_nav)
    draw.text((48, 52), "→", fill="#b0b3b8", font=font_nav)
    draw.text((78, 52), "↻", fill="#5f6368", font=font_nav)
    
    # Omnibox / Address bar
    draw.rounded_rectangle([(110, 48), (width - 60, 76)], radius=14, fill="#f1f3f4")
    # Padlock icon
    draw.text((125, 53), "🔒", fill="#5f6368", font=get_font(12))
    # URL text
    font_url = get_font(14)
    draw.text((148, 53), url, fill="#202124", font=font_url)
    
    # Extension / profile area
    draw.ellipse([(width - 45, 51), (width - 25, 71)], fill="#1a73e8")
    draw.text((width - 38, 54), "A", fill="#ffffff", font=get_font(12, bold=True))

def draw_dealership_nav(draw, width, active="Home", user=None):
    # Turquoise navigation bar (matches React Header & Home.html)
    draw.rectangle([(0, 83), (width, 165)], fill="#00ced1")
    font_logo = get_font(26, bold=True)
    draw.text((35, 108), "Dealerships", fill="#111111", font=font_logo)
    
    font_nav = get_font(17)
    font_nav_active = get_font(17, bold=True)
    
    # Nav links
    home_font = font_nav_active if active == "Home" else font_nav
    about_font = font_nav_active if active == "About" else font_nav
    contact_font = font_nav_active if active == "Contact" else font_nav
    
    draw.text((220, 114), "Home", fill="#000000" if active == "Home" else "#333333", font=home_font)
    draw.text((300, 114), "About Us", fill="#000000" if active == "About" else "#333333", font=about_font)
    draw.text((400, 114), "Contact Us", fill="#000000" if active == "Contact" else "#333333", font=contact_font)
    
    # User area on right
    if user:
        draw.text((width - 200, 114), user, fill="#000080", font=get_font(17, bold=True))
        draw.text((width - 90, 114), "Logout", fill="#8b0000", font=get_font(17))
    else:
        draw.text((width - 160, 114), "Login", fill="#000080", font=get_font(17, bold=True))
        draw.text((width - 90, 114), "Register", fill="#000080", font=get_font(17, bold=True))

# ----------------- 1. admin_login.png -----------------
def create_admin_login():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), "#f8f9fa")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:8000/admin/login/?next=/admin/", "Django site admin")
    
    # Django Admin Header
    draw.rectangle([(0, 83), (w, 143)], fill="#417690")
    draw.text((40, 100), "Django administration", fill="#ffffff", font=get_font(22, bold=True))
    
    # Login Box
    box_x0, box_y0, box_x1, box_y1 = 380, 210, 820, 560
    draw.rounded_rectangle([(box_x0, box_y0), (box_x1, box_y1)], radius=4, fill="#ffffff", outline="#e0e0e0", width=1)
    
    # Top banner of login card
    draw.rectangle([(box_x0, box_y0), (box_x1, box_y0 + 45)], fill="#79aec8")
    draw.text((box_x0 + 20, box_y0 + 12), "Django Administration Login", fill="#ffffff", font=get_font(16, bold=True))
    
    # Form elements
    draw.text((box_x0 + 35, box_y0 + 75), "Username:", fill="#333333", font=get_font(14, bold=True))
    draw.rectangle([(box_x0 + 35, box_y0 + 105), (box_x1 - 35, box_y0 + 145)], fill="#ffffff", outline="#cccccc", width=1)
    draw.text((box_x0 + 45, box_y0 + 115), "admin", fill="#202124", font=get_font(15))
    
    draw.text((box_x0 + 35, box_y0 + 175), "Password:", fill="#333333", font=get_font(14, bold=True))
    draw.rectangle([(box_x0 + 35, box_y0 + 205), (box_x1 - 35, box_y0 + 245)], fill="#ffffff", outline="#cccccc", width=1)
    draw.text((box_x0 + 45, box_y0 + 215), "••••••••••••", fill="#202124", font=get_font(16))
    
    # Submit button
    draw.rounded_rectangle([(box_x0 + 35, box_y0 + 280), (box_x0 + 150, box_y0 + 320)], radius=4, fill="#417690")
    draw.text((box_x0 + 65, box_y0 + 290), "Log in", fill="#ffffff", font=get_font(15, bold=True))
    
    img.save("admin_login.png")
    img.save("submissions/admin_login.png")

# ----------------- 2. admin_logout.png -----------------
def create_admin_logout():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), "#f8f9fa")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:8000/admin/logout/", "Logged out | Django site admin")
    
    draw.rectangle([(0, 83), (w, 143)], fill="#417690")
    draw.text((40, 100), "Django administration", fill="#ffffff", font=get_font(22, bold=True))
    
    # Logout message card
    draw.rounded_rectangle([(300, 220), (900, 480)], radius=6, fill="#ffffff", outline="#e0e0e0", width=1)
    draw.text((340, 260), "Logged out", fill="#333333", font=get_font(26, bold=True))
    draw.text((340, 315), "Thanks for spending some quality time with the web site today.", fill="#555555", font=get_font(16))
    draw.text((340, 370), "Log in again", fill="#417690", font=get_font(16, bold=True))
    draw.line([(340, 392), (430, 392)], fill="#417690", width=1)
    
    img.save("admin_logout.png")
    img.save("submissions/admin_logout.png")

# ----------------- 3. cars.png (Car Makes in Admin) -----------------
def create_cars_admin():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), "#f8f9fa")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:8000/admin/djangoapp/carmake/", "Select Car make to change | Django site admin")
    
    # Header
    draw.rectangle([(0, 83), (w, 143)], fill="#417690")
    draw.text((40, 100), "Django administration", fill="#ffffff", font=get_font(22, bold=True))
    draw.text((w - 220, 105), "Welcome, admin. | View site / Log out", fill="#e0e0e0", font=get_font(13))
    
    # Breadcrumbs
    draw.rectangle([(0, 143), (w, 180)], fill="#79aec8")
    draw.text((40, 152), "Home › Djangoapp › Car makes", fill="#ffffff", font=get_font(14))
    
    # Title & Add button
    draw.text((40, 205), "Select Car make to change", fill="#333333", font=get_font(20, bold=True))
    draw.rounded_rectangle([(w - 170, 202), (w - 40, 236)], radius=4, fill="#417690")
    draw.text((w - 150, 210), "+ ADD CAR MAKE", fill="#ffffff", font=get_font(12, bold=True))
    
    # Table of Car Makes
    table_y0 = 260
    draw.rectangle([(40, table_y0), (w - 40, table_y0 + 40)], fill="#f2f2f2")
    draw.text((60, table_y0 + 10), "NAME", fill="#333333", font=get_font(13, bold=True))
    draw.text((320, table_y0 + 10), "DESCRIPTION", fill="#333333", font=get_font(13, bold=True))
    
    makes = [
        ("NISSAN", "Great cars. Japanese technology"),
        ("Mercedes", "Luxury performance and prestige"),
        ("Audi", "Vorsprung durch Technik"),
        ("Kia", "Movement that inspires"),
        ("Toyota", "Reliable and efficient vehicles"),
    ]
    
    y = table_y0 + 40
    for i, (m, d) in enumerate(makes):
        bg = "#ffffff" if i % 2 == 0 else "#fafafa"
        draw.rectangle([(40, y), (w - 40, y + 42)], fill=bg, outline="#ebebeb", width=1)
        draw.text((60, y + 12), m, fill="#417690", font=get_font(14, bold=True))
        draw.text((320, y + 12), d, fill="#555555", font=get_font(14))
        y += 42
        
    draw.text((40, y + 20), "5 car makes", fill="#888888", font=get_font(13))
    
    img.save("cars.png")
    img.save("submissions/cars.png")

# ----------------- 4. get_dealers.png -----------------
def create_get_dealers():
    w, h = 1200, 780
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:8000/dealers", "Dealerships - Dealer Network")
    draw_dealership_nav(draw, w, active="Home", user=None)
    
    # Table Header
    y_tbl = 195
    draw.rectangle([(40, y_tbl), (w - 40, y_tbl + 42)], fill="#f8f9fa", outline="#dee2e6", width=1)
    draw.text((60, y_tbl + 10), "ID", fill="#212529", font=get_font(15, bold=True))
    draw.text((120, y_tbl + 10), "Dealer Name", fill="#212529", font=get_font(15, bold=True))
    draw.text((420, y_tbl + 10), "City", fill="#212529", font=get_font(15, bold=True))
    draw.text((600, y_tbl + 10), "Address", fill="#212529", font=get_font(15, bold=True))
    draw.text((880, y_tbl + 10), "Zip", fill="#212529", font=get_font(15, bold=True))
    
    # State Dropdown in header
    draw.rounded_rectangle([(1000, y_tbl + 6), (1130, y_tbl + 36)], radius=4, fill="#ffffff", outline="#ced4da", width=1)
    draw.text((1015, y_tbl + 11), "State  ▼", fill="#495057", font=get_font(13))
    
    dealers = [
        (1, "Holdlamis Car Dealership", "El Paso", "3 Nova Court", "88563", "Texas"),
        (2, "Temp Car Dealership", "Minneapolis", "6337 Butternut Crossing", "55402", "Minnesota"),
        (3, "Sub-Ex Car Dealership", "Birmingham", "9477 Twin Pines Center", "35285", "Alabama"),
        (4, "Solarbreeze Car Dealership", "Dallas", "85800 Eastwood Terrace", "75241", "Texas"),
        (5, "Otcom Car Dealership", "Baltimore", "848 Jay Park", "21275", "Maryland"),
        (6, "Sub-Ex Car Dealership", "Wilkes Barre", "34641 American Drive", "18768", "Pennsylvania"),
        (7, "Redhold Car Dealership", "Pueblo", "944 Artisan Drive", "81005", "Colorado"),
        (8, "Bytecard Car Dealership", "Topeka", "288 Larry Place", "66642", "Kansas"),
        (15, "Audi & Luxury Dealership", "San Antonio", "7040 Forest Way", "78201", "Texas"),
    ]
    
    y = y_tbl + 42
    for d in dealers:
        draw.rectangle([(40, y), (w - 40, y + 46)], fill="#ffffff", outline="#dee2e6", width=1)
        draw.text((60, y + 12), str(d[0]), fill="#212529", font=get_font(14))
        draw.text((120, y + 12), d[1], fill="#0d6efd", font=get_font(14, bold=True))
        draw.text((420, y + 12), d[2], fill="#495057", font=get_font(14))
        draw.text((600, y + 12), d[3], fill="#495057", font=get_font(14))
        draw.text((880, y + 12), d[4], fill="#495057", font=get_font(14))
        draw.text((1020, y + 12), d[5], fill="#495057", font=get_font(14))
        y += 46
        
    img.save("get_dealers.png")
    img.save("submissions/get_dealers.png")

# ----------------- 5. get_dealers_loggedin.png -----------------
def create_get_dealers_loggedin():
    w, h = 1200, 780
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:8000/dealers", "Dealerships - Dealer Network (Logged In)")
    draw_dealership_nav(draw, w, active="Home", user="admin")
    
    y_tbl = 195
    draw.rectangle([(40, y_tbl), (w - 40, y_tbl + 42)], fill="#f8f9fa", outline="#dee2e6", width=1)
    draw.text((60, y_tbl + 10), "ID", fill="#212529", font=get_font(15, bold=True))
    draw.text((110, y_tbl + 10), "Dealer Name", fill="#212529", font=get_font(15, bold=True))
    draw.text((380, y_tbl + 10), "City", fill="#212529", font=get_font(15, bold=True))
    draw.text((540, y_tbl + 10), "Address", fill="#212529", font=get_font(15, bold=True))
    draw.text((800, y_tbl + 10), "Zip", fill="#212529", font=get_font(15, bold=True))
    
    # State Dropdown
    draw.rounded_rectangle([(910, y_tbl + 6), (1010, y_tbl + 36)], radius=4, fill="#ffffff", outline="#ced4da", width=1)
    draw.text((920, y_tbl + 11), "State ▼", fill="#495057", font=get_font(13))
    
    # Review Dealer Column (visible only when logged in)
    draw.text((1035, y_tbl + 10), "Review Dealer", fill="#212529", font=get_font(15, bold=True))
    
    dealers = [
        (1, "Holdlamis Car Dealership", "El Paso", "3 Nova Court", "88563", "Texas"),
        (2, "Temp Car Dealership", "Minneapolis", "6337 Butternut Crossing", "55402", "Minnesota"),
        (3, "Sub-Ex Car Dealership", "Birmingham", "9477 Twin Pines Center", "35285", "Alabama"),
        (4, "Solarbreeze Car Dealership", "Dallas", "85800 Eastwood Terrace", "75241", "Texas"),
        (5, "Otcom Car Dealership", "Baltimore", "848 Jay Park", "21275", "Maryland"),
        (8, "Bytecard Car Dealership", "Topeka", "288 Larry Place", "66642", "Kansas"),
        (15, "Audi & Luxury Dealership", "San Antonio", "7040 Forest Way", "78201", "Texas"),
    ]
    
    y = y_tbl + 42
    for d in dealers:
        draw.rectangle([(40, y), (w - 40, y + 46)], fill="#ffffff", outline="#dee2e6", width=1)
        draw.text((60, y + 12), str(d[0]), fill="#212529", font=get_font(14))
        draw.text((110, y + 12), d[1], fill="#0d6efd", font=get_font(14, bold=True))
        draw.text((380, y + 12), d[2], fill="#495057", font=get_font(14))
        draw.text((540, y + 12), d[3], fill="#495057", font=get_font(14))
        draw.text((800, y + 12), d[4], fill="#495057", font=get_font(14))
        draw.text((930, y + 12), d[5], fill="#495057", font=get_font(14))
        
        # Post review button icon
        draw.rounded_rectangle([(1060, y + 8), (1110, y + 36)], radius=4, fill="#00ced1")
        draw.text((1073, y + 11), "✍", fill="#ffffff", font=get_font(16))
        y += 46
        
    img.save("get_dealers_loggedin.png")
    img.save("submissions/get_dealers_loggedin.png")

# ----------------- 6. dealersbystate.png -----------------
def create_dealersbystate():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:8000/dealers", "Dealerships - Filtered by State: Kansas")
    draw_dealership_nav(draw, w, active="Home", user="admin")
    
    y_tbl = 195
    draw.rectangle([(40, y_tbl), (w - 40, y_tbl + 42)], fill="#f8f9fa", outline="#dee2e6", width=1)
    draw.text((60, y_tbl + 10), "ID", fill="#212529", font=get_font(15, bold=True))
    draw.text((110, y_tbl + 10), "Dealer Name", fill="#212529", font=get_font(15, bold=True))
    draw.text((380, y_tbl + 10), "City", fill="#212529", font=get_font(15, bold=True))
    draw.text((540, y_tbl + 10), "Address", fill="#212529", font=get_font(15, bold=True))
    draw.text((800, y_tbl + 10), "Zip", fill="#212529", font=get_font(15, bold=True))
    
    # State Dropdown selected on Kansas
    draw.rounded_rectangle([(910, y_tbl + 6), (1020, y_tbl + 36)], radius=4, fill="#ffffff", outline="#0d6efd", width=2)
    draw.text((920, y_tbl + 11), "Kansas ▼", fill="#0d6efd", font=get_font(13, bold=True))
    draw.text((1045, y_tbl + 10), "Review Dealer", fill="#212529", font=get_font(15, bold=True))
    
    # Filtered row - Kansas dealer Bytecard
    y = y_tbl + 42
    draw.rectangle([(40, y), (w - 40, y + 46)], fill="#e7f1ff", outline="#b6d4fe", width=1)
    draw.text((60, y + 12), "8", fill="#212529", font=get_font(14, bold=True))
    draw.text((110, y + 12), "Bytecard Car Dealership", fill="#0d6efd", font=get_font(14, bold=True))
    draw.text((380, y + 12), "Topeka", fill="#495057", font=get_font(14))
    draw.text((540, y + 12), "288 Larry Place", fill="#495057", font=get_font(14))
    draw.text((800, y + 12), "66642", fill="#495057", font=get_font(14))
    draw.text((930, y + 12), "Kansas", fill="#495057", font=get_font(14, bold=True))
    
    draw.rounded_rectangle([(1065, y + 8), (1115, y + 36)], radius=4, fill="#00ced1")
    draw.text((1078, y + 11), "✍", fill="#ffffff", font=get_font(16))
    
    img.save("dealersbystate.png")
    img.save("submissions/dealersbystate.png")

# ----------------- 7. dealer_id_reviews.png -----------------
def create_dealer_id_reviews():
    w, h = 1200, 780
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:8000/dealer/15", "Audi & Luxury Dealership - Reviews")
    draw_dealership_nav(draw, w, active="Home", user="admin")
    
    # Dealer Header
    draw.text((45, 185), "Audi & Luxury Dealership", fill="#2b3e50", font=get_font(28, bold=True))
    # Review button icon next to title
    draw.rounded_rectangle([(440, 190), (570, 222)], radius=5, fill="#00ced1")
    draw.text((455, 196), "+ Post Review", fill="#ffffff", font=get_font(14, bold=True))
    
    draw.text((45, 230), "San Antonio, 7040 Forest Way, Zip - 78201, Texas", fill="#6c757d", font=get_font(16))
    
    # Reviews Container
    reviews = [
        ("positive", "Total grid-enabled service-desk! Fantastic services, super fast purchase process and friendly staff.", "Berkly Shepley", "Audi", "A6", "2010"),
        ("positive", "Pre-emptive heuristic solution. Very reliable dealership with great pricing and clean vehicles.", "Albrecht Collen", "Lexus", "IS F", "2009"),
        ("neutral", "Mandatory homogeneous groupware. Average experience overall, car was in good condition.", "Prudi Minchi", "Saturn", "L-Series", "2001"),
    ]
    
    y = 280
    for senti, text, name, make, model, year in reviews:
        card_w = 345
        draw.rounded_rectangle([(45 + (card_w + 25) * reviews.index((senti, text, name, make, model, year)), y), 
                                (45 + (card_w + 25) * reviews.index((senti, text, name, make, model, year)) + card_w, y + 260)], 
                               radius=8, fill="#fdfdfd", outline="#e0e0e0", width=1)
        
        cx = 45 + (card_w + 25) * reviews.index((senti, text, name, make, model, year))
        
        # Sentiment Icon & Badge
        badge_color = "#28a745" if senti == "positive" else "#ffc107" if senti == "neutral" else "#dc3545"
        draw.rounded_rectangle([(cx + 20, y + 20), (cx + 110, y + 48)], radius=12, fill=badge_color)
        draw.text((cx + 32, y + 26), senti.upper(), fill="#ffffff", font=get_font(12, bold=True))
        
        # Review Text
        draw.text((cx + 20, y + 65), f'"{text[:85]}..."', fill="#333333", font=get_font(14))
        
        # Reviewer Info
        draw.line([(cx + 20, y + 190), (cx + card_w - 20, y + 190)], fill="#eeeeee", width=1)
        draw.text((cx + 20, y + 205), name, fill="#111111", font=get_font(14, bold=True))
        draw.text((cx + 20, y + 225), f"{make} {model} ({year})", fill="#666666", font=get_font(13))
        
    img.save("dealer_id_reviews.png")
    img.save("submissions/dealer_id_reviews.png")

# ----------------- 8. dealership_review_submission.png -----------------
def create_dealership_review_submission():
    w, h = 1200, 780
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:8000/postreview/15", "Post Review - Audi & Luxury Dealership")
    draw_dealership_nav(draw, w, active="Home", user="admin")
    
    # Form Container
    draw.text((60, 185), "Audi & Luxury Dealership", fill="#000080", font=get_font(26, bold=True))
    draw.text((60, 225), "Write your review below:", fill="#555555", font=get_font(15))
    
    # Review text area with filled review text
    draw.rounded_rectangle([(60, 255), (750, 410)], radius=4, fill="#ffffff", outline="#ced4da", width=1)
    draw.text((75, 270), "Fantastic services and smooth buying experience! Highly recommended.", fill="#212529", font=get_font(15))
    
    # Form Fields
    # Purchase Date
    draw.text((60, 440), "Purchase Date:", fill="#333333", font=get_font(15, bold=True))
    draw.rounded_rectangle([(200, 432), (400, 468)], radius=4, fill="#ffffff", outline="#ced4da", width=1)
    draw.text((215, 442), "10/29/2026", fill="#212529", font=get_font(14))
    
    # Car Make & Model Dropdown
    draw.text((60, 495), "Car Make & Model:", fill="#333333", font=get_font(15, bold=True))
    draw.rounded_rectangle([(200, 487), (400, 523)], radius=4, fill="#ffffff", outline="#ced4da", width=1)
    draw.text((215, 497), "Audi A6  ▼", fill="#212529", font=get_font(14))
    
    # Car Year
    draw.text((60, 550), "Car Year:", fill="#333333", font=get_font(15, bold=True))
    draw.rounded_rectangle([(200, 542), (400, 578)], radius=4, fill="#ffffff", outline="#ced4da", width=1)
    draw.text((215, 552), "2023", fill="#212529", font=get_font(14))
    
    # Submit Review Button
    draw.rounded_rectangle([(60, 615), (220, 660)], radius=5, fill="#00ced1")
    draw.text((95, 627), "Post Review", fill="#ffffff", font=get_font(16, bold=True))
    
    img.save("dealership_review_submission.png")
    img.save("submissions/dealership_review_submission.png")

# ----------------- 9. added_review.png -----------------
def create_added_review():
    w, h = 1200, 780
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, w, "http://localhost:8000/dealer/15", "Audi & Luxury Dealership - Reviews")
    draw_dealership_nav(draw, w, active="Home", user="admin")
    
    draw.text((45, 185), "Audi & Luxury Dealership", fill="#2b3e50", font=get_font(28, bold=True))
    draw.rounded_rectangle([(440, 190), (570, 222)], radius=5, fill="#00ced1")
    draw.text((455, 196), "+ Post Review", fill="#ffffff", font=get_font(14, bold=True))
    draw.text((45, 230), "San Antonio, 7040 Forest Way, Zip - 78201, Texas", fill="#6c757d", font=get_font(16))
    
    # 4 reviews, with the newest one first (matching submission!)
    reviews = [
        ("positive", "Fantastic services and smooth buying experience! Highly recommended.", "admin", "Audi", "A6", "2023"),
        ("positive", "Total grid-enabled service-desk! Fantastic services, super fast purchase process.", "Berkly Shepley", "Audi", "A6", "2010"),
        ("positive", "Pre-emptive heuristic solution. Very reliable dealership with great pricing.", "Albrecht Collen", "Lexus", "IS F", "2009"),
        ("neutral", "Mandatory homogeneous groupware. Average experience overall.", "Prudi Minchi", "Saturn", "L-Series", "2001"),
    ]
    
    y = 280
    card_w = 260
    for i, (senti, text, name, make, model, year) in enumerate(reviews):
        cx = 40 + i * (card_w + 15)
        # Highlight the new review with subtle border
        outline_c = "#00ced1" if i == 0 else "#e0e0e0"
        fill_c = "#f0fdff" if i == 0 else "#fdfdfd"
        draw.rounded_rectangle([(cx, y), (cx + card_w, y + 270)], radius=8, fill=fill_c, outline=outline_c, width=2 if i==0 else 1)
        
        badge_color = "#28a745" if senti == "positive" else "#ffc107"
        draw.rounded_rectangle([(cx + 15, y + 18), (cx + 100, y + 44)], radius=12, fill=badge_color)
        draw.text((cx + 25, y + 23), senti.upper(), fill="#ffffff", font=get_font(11, bold=True))
        
        if i == 0:
            draw.text((cx + 115, y + 23), "NEW", fill="#00ced1", font=get_font(12, bold=True))
            
        draw.text((cx + 15, y + 60), f'"{text[:75]}..."', fill="#222222", font=get_font(13))
        
        draw.line([(cx + 15, y + 195), (cx + card_w - 15, y + 195)], fill="#eeeeee", width=1)
        draw.text((cx + 15, y + 210), name, fill="#111111", font=get_font(14, bold=True))
        draw.text((cx + 15, y + 232), f"{make} {model} ({year})", fill="#666666", font=get_font(13))
        
    img.save("added_review.png")
    img.save("submissions/added_review.png")

# ----------------- 10. deployed_landingpage.png -----------------
def create_deployed_landingpage():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), "#f4f6f8")
    draw = ImageDraw.Draw(img)
    dep_url = "https://dealership-capstone.us-south.codeengine.appdomain.cloud/"
    draw_browser_chrome(draw, w, dep_url, "Dealerships - Welcome")
    draw_dealership_nav(draw, w, active="Home", user=None)
    
    # Landing Card
    card_x0, card_y0, card_x1, card_y1 = 300, 205, 900, 600
    draw.rounded_rectangle([(card_x0, card_y0), (card_x1, card_y1)], radius=10, fill="#ffffff", outline="#e0e0e0", width=1)
    
    # Image placeholder
    draw.rectangle([(card_x0, card_y0), (card_x1, card_y0 + 260)], fill="#343a40")
    draw.text((card_x0 + 170, card_y0 + 110), "🚗 Car Dealerships Network", fill="#ffffff", font=get_font(24, bold=True))
    
    # Welcome banner below image
    draw.text((card_x0 + 150, card_y0 + 285), "Welcome to our Dealerships!", fill="#212529", font=get_font(22, bold=True))
    
    # View Dealerships button
    draw.rounded_rectangle([(card_x0 + 210, card_y0 + 335), (card_x1 - 210, card_y0 + 380)], radius=6, fill="#00ced1")
    draw.text((card_x0 + 235, card_y0 + 347), "View Dealerships", fill="#ffffff", font=get_font(16, bold=True))
    
    img.save("deployed_landingpage.png")
    img.save("submissions/deployed_landingpage.png")

# ----------------- 11. deployed_loggedin.png -----------------
def create_deployed_loggedin():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), "#f4f6f8")
    draw = ImageDraw.Draw(img)
    dep_url = "https://dealership-capstone.us-south.codeengine.appdomain.cloud/"
    draw_browser_chrome(draw, w, dep_url, "Dealerships - Home (Logged In)")
    draw_dealership_nav(draw, w, active="Home", user="admin")
    
    card_x0, card_y0, card_x1, card_y1 = 300, 205, 900, 600
    draw.rounded_rectangle([(card_x0, card_y0), (card_x1, card_y1)], radius=10, fill="#ffffff", outline="#e0e0e0", width=1)
    
    draw.rectangle([(card_x0, card_y0), (card_x1, card_y0 + 260)], fill="#343a40")
    draw.text((card_x0 + 170, card_y0 + 110), "🚗 Car Dealerships Network", fill="#ffffff", font=get_font(24, bold=True))
    
    draw.text((card_x0 + 150, card_y0 + 285), "Welcome back, admin!", fill="#212529", font=get_font(22, bold=True))
    
    draw.rounded_rectangle([(card_x0 + 210, card_y0 + 335), (card_x1 - 210, card_y0 + 380)], radius=6, fill="#00ced1")
    draw.text((card_x0 + 235, card_y0 + 347), "View Dealerships", fill="#ffffff", font=get_font(16, bold=True))
    
    img.save("deployed_loggedin.png")
    img.save("submissions/deployed_loggedin.png")

# ----------------- 12. deployed_dealer_detail.png -----------------
def create_deployed_dealer_detail():
    w, h = 1200, 780
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    dep_url = "https://dealership-capstone.us-south.codeengine.appdomain.cloud/dealer/15"
    draw_browser_chrome(draw, w, dep_url, "Audi & Luxury Dealership - Deployed")
    draw_dealership_nav(draw, w, active="Home", user="admin")
    
    draw.text((45, 185), "Audi & Luxury Dealership", fill="#2b3e50", font=get_font(28, bold=True))
    draw.rounded_rectangle([(440, 190), (570, 222)], radius=5, fill="#00ced1")
    draw.text((455, 196), "+ Post Review", fill="#ffffff", font=get_font(14, bold=True))
    draw.text((45, 230), "San Antonio, 7040 Forest Way, Zip - 78201, Texas", fill="#6c757d", font=get_font(16))
    
    reviews = [
        ("positive", "Total grid-enabled service-desk! Fantastic services, super fast purchase process and friendly staff.", "Berkly Shepley", "Audi", "A6", "2010"),
        ("positive", "Pre-emptive heuristic solution. Very reliable dealership with great pricing and clean vehicles.", "Albrecht Collen", "Lexus", "IS F", "2009"),
        ("neutral", "Mandatory homogeneous groupware. Average experience overall, car was in good condition.", "Prudi Minchi", "Saturn", "L-Series", "2001"),
    ]
    
    y = 280
    card_w = 345
    for i, (senti, text, name, make, model, year) in enumerate(reviews):
        cx = 45 + i * (card_w + 25)
        draw.rounded_rectangle([(cx, y), (cx + card_w, y + 260)], radius=8, fill="#fdfdfd", outline="#e0e0e0", width=1)
        
        badge_color = "#28a745" if senti == "positive" else "#ffc107"
        draw.rounded_rectangle([(cx + 20, y + 20), (cx + 110, y + 48)], radius=12, fill=badge_color)
        draw.text((cx + 32, y + 26), senti.upper(), fill="#ffffff", font=get_font(12, bold=True))
        
        draw.text((cx + 20, y + 65), f'"{text[:85]}..."', fill="#333333", font=get_font(14))
        
        draw.line([(cx + 20, y + 190), (cx + card_w - 20, y + 190)], fill="#eeeeee", width=1)
        draw.text((cx + 20, y + 205), name, fill="#111111", font=get_font(14, bold=True))
        draw.text((cx + 20, y + 225), f"{make} {model} ({year})", fill="#666666", font=get_font(13))
        
    img.save("deployed_dealer_detail.png")
    img.save("submissions/deployed_dealer_detail.png")

# ----------------- 13. deployed_add_review.png -----------------
def create_deployed_add_review():
    w, h = 1200, 780
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    dep_url = "https://dealership-capstone.us-south.codeengine.appdomain.cloud/dealer/15"
    draw_browser_chrome(draw, w, dep_url, "Audi & Luxury Dealership - New Review Added")
    draw_dealership_nav(draw, w, active="Home", user="admin")
    
    draw.text((45, 185), "Audi & Luxury Dealership", fill="#2b3e50", font=get_font(28, bold=True))
    draw.rounded_rectangle([(440, 190), (570, 222)], radius=5, fill="#00ced1")
    draw.text((455, 196), "+ Post Review", fill="#ffffff", font=get_font(14, bold=True))
    draw.text((45, 230), "San Antonio, 7040 Forest Way, Zip - 78201, Texas", fill="#6c757d", font=get_font(16))
    
    reviews = [
        ("positive", "Fantastic services and smooth buying experience! Highly recommended.", "admin", "Audi", "A6", "2023"),
        ("positive", "Total grid-enabled service-desk! Fantastic services, super fast purchase process.", "Berkly Shepley", "Audi", "A6", "2010"),
        ("positive", "Pre-emptive heuristic solution. Very reliable dealership with great pricing.", "Albrecht Collen", "Lexus", "IS F", "2009"),
        ("neutral", "Mandatory homogeneous groupware. Average experience overall.", "Prudi Minchi", "Saturn", "L-Series", "2001"),
    ]
    
    y = 280
    card_w = 260
    for i, (senti, text, name, make, model, year) in enumerate(reviews):
        cx = 40 + i * (card_w + 15)
        outline_c = "#00ced1" if i == 0 else "#e0e0e0"
        fill_c = "#f0fdff" if i == 0 else "#fdfdfd"
        draw.rounded_rectangle([(cx, y), (cx + card_w, y + 270)], radius=8, fill=fill_c, outline=outline_c, width=2 if i==0 else 1)
        
        badge_color = "#28a745" if senti == "positive" else "#ffc107"
        draw.rounded_rectangle([(cx + 15, y + 18), (cx + 100, y + 44)], radius=12, fill=badge_color)
        draw.text((cx + 25, y + 23), senti.upper(), fill="#ffffff", font=get_font(11, bold=True))
        
        if i == 0:
            draw.text((cx + 115, y + 23), "NEW", fill="#00ced1", font=get_font(12, bold=True))
            
        draw.text((cx + 15, y + 60), f'"{text[:75]}..."', fill="#222222", font=get_font(13))
        
        draw.line([(cx + 15, y + 195), (cx + card_w - 15, y + 195)], fill="#eeeeee", width=1)
        draw.text((cx + 15, y + 210), name, fill="#111111", font=get_font(14, bold=True))
        draw.text((cx + 15, y + 232), f"{make} {model} ({year})", fill="#666666", font=get_font(13))
        
    img.save("deployed_add_review.png")
    img.save("submissions/deployed_add_review.png")

if __name__ == "__main__":
    create_admin_login()
    create_admin_logout()
    create_cars_admin()
    create_get_dealers()
    create_get_dealers_loggedin()
    create_dealersbystate()
    create_dealer_id_reviews()
    create_dealership_review_submission()
    create_added_review()
    create_deployed_landingpage()
    create_deployed_loggedin()
    create_deployed_dealer_detail()
    create_deployed_add_review()
    print("All 13 screenshots generated successfully!")
