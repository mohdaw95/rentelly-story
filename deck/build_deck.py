import base64, pathlib, subprocess, re
here = pathlib.Path(__file__).parent; src = here.parent/'src'
t = (here/'deck-template.html').read_text()
def data(name, mime): return f"data:{mime};base64," + base64.b64encode((src/name).read_bytes()).decode()
white = pathlib.Path('/Users/mohammeddawoud/rentelly-profile/rentelly-logo-white-text.svg').read_text()
white = white.replace('width="180" height="36"', 'class="mark" width="180" height="36" role="img" aria-label="Rentelly"')
t = (t.replace('{{LOGO_WHITE_BIG}}', white)
      .replace('{{IMG_HOME}}', data('home.jpg','image/jpeg'))
      .replace('{{IMG_SEARCH}}', data('search.jpg','image/jpeg'))
      .replace('{{IMG_LISTING}}', data('listing.jpg','image/jpeg'))
      .replace('{{CONTACT_EMAIL}}', 'mohammed.dawoud@mzadqatar.com'))
assert '{{' not in t
out = here/'deck.html'; out.write_text(t)
pdf = here/'Rentelly-Pitch-Deck.pdf'
subprocess.run(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','--headless=new','--disable-gpu','--no-pdf-header-footer',
                '--virtual-time-budget=8000','--run-all-compositor-stages-before-draw',f'--print-to-pdf={pdf}',f'file://{out}'],check=True,capture_output=True)
print('pdf', pdf.stat().st_size, 'bytes')
