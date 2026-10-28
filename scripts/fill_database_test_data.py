import os
import random

# Путь к файлу результата
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_SQL_PATH = os.path.join(BASE_DIR, "database", "init", "generated_test_data.sql")

# Теперь можно смело ставить любое количество строк без риска дубликатов
COUNTS = {
    'E1': 100,
    'E2': 100, 
    'E3': 100,
    'E4': 100,
    'E5': 100,
    'E6': 100, 
    'E7': 100, 
    'E8': 100, 
    'E9': 100, 
    'E10': 100,
    'E11': 100, 
    'E12': 100, 
    'E13': 100, 
    'E14': 100, 
    'E15': 100,
    'E16': 100, 
    'E17': 100, 
    'E18': 100, 
    'E19': 100, 
    'E20': 100, 
    'E21': 100
}

# Расширенные статические пулы данных для всех сущностей (E1 - E18)

POOLS_E1 = {
    "comp_name": [
        "Core i7-14700K", "Ryzen 7 7800X3D", "RTX 4070 OC", "RX 7800 XT", "Fury Beast 32GB", 
        "Vengeance 32GB", "990 PRO 1TB", "SN850X 1TB", "PK750D 750W", "RM850x 850W",
        "Core i5-13600K", "Ryzen 5 7600X", "RTX 4080 Super", "RX 7900 XTX", "Dominator Platinum",
        "Trident Z5 RGB", "T700 2TB", "P5 Plus 2TB", "HX1000i 1000W", "System Power 10",
        "Pure Power 12 M", "TUF Gaming Z790", "ROG Strix X670E", "MAG B650 Tomahawk", "PRIME H610M-E",
        "MP500 CPU Cooler", "AK620 Digital", "Peerless Assassin 120", "Liquid Freezer III 360", "H6 Flow RGB",
        "Lancool 216", "North Charcoal", "O11 Dynamic EVO", "Odyssey G7", "TUF Gaming VG27AQ",
        "UltraGear 27GP850", "BlackWidow V4", "DeathAdder V3", "G Pro X Superlight", "K70 MAX",
        "Apex Pro TKL", "Cloud III Wireless", "Virtuoso RGB", "Huntsman V3 Pro", "G915 Lightspeed",
        "Basilisk V3 Pro", "Viper V2 Pro", "Pro X TKL", "Ornata V3", "Cynosa V2"
    ],
    "manufacturer": [
        "Intel", "AMD", "NVIDIA", "Kingston", "Corsair", "Samsung", "WD", "DeepCool", "MSI", "Gigabyte",
        "ASUS", "AsRock", "BeQuiet", "Seasonic", "Toshiba", "Crucial", "G.Skill", "Thermalright", "Arctic", "NZXT",
        "Lian Li", "Fractal Design", "Samsung", "LG", "AOC", "Razer", "Logitech", "SteelSeries", "HyperX", "Corsair",
        "Intel", "AMD", "NVIDIA", "Kingston", "Corsair", "Samsung", "WD", "DeepCool", "MSI", "Gigabyte",
        "ASUS", "AsRock", "BeQuiet", "Seasonic", "Toshiba", "Crucial", "G.Skill", "Thermalright", "Arctic", "NZXT"
    ],
    "price": [round(5000.0 + i * 45.5, 2) for i in range(1000)], # 1000 числовых вариантов
    "warranty_period": [12, 24, 36, 60, 120, 12, 24, 36, 60, 12, 24, 36, 60, 12, 24, 36, 60, 12, 24, 36, 60, 12, 24, 36, 60, 12, 24, 36, 60, 12, 24, 36, 60, 12, 24, 36, 60, 12, 24, 36, 60, 12, 24, 36, 60, 12, 24, 36, 60, 12]
}

POOLS_E2 = {
    "cat_name": [f"Категория оборудования №{i}" for i in range(1, 51)],
    "cat_description": [f"Техническое описание спецификации и группы устройств #{i} для сборки" for i in range(1, 51)]
}

POOLS_E3 = {
    "value_type": ["TEXT", "NUMERIC", "TEXT", "NUMERIC", "TEXT", "NUMERIC", "TEXT", "NUMERIC", "TEXT", "NUMERIC"],
    "charac_name": [f"Параметр характеристики элемента конфигурации {i}" for i in range(1, 51)],
    "is_required": [True, False, True, True, False, True, False, True, False, True],
    "unit": [None, "MB", "MHz", "W", "mm", "kg", "V", "A", "GHz", None]
}

POOLS_E5 = {
    "comp_name": [f"RULE_COMPATIBILITY_CHECK_UNIT_{i}" for i in range(1, 51)],
    "argument_1": ["socket", "memory_type", "total_tdp", "pci_version", "m2_slots", "freq", "vram", "power", "slots", "size"],
    "comparator": ["=", "<=", ">=", "=", "<", ">", "!=", "=", "<=", ">="],
    "argument_2": ["socket", "memory_type", "max_power", "pci_version", "m2_slots", "freq", "vram", "power", "slots", "size"],
    "comp_status": ["active", "deprecated", "draft", "active", "active", "deprecated", "active", "draft", "active", "active"]
}

POOLS_E6 = {
    "sup_name": [f"ООО Поставщик-Партнер Техно Групп #{i}" for i in range(1, 51)],
    "contact_info": [f"b2b_sales_department_code_{i}@hardware-store.ru" for i in range(1, 51)],
    "requisites": [f"ИНН 77{i:08d} ОГРН 1157746{i:05d}" for i in range(1, 1000)], # 1000 вариантов
    "sup_status": ["active", "active", "active", "inactive", "blacklisted", "active", "active", "inactive", "active", "active"]
}

POOLS_E7 = {
    "responsible_person": [f"Старший логист смены складского комплекса №{i}" for i in range(1, 51)],
    "sup_status": ["created", "in_transit", "delivered", "cancelled", "delivered", "created", "delivered", "in_transit", "delivered", "created"],
    "sup_comment": [None] + [f"Партия груза оформлена штатно по транспортной накладной #{i}" for i in range(1, 51)]
}

POOLS_E8 = {
    "batch_status": ["received", "depleted", "written_off", "received", "received", "depleted", "received", "received", "received", "written_off"]
}

POOLS_E9 = {
    "exemp_location": [f"Складской распределительный комплекс Юг, Зона {chr(65 + i%5)}, Стеллаж Ряд-{i}" for i in range(1, 51)],
    "exemp_status": ["in_stock", "reserved", "sold", "defective", "written_off", "in_stock", "sold", "reserved", "in_stock", "defective"]
}

POOLS_E10 = {
    "responsible_person": [f"Менеджер отдела по работе с клиентами №{i}" for i in range(1, 51)],
    "cust_status": ["new", "processing", "assembled", "completed", "cancelled", "new", "processing", "completed", "assembled", "new"],
    "cust_comment": [None] + [f"Самовывоз клиентом со склада после предварительной проверки заказа #{i}" for i in range(1, 51)],
    "customer_name": [f"Покупатель Физическое Лицо Профиль №{i}" for i in range(1, 51)],
    "contact_info": [f"client_corporate_mail_box_{i}@yandex.ru" for i in range(1, 51)]
}

POOLS_E11 = {
    "component_list": [f'{{"config_node_id": {i}, "status": "verified", "tier": "high-end"}}' for i in range(1, 51)],
    "build_status": ["draft", "verified", "approved", "assembled", "archived", "draft", "verified", "approved", "assembled", "archived"],
    "compatibility_check_result": ['{"ok": true}', '{"ok": false}', '{"ok": true}', '{"ok": true}', '{"ok": false}']
}

POOLS_E13 = {
    "exemp_status": ["active", "expired", "fulfilled", "cancelled", "active", "active", "fulfilled", "expired", "active", "cancelled"]
}

POOLS_E14 = {
    "installed_components": ['{"cpu": true, "gpu": true, "ram": true, "psu": true}', '{"status": "fully_mounted"}'],
    "assembler": [f"Сертифицированный инженер-сборщик ПК лаборатории №{i}" for i in range(1, 51)],
    "build_status": ["in_progress", "assembled", "testing_passed", "testing_failed", "completed"],
    "build_comment": [None] + [f"Сборка протестирована на стенде, параметры стабильны, код проверки #{i}" for i in range(1, 51)]
}

POOLS_E15 = {
    "test_status": ["pending", "running", "passed", "failed", "error", "passed", "passed", "running", "passed", "passed"],
    "build_comment": [None] + [f"Стресс-тест стабильности пройден с запасом по температуре чипа #{i}" for i in range(1, 51)]
}

POOLS_E16 = {
    "test_name": [f"Benchmark Diagnostic Stress Suite Profile v{i}.0 Ultimate Edition" for i in range(1, 51)],
    "test_status": ["pending", "passed", "failed", "skipped", "warning", "passed", "passed", "passed", "passed", "passed"]
}

POOLS_E17 = {
    "customer_name": [f"Заказчик Розничной Сети Покупатель #{i}" for i in range(1, 51)],
    "responsible_person": [f"Менеджер оформления финансовых документов №{i}" for i in range(1, 51)],
    "sale_status": ["completed", "completed", "completed", "completed", "completed", "completed", "completed", "completed", "completed", "completed"]
}

POOLS_E18 = {
    "warr_description": [f"Дефект аппаратного узла подсистемы питания или графического чипа код рекламации #{i}" for i in range(1, 51)],
    "warranty_terms": [f"Расширенный гарантийный сервисный сертификат сроком действия {i} месяцев" for i in range(1, 51)],
    "warr_status": ["open", "in_progress", "resolved", "rejected", "closed", "open", "in_progress", "resolved", "closed", "open"],
    "reason": [f"Отказ элемента силовой схемы из-за скачка напряжения в сети, кейс #{i}" for i in range(1, 51)],
    "customer_name": [f"Заявитель Претензии Клиент #{i}" for i in range(1, 51)]
}

def esc(val):
    if val is None:
        return "NULL"
    if isinstance(val, str):
        return f"'{val.replace('\'', '\'\'')}'"
    return str(val)

# ==========================================
# ФУНКЦИИ ГЕНЕРАЦИИ С ДИНАМИЧЕСКИМИ UNIQUE ПОЛЯМИ
# ==========================================

def generate_E1_row(i):
    cat_id = ((i - 1) % COUNTS['E2']) + 1
    articul = f"ART-{i:05d}" # Гарантированно уникально
    name = POOLS_E1["comp_name"][(i - 1) % len(POOLS_E1["comp_name"])]
    mfr = POOLS_E1["manufacturer"][(i - 1) % len(POOLS_E1["manufacturer"])]
    price = POOLS_E1["price"][(i - 1) % len(POOLS_E1["price"])] + (i * 10)
    warr = POOLS_E1["warranty_period"][(i - 1) % len(POOLS_E1["warranty_period"])]
    return f"({i}, {cat_id}, '{articul}', '{name} #{i}', '{mfr}', {price}, {warr})"

def generate_E2_row(i):
    parent = None if i <= 5 else ((i - 6) % 5) + 1
    parent_val = parent if parent is not None else "NULL"
    cat_code = f"CAT-{i:03d}" # Уникальный код категории
    name = POOLS_E2["cat_name"][(i - 1) % len(POOLS_E2["cat_name"])]
    desc = POOLS_E2["cat_description"][(i - 1) % len(POOLS_E2["cat_description"])]
    return f"({i}, {parent_val}, '{cat_code}', '{name} {i}', '{desc}')"

def generate_E3_row(i):
    cat_id = ((i - 1) % COUNTS['E2']) + 1
    vtype = POOLS_E3["value_type"][(i - 1) % len(POOLS_E3["value_type"])]
    cname = POOLS_E3["charac_name"][(i - 1) % len(POOLS_E3["charac_name"])]
    req = str(POOLS_E3["is_required"][(i - 1) % len(POOLS_E3["is_required"])]).upper()
    unit = POOLS_E3["unit"][(i - 1) % len(POOLS_E3["unit"])]
    unit_val = esc(unit) if unit is not None else "NULL"
    return f"({i}, {cat_id}, '{vtype}', '{cname} #{i}', {req}, {unit_val})"

def generate_E4_row(i):
    m_id = ((i - 1) % COUNTS['E1']) + 1
    c_id = ((i - 1) % COUNTS['E3']) + 1
    val = round(100.0 + i * 1.5, 3)
    return f"({m_id}, {c_id}, {val})"

def generate_E5_row(i):
    cat_id = ((i - 1) % COUNTS['E2']) + 1
    cname = POOLS_E5["comp_name"][(i - 1) % len(POOLS_E5["comp_name"])]
    arg1 = POOLS_E5["argument_1"][(i - 1) % len(POOLS_E5["argument_1"])]
    comp = POOLS_E5["comparator"][(i - 1) % len(POOLS_E5["comparator"])]
    arg2 = POOLS_E5["argument_2"][(i - 1) % len(POOLS_E5["argument_2"])]
    rel_cat = ((i + 1) % COUNTS['E2']) + 1
    status = POOLS_E5["comp_status"][(i - 1) % len(POOLS_E5["comp_status"])]
    return f"({i}, {cat_id}, '{cname}_{i}', '{arg1}', '{comp}', '{arg2}', {rel_cat}, '{status}', '2026-01-01'::date, NULL, NULL)"

def generate_E6_row(i):
    name = POOLS_E6["sup_name"][(i - 1) % len(POOLS_E6["sup_name"])]
    info = POOLS_E6["contact_info"][(i - 1) % len(POOLS_E6["contact_info"])]
    reqs = f"ИНН 77{i:08d}" # Уникальные реквизиты/ИНН
    status = POOLS_E6["sup_status"][(i - 1) % len(POOLS_E6["sup_status"])]
    return f"({i}, '{name} #{i}', '{info}', '{reqs}', '{status}')"

def generate_E7_row(i):
    sup_id = ((i - 1) % COUNTS['E6']) + 1
    cost = 100000 + i * 5000
    resp = POOLS_E7["responsible_person"][(i - 1) % len(POOLS_E7["responsible_person"])]
    status = POOLS_E7["sup_status"][(i - 1) % len(POOLS_E7["sup_status"])]
    return f"({i}, {sup_id}, '2026-03-01'::date, {cost}, '{resp}', '{status}', 'Поставка #{i}')"

def generate_E8_row(i):
    m_id = ((i - 1) % COUNTS['E1']) + 1
    sup_id = ((i - 1) % COUNTS['E7']) + 1
    qty = 50
    status = POOLS_E8["batch_status"][(i - 1) % len(POOLS_E8["batch_status"])]
    price = 20000.0 + i * 100
    return f"({i}, {m_id}, {sup_id}, '2026-03-02'::date, {qty}, '{status}', {price}, {qty})"

def generate_E9_row(i):
    batch_id = ((i - 1) % COUNTS['E8']) + 1
    serial = f"SN-{1000000 + i}" # Уникальный серийный номер
    loc = POOLS_E9["exemp_location"][(i - 1) % len(POOLS_E9["exemp_location"])]
    status = POOLS_E9["exemp_status"][(i - 1) % len(POOLS_E9["exemp_status"])]
    return f"({i}, {batch_id}, '{serial}', '2026-03-03'::date, '{loc}', '{status}')"

def generate_E10_row(i):
    cfg_id = ((i - 1) % COUNTS['E11']) + 1
    cust_num = f"ORD-{i:05d}" # Уникальный номер заказа
    resp = POOLS_E10["responsible_person"][(i - 1) % len(POOLS_E10["responsible_person"])]
    cost = 75000 + i * 1000
    status = POOLS_E10["cust_status"][(i - 1) % len(POOLS_E10["cust_status"])]
    name = POOLS_E10["customer_name"][(i - 1) % len(POOLS_E10["customer_name"])]
    contact = POOLS_E10["contact_info"][(i - 1) % len(POOLS_E10["contact_info"])]
    return f"({i}, {cfg_id}, '{cust_num}', '2026-05-01'::date, '{resp}', {cost}, '{status}', NULL, '{name} #{i}', '{contact}')"

def generate_E11_row(i):
    prev = None if i <= 10 else i - 10
    prev_val = prev if prev is not None else "NULL"
    clist = POOLS_E11["component_list"][(i - 1) % len(POOLS_E11["component_list"])]
    status = POOLS_E11["build_status"][(i - 1) % len(POOLS_E11["build_status"])]
    ref = f"REF-{i:05d}" # Уникальная ссылка
    chk = POOLS_E11["compatibility_check_result"][(i - 1) % len(POOLS_E11["compatibility_check_result"])]
    return f"({i}, {prev_val}, '{clist}', '{status}', '{ref}', '{chk}')"

def generate_E12_row(i):
    cfg_id = ((i - 1) % COUNTS['E11']) + 1
    model_id = ((i - 1) % COUNTS['E1']) + 1
    return f"({i}, {cfg_id}, {model_id})"

def generate_E13_row(i):
    ex_id = ((i - 1) % COUNTS['E9']) + 1
    comp_id = ((i - 1) % COUNTS['E12']) + 1
    order_id = ((i - 1) % COUNTS['E10']) + 1
    status = POOLS_E13["exemp_status"][(i - 1) % len(POOLS_E13["exemp_status"])]
    return f"({i}, {ex_id}, {comp_id}, {order_id}, '2026-05-02'::date, 7, '{status}')"

def generate_E14_row(i):
    cfg_id = ((i - 1) % COUNTS['E11']) + 1
    bld_num = f"BLD-{i:05d}" # Уникальный номер сборки
    comps = POOLS_E14["installed_components"][(i - 1) % len(POOLS_E14["installed_components"])]
    asm = POOLS_E14["assembler"][(i - 1) % len(POOLS_E14["assembler"])]
    status = POOLS_E14["build_status"][(i - 1) % len(POOLS_E14["build_status"])]
    return f"({i}, {cfg_id}, '{bld_num}', '2026-05-03'::date, '{comps}', '{asm}', NULL, '{status}', NULL)"

def generate_E15_row(i):
    bld_id = ((i - 1) % COUNTS['E14']) + 1
    status = POOLS_E15["test_status"][(i - 1) % len(POOLS_E15["test_status"])]
    return f"({i}, {bld_id}, '{status}', NULL, '2026-05-04'::date)"

def generate_E16_row(i):
    test_id = ((i - 1) % COUNTS['E15']) + 1
    tname = POOLS_E16["test_name"][(i - 1) % len(POOLS_E16["test_name"])]
    status = POOLS_E16["test_status"][(i - 1) % len(POOLS_E16["test_status"])]
    return f"({i}, {test_id}, '{tname} #{i}', '2026-05-04'::date, '{status}')"

def generate_E17_row(i):
    order_id = ((i - 1) % COUNTS['E10']) + 1
    build_id = ((i - 1) % COUNTS['E14']) + 1
    sale_num = f"SALE-{i:05d}" # Уникальный номер продажи
    name = POOLS_E17["customer_name"][(i - 1) % len(POOLS_E17["customer_name"])]
    cost = 80000.0 + i * 1200
    resp = POOLS_E17["responsible_person"][(i - 1) % len(POOLS_E17["responsible_person"])]
    status = POOLS_E17["sale_status"][(i - 1) % len(POOLS_E17["sale_status"])]
    return f"({i}, {order_id}, {build_id}, '{sale_num}', '2026-05-05'::date, '{name}', {cost}, '{resp}', '{status}')"

def generate_E18_row(i):
    sale_id = ((i - 1) % COUNTS['E17']) + 1
    build_id = ((i - 1) % COUNTS['E14']) + 1
    ex_id = ((i - 1) % COUNTS['E9']) + 1
    warr_num = f"WARR-{i:05d}" # Уникальный номер гарантии
    desc = POOLS_E18["warr_description"][(i - 1) % len(POOLS_E18["warr_description"])]
    terms = POOLS_E18["warranty_terms"][(i - 1) % len(POOLS_E18["warranty_terms"])]
    status = POOLS_E18["warr_status"][(i - 1) % len(POOLS_E18["warr_status"])]
    reason = POOLS_E18["reason"][(i - 1) % len(POOLS_E18["reason"])]
    name = POOLS_E18["customer_name"][(i - 1) % len(POOLS_E18["customer_name"])]
    return f"({i}, {sale_id}, {build_id}, {ex_id}, '{warr_num}', '{desc}', '{terms}', '{status}', '{reason}', '2026-06-01'::date, '{name}')"

def generate_E19_row(i):
    b_id = ((i - 1) % COUNTS['E8']) + 1
    m_id = ((i - 1) % COUNTS['E1']) + 1
    return f"({b_id}, {m_id})"

def generate_E20_row(i):
    bld_id = ((i - 1) % COUNTS['E14']) + 1
    ex_id = ((i - 1) % COUNTS['E9']) + 1
    return f"({bld_id}, {ex_id})"

def generate_E21_row(i):
    ex_id = ((i - 1) % COUNTS['E9']) + 1
    sale_id = ((i - 1) % COUNTS['E17']) + 1
    return f"({ex_id}, {sale_id})"


def generate_sql():
    lines = ["SET search_path TO dhcp_store, public;\n"]

    tables_config = [
        ('E2', 'category', "category_id, parent_category_id, cat_code, cat_name, cat_description", generate_E2_row, True),
        ('E6', 'supplier', "supplier_id, sup_name, contact_info, requisites, sup_status", generate_E6_row, True),
        ('E1', 'component_model', "model_id, category_id, articul, comp_name, manufacturer, price, warranty_period", generate_E1_row, True),
        ('E3', 'characteristic', "characteristic_id, category_id, value_type, charac_name, is_required, unit", generate_E3_row, True),
        ('E4', 'characteristic_value', "model_id, characteristic_id, charac_value", generate_E4_row, False),
        ('E5', 'compability_rule', "rule_id, category_id, comp_name, argument_1, comparator, argument_2, related_category_id, comp_status, created_at, deprecated_at, error_image", generate_E5_row, True),
        ('E7', 'supply', "supply_id, supplier_id, arrival_date, total_cost, responsible_person, sup_status, sup_comment", generate_E7_row, True),
        ('E8', 'batch', "batch_id, model_id, supply_id, arrival_date, quantity, batch_status, purchase_price, current_stock", generate_E8_row, True),
        ('E9', 'exemplar', "exemplar_id, batch_id, serial_number, arrival_date, exemp_location, exemp_status", generate_E9_row, True),
        ('E11', 'build_configuration', "configuration_id, prev_version_id, component_list, build_status, customer_order_ref, compatibility_check_result", generate_E11_row, True),
        ('E10', 'customer_order', "order_id, configuration_id, cust_number, order_date, responsible_person, cust_cost, cust_status, cust_comment, customer_name, contact_info", generate_E10_row, True),
        ('E12', 'configuration_component', "component_id, configuration_id, model_id", generate_E12_row, True),
        ('E13', 'exemplar_reservation', "reservation_id, exemplar_id, component_id, order_id, created_at, validity_period, exemp_status", generate_E13_row, True),
        ('E14', 'build', "build_id, configuration_id, build_number, build_date, installed_components, assembler, build_test_info, build_status, build_comment", generate_E14_row, True),
        ('E15', 'build_test', "test_id, build_id, test_status, build_comment, test_date", generate_E15_row, True),
        ('E16', 'test_result', "test_result_id, test_id, test_name, result_date, test_status", generate_E16_row, True),
        ('E17', 'sale', "sale_id, order_id, build_id, sale_number, sale_date, customer_name, sale_cost, responsible_person, sale_status", generate_E17_row, True),
        ('E18', 'warranty_claim', "claim_id, sale_id, build_id, exemplar_id, warr_number, warr_description, warranty_terms, warr_status, reason, claim_date, customer_name", generate_E18_row, True),
        ('E19', 'batch_item', "batch_id, model_id", generate_E19_row, False),
        ('E20', 'build_item', "build_id, exemplar_id", generate_E20_row, False),
        ('E21', 'sale_item', "exemplar_id, sale_id", generate_E21_row, False)
    ]

    for key, table_name, columns, gen_func, has_identity in tables_config:
        n = COUNTS[key]
        lines.append(f"-- {key}: {table_name}")
        
        insert_prefix = f"INSERT INTO dhcp_store.{table_name} ({columns})"
        if has_identity:
            insert_prefix += " OVERRIDING SYSTEM VALUE"
        insert_prefix += " VALUES"

        rows = [gen_func(i) for i in range(1, n + 1)]
        
        conflict_keys = []
        if key == 'E1': conflict_keys = ["model_id"]
        elif key == 'E2': conflict_keys = ["category_id"]
        elif key == 'E3': conflict_keys = ["characteristic_id"]
        elif key == 'E4': conflict_keys = ["model_id", "characteristic_id"]
        elif key == 'E5': conflict_keys = ["rule_id"]
        elif key == 'E6': conflict_keys = ["supplier_id"]
        elif key == 'E7': conflict_keys = ["supply_id"]
        elif key == 'E8': conflict_keys = ["batch_id"]
        elif key == 'E9': conflict_keys = ["exemplar_id"]
        elif key == 'E10': conflict_keys = ["order_id"]
        elif key == 'E11': conflict_keys = ["configuration_id"]
        elif key == 'E12': conflict_keys = ["component_id"]
        elif key == 'E13': conflict_keys = ["reservation_id"]
        elif key == 'E14': conflict_keys = ["build_id"]
        elif key == 'E15': conflict_keys = ["test_id"]
        elif key == 'E16': conflict_keys = ["test_result_id"]
        elif key == 'E17': conflict_keys = ["sale_id"]
        elif key == 'E18': conflict_keys = ["claim_id"]
        elif key == 'E19': conflict_keys = ["batch_id", "model_id"]
        elif key == 'E20': conflict_keys = ["build_id", "exemplar_id"]
        elif key == 'E21': conflict_keys = ["exemplar_id", "sale_id"]

        conflict_clause = f"ON CONFLICT ({', '.join(conflict_keys)}) DO NOTHING;\n" if conflict_keys else ";"

        stmt = f"{insert_prefix}\n" + ",\n".join(rows) + f"\n{conflict_clause}\n"
        lines.append(stmt)

    os.makedirs(os.path.dirname(OUTPUT_SQL_PATH), exist_ok=True)
    with open(OUTPUT_SQL_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    print(f"Successfully generated independent test data at: {OUTPUT_SQL_PATH}")

if __name__ == "__main__":
    generate_sql()