"""Build index.html (the public GitHub Pages copy) from the private working page.
Usage: python build.py <path to mj-venues.html>"""
import io, sys
s = io.open(sys.argv[1], encoding='utf-8').read()
def rep(a, b):
    global s
    assert s.count(a) >= 1, a[:60]
    s = s.replace(a, b)
rep('<span class="favtag">Your favourite</span>', '<span class="favtag">Top pick</span>')
rep('<span class="favmark">YOUR FAVOURITE</span>', '<span class="favmark">TOP PICK</span>')
rep(' The full notes, including ruled-out venues, are in brampton-party-venues-dec-19-2026.md in Downloads.', '')
head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="robots" content="noindex, nofollow">\n')
assert s.lstrip().startswith('<title>') or '<title>' in s[:300]
io.open('index.html', 'w', encoding='utf-8', newline='\n').write(head + s + '\n</html>\n')
print('ok', len(s))
