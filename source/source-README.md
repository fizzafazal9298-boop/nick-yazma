# Nick Ustasi — Source (Master) Files

Ye folder asal "master" files rakhta hai jin se poori website banti hai.
Live site ki files repo ke root mein hain (GitHub Pages wahi se chalti hai).

## Files
- `build.py` — generator script: templates + saari pages banane ka logic
- `content.py` — tamam pages ka text, FAQ, lists aur settings (content badalna ho to ye file)
- `src/engine.js` — nick generator ka engine (110 styles, semboller, copy system)
- `src/style.css` — poori site ka design (premium ivory/ink/gold theme)

## Site dobara banani ho to
1. Is folder ko apne computer par rakho (structure yahi rahe: build.py, content.py, src/)
2. Command chalao: `python3 build.py`
3. `site/` folder mein tayyar website ban jayegi — us ki files repo ke root mein upload kar do

## Note
Root wali files haath se edit karna theek hai chhoti tabdeeli ke liye, lekin
bari tabdeeli hamesha in source files se karo aur rebuild karo, warna agli
rebuild mein root wali tabdeeli mit jayegi.
