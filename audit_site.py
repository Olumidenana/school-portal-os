import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.olivebranchesschoolsosogbo.com'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=12, context=ctx) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print(f"Status: {resp.status}")
        print(f"HTML Size: {len(html)} bytes")
        title = re.search(r'<title>(.*?)</title>', html, re.I)
        print(f"Title: {title.group(1) if title else 'None'}")
        
        themes = set(re.findall(r'wp-content/themes/([^/\'"]+)', html))
        plugins = set(re.findall(r'wp-content/plugins/([^/\'"]+)', html))
        scripts = re.findall(r'<script[^>]+src=[\'"]([^\'"]+)[\'"]', html)
        
        print("\n--- THEME & STACK ---")
        print("Theme detected:", themes)
        print(f"Plugins detected ({len(plugins)}):", sorted(list(plugins)))
        print(f"External Scripts loaded: {len(scripts)}")
        
        anim_scripts = [s for s in scripts if any(k in s.lower() for k in ['anim', 'wow', 'gsap', 'lottie', 'scroll', 'swiper', 'slick', 'tween'])]
        print("\n--- ANIMATION LIBRARIES ---")
        for s in anim_scripts:
            print(" -", s)
            
        # Check portal links
        portal_links = [l for l in re.findall(r'href=[\'"]([^\'"]+)[\'"]', html) if 'portal' in l.lower() or 'softedu' in l.lower()]
        print("\n--- PORTAL LINKS ---")
        print("Portal links found:", set(portal_links))

except Exception as e:
    print("Fetch error:", e)
