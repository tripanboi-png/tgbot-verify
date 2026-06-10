"""PNG 学生证生成模块 - ZAMZZZ EDITION (UNIVERSITAS INDONESIA) - REALISTIC VERSION"""
import random
from datetime import datetime
from io import BytesIO
import base64
import string


def generate_student_id():
    """生成随机 NIM (Mahasiswa ID)"""
    return f"{random.randint(10000000, 99999999)}"


def generate_email(first_name, last_name):
    """
    Generate email - FORCED to use Gmail ONLY!
    """
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{username}@gmail.com"


generate_psu_email = generate_email


def generate_html(first_name, last_name, school_id='349653'):
    """
    生成 Universitas Indonesia Student Portal HTML
    """
    student_id = generate_student_id()
    name = f"{first_name} {last_name}"
    date = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    valid_until = datetime.now().strftime('%d %B %Y')

    majors = [
        'Teknik Informatika (S1)',
        'Sistem Informasi (S1)',
        'Ilmu Komputer (S1)'
    ]
    major = random.choice(majors)
    
    faculties = ['Fakultas Ilmu Komputer', 'Fakultas Teknik']
    faculty = random.choice(faculties)

    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kartu Tanda Mahasiswa - Universitas Indonesia</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Courier New', 'Segoe UI', Arial, sans-serif;
            background: #e0e0e0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }}
        .card {{
            max-width: 800px;
            width: 100%;
            background: white;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            overflow: hidden;
            border: 1px solid #ccc;
        }}
        .header {{
            background: #FF6600;
            padding: 15px;
            text-align: center;
            color: white;
        }}
        .header h1 {{
            font-size: 24px;
            margin-bottom: 5px;
        }}
        .header p {{
            font-size: 14px;
        }}
        .content {{
            padding: 25px;
        }}
        .photo-section {{
            display: flex;
            gap: 20px;
            margin-bottom: 25px;
            border-bottom: 1px solid #ddd;
            padding-bottom: 15px;
        }}
        .photo-placeholder {{
            width: 120px;
            height: 140px;
            background: #f0f0f0;
            border: 1px solid #aaa;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            color: #777;
        }}
        .info {{
            flex: 1;
        }}
        .info-row {{
            margin-bottom: 12px;
        }}
        .info-label {{
            font-weight: bold;
            font-size: 12px;
            color: #555;
            text-transform: uppercase;
        }}
        .info-value {{
            font-size: 16px;
            font-weight: 500;
            color: #222;
            border-bottom: 1px solid #eee;
            padding-bottom: 4px;
        }}
        .barcode {{
            margin-top: 20px;
            text-align: center;
            padding: 15px;
            background: #fafafa;
            border-top: 1px dashed #ccc;
        }}
        .barcode div {{
            font-family: monospace;
            letter-spacing: 2px;
            font-size: 18px;
            margin-bottom: 5px;
        }}
        .valid-badge {{
            background: #e6f7e6;
            border-left: 4px solid #28a745;
            padding: 10px;
            margin-top: 15px;
            font-size: 13px;
            color: #155724;
        }}
        .stamp {{
            text-align: right;
            margin-top: 20px;
            font-style: italic;
            color: #888;
            font-size: 12px;
            border-top: 1px solid #eee;
            padding-top: 12px;
        }}
        @media print {{
            body {{
                background: white;
                padding: 0;
            }}
            .card {{
                box-shadow: none;
                border: 1px solid #aaa;
            }}
        }}
    </style>
</head>
<body>
<div class="card">
    <div class="header">
        <h1>UNIVERSITAS INDONESIA</h1>
        <p>KARTU TANDA MAHASISWA</p>
    </div>
    <div class="content">
        <div class="photo-section">
            <div class="photo-placeholder">
                [FOTO]<br>3x4 cm
            </div>
            <div class="info">
                <div class="info-row">
                    <div class="info-label">Nama Lengkap</div>
                    <div class="info-value">{name}</div>
                </div>
                <div class="info-row">
                    <div class="info-label">NIM / Student ID</div>
                    <div class="info-value">{student_id}</div>
                </div>
                <div class="info-row">
                    <div class="info-label">Program Studi</div>
                    <div class="info-value">{major}</div>
                </div>
                <div class="info-row">
                    <div class="info-label">Fakultas</div>
                    <div class="info-value">{faculty}</div>
                </div>
            </div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
            <div><span class="info-label">Status</span><br>AKTIF</div>
            <div><span class="info-label">Semester</span><br>Ganjil 2025/2026</div>
            <div><span class="info-label">SKS</span><br>24</div>
        </div>
        <div class="valid-badge">
            ✓ SURAT KETERANGAN AKTIF MAHASISWA<br>
            Diterbitkan untuk keperluan verifikasi layanan student.<br>
            <strong>Valid hingga: {valid_until}</strong>
        </div>
        <div class="barcode">
            <div>*{student_id}*</div>
            <div style="font-size: 10px;">Barcode Student ID</div>
        </div>
        <div class="stamp">
            Dikeluarkan oleh Sistem Informasi Kampus<br>
            {date}
        </div>
    </div>
</div>
</body>
</html>
"""
    return html


def generate_image(first_name, last_name, school_id='349653'):
    try:
        from playwright.sync_api import sync_playwright

        html_content = generate_html(first_name, last_name, school_id)

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={'width': 600, 'height': 800})
            page.set_content(html_content, wait_until='load')
            page.wait_for_timeout(500)
            screenshot_bytes = page.screenshot(type='png', full_page=True)
            browser.close()

        return screenshot_bytes

    except ImportError:
        raise Exception("Install playwright: pip install playwright && playwright install chromium")
    except Exception as e:
        raise Exception(f"Gagal generate: {str(e)}")


if __name__ == '__main__':
    import sys
    import io

    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("Testing KTM Generator...")
    first_name = "Budi"
    last_name = "Santoso"

    try:
        img_data = generate_image(first_name, last_name)
        with open('test_ktm_ui.png', 'wb') as f:
            f.write(img_data)
        print(f"✓ Berhasil! Size: {len(img_data)} bytes")
        print("✓ Tersimpan sebagai test_ktm_ui.png")
    except Exception as e:
        print(f"✗ Error: {e}")
