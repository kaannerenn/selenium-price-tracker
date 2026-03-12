import json
from datetime import datetime

def save_to_json(data, filename="products.json"):

    try:
        filename = f"{datetime.now().strftime('%Y%m%d_%H%M')}_{filename}"

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"[Hata] JSON kaydedilirken sorun var: {e}")