-- E2
CREATE TABLE category (
    category_id INT GENERATED ALWAYS AS IDENTITY,
    parent_category_id INT,
    cat_code VARCHAR(80) NOT NULL,
    cat_name VARCHAR(80) NOT NULL,
    cat_description VARCHAR(1000),

    CONSTRAINT pk_category PRIMARY KEY (category_id),
    CONSTRAINT uk_category_cat_code UNIQUE (cat_code),
    CONSTRAINT fk_category_parent
        FOREIGN KEY (parent_category_id)
        REFERENCES category (category_id)
);

-- E1
CREATE TABLE component_model (
    model_id INT GENERATED ALWAYS AS IDENTITY,
    category_id INT NOT NULL,
    articul VARCHAR(80) NOT NULL,
    comp_name VARCHAR(100) NOT NULL,
    manufacturer VARCHAR(80) NOT NULL,
    price NUMERIC(12,2) NOT NULL CHECK (price >= 0),
    warranty_period INT CHECK (warranty_period > 0), -- NULL = отсутствие гарантии

    CONSTRAINT pk_component_model PRIMARY KEY (model_id),
    CONSTRAINT uk_component_model_articul UNIQUE (articul),
    CONSTRAINT fk_component_model_category
        FOREIGN KEY (category_id)
        REFERENCES category (category_id)
);

CREATE TABLE characteristic (
    characteristic_id INT GENERATED ALWAYS AS IDENTITY,
    category_id INT NOT NULL,
    value_type VARCHAR(80) NOT NULL,
    charac_name VARCHAR(80) NOT NULL,
    is_required BOOLEAN NOT NULL DEFAULT FALSE,
    unit VARCHAR(20) CHECK (unit IN ('MB', 'MHz', 'W', 'mm', 'kg', 'pcs', 'V', 'A', 'GHz')),

    CONSTRAINT pk_characteristic PRIMARY KEY (characteristic_id),
    CONSTRAINT fk_characteristic_category
        FOREIGN KEY (category_id)  
        REFERENCES category (category_id)
);

-- E4
CREATE TABLE characteristic_value (
    model_id INT NOT NULL,
    characteristic_id INT NOT NULL,
    charac_value NUMERIC (12, 2),

    CONSTRAINT pk_characteristic_value PRIMARY KEY (model_id, characteristic_id),
    CONSTRAINT fk_characteristic_value_model
        FOREIGN KEY (model_id)
        REFERENCES component_model (model_id),

    CONSTRAINT fk_characteristic_value_characteristic
        FOREIGN KEY (characteristic_id)
        REFERENCES characteristic (characteristic_id)
);

-- E5
CREATE TABLE compability_rule (
    rule_id INT GENERATED ALWAYS AS IDENTITY,
    category_id INT NOT NULL,
    comp_name VARCHAR(300) NOT NULL,
    argument_1 VARCHAR(300) NOT NULL,
    comparator VARCHAR(80) NOT NULL,
    argument_2 VARCHAR(300) NOT NULL,
    related_category_id INT,
    comp_status VARCHAR(20) NOT NULL DEFAULT 'active'CHECK (comp_status IN ('active', 'deprecated', 'draft')),
    created_at DATE NOT NULL DEFAULT CURRENT_DATE,
    deprecated_at DATE,
    error_image VARCHAR(200),

    CONSTRAINT pk_compatibility_rule PRIMARY KEY (rule_id),
    CONSTRAINT fk_compatibility_rule_category
        FOREIGN KEY (category_id)
        REFERENCES category (category_id),

    CONSTRAINT fk_compatibility_rule_related_category
        FOREIGN KEY (related_category_id)
        REFERENCES category (category_id),

    CONSTRAINT chk_compatibility_rule_dates
        CHECK (deprecated_at IS NULL OR deprecated_at >= created_at)
);