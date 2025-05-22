-- Categorias
INSERT INTO categories (id, description) VALUES
(1, 'chapas'),
(2, 'tubos'),
(3, 'laminados (cantoneiras e vigas)'),
(4, 'instrumentos (válvulas)'),
(5, 'conexões');

-- Materiais
INSERT INTO materials (id, description) VALUES
(1, 'Inox 316'),
(2, 'Inox 304'),
(3, 'Latão'),
(4, 'Alumínio'),
(5, 'Duplex'),
(6, 'Aço Carbono');

-- Fornecedores
INSERT INTO suppliers (id, name, email) VALUES
(1, 'SteelFlow Ltd.', 'contact@steelflow.com'),
(2, 'InoxPrime', 'vendas@inoxprime.com.br'),
(3, 'FlatFab Metals', 'hello@flatfabmetals.com'),
(4, 'BrassControl', 'sales@brasscontrol.io'),
(5, 'VálvulaMais', 'suporte@valvulamais.ind.br'),
(6, 'PrecisaTech', 'atendimento@precisatech.com.br');

-- supplier_materials (fornecedores por categoria + material)
-- Categoria 1 (chapas) + Material 2 (Inox 304)
INSERT INTO supplier_materials (supplier_id, category_id, material_id) VALUES
(1, 1, 2),
(2, 1, 2),
(3, 1, 2);

-- Categoria 4 (instrumentos) + Material 3 (Latão)
INSERT INTO supplier_materials (supplier_id, category_id, material_id) VALUES
(4, 4, 3),
(5, 4, 3),
(6, 4, 3);

-- Categoria 5 (conexões) + Material 5 (Duplex)
INSERT INTO supplier_materials (supplier_id, category_id, material_id) VALUES
(1, 5, 5),
(3, 5, 5),
(5, 5, 5);
