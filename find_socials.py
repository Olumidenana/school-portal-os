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
        
        # Social links
        social_pattern = r'href=[\'"](https?://(?:www\.)?(?:facebook|instagram|youtube|twitter|x|linkedin|tiktok)\.com/[^\'"]+)[\'"]'
        socials = set(re.findall(social_pattern, html, re.I))
        print("Social Links found:")
        for s in socials:
            print("  -", s)
        
        # Check all links containing blog, news, etc.
        all_links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', html)
        blog_links = set([l for l in all_links if any(k in l.lower() for k in ['blog', 'news', 'category', 'post', 'article', '2023', '2024', '2025', '2026'])])
        print("\nBlog/News links:")
        for b in sorted(list(blog_links))[:15]:
            print("  -", b)
            
        # Check YouTube embeds or IDs
        yt_pattern = r'(?:https?:)?//(?:www\.)?(?:youtube\.com|youtu\.be)/(?:channel/|c/|user/|embed/|watch\?v=|@)?([a-zA-Z0-9_-]+)'
        yt = set(re.findall(yt_pattern, html))
        print("\nYouTube IDs/Channels found:", yt)

except Exception as e:
    print("Error:", e)
