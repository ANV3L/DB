-- E6
CREATE TABLE dhcp_store.supplier (
    supplier_id INT GENERATED ALWAYS AS IDENTITY,
    sup_name VARCHAR(80) NOT NULL,
    contact_info VARCHAR(250),
    requisites VARCHAR(250),
    sup_status VARCHAR(20) NOT NULL DEFAULT 'active' CHECK (sup_status IN ('active', 'inactive', 'blacklisted')),
    CONSTRAINT pk_supplier PRIMARY KEY (supplier_id)
);

-- E7
CREATE TABLE dhcp_store.supply (
    supply_id INT GENERATED ALWAYS AS IDENTITY,
    supplier_id INT NOT NULL,
    arrival_date DATE NOT NULL DEFAULT CURRENT_DATE,
    total_cost INT NOT NULL CHECK (total_cost >= 0),
    responsible_person VARCHAR(150),
    sup_status VARCHAR(20) NOT NULL DEFAULT 'created' CHECK (sup_status IN ('created', 'in_transit', 'delivered', 'cancelled')),
    sup_comment VARCHAR(320),

    CONSTRAINT pk_supply PRIMARY KEY (supply_id),
    CONSTRAINT fk_supply_supplier
        FOREIGN KEY (supplier_id)
        REFERENCES dhcp_store.supplier (supplier_id)
);

-- E8
CREATE TABLE dhcp_store.batch (
    batch_id INT GENERATED ALWAYS AS IDENTITY,
    model_id INT NOT NULL,
    supply_id INT NOT NULL,
    arrival_date DATE NOT NULL,
    quantity INT NOT NULL CHECK (quantity >= 0),
    batch_status VARCHAR(20) NOT NULL DEFAULT 'received' CHECK (batch_status IN ('received', 'depleted', 'written_off')),
    purchase_price NUMERIC(12, 2) NOT NULL CHECK (purchase_price >= 0),
    current_stock INT NOT NULL DEFAULT 0 CHECK (current_stock >= 0),
    CONSTRAINT pk_batch PRIMARY KEY (batch_id),
    CONSTRAINT fk_batch_model
        FOREIGN KEY (model_id)
        REFERENCES dhcp_store.component_model (model_id),

    CONSTRAINT fk_batch_supply
        FOREIGN KEY (supply_id)
        REFERENCES dhcp_store.supply (supply_id)
);

-- E9
CREATE TABLE dhcp_store.exemplar (
    exemplar_id INT GENERATED ALWAYS AS IDENTITY,
    batch_id INT NOT NULL,
    serial_number VARCHAR(80) NOT NULL,
    arrival_date DATE NOT NULL,
    exemp_location VARCHAR(100),
    exemp_status VARCHAR(20) NOT NULL DEFAULT 'in_stock' CHECK (exemp_status IN ('in_stock', 'reserved', 'sold', 'defective', 'written_off')),
    CONSTRAINT pk_exemplar PRIMARY KEY (exemplar_id),
    CONSTRAINT uk_exemplar_serial UNIQUE (serial_number),
    CONSTRAINT fk_exemplar_batch
        FOREIGN KEY (batch_id)
        REFERENCES dhcp_store.batch (batch_id)
);

-- E19
CREATE TABLE dhcp_store.batch_item (
    batch_id INT NOT NULL,
    model_id INT NOT NULL,
    CONSTRAINT pk_batch_item PRIMARY KEY (batch_id, model_id),
    CONSTRAINT fk_batch_item_batch
        FOREIGN KEY (batch_id)
        REFERENCES dhcp_store.batch (batch_id),

    CONSTRAINT fk_batch_item_model
        FOREIGN KEY (model_id)
        REFERENCES dhcp_store.component_model (model_id)
);