-- E11
CREATE TABLE dhcp_store.build_configuration (
    configuration_id INT GENERATED ALWAYS AS IDENTITY,
    prev_version_id INT,
    component_list VARCHAR(2000),
    build_status VARCHAR(20) NOT NULL DEFAULT 'draft' CHECK (build_status IN ('draft', 'verified', 'approved', 'assembled', 'archived')),
    customer_order_ref VARCHAR(80),
    compatibility_check_result VARCHAR(80),
    CONSTRAINT pk_build_configuration PRIMARY KEY (configuration_id),
    CONSTRAINT fk_build_configuration_prev
        FOREIGN KEY (prev_version_id)
        REFERENCES dhcp_store.build_configuration (configuration_id)
        ON DELETE SET NULL
);

-- E10
CREATE TABLE dhcp_store.customer_order (
    order_id INT GENERATED ALWAYS AS IDENTITY,
    configuration_id INT,
    cust_number VARCHAR(80) NOT NULL,
    order_date DATE NOT NULL DEFAULT CURRENT_DATE,
    responsible_person VARCHAR(140),
    cust_cost NUMERIC(12,2) CHECK (cust_cost >= 0),
    cust_status VARCHAR(20) NOT NULL DEFAULT 'new' CHECK (cust_status IN ('new', 'processing', 'assembled', 'completed', 'cancelled')),
    cust_comment VARCHAR(500),
    customer_name VARCHAR(80) NOT NULL,
    contact_info VARCHAR(90),
    CONSTRAINT pk_customer_order PRIMARY KEY (order_id),
    CONSTRAINT uk_customer_order_number UNIQUE (cust_number),
    CONSTRAINT fk_customer_order_configuration
        FOREIGN KEY (configuration_id)
        REFERENCES dhcp_store.build_configuration (configuration_id)
        ON DELETE SET NULL
);

-- E12
CREATE TABLE dhcp_store.configuration_component (
    component_id INT GENERATED ALWAYS AS IDENTITY,
    configuration_id INT NOT NULL,
    model_id INT NOT NULL,
    CONSTRAINT pk_configuration_component PRIMARY KEY (component_id),
    CONSTRAINT fk_configuration_component_configuration
        FOREIGN KEY (configuration_id)
        REFERENCES dhcp_store.build_configuration (configuration_id),

    CONSTRAINT fk_configuration_component_model
        FOREIGN KEY (model_id)
        REFERENCES dhcp_store.component_model (model_id)
);

-- E13
CREATE TABLE dhcp_store.exemplar_reservation (
    reservation_id INT GENERATED ALWAYS AS IDENTITY,
    exemplar_id INT NOT NULL,
    component_id INT NOT NULL,
    order_id INT NOT NULL,
    created_at DATE NOT NULL DEFAULT CURRENT_DATE,
    validity_period INT CHECK (validity_period >= 0),
    exemp_status VARCHAR(20) NOT NULL DEFAULT 'active' CHECK (exemp_status IN ('active', 'expired', 'fulfilled', 'cancelled')),
    CONSTRAINT pk_exemplar_reservation PRIMARY KEY (reservation_id),
    CONSTRAINT fk_exemplar_reservation_exemplar
        FOREIGN KEY (exemplar_id)
        REFERENCES dhcp_store.exemplar (exemplar_id),

    CONSTRAINT fk_exemplar_reservation_component
        FOREIGN KEY (component_id)
        REFERENCES dhcp_store.configuration_component (component_id),

    CONSTRAINT fk_exemplar_reservation_order
        FOREIGN KEY (order_id)
        REFERENCES dhcp_store.customer_order (order_id)
);