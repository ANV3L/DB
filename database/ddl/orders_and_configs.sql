-- E11
CREATE TABLE build_configuration (
    configuration_id INT GENERATED ALWAYS AS IDENTITY,
    prev_version_id INT,
    component_list TEXT,
    build_status TEXT NOT NULL DEFAULT 'draft',
    customer_order_ref TEXT,
    compatibility_check_result TEXT,
    CONSTRAINT pk_build_configuration PRIMARY KEY (configuration_id),
    CONSTRAINT fk_build_configuration_prev
        FOREIGN KEY (prev_version_id)
        REFERENCES build_configuration (configuration_id)
        ON DELETE SET NULL
);

-- E10
CREATE TABLE customer_order (
    order_id INT GENERATED ALWAYS AS IDENTITY,
    configuration_id INT,
    cust_number TEXT NOT NULL,
    order_date DATE NOT NULL DEFAULT CURRENT_DATE,
    responsible_person TEXT,
    cust_cost INT CHECK (cust_cost >= 0),
    cust_status TEXT NOT NULL DEFAULT 'new',
    cust_comment TEXT,
    customer_name TEXT NOT NULL,
    contact_info TEXT,
    CONSTRAINT pk_customer_order PRIMARY KEY (order_id),
    CONSTRAINT uk_customer_order_number UNIQUE (cust_number),
    CONSTRAINT fk_customer_order_configuration
        FOREIGN KEY (configuration_id)
        REFERENCES build_configuration (configuration_id)
        ON DELETE SET NULL
);

-- E12
CREATE TABLE configuration_component (
    component_id INT GENERATED ALWAYS AS IDENTITY,
    configuration_id INT NOT NULL,
    model_id INT NOT NULL,
    CONSTRAINT pk_configuration_component PRIMARY KEY (component_id),
    CONSTRAINT fk_configuration_component_configuration
        FOREIGN KEY (configuration_id)
        REFERENCES build_configuration (configuration_id),

    CONSTRAINT fk_configuration_component_model
        FOREIGN KEY (model_id)
        REFERENCES component_model (model_id)
);

-- E13
CREATE TABLE exemplar_reservation (
    reservation_id INT GENERATED ALWAYS AS IDENTITY,
    exemplar_id INT NOT NULL,
    component_id INT NOT NULL,
    order_id INT NOT NULL,
    created_at DATE NOT NULL DEFAULT CURRENT_DATE,
    validity_period INT CHECK (validity_period >= 0),
    exemp_status TEXT NOT NULL DEFAULT 'active',
    CONSTRAINT pk_exemplar_reservation PRIMARY KEY (reservation_id),
    CONSTRAINT fk_exemplar_reservation_exemplar
        FOREIGN KEY (exemplar_id)
        REFERENCES exemplar (exemplar_id),

    CONSTRAINT fk_exemplar_reservation_component
        FOREIGN KEY (component_id)
        REFERENCES configuration_component (component_id),

    CONSTRAINT fk_exemplar_reservation_order
        FOREIGN KEY (order_id)
        REFERENCES customer_order (order_id)
);