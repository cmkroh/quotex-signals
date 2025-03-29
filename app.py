@@ -0,0 +1,20 @@
 from flask import Flask, render_template
 import random
 
 app = Flask(_name_)
 
 def predict_candle():
     # (بعد میں AI/API سے تبدیل کریں)
     return random.choice(["🔴 RED", "🟢 GREEN"]), random.randint(50, 90)
 
 @app.route('/')
 def dashboard():
     timeframes = ["1m", "2m", "3m", "5m", "15m", "30m"]
     signals = []
     for tf in timeframes:
         candle, confidence = predict_candle()
         signals.append({"timeframe": tf, "candle": candle, "confidence": f"{confidence}%"})
     return render_template("index.html", signals=signals)
 
 if _name_ == '_main_':
     app.run(debug=True)
