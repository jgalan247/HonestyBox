-- Admin user
INSERT INTO user (username, password_h, email, lat, lon, role, confirmed)
VALUES (
  'admin',
  '$argon2id$v=19$m=65536,t=3,p=4$bK1VCsFYa83Z29u79/6fkw$9WSq61Uevm6o6ClQpWbagIcMNvFXrNFfTW34ICy3xE0',
  'admin@example.com',
  '49.2',
  '-2.1',
  'admin',
  1
);

-- Farmer
INSERT INTO user (username, password_h, email, lat, lon, role, confirmed)
VALUES (
  'farmerjoe',
  '$argon2id$v=19$m=65536,t=3,p=4$CkqU2zSICnGSy/5mM0GEdw$k5b7Q3l8j/NlVRmEAhSwhKApBaRR7f1AZDnpX0joiBQ',
  'joe@example.com',
  '49.3',
  '-2.2',
  'farmer',
  1
);

-- Product
INSERT INTO product (name, description, price, available, owner_id)
VALUES ('Tomatoes', 'Fresh from the farm', '2.50', 'yes', 2);

