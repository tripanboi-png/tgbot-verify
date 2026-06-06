"""PNG 学生证生成模块 - ZAMZZZ EDITION (UNIVERSITAS INDONESIA)"""
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
    Parameter first_name, last_name DIABAIKAN!
    """
    # Generate username random (huruf kecil + angka)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    
    # PAKSA PAKE GMAIL!
    return f"{username}@gmail.com"


# Aliase untuk kompatibilitas dengan code lama yang panggil generate_psu_email
generate_psu_email = generate_email


def generate_html(first_name, last_name, school_id='349653'):
    """
    生成 Universitas Indonesia Student Portal HTML

    Args:
        first_name: 名字
        last_name: 姓氏
        school_id: 学校 ID (default: UI)

    Returns:
        str: HTML 内容
    """
    student_id = generate_student_id()
    name = f"{first_name} {last_name}"
    date = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')

    # Daftar prodi Indonesia
    majors = [
        'Teknik Informatika (S1)',
        'Sistem Informasi (S1)',
        'Teknik Komputer (S1)',
        'Manajemen Informatika (D3)',
        'Ilmu Komputer (S1)',
        'Teknik Elektro (S1)',
        'Bisnis Digital (S1)'
    ]
    major = random.choice(majors)
    
    # Daftar fakultas
    faculties = ['Fakultas Ilmu Komputer', 'Fakultas Teknik', 'Fakultas Ekonomi dan Bisnis']
    faculty = random.choice(faculties)

    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SIKADU - Portal Mahasiswa</title>
    <style>
        :root {{
            --ui-red: #FF6600;
            --ui-dark: #800000;
            --bg-gray: #f4f4f4;
            --text-color: #333;
        }}

        body {{
            font-family: "Segoe UI", "Roboto", "Helvetica Neue", Arial, sans-serif;
            background-color: #e0e0e0;
            margin: 0;
            padding: 20px;
            color: var(--text-color);
            display: flex;
            justify-content: center;
        }}

        .viewport {{
            width: 100%;
            max-width: 1100px;
            background-color: #fff;
            box-shadow: 0 5px 20px rgba(0,0,0,0.15);
            min-height: 800px;
            display: flex;
            flex-direction: column;
        }}

        .header {{
            background-color: var(--ui-red);
            color: white;
            padding: 0 20px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .brand {{
            display: flex;
            align-items: center;
            gap: 15px;
        }}

        .uni-logo {{
            font-family: "Georgia", serif;
            font-size: 18px;
            font-weight: bold;
            letter-spacing: 1px;
            border-right: 1px solid rgba(255,255,255,0.3);
            padding-right: 15px;
        }}

        .system-name {{
            font-size: 16px;
            font-weight: 300;
        }}

        .user-menu {{
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 20px;
        }}

        .nav-bar {{
            background-color: #f8f8f8;
            border-bottom: 1px solid #ddd;
            padding: 10px 20px;
            font-size: 13px;
            color: #666;
            display: flex;
            gap: 20px;
        }}
        .nav-item {{ cursor: pointer; }}
        .nav-item.active {{ color: var(--ui-red); font-weight: bold; border-bottom: 2px solid var(--ui-red); padding-bottom: 8px; }}

        .content {{
            padding: 30px;
            flex: 1;
        }}

        .page-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            margin-bottom: 20px;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }}

        .page-title {{
            font-size: 24px;
            color: var(--ui-red);
            margin: 0;
        }}

        .term-selector {{
            background: #fff;
            border: 1px solid #ccc;
            padding: 5px 10px;
            border-radius: 4px;
            font-size: 14px;
            color: #333;
            font-weight: bold;
        }}

        .student-card {{
            background: #fcfcfc;
            border: 1px solid #e0e0e0;
            padding: 15px;
            margin-bottom: 25px;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            font-size: 13px;
        }}
        .info-label {{ color: #777; font-size: 11px; text-transform: uppercase; margin-bottom: 4px; }}
        .info-val {{ font-weight: bold; color: #333; font-size: 14px; }}
        .status-badge {{
            background-color: #e6fffa; color: #007a5e;
            padding: 4px 8px; border-radius: 4px; font-weight: bold; border: 1px solid #b2f5ea;
        }}

        .schedule-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
        }}

        .schedule-table th {{
            text-align: left;
            padding: 12px;
            background-color: #f0f0f0;
            border-bottom: 2px solid #ccc;
            color: #555;
        }}

        .schedule-table td {{
            padding: 15px 12px;
            border-bottom: 1px solid #eee;
        }}

        .course-code {{ font-weight: bold; color: var(--ui-red); }}
        .course-title {{ font-weight: 500; }}

        @media print {{
            body {{ background: white; padding: 0; }}
            .viewport {{ box-shadow: none; max-width: 100%; min-height: auto; }}
            .nav-bar {{ display: none; }}
            @page {{ margin: 1cm; size: landscape; }}
        }}
    </style>
</head>
<body>

<div class="viewport">
    <div class="header">
        <div class="brand">
            <div class="uni-logo">UNIVERSITAS INDONESIA</div>
            <div class="system-name">SIKADU - Portal Mahasiswa</div>
        </div>
        <div class="user-menu">
            <span>Selamat Datang, <strong>{name}</strong></span>
            <span>|</span>
            <span>Keluar</span>
        </div>
    </div>

    <div class="nav-bar">
        <div class="nav-item">Beranda</div>
        <div class="nav-item active">Jadwal Kuliah</div>
        <div class="nav-item">Akademik</div>
        <div class="nav-item">Keuangan</div>
        <div class="nav-item">Kemahasiswaan</div>
    </div>

    <div class="content">
        <div class="page-header">
            <h1 class="page-title">Jadwal Kuliah Semester Ganjil 2025/2026</h1>
            <div class="term-selector">
                Semester: <strong>Ganjil 2025/2026</strong> (Agustus - Desember)
            </div>
        </div>

        <div class="student-card">
            <div>
                <div class="info-label">Nama Mahasiswa</div>
                <div class="info-val">{name}</div>
            </div>
            <div>
                <div class="info-label">NIM</div>
                <div class="info-val">{student_id}</div>
            </div>
            <div>
                <div class="info-label">Program Studi</div>
                <div class="info-val">{major}</div>
            </div>
            <div>
                <div class="info-label">Fakultas</div>
                <div class="info-val">{faculty}</div>
            </div>
        </div>

        <div style="margin-bottom: 10px; font-size: 12px; color: #666; text-align: right;">
            Data diambil: <span>{date}</span>
        </div>

        <table class="schedule-table">
            <thead>
                <tr>
                    <th width="10%">Kode</th>
                    <th width="15%">Mata Kuliah</th>
                    <th width="35%">Nama Mata Kuliah</th>
                    <th width="20%">Hari & Jam</th>
                    <th width="10%">Ruangan</th>
                    <th width="10%">SKS</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>CSIK6023</td>
                    <td class="course-code">Algoritma dan Pemrograman</td>
                    <td class="course-title">Dasar-dasar Pemrograman</td>
                    <td>Senin 08:00 - 10:30</td>
                    <td>Ruang 301</td>
                    <td>3</td>
                </tr>
                <tr>
                    <td>CSIK6045</td>
                    <td class="course-code">Struktur Data</td>
                    <td class="course-title">Pemrograman Lanjut</td>
                    <td>Selasa 10:00 - 12:30</td>
                    <td>Lab Komputer A</td>
                    <td>3</td>
                </tr>
                <tr>
                    <td>CSIK6012</td>
                    <td class="course-code">Basis Data</td>
                    <td class="course-title">Sistem Manajemen Basis Data</td>
                    <td>Rabu 13:00 - 15:30</td>
                    <td>Ruang 205</td>
                    <td>3</td>
                </tr>
                <tr>
                    <td>CSIK6078</td>
                    <td class="course-code">Pemrograman Web</td>
                    <td class="course-title">Pengembangan Aplikasi Web</td>
                    <td>Kamis 08:00 - 10:30</td>
                    <td>Lab Web</td>
                    <td>3</td>
                </tr>
                <tr>
                    <td>CSIK6090</td>
                    <td class="course-code">Rekayasa Perangkat Lunak</td>
                    <td class="course-title">Metodologi Pengembangan Sistem</td>
                    <td>Jumat 13:00 - 15:30</td>
                    <td>Ruang 102</td>
                    <td>3</td>
                </tr>
            </tbody>
        </table>

        <div style="margin-top: 50px; border-top: 1px solid #ddd; padding-top: 10px; font-size: 11px; color: #888; text-align: center;">
            &copy; 2025 Universitas Indonesia. Semua hak dilindungi.<br>
            SIKADU - Sistem Informasi Kampus Terpadu
        </div>
    </div>
</div>

</body>
</html>
"""

    return html


def generate_image(first_name, last_name, school_id='349653'):
    """
    生成 Universitas Indonesia SIKADU screenshot PNG

    Args:
        first_name: 名字
        last_name: 姓氏
        school_id: 学校 ID (default: UI)

    Returns:
        bytes: PNG 图片数据
    """
    try:
        from playwright.sync_api import sync_playwright

        # 生成 HTML
        html_content = generate_html(first_name, last_name, school_id)

        # 使用 Playwright 截图
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={'width': 1200, 'height': 900})
            page.set_content(html_content, wait_until='load')
            page.wait_for_timeout(500)
            screenshot_bytes = page.screenshot(type='png', full_page=True)
            browser.close()

        return screenshot_bytes

    except ImportError:
        raise Exception("需要安装 playwright: pip install playwright && playwright install chromium")
    except Exception as e:
        raise Exception(f"生成图片失败: {str(e)}")


if __name__ == '__main__':
    # 测试代码
    import sys
    import io

    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("测试 SIKADU 图片生成 (Universitas Indonesia)...")

    first_name = "Budi"
    last_name = "Santoso"

    print(f"Nama: {first_name} {last_name}")
    print(f"NIM: {generate_student_id()}")
    print(f"Email: {generate_email(first_name, last_name)}")

    try:
        img_data = generate_image(first_name, last_name)

        with open('test_ui_card.png', 'wb') as f:
            f.write(img_data)

        print(f"✓ Gambar berhasil! Size: {len(img_data)} bytes")
        print(f"✓ Tersimpan sebagai test_ui_card.png")

    except Exception as e:
        print(f"✗ Error: {e}")
