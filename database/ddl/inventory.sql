-- E6
CREATE TABLE supplier (
    supplier_id INT GENERATED ALWAYS AS IDENTITY,
    sup_name TEXT NOT NULL,
    contact_info TEXT,
    requisites TEXT,
    sup_status TEXT NOT NULL DEFAULT 'active',
    CONSTRAINT pk_supplier PRIMARY KEY (supplier_id)
);

-- E7
CREATE TABLE supply (
    supply_id INT GENERATED ALWAYS AS IDENTITY,
    supplier_id INT NOT NULL,
    arrival_date DATE NOT NULL,
    total_cost INT NOT NULL CHECK (total_cost >= 0),
    responsible_person TEXT,
    sup_status TEXT NOT NULL DEFAULT 'created',
    sup_comment TEXT,
    CONSTRAINT pk_supply PRIMARY KEY (supply_id),
    CONSTRAINT fk_supply_supplier
        FOREIGN KEY (supplier_id)
        REFERENCES supplier (supplier_id)
);

-- E8
CREATE TABLE batch (
    batch_id INT GENERATED ALWAYS AS IDENTITY,
    model_id INT NOT NULL,
    supply_id INT NOT NULL,
    arrival_date DATE NOT NULL,
    quantity INT NOT NULL CHECK (quantity >= 0),
    batch_status TEXT NOT NULL DEFAULT 'received',
    purchase_price INT NOT NULL CHECK (purchase_price >= 0),
    current_stock INT NOT NULL DEFAULT 0 CHECK (current_stock >= 0),
    CONSTRAINT pk_batch PRIMARY KEY (batch_id),
    CONSTRAINT fk_batch_model
        FOREIGN KEY (model_id)
        REFERENCES component_model (model_id),

    CONSTRAINT fk_batch_supply
        FOREIGN KEY (supply_id)
        REFERENCES supply (supply_id)
);

-- E9
CREATE TABLE exemplar (
    exemplar_id INT GENERATED ALWAYS AS IDENTITY,
    batch_id INT NOT NULL,
    serial_number INT NOT NULL,
    arrival_date DATE NOT NULL,
    exemp_location TEXT,
    exemp_status TEXT NOT NULL DEFAULT 'in_stock',
    CONSTRAINT pk_exemplar PRIMARY KEY (exemplar_id),
    CONSTRAINT uk_exemplar_serial UNIQUE (serial_number),
    CONSTRAINT fk_exemplar_batch
        FOREIGN KEY (batch_id)
        REFERENCES batch (batch_id)
);

-- E19
CREATE TABLE batch_item (
    batch_id INT NOT NULL,
    model_id INT NOT NULL,
    CONSTRAINT pk_batch_item PRIMARY KEY (batch_id, model_id),
    CONSTRAINT fk_batch_item_batch
        FOREIGN KEY (batch_id)
        REFERENCES batch (batch_id),

    CONSTRAINT fk_batch_item_model
        FOREIGN KEY (model_id)
        REFERENCES component_model (model_id)
);