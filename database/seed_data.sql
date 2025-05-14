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

