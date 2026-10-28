-- E17
CREATE TABLE dhcp_store.sale (
    sale_id INT GENERATED ALWAYS AS IDENTITY,
    order_id INT NOT NULL,
    build_id INT NOT NULL,
    sale_number VARCHAR(80) NOT NULL,
    sale_date DATE NOT NULL DEFAULT CURRENT_DATE,
    customer_name VARCHAR(80) NOT NULL,
    sale_cost NUMERIC(12,2) NULL CHECK (sale_cost >= 0),
    responsible_person TEXT,
    sale_status VARCHAR(80) NOT NULL DEFAULT 'completed',
    CONSTRAINT pk_sale PRIMARY KEY (sale_id),
    CONSTRAINT uk_sale_number UNIQUE (sale_number),
    CONSTRAINT fk_sale_order
        FOREIGN KEY (order_id)
        REFERENCES dhcp_store.customer_order (order_id),

    CONSTRAINT fk_sale_build
        FOREIGN KEY (build_id)
        REFERENCES dhcp_store.build (build_id)
);

-- E18
CREATE TABLE dhcp_store.warranty_claim (
    claim_id INT GENERATED ALWAYS AS IDENTITY,
    sale_id INT NOT NULL,
    build_id INT NOT NULL,
    exemplar_id INT NOT NULL,
    warr_number VARCHAR(80) NOT NULL,
    warr_description TEXT,
    warranty_terms TEXT,
    warr_status VARCHAR(20) NOT NULL DEFAULT 'open' CHECK (warr_status IN ('open', 'in_progress', 'resolved', 'rejected', 'closed')),
    reason TEXT,
    claim_date DATE NOT NULL DEFAULT CURRENT_DATE,
    customer_name VARCHAR(150),

    CONSTRAINT pk_claim PRIMARY KEY (claim_id),
    CONSTRAINT uk_warranty_claim_number UNIQUE (warr_number),
    CONSTRAINT fk_warranty_claim_sale
        FOREIGN KEY (sale_id)
        REFERENCES dhcp_store.sale (sale_id),

    CONSTRAINT fk_warranty_claim_build
        FOREIGN KEY (build_id)
        REFERENCES dhcp_store.build (build_id),

    CONSTRAINT fk_warranty_claim_exemplar
        FOREIGN KEY (exemplar_id)
        REFERENCES dhcp_store.exemplar (exemplar_id)
);

-- E21
CREATE TABLE dhcp_store.sale_item (
    exemplar_id INT NOT NULL,
    sale_id INT NOT NULL,

    CONSTRAINT pk_sale_item PRIMARY KEY (exemplar_id, sale_id),
    CONSTRAINT fk_sale_item_exemplar
        FOREIGN KEY (exemplar_id)
        REFERENCES dhcp_store.exemplar (exemplar_id),

    CONSTRAINT fk_sale_item_sale
        FOREIGN KEY (sale_id)
        REFERENCES dhcp_store.sale (sale_id)
);