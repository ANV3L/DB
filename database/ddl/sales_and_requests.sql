-- E14
CREATE TABLE build (
    build_id INT GENERATED ALWAYS AS IDENTITY,
    configuration_id INT NOT NULL,
    build_number TEXT NOT NULL,
    build_date DATE NOT NULL DEFAULT CURRENT_DATE,
    installed_components TEXT,
    assembler TEXT,
    build_test_info TEXT,
    build_status TEXT NOT NULL DEFAULT 'in_progress',
    build_comment TEXT,
    CONSTRAINT pk_build PRIMARY KEY (build_id),
    CONSTRAINT uk_build_number UNIQUE (build_number),
    CONSTRAINT fk_build_configuration
        FOREIGN KEY (configuration_id)
        REFERENCES build_configuration (configuration_id)
);

-- E15
CREATE TABLE build_test (
    test_id INT GENERATED ALWAYS AS IDENTITY,
    build_id INT NOT NULL,
    build_status TEXT NOT NULL DEFAULT 'pending',
    build_comment TEXT,
    test_date DATE NOT NULL DEFAULT CURRENT_DATE,
    CONSTRAINT pk_build_test PRIMARY KEY (test_id),
    CONSTRAINT fk_build_test_build
        FOREIGN KEY (build_id)
        REFERENCES build (build_id)
);

-- E16
CREATE TABLE test_result (
    test_result_id INT GENERATED ALWAYS AS IDENTITY,
    test_id INT NOT NULL,
    test_name TEXT NOT NULL,
    result_date DATE NOT NULL DEFAULT CURRENT_DATE,
    test_status TEXT NOT NULL DEFAULT 'pending',
    CONSTRAINT pk_test_result PRIMARY KEY (test_result_id),
    CONSTRAINT fk_test_result_test
        FOREIGN KEY (test_id)
        REFERENCES build_test (test_id)
);

-- E20
CREATE TABLE build_item (
    build_id INT NOT NULL,
    exemplar_id INT NOT NULL,
    CONSTRAINT pk_build_item PRIMARY KEY (build_id, exemplar_id),
    CONSTRAINT fk_build_item_build
        FOREIGN KEY (build_id)
        REFERENCES build (build_id),

    CONSTRAINT fk_build_item_exemplar
        FOREIGN KEY (exemplar_id)
        REFERENCES exemplar (exemplar_id)
);