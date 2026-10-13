import random
from datetime import datetime, timedelta

E1_MODELS_QUANTITY = 25
E2_CATEGORIES_QUANTITY = 9
E3_CHARACTERISTICS_QUANTITY = 6
E4_CHAR_VALUES_QUANTITY = 35
E5_COMP_RULES_QUANTITY = 3
E6_SUPPLIERS_QUANTITY = 4
E7_SUPPLIES_QUANTITY = 5
E8_BATCHES_QUANTITY = 15
E9_EXEMPLARS_QUANTITY = 60
E10_ORDERS_QUANTITY = 10
E11_CONFIGS_QUANTITY = 10
E12_CONFIG_COMPS_QUANTITY = 15
E13_RESERVATIONS_QUANTITY = 10
E14_BUILDS_QUANTITY = 8
E15_TESTS_QUANTITY = 8
E16_TEST_RESULTS_QUANTITY = 8
E17_SALES_QUANTITY = 6
E18_WARRANTY_CLAIMS_QUANTITY = 2
E19_BATCH_ITEMS_QUANTITY = 15
E20_BUILD_ITEMS_QUANTITY = 8
E21_SALE_ITEMS_QUANTITY = 6

OUTPUT_SQL_PATH = "database/init/generated_test_data.sql"

def esc(val):
    """Экранирование одинарных кавычек для SQL"""
    if val is None:
        return "NULL"
    return str(val).replace("'", "''")

def generate_sql():
    lines = []
    lines.append("SET search_path TO dhcp_store, public;\n")
    base_date = datetime.now() - timedelta(days=90)

    suppliers_pool = [
        ("ООО \"ТехноТрейд\"", "order@technotrade.ru", "ИНН 7701234567"),
        ("АО \"Электроника Опт\"", "info@elopt.ru", "ИНН 7802987654"),
        ("ООО \"МСК Комплект\"", "b2b@mskcomp.ru", "ИНН 7712345678"),
        ("ИП Смирнов А.В.", "smirrov@mail.ru", "ИНН 500123456789"),
        ("ТД \"ПромЭлектроника\"", "sales@promelec.ru", "ИНН 6671234567")
    ]
    
    mfr_by_category = {
        1: ["Intel", "AMD"],
        2: ["NVIDIA", "AMD", "ASUS", "MSI", "Gigabyte"],
        3: ["Kingston", "Corsair", "G.Skill", "Crucial", "TeamGroup"],
        4: ["ASUS", "MSI", "Gigabyte", "ASRock"],
        5: ["Seasonic", "Be Quiet!", "Corsair", "DeepCool", "MSI"],
        6: ["Kingston", "Corsair", "G.Skill", "Crucial"],
        7: ["Kingston", "Corsair", "G.Skill", "TeamGroup"],
        8: ["ASUS", "MSI", "Gigabyte"],
        9: ["ASUS", "MSI", "ASRock"]
    }
    
    clients = [
        ("Александр Иванов", "alex.ivanov@gmail.com"),
        ("Екатерина Смирнова", "katrin_s@yandex.ru"),
        ("Дмитрий Петров", "dpetrov@mail.ru"),
        ("Ольга Васильева", "olga.v@tech-user.org"),
        ("Максим Ковалев", "max_kov@bk.ru"),
        ("Анна Морозова", "morozova_anna@gmail.com")
    ]

    engineers = ["Инженер Смит", "Мастер Джонс", "Техник Гарсия", "Специалист Вонг"]
    test_names = ["AIDA64 FPU Stress", "FurMark Benchmark", "Prime95 Blend", "MemTest86 Pro", "OCCT Power Test"]

    lines.append("-- E6: supplier")
    e6_vals = []
    for i in range(1, E6_SUPPLIERS_QUANTITY + 1):
        name, info, req = suppliers_pool[(i - 1) % len(suppliers_pool)]
        full_name = f"{name} #{i}"
        e6_vals.append(f"({i}, '{esc(full_name)}', '{esc(info)}', '{esc(req)}', 'active')")
    
    lines.append(
        "INSERT INTO supplier (supplier_id, sup_name, contact_info, requisites, sup_status) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e6_vals) + 
        "\nON CONFLICT (supplier_id) DO NOTHING;\n"
    )

    lines.append("-- E1: component_model")
    e1_vals = []
    for i in range(1, E1_MODELS_QUANTITY + 1):
        cat_id = random.randint(1, E2_CATEGORIES_QUANTITY)
        mfrs = mfr_by_category.get(cat_id, ["Generic Mfr"])
        mfr = random.choice(mfrs)
        art = f"ART-{cat_id}-{i:04d}"
        name = f"{mfr} Model Line X-{i}"
        price = random.randint(4000, 180000)
        e1_vals.append(f"({i}, {cat_id}, '{esc(art)}', '{esc(name)}', '{esc(mfr)}', {price})")
    
    lines.append(
        "INSERT INTO component_model (model_id, category_id, articul, comp_name, manufacturer, price) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e1_vals) + 
        "\nON CONFLICT (model_id) DO NOTHING;\n"
    )

    lines.append("-- E3: characteristic")
    char_defs = [
        (1, 1, 'TEXT', 'Сокет', 'TRUE', 'NULL'),
        (2, 1, 'NUMERIC', 'TDP', 'TRUE', "'Вт'"),
        (3, 2, 'NUMERIC', 'Объем VRAM', 'TRUE', "'ГБ'"),
        (4, 3, 'NUMERIC', 'Частота', 'TRUE', "'МГц'"),
        (5, 4, 'TEXT', 'Форм-фактор', 'TRUE', 'NULL'),
        (6, 5, 'NUMERIC', 'Мощность', 'TRUE', "'Вт'")
    ]
    e3_vals = []
    for cid, cat_id, vtype, cname, req, unit in char_defs[:E3_CHARACTERISTICS_QUANTITY]:
        e3_vals.append(f"({cid}, {cat_id}, '{esc(vtype)}', '{esc(cname)}', {req}, {unit})")
    
    lines.append(
        "INSERT INTO characteristic (characteristic_id, category_id, value_type, charac_name, is_required, unit) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e3_vals) + 
        "\nON CONFLICT (characteristic_id) DO NOTHING;\n"
    )

    lines.append("-- E4: characteristic_value")
    e4_vals = []
    added_cv = set()
    for _ in range(E4_CHAR_VALUES_QUANTITY):
        m_id = random.randint(1, E1_MODELS_QUANTITY)
        c_id = random.randint(1, E3_CHARACTERISTICS_QUANTITY)
        if (m_id, c_id) in added_cv:
            continue
        added_cv.add((m_id, c_id))
        val = random.choice([8, 16, 32, 65, 95, 125, 3200, 4800, 5600, 650, 750, 850])
        e4_vals.append(f"({m_id}, {c_id}, {val})")
    
    lines.append(
        "INSERT INTO characteristic_value (model_id, characteristic_id, charac_value) VALUES\n" + 
        ",\n".join(e4_vals) + "\nON CONFLICT (model_id, characteristic_id) DO NOTHING;\n"
    )

    lines.append("-- E5: compability_rule")
    rules = [
        (1, 1, 'CPU_MOBO_SOCKET_CHECK', 'socket', '=', 'socket', 4, 'active'),
        (2, 4, 'MOBO_RAM_TYPE_CHECK', 'memory_type', '=', 'memory_type', 3, 'active'),
        (3, 5, 'PSU_POWER_CHECK', 'total_tdp', '<=', 'max_power', 1, 'active')
    ]
    e5_vals = []
    for r in rules[:E5_COMP_RULES_QUANTITY]:
        e5_vals.append(f"({r[0]}, {r[1]}, '{esc(r[2])}', '{esc(r[3])}', '{esc(r[4])}', '{esc(r[5])}', {r[6]}, '{esc(r[7])}')")
    
    lines.append(
        "INSERT INTO compability_rule (rule_id, category_id, comp_name, argument_1, comparator, argument_2, related_category_id, comp_status) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e5_vals) + 
        "\nON CONFLICT (rule_id) DO NOTHING;\n"
    )

    lines.append("-- E7: supply")
    e7_vals = []
    for i in range(1, E7_SUPPLIES_QUANTITY + 1):
        d = (base_date + timedelta(days=i * 4)).strftime('%Y-%m-%d')
        sup_id = random.randint(1, E6_SUPPLIERS_QUANTITY)
        cost = random.randint(150000, 1200000)
        resp = random.choice(engineers)
        e7_vals.append(f"({i}, {sup_id}, '{d}', {cost}, '{esc(resp)}', 'received')")
    
    lines.append(
        "INSERT INTO supply (supply_id, supplier_id, arrival_date, total_cost, responsible_person, sup_status) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e7_vals) + 
        "\nON CONFLICT (supply_id) DO NOTHING;\n"
    )

    lines.append("-- E8: batch")
    e8_vals = []
    for i in range(1, E8_BATCHES_QUANTITY + 1):
        m_id = random.randint(1, E1_MODELS_QUANTITY)
        sup_id = random.randint(1, E7_SUPPLIES_QUANTITY)
        d = (base_date + timedelta(days=sup_id * 4)).strftime('%Y-%m-%d')
        qty = E9_EXEMPLARS_QUANTITY // E8_BATCHES_QUANTITY
        price = random.randint(3000, 90000)
        e8_vals.append(f"({i}, {m_id}, {sup_id}, '{d}', {qty}, {price}, {qty})")
    
    lines.append(
        "INSERT INTO batch (batch_id, model_id, supply_id, arrival_date, quantity, purchase_price, current_stock) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e8_vals) + 
        "\nON CONFLICT (batch_id) DO NOTHING;\n"
    )

    lines.append("-- E9: exemplar")
    e9_vals = []
    per_batch = E9_EXEMPLARS_QUANTITY // E8_BATCHES_QUANTITY
    curr_batch = 1
    count_in_batch = 0
    for i in range(1, E9_EXEMPLARS_QUANTITY + 1):
        serial = random.randint(10000000, 99999999)
        d = base_date.strftime('%Y-%m-%d')
        e9_vals.append(f"({i}, {curr_batch}, {serial}, '{d}', 'in_stock')")
        count_in_batch += 1
        if count_in_batch >= per_batch and curr_batch < E8_BATCHES_QUANTITY:
            curr_batch += 1
            count_in_batch = 0
    
    lines.append(
        "INSERT INTO exemplar (exemplar_id, batch_id, serial_number, arrival_date, exemp_status) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e9_vals) + 
        "\nON CONFLICT (exemplar_id) DO NOTHING;\n"
    )

    lines.append("-- E11: build_configuration")
    e11_vals = []
    for i in range(1, E11_CONFIGS_QUANTITY + 1):
        e11_vals.append(f"({i}, NULL, 'ready', 'REF-2026-{i:03d}')")
    
    lines.append(
        "INSERT INTO build_configuration (configuration_id, prev_version_id, build_status, customer_order_ref) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e11_vals) + 
        "\nON CONFLICT (configuration_id) DO NOTHING;\n"
    )

    lines.append("-- E10: customer_order")
    e10_vals = []
    for i in range(1, E10_ORDERS_QUANTITY + 1):
        d = (base_date + timedelta(days=i * 2)).strftime('%Y-%m-%d')
        cfg_id = ((i - 1) % E11_CONFIGS_QUANTITY) + 1
        client_name, client_email = random.choice(clients)
        cost = random.randint(45000, 280000)
        e10_vals.append(f"({i}, {cfg_id}, 'ORD-{i:04d}', '{d}', {cost}, 'completed', '{esc(client_name)}', '{esc(client_email)}')")
    
    lines.append(
        "INSERT INTO customer_order (order_id, configuration_id, cust_number, order_date, cust_cost, cust_status, customer_name, contact_info) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e10_vals) + 
        "\nON CONFLICT (order_id) DO NOTHING;\n"
    )

    lines.append("-- E12: configuration_component")
    e12_vals = []
    for i in range(1, E12_CONFIG_COMPS_QUANTITY + 1):
        cfg_id = random.randint(1, E11_CONFIGS_QUANTITY)
        m_id = random.randint(1, E1_MODELS_QUANTITY)
        e12_vals.append(f"({i}, {cfg_id}, {m_id})")
    
    lines.append(
        "INSERT INTO configuration_component (component_id, configuration_id, model_id) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e12_vals) + 
        "\nON CONFLICT (component_id) DO NOTHING;\n"
    )

    lines.append("-- E13: exemplar_reservation")
    e13_vals = []
    for i in range(1, E13_RESERVATIONS_QUANTITY + 1):
        ex_id = random.randint(1, E9_EXEMPLARS_QUANTITY)
        comp_id = random.randint(1, E12_CONFIG_COMPS_QUANTITY)
        ord_id = random.randint(1, E10_ORDERS_QUANTITY)
        e13_vals.append(f"({i}, {ex_id}, {comp_id}, {ord_id}, 7, 'active')")
    
    lines.append(
        "INSERT INTO exemplar_reservation (reservation_id, exemplar_id, component_id, order_id, validity_period, exemp_status) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e13_vals) + 
        "\nON CONFLICT (reservation_id) DO NOTHING;\n"
    )

    lines.append("-- E14: build")
    e14_vals = []
    for i in range(1, E14_BUILDS_QUANTITY + 1):
        d = (base_date + timedelta(days=i * 2 + 1)).strftime('%Y-%m-%d')
        cfg_id = ((i - 1) % E11_CONFIGS_QUANTITY) + 1
        assembler = random.choice(engineers)
        e14_vals.append(f"({i}, {cfg_id}, 'BLD-{i:04d}', '{d}', 'completed', '{esc(assembler)}')")
    
    lines.append(
        "INSERT INTO build (build_id, configuration_id, build_number, build_date, build_status, assembler) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e14_vals) + 
        "\nON CONFLICT (build_id) DO NOTHING;\n"
    )

    lines.append("-- E15: build_test")
    e15_vals = []
    for i in range(1, E15_TESTS_QUANTITY + 1):
        d = (base_date + timedelta(days=i * 2 + 2)).strftime('%Y-%m-%d')
        bld_id = ((i - 1) % E14_BUILDS_QUANTITY) + 1
        e15_vals.append(f"({i}, {bld_id}, 'passed', '{d}')")
    
    lines.append(
        "INSERT INTO build_test (test_id, build_id, build_status, test_date) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e15_vals) + 
        "\nON CONFLICT (test_id) DO NOTHING;\n"
    )

    lines.append("-- E16: test_result")
    e16_vals = []
    for i in range(1, E16_TEST_RESULTS_QUANTITY + 1):
        d = (base_date + timedelta(days=i * 2 + 2)).strftime('%Y-%m-%d')
        t_id = random.randint(1, E15_TESTS_QUANTITY)
        t_name = random.choice(test_names)
        e16_vals.append(f"({i}, {t_id}, '{esc(t_name)}', '{d}', 'success')")
    
    lines.append(
        "INSERT INTO test_result (test_result_id, test_id, test_name, result_date, test_status) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e16_vals) + 
        "\nON CONFLICT (test_result_id) DO NOTHING;\n"
    )

    lines.append("-- E17: sale")
    e17_vals = []
    for i in range(1, E17_SALES_QUANTITY + 1):
        d = (base_date + timedelta(days=i * 3 + 3)).strftime('%Y-%m-%d')
        ord_id = ((i - 1) % E10_ORDERS_QUANTITY) + 1
        bld_id = ((i - 1) % E14_BUILDS_QUANTITY) + 1
        client_name, _ = random.choice(clients)
        cost = random.randint(50000, 300000)
        e17_vals.append(f"({i}, {ord_id}, {bld_id}, 'SALE-{i:04d}', '{d}', '{esc(client_name)}', {cost}, 'completed')")
    
    lines.append(
        "INSERT INTO sale (sale_id, order_id, build_id, sale_number, sale_date, customer_name, sale_cost, sale_status) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e17_vals) + 
        "\nON CONFLICT (sale_id) DO NOTHING;\n"
    )

    lines.append("-- E18: warranty_claim")
    e18_vals = []
    reasons = ["Дефект питания", "Артефакты GPU", "Не запускается память", "Перегрев CPU"]
    for i in range(1, E18_WARRANTY_CLAIMS_QUANTITY + 1):
        d = (base_date + timedelta(days=i * 5 + 10)).strftime('%Y-%m-%d')
        sale_id = random.randint(1, E17_SALES_QUANTITY)
        bld_id = random.randint(1, E14_BUILDS_QUANTITY)
        ex_id = random.randint(1, E9_EXEMPLARS_QUANTITY)
        reason = random.choice(reasons)
        client_name, _ = random.choice(clients)
        e18_vals.append(f"({i}, {sale_id}, {bld_id}, {ex_id}, 'WARR-{i:04d}', 'open', '{esc(reason)}', '{d}', '{esc(client_name)}')")
    
    lines.append(
        "INSERT INTO warranty_claim (claim_id, sale_id, build_id, exemplar_id, warr_number, warr_status, reason, claim_date, customer_name) "
        "OVERRIDING SYSTEM VALUE VALUES\n" + ",\n".join(e18_vals) + 
        "\nON CONFLICT (claim_id) DO NOTHING;\n"
    )

    lines.append("-- E19: batch_item")
    e19_vals = []
    for i in range(1, E19_BATCH_ITEMS_QUANTITY + 1):
        b_id = i
        m_id = random.randint(1, E1_MODELS_QUANTITY)
        e19_vals.append(f"({b_id}, {m_id})")
    
    lines.append(
        "INSERT INTO batch_item (batch_id, model_id) VALUES\n" + ",\n".join(e19_vals) + 
        "\nON CONFLICT (batch_id, model_id) DO NOTHING;\n"
    )

    lines.append("-- E20: build_item")
    e20_vals = []
    for i in range(1, E20_BUILD_ITEMS_QUANTITY + 1):
        bld_id = i
        ex_id = random.randint(1, E9_EXEMPLARS_QUANTITY)
        e20_vals.append(f"({bld_id}, {ex_id})")
    
    lines.append(
        "INSERT INTO build_item (build_id, exemplar_id) VALUES\n" + ",\n".join(e20_vals) + 
        "\nON CONFLICT (build_id, exemplar_id) DO NOTHING;\n"
    )

    lines.append("-- E21: sale_item")
    e21_vals = []
    for i in range(1, E21_SALE_ITEMS_QUANTITY + 1):
        sale_id = i
        ex_id = random.randint(1, E9_EXEMPLARS_QUANTITY)
        e21_vals.append(f"({ex_id}, {sale_id})")
    
    lines.append(
        "INSERT INTO sale_item (exemplar_id, sale_id) VALUES\n" + ",\n".join(e21_vals) + 
        "\nON CONFLICT (exemplar_id, sale_id) DO NOTHING;"
    )

    with open(OUTPUT_SQL_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    print(f"Successfully generated independent test data at: {OUTPUT_SQL_PATH}")

if __name__ == "__main__":
    generate_sql()