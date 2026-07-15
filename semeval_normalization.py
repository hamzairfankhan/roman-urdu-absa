# ============================================================
# SemEval Span Normalization v2
# Three-step normalization:
#   1. Exact dictionary lookup (original 179 entries + 75 new)
#   2. Keyword-based fallback for compound/variant phrases
#   3. Final fallback: 'features'
# ============================================================

SEMEVAL_TO_CATEGORY = {
    # â”€â”€ Battery â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'battery': 'battery life', 'battery life': 'battery life',
    'battery backup': 'battery life', 'battery timing': 'battery life',
    'battery performance': 'battery life', 'power': 'battery life',
    'battery cells': 'battery life', 'battery life of the laptop': 'battery life',
    '12 cell battery': 'battery life', '6 cell battery': 'battery life',
    '9 cell battery': 'battery life', 'battery capacity': 'battery life',

    # â”€â”€ Screen / Display â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'screen': 'screen', 'screen size': 'screen',
    'screen resolution': 'screen', 'screen quality': 'screen',
    'resolution': 'screen', 'screen brightness': 'screen',
    '15"': 'screen', '13"': 'screen', '14"': 'screen', '17"': 'screen',
    '11"': 'screen', '12"': 'screen', '13.3"': 'screen', '15.6"': 'screen',
    '11.6"': 'screen', '13.3 inch': 'screen', '15.6 inch': 'screen',
    '15 inch': 'screen', '17 inch': 'screen', '13 inch': 'screen',
    '14 inch': 'screen', '11 inch': 'screen', '18-inch': 'screen',
    '17-inch screen': 'screen', '17 inch screen': 'screen',
    '17" inch screen': 'screen', '17 ince screen': 'screen',
    '30" hd monitor': 'screen',
    'display': 'display', 'display quality': 'display',
    'brightness': 'display', 'backlight': 'display',
    'color': 'display', 'colours': 'display', 'colors': 'display',
    'color accuracy': 'display', 'color reproduction': 'display',
    'glare': 'display', 'contrast': 'display',

    # â”€â”€ Keyboard / Input â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'keyboard': 'keyboard', 'keys': 'keyboard', 'keypad': 'keyboard',
    'num pad': 'keyboard', 'numpad': 'keyboard', 'number pad': 'keyboard',
    'backlit keyboard': 'keyboard', 'keyboard backlight': 'keyboard',
    'function keys': 'keyboard', 'fn keys': 'keyboard',
    'keyboard feel': 'keyboard', 'keyboard layout': 'keyboard',
    'typing experience': 'keyboard', 'caps lock key': 'keyboard',
    'number keys': 'keyboard', 'num keys': 'keyboard', '10-key': 'keyboard',
    'touchpad': 'touchscreen', 'trackpad': 'touchscreen',
    'touchscreen': 'touchscreen', 'touch screen': 'touchscreen',
    'touch': 'touchscreen', 'pointer': 'touchscreen',
    'cursor': 'touchscreen', 'mouse': 'touchscreen',
    'mouse pad': 'touchscreen', 'mousepad': 'touchscreen',
    'scroll wheel': 'touchscreen', 'stylus': 'touchscreen',
    'trackpad sensitivity': 'touchscreen',

    # â”€â”€ Performance â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'performance': 'performance', 'speed': 'performance',
    'start up': 'performance', 'boot time': 'performance',
    'boot': 'performance', 'startup': 'performance', 'startup time': 'performance',
    'loading': 'performance', 'lag': 'performance', 'freezing': 'performance',
    'processor speed': 'performance', 'boot up': 'performance',
    'boot up time': 'performance', 'gaming performance': 'performance',
    'overall performance': 'performance', 'system performance': 'performance',
    'game performance': 'performance', 'gaming': 'performance',

    # â”€â”€ Processor â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'processor': 'processor', 'cpu': 'processor',
    'chip': 'processor', 'chips': 'processor',
    'amd processor': 'processor', 'intel processor': 'processor',
    'i5 processor': 'processor', 'i7 processor': 'processor',
    'intel core i5': 'processor', 'intel core i7': 'processor',
    'intel core i3': 'processor', 'processor performance': 'processor',

    # â”€â”€ Features / Specs â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'RAM': 'features', 'ram': 'features', 'memory': 'features',
    'hard drive': 'features', 'hard disk': 'features',
    'SSD': 'features', 'storage': 'features',
    'disk': 'features', 'drive': 'features', 'space': 'features',
    'use': 'features', 'usability': 'features',
    'overall': 'features', 'everything': 'features',
    'features': 'features', 'feature': 'features',
    'graphics card': 'features', 'gpu': 'features', 'graphics': 'features',
    'integrated graphics': 'features', 'graphics chip': 'features',
    'optical drive': 'features', 'dvd drive': 'features',
    'cd drive': 'features', 'dvd': 'features',
    'disk space': 'features', 'hard disk space': 'features',
    'storage capacity': 'features', 'memory capacity': 'features',
    'ram capacity': 'features',
    '1 gb ram': 'features', '2 gb ram': 'features', '4 gb ram': 'features',
    '8 gb ram': 'features', '16 gb ram': 'features', '1gb of ram': 'features',
    '2 gb of ram': 'features', '4gb ram': 'features', '8gb ram': 'features',
    '2gb ram stick': 'features', '16gb ram support': 'features',
    '4 gb of ram': 'features', '6 gb ram': 'features', '1gb ram': 'features',

    # â”€â”€ Software â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'software': 'software', 'OS': 'software',
    'operating system': 'software', 'Windows': 'software',
    'programs': 'software', 'apps': 'software',
    'applications': 'software', 'application': 'software',
    'GUI': 'software', 'ui': 'software', 'interface': 'software',
    'setup': 'software', 'installation': 'software',
    'drivers': 'software', 'driver': 'software',
    'update': 'software', 'updates': 'software',
    'crash': 'software', 'crashes': 'software', 'menu': 'software',
    'linux': 'software', 'chrome os': 'software', 'bios': 'software',
    'bloatware': 'software', 'linux support': 'software',
    'microsoft support': 'customer service',
    'web browser': 'software', 'browser': 'software',

    # â”€â”€ Build Quality â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'build quality': 'build quality', 'build': 'build quality',
    'quality': 'build quality', 'construction': 'build quality',
    'durability': 'build quality', 'reliability': 'build quality',
    'cover': 'build quality', 'lid': 'build quality',
    'hinge': 'build quality', 'casing': 'build quality',
    'chassis': 'build quality', 'frame': 'build quality',
    'shell': 'build quality', 'finish': 'build quality',
    'material': 'build quality', 'body': 'build quality',
    'button': 'build quality', 'buttons': 'build quality',
    'power button': 'build quality',

    # â”€â”€ Design â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'design': 'design', 'look': 'design', 'appearance': 'design',
    'size': 'design', 'weight': 'design',
    'left side': 'design', 'right side': 'design',
    'back': 'design', 'front': 'design',
    'portability': 'design', 'portable': 'design',
    'form factor': 'design', 'slim design': 'design',
    'palm rest': 'design', 'wrist rest': 'design',
    'light': 'design', 'lights': 'design',
    'design of the laptop': 'design', 'weight of laptop': 'design',

    # â”€â”€ Connectivity â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'wifi': 'connectivity', 'wireless': 'connectivity',
    'bluetooth': 'connectivity', 'connectivity': 'connectivity',
    'network': 'connectivity', 'internet': 'connectivity',
    'hdmi': 'connectivity', 'ethernet': 'connectivity',
    'usb port': 'connectivity', 'usb ports': 'connectivity',
    'thunderbolt': 'connectivity', 'vga': 'connectivity',
    'sd card': 'connectivity', 'sd slot': 'connectivity',
    'sd card slot': 'connectivity', '3g network': 'connectivity',
    '4g': 'connectivity', '5g': 'connectivity', 'lte': 'connectivity',
    'bluetooth connectivity': 'connectivity',
    'data transfer': 'connectivity', 'data transfer speed': 'connectivity',
    'transfer speed': 'connectivity', 'wireless performance': 'connectivity',
    'wifi reception': 'connectivity', 'dell support': 'customer service',

    # â”€â”€ Speaker / Audio â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'speakers': 'speaker', 'speaker': 'speaker', 'volume': 'speaker',
    'left speaker': 'sound quality', 'right speaker': 'sound quality',
    'sound': 'sound quality', 'sound quality': 'sound quality',
    'audio': 'sound quality', 'microphone': 'sound quality',
    'mic': 'sound quality', 'headphone jack': 'sound quality',
    'jack': 'sound quality', 'sound system': 'sound quality',
    'bass': 'sound quality',

    # â”€â”€ Price â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'price': 'price', 'cost': 'price', 'value': 'price',
    'value for money': 'price', 'price point': 'price', 'price tag': 'price',

    # â”€â”€ Customer Service â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'customer service': 'customer service', 'service': 'customer service',
    'support': 'customer service', 'tech support': 'customer service',
    'service center': 'customer service', 'sales team': 'customer service',
    'tech guy': 'customer service', 'sales': 'customer service',
    'store': 'customer service', 'shop': 'customer service',
    'seller': 'customer service', 'customer support': 'customer service',
    'sales staff': 'customer service', 'staff': 'customer service',
    '"sales" team': 'customer service', 'apple support': 'customer service',
    'hp support': 'customer service', 'lenovo support': 'customer service',

    # â”€â”€ Charger / Power â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'charger': 'charger', 'adapter': 'charger',
    'power supply': 'charger', 'power adapter': 'charger',
    'port': 'charger', 'ports': 'charger', 'ac adapter': 'charger',
    'power brick': 'charger', 'magsafe': 'charger',
    'magsafe connector': 'charger',

    # â”€â”€ Charging Speed â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'charging': 'charging speed', 'charging speed': 'charging speed',
    'charging time': 'charging speed', 'charge time': 'charging speed',
    'charge speed': 'charging speed',

    # â”€â”€ Cable â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'cable': 'cable', 'cord': 'cable',
    'power cord': 'cable', 'usb': 'cable', 'usb cable': 'cable',

    # â”€â”€ Laptop (device) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'laptop': 'laptop', 'computer': 'laptop', 'machine': 'laptop',
    'netbook': 'laptop', 'notebook': 'laptop', 'macbook': 'laptop',
    'chromebook': 'laptop', 'ultrabook': 'laptop', 'pc': 'laptop',
    'unit': 'laptop', 'system': 'laptop', 'laptop body': 'laptop',

    # â”€â”€ Phone / General Device â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'device': 'phone', 'product': 'phone', 'tablet': 'phone',

    # â”€â”€ Camera â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'camera': 'camera', 'webcam': 'camera', 'web cam': 'camera',
    'front camera': 'camera', 'rear camera': 'camera',
    'back camera': 'camera', 'image quality': 'camera',
    'picture quality': 'camera', 'built in camera': 'camera',
    'video quality': 'camera',

    # â”€â”€ Heating / Thermal â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'heating': 'heating', 'heat': 'heating', 'temperature': 'heating',
    'fan': 'heating', 'vent': 'heating', 'vents': 'heating',
    'cooling': 'heating', 'heat sink': 'heating',
    'cooling system': 'heating', 'thermal management': 'heating',
    'fan noise': 'heating', 'heat management': 'heating',
    'ventilation': 'heating', 'venting': 'heating',

    # â”€â”€ Warranty â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'warranty': 'warranty', 'guarantee': 'warranty',
    '1-year-warranty': 'warranty', '3 year warranty': 'warranty',
    '1 year warranty': 'warranty', '2 year warranty': 'warranty',

    # â”€â”€ Packaging â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'packaging': 'packaging', 'box': 'packaging', 'packing': 'packaging',

    # â”€â”€ Delivery â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    'delivery': 'delivery', 'shipping': 'delivery',
}


# â”€â”€ Keyword-based fallback â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# First match wins. More specific keywords first.

KEYWORD_RULES = [
    (['battery', 'batteries', 'mah'],                            'battery life'),
    (['ghz', 'intel', 'amd', 'ryzen', 'celeron', 'pentium',
      'snapdragon', 'mediatek', 'helio', 'exynos',
      'i3', 'i5', 'i7', 'i9', 'cpu'],                           'processor'),
    (['windows', 'linux', 'android', 'ios', 'bios',
      'bloatware', 'driver', 'drivers'],                         'software'),
    (['keyboard', 'keys', 'key', 'numpad', 'keycap',
      'typing', '10-key'],                                       'keyboard'),
    (['touchpad', 'trackpad', 'touchscreen', 'stylus'],          'touchscreen'),
    (['wifi', 'wi-fi', 'bluetooth', 'hdmi', 'ethernet',
      'thunderbolt', 'usb', 'slot', 'vga', '3g', '4g',
      '5g', 'lte', 'nfc', 'sd'],                                 'connectivity'),
    (['speaker', 'audio', 'sound', 'bass', 'treble',
      'microphone', 'mic', 'headphone', 'headset',
      'earphone', 'jack'],                                        'sound quality'),
    (['camera', 'webcam', 'megapixel', 'lens'],                   'camera'),
    (['hinge', 'chassis', 'casing', 'plastic', 'metal',
      'aluminum', 'magnesium', 'durability', 'sturdy',
      'flimsy'],                                                   'build quality'),
    (['heat', 'heating', 'hot', 'thermal', 'cooling',
      'overheat', 'fan', 'ventilation'],                          'heating'),
    (['warranty', 'guarantee'],                                   'warranty'),
    (['price', 'cost', 'value', 'money', 'worth',
      'expensive', 'cheap', 'affordable'],                        'price'),
    (['service', 'support', 'staff', 'sales', 'seller',
      'customer'],                                                'customer service'),
    (['charger', 'adapter', 'magsafe', 'ac'],                     'charger'),
    (['charging'],                                                'charging speed'),
    (['weight', 'portable', 'portability', 'slim',
      'thin', 'design'],                                          'design'),
    (['ram', 'gb', 'tb', 'mb', 'ssd', 'hdd', 'memory',
      'storage', 'hard', 'flash', 'nvme', 'emmc',
      'graphics', 'gpu', 'dvd', 'optical'],                       'features'),
    (['inch', '"', 'screen', 'lcd', 'led', 'oled',
      'retina', 'pixel', 'resolution', 'fhd', 'hd',
      '4k', '1080', '720', 'ips'],                                'screen'),
    (['display', 'brightness', 'backlight', 'color',
      'colour', 'glare'],                                         'display'),
    (['laptop', 'computer', 'notebook', 'netbook',
      'ultrabook', 'macbook', 'chromebook', 'machine'],           'laptop'),
    (['speed', 'performance', 'fast', 'slow', 'lag',
      'boot', 'startup', 'load', 'freeze', 'hang',
      'smooth', 'gaming'],                                        'performance'),
]


def _keyword_fallback(span_lower):
    tokens = set(span_lower.replace('-', ' ').replace('"', ' inch').split())
    for keywords, category in KEYWORD_RULES:
        if any(kw in tokens for kw in keywords):
            return category
    return None


def normalize_semeval_spans(df):
    df = df.copy()
    def map_span(span):
        s = str(span).lower().strip()
        if s in SEMEVAL_TO_CATEGORY:
            return SEMEVAL_TO_CATEGORY[s]
        kw = _keyword_fallback(s)
        if kw:
            return kw
        return 'features'
    df['span'] = df['span'].apply(map_span)
    return df


def validate_normalization(original_df, normalized_df):
    original_spans  = set(original_df['span'].str.lower().unique())
    normalized_spans = set(normalized_df['span'].unique())
    still_fallback   = [
        s for s in original_spans
        if s not in SEMEVAL_TO_CATEGORY and _keyword_fallback(s.lower()) is None
    ]
    print(f"Original unique spans:    {len(original_spans)}")
    print(f"Normalized unique spans:  {len(normalized_spans)}")
    print(f"Spans using final fallback ('features'): {len(still_fallback)}")
    if still_fallback:
        print(f"  Examples: {sorted(still_fallback)[:10]}")
    print(f"\nFinal category distribution:")
    print(normalized_df['span'].value_counts())
    return normalized_df

