-- E14
CREATE TABLE dhcp_store.build (
    build_id INT GENERATED ALWAYS AS IDENTITY,
    configuration_id INT NOT NULL,
    build_number VARCHAR(80) NOT NULL,
    build_date DATE NOT NULL DEFAULT CURRENT_DATE,
    installed_components VARCHAR(80),
    assembler VARCHAR(80),
    build_test_info TEXT,
    build_status VARCHAR(20) NOT NULL DEFAULT 'in_progress' CHECK (build_status IN ('in_progress', 'assembled', 'testing_passed', 'testing_failed', 'completed')),
    build_comment VARCHAR(80),
    CONSTRAINT pk_build PRIMARY KEY (build_id),
    CONSTRAINT uk_build_number UNIQUE (build_number),
    CONSTRAINT fk_build_configuration
        FOREIGN KEY (configuration_id)
        REFERENCES dhcp_store.build_configuration (configuration_id)
);

-- E15
CREATE TABLE dhcp_store.build_test (
    test_id INT GENERATED ALWAYS AS IDENTITY,
    build_id INT NOT NULL,
    test_status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (test_status IN ('pending', 'running', 'passed', 'failed', 'error')),
    build_comment VARCHAR(500),
    test_date DATE NOT NULL DEFAULT CURRENT_DATE,
    CONSTRAINT pk_build_test PRIMARY KEY (test_id),
    CONSTRAINT fk_build_test_build
        FOREIGN KEY (build_id)
        REFERENCES dhcp_store.build (build_id)
);

-- E16
CREATE TABLE dhcp_store.test_result (
    test_result_id INT GENERATED ALWAYS AS IDENTITY,
    test_id INT NOT NULL,
    test_name VARCHAR(80) NOT NULL,
    result_date DATE NOT NULL DEFAULT CURRENT_DATE,
    test_status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (test_status IN ('pending', 'passed', 'failed', 'skipped', 'warning')),
    CONSTRAINT pk_test_result PRIMARY KEY (test_result_id),
    CONSTRAINT fk_test_result_test
        FOREIGN KEY (test_id)
        REFERENCES dhcp_store.build_test (test_id)
);

-- E20
CREATE TABLE dhcp_store.build_item (
    build_id INT NOT NULL,
    exemplar_id INT NOT NULL,
    CONSTRAINT pk_build_item PRIMARY KEY (build_id, exemplar_id),
    CONSTRAINT fk_build_item_build
        FOREIGN KEY (build_id)
        REFERENCES dhcp_store.build (build_id),

    CONSTRAINT fk_build_item_exemplar
        FOREIGN KEY (exemplar_id)
        REFERENCES dhcp_store.exemplar (exemplar_id)
);