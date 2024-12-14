from datetime import datetime
import os

def generate_sitemap():
    # Base URL of your website
    base_url = "https://rickjeffersonsolutions.com"
    
    # Core pages with their change frequency and priority
    pages = [
        {
            "loc": "/",
            "lastmod": datetime.now().strftime("%Y-%m-%d"),
            "changefreq": "weekly",
            "priority": "1.0"
        },
        {
            "loc": "/services",
            "lastmod": datetime.now().strftime("%Y-%m-%d"),
            "changefreq": "weekly",
            "priority": "0.9"
        },
        {
            "loc": "/about",
            "lastmod": datetime.now().strftime("%Y-%m-%d"),
            "changefreq": "monthly",
            "priority": "0.8"
        },
        {
            "loc": "/portfolio",
            "lastmod": datetime.now().strftime("%Y-%m-%d"),
            "changefreq": "weekly",
            "priority": "0.8"
        },
        {
            "loc": "/contact",
            "lastmod": datetime.now().strftime("%Y-%m-%d"),
            "changefreq": "monthly",
            "priority": "0.8"
        },
        {
            "loc": "/privacy",
            "lastmod": datetime.now().strftime("%Y-%m-%d"),
            "changefreq": "yearly",
            "priority": "0.5"
        },
        {
            "loc": "/terms",
            "lastmod": datetime.now().strftime("%Y-%m-%d"),
            "changefreq": "yearly",
            "priority": "0.5"
        }
    ]
    
    # Service pages
    service_pages = [
        "business-formation",
        "credit-repair",
        "business-automation",
        "hr-services",
        "custom-apps",
        "grants"
    ]
    
    for service in service_pages:
        pages.append({
            "loc": f"/services#{service}",
            "lastmod": datetime.now().strftime("%Y-%m-%d"),
            "changefreq": "monthly",
            "priority": "0.8"
        })

    # Generate sitemap XML
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for page in pages:
        sitemap += '  <url>\n'
        sitemap += f'    <loc>{base_url}{page["loc"]}</loc>\n'
        sitemap += f'    <lastmod>{page["lastmod"]}</lastmod>\n'
        sitemap += f'    <changefreq>{page["changefreq"]}</changefreq>\n'
        sitemap += f'    <priority>{page["priority"]}</priority>\n'
        sitemap += '  </url>\n'
    
    sitemap += '</urlset>'
    
    # Write sitemap to file
    with open('static/sitemap.xml', 'w') as f:
        f.write(sitemap)

    # Generate robots.txt
    robots_txt = f"""User-agent: *
Allow: /
Sitemap: {base_url}/sitemap.xml

# Disallow admin and private areas
Disallow: /admin/
Disallow: /private/
Disallow: /tmp/
Disallow: /includes/

# Allow search engines to crawl static assets
Allow: /static/css/
Allow: /static/js/
Allow: /static/img/
"""
    
    with open('static/robots.txt', 'w') as f:
        f.write(robots_txt)

if __name__ == "__main__":
    generate_sitemap() 