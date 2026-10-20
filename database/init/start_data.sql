SET search_path TO dhcp_store, public;

INSERT INTO category (category_id, parent_category_id, cat_code, cat_name, cat_description) OVERRIDING SYSTEM VALUE VALUES
(1, NULL, 'CPU', 'Процессоры', 'Центральные процессоры для ПК и серверов'),
(2, NULL, 'GPU', 'Видеокарты', 'Графические ускорители'),
(3, NULL, 'RAM', 'Оперативная память', 'Модули памяти ПК'),
(4, NULL, 'MOBO', 'Материнские платы', 'Системные платы для сборки'),
(5, NULL, 'PSU', 'Блоки питания', 'Источники питания компонентов'),
(6, 3, 'RAM_DDR4', 'Оперативная память DDR4', 'Модули памяти стандарта DDR4'),
(7, 3, 'RAM_DDR5', 'Оперативная память DDR5', 'Модули памяти стандарта DDR5'),
(8, 4, 'MOBO_LGA1700', 'Материнские платы LGA1700', 'Плата под процессоры Intel Core (12-14 ген)'),
(9, 4, 'MOBO_AM5', 'Материнские платы AM5', 'Плата под процессоры AMD Ryzen (серии 7000 и выше)');

INSERT INTO supplier (supplier_id, sup_name, contact_info, requisites, sup_status) OVERRIDING SYSTEM VALUE VALUES
(1, 'ООО "Двенашка"', 'panel@technotrade.ru', 'ИНН 1212121212 / КПП 770101001', 'active'),
(2, 'АО "Электроника №3"', 'info@elopt.ru', 'ИНН 7802987654 / КПП 780201001', 'active');

INSERT INTO characteristic (characteristic_id, category_id, value_type, charac_name, is_required, unit) OVERRIDING SYSTEM VALUE VALUES
(1, 1, 'TEXT', 'Сокет', TRUE, NULL),
(2, 1, 'NUMERIC', 'TDP', TRUE, 'W'),
(3, 6, 'NUMERIC', 'Частота', TRUE, 'MHz'),
(4, 7, 'NUMERIC', 'Частота', TRUE, 'MHz');

INSERT INTO compability_rule (rule_id, category_id, comp_name, argument_1, comparator, argument_2, related_category_id, comp_status) OVERRIDING SYSTEM VALUE VALUES
(1, 1, 'CPU_MOBO_SOCKET_CHECK', 'socket', '=', 'socket', 4, 'active');