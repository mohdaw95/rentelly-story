import base64, pathlib, re
src = pathlib.Path(__file__).parent
t = (src/'template.html').read_text()
def data(name, mime):
    return f"data:{mime};base64," + base64.b64encode((src/name).read_bytes()).decode()
logo = (pathlib.Path('/Users/mohammeddawoud/rentelly-profile/rentelly-logo-dark-text.svg').read_text()
        .replace('fill="#1B1B3A"','fill="#0D3934"').replace('width="180" height="36"','width="130" height="26" role="img" aria-label="Rentelly"'))
t = (t.replace('{{LOGO_SVG}}', logo)
      .replace('{{IMG_HOME}}', data('home.jpg','image/jpeg'))
      .replace('{{IMG_LISTING}}', data('listing.jpg','image/jpeg'))
      .replace('{{IMG_SEARCH}}', data('search.jpg','image/jpeg'))
      .replace('{{IMG_MZAD}}', data('mzad-app.png','image/png'))
      .replace('{{CONTACT_EMAIL}}', 'mohammed.dawoud@mzadqatar.com'))
assert '{{' not in t, re.findall(r'\{\{\w+\}\}', t)
(src.parent/'index.html').write_text(t)
print('wrote', len(t), 'bytes')
