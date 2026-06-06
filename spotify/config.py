# SheerID 验证配置文件

# SheerID API 配置
PROGRAM_ID = '63fd266996552d469aea40e1'
SHEERID_BASE_URL = 'https://services.sheerid.com'
MY_SHEERID_URL = 'https://my.sheerid.com'

MAX_FILE_SIZE = 1 * 1024 * 1024

# 学校配置 - UNIVERSITAS INDONESIA
SCHOOLS = {
    '349653': {
        'id': 349653,
        'idExtended': '349653',
        'name': 'Universitas Indonesia',
        'city': 'Depok',
        'state': 'Jawa Barat',
        'country': 'ID',
        'type': 'UNIVERSITY',
        'domain': 'ui.ac.id',
        'latitude': -6.362764,
        'longitude': 106.82705
    },
    '349650': {
        'id': 349650,
        'idExtended': '349650',
        'name': 'Universitas Gadjah Mada',
        'city': 'Yogyakarta',
        'state': 'DI Yogyakarta',
        'country': 'ID',
        'type': 'UNIVERSITY',
        'domain': 'ugm.ac.id',
        'latitude': -7.7715616,
        'longitude': 110.3777
    },
    '349647': {
        'id': 349647,
        'idExtended': '349647',
        'name': 'Universitas Brawijaya',
        'city': 'Malang',
        'state': 'Jawa Timur',
        'country': 'ID',
        'type': 'UNIVERSITY',
        'domain': 'ub.ac.id',
        'latitude': -7.952465,
        'longitude': 112.61368
    },
    '353147': {
        'id': 353147,
        'idExtended': '353147',
        'name': 'Universitas Telkom',
        'city': 'Bandung',
        'state': 'West Java',
        'country': 'ID',
        'type': 'UNIVERSITY',
        'domain': 'telkomuniversity.ac.id',
        'latitude': -6.973007,
        'longitude': 107.63168
    },
    '353834': {
        'id': 353834,
        'idExtended': '353834',
        'name': 'Universitas Tarumanagara',
        'city': 'Jakarta Barat',
        'state': 'DKI Jakarta',
        'country': 'ID',
        'type': 'UNIVERSITY',
        'domain': 'untar.ac.id',
        'latitude': -6.169335,
        'longitude': 106.78859
    }
}

DEFAULT_SCHOOL_ID = '349653'

