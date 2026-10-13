-- E2
CREATE TABLE category (
    category_id INT GENERATED ALWAYS AS IDENTITY,
    parent_category_id INT,
    cat_code TEXT NOT NULL,
    cat_name TEXT NOT NULL,
    cat_description TEXT,

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
    articul TEXT NOT NULL,
    comp_name TEXT NOT NULL,
    manufacturer TEXT NOT NULL,
    price INT NOT NULL CHECK (price >= 0),
    warranty_period DATE,

    CONSTRAINT pk_component_model PRIMARY KEY (model_id),
    CONSTRAINT uk_component_model_articul UNIQUE (articul),
    CONSTRAINT fk_component_model_category
        FOREIGN KEY (category_id)
        REFERENCES category (category_id)
);

-- E3
CREATE TABLE characteristic (
    characteristic_id INT GENERATED ALWAYS AS IDENTITY,
    category_id INT NOT NULL,
    value_type TEXT NOT NULL,
    charac_name TEXT NOT NULL,
    is_required BOOLEAN NOT NULL DEFAULT FALSE,
    unit TEXT,

    CONSTRAINT pk_characteristic PRIMARY KEY (characteristic_id),
    CONSTRAINT fk_characteristic_category
        FOREIGN KEY (category_id)
        REFERENCES category (category_id)
);

-- E4
CREATE TABLE characteristic_value (
    model_id INT NOT NULL,
    characteristic_id INT NOT NULL,
    charac_value NUMERIC (10, 3),

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
    comp_name TEXT NOT NULL,
    argument_1 TEXT NOT NULL,
    comparator TEXT NOT NULL,
    argument_2 TEXT NOT NULL,
    related_category_id INT,
    comp_status TEXT NOT NULL DEFAULT 'active',
    created_at DATE NOT NULL DEFAULT CURRENT_DATE,
    deprecated_at DATE,
    error_image TEXT,

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