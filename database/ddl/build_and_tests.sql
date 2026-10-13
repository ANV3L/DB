-- E17
CREATE TABLE sale (
    sale_id INT GENERATED ALWAYS AS IDENTITY,
    order_id INT NOT NULL,
    build_id INT NOT NULL,
    sale_number TEXT NOT NULL,
    sale_date DATE NOT NULL DEFAULT CURRENT_DATE,
    customer_name TEXT NOT NULL,
    sale_cost INT NOT NULL CHECK (sale_cost >= 0),
    responsible_person TEXT,
    sale_status TEXT NOT NULL DEFAULT 'completed',
    CONSTRAINT pk_sale PRIMARY KEY (sale_id),
    CONSTRAINT uk_sale_number UNIQUE (sale_number),
    CONSTRAINT fk_sale_order
        FOREIGN KEY (order_id)
        REFERENCES customer_order (order_id),

    CONSTRAINT fk_sale_build
        FOREIGN KEY (build_id)
        REFERENCES build (build_id)
);

-- E18
CREATE TABLE warranty_claim (
    claim_id INT GENERATED ALWAYS AS IDENTITY,
    sale_id INT NOT NULL,
    build_id INT NOT NULL,
    exemplar_id INT NOT NULL,
    warr_number TEXT NOT NULL,
    warr_description TEXT,
    warranty_terms TEXT,
    warr_status TEXT NOT NULL DEFAULT 'open',
    reason TEXT,
    claim_date DATE NOT NULL DEFAULT CURRENT_DATE,
    customer_name TEXT,
    CONSTRAINT pk_claim PRIMARY KEY (claim_id),
    CONSTRAINT uk_warranty_claim_number UNIQUE (warr_number),
    CONSTRAINT fk_warranty_claim_sale
        FOREIGN KEY (sale_id)
        REFERENCES sale (sale_id),

    CONSTRAINT fk_warranty_claim_build
        FOREIGN KEY (build_id)
        REFERENCES build (build_id),

    CONSTRAINT fk_warranty_claim_exemplar
        FOREIGN KEY (exemplar_id)
        REFERENCES exemplar (exemplar_id)
);

-- E21
CREATE TABLE sale_item (
    exemplar_id INT NOT NULL,
    sale_id INT NOT NULL,
    CONSTRAINT pk_sale_item PRIMARY KEY (exemplar_id, sale_id),
    CONSTRAINT fk_sale_item_exemplar
        FOREIGN KEY (exemplar_id)
        REFERENCES exemplar (exemplar_id),

    CONSTRAINT fk_sale_item_sale
        FOREIGN KEY (sale_id)
        REFERENCES sale (sale_id)
);