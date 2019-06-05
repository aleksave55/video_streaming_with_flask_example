CREATE TABLE koristi
(
  id      INT AUTO_INCREMENT
    PRIMARY KEY,
  id_stud INT NULL,
  id_rac  INT NULL
)
  ENGINE = InnoDB;

CREATE INDEX koristi_student_id_fk
  ON koristi (id_stud);

CREATE INDEX koristi_racunar_id_fk
  ON koristi (id_rac);

CREATE TABLE pohadja
(
  id      INT AUTO_INCREMENT
    PRIMARY KEY,
  id_stud INT NULL,
  id_pred INT NULL
)
  ENGINE = InnoDB;

CREATE INDEX pohadja_student_id_fk
  ON pohadja (id_stud);

CREATE INDEX pohadja_predmet_id_fk
  ON pohadja (id_pred);

CREATE TABLE predaje
(
  id      INT AUTO_INCREMENT
    PRIMARY KEY,
  id_prof INT NULL,
  id_pred INT NULL
)
  ENGINE = InnoDB;

CREATE INDEX predaje_profesor_id_fk
  ON predaje (id_prof);

CREATE INDEX predaje_predmet_id_fk
  ON predaje (id_pred);

CREATE TABLE predavanje
(
  id      INT AUTO_INCREMENT
    PRIMARY KEY,
  id_pred INT NULL,
  id_strm INT NULL
)
  ENGINE = InnoDB;

CREATE INDEX predavanje_predmet_id_fk
  ON predavanje (id_pred);

CREATE INDEX predavanje_stream_id_fk
  ON predavanje (id_strm);

CREATE TABLE predmet
(
  id    INT AUTO_INCREMENT
    PRIMARY KEY,
  naziv VARCHAR(256) NOT NULL,
  CONSTRAINT predmet_naziv_uindex
  UNIQUE (naziv)
)
  ENGINE = InnoDB;

ALTER TABLE pohadja
  ADD CONSTRAINT pohadja_predmet_id_fk
FOREIGN KEY (id_pred) REFERENCES predmet (id)
  ON UPDATE CASCADE
  ON DELETE CASCADE;

ALTER TABLE predaje
  ADD CONSTRAINT predaje_predmet_id_fk
FOREIGN KEY (id_pred) REFERENCES predmet (id)
  ON UPDATE CASCADE
  ON DELETE CASCADE;

ALTER TABLE predavanje
  ADD CONSTRAINT predavanje_predmet_id_fk
FOREIGN KEY (id_pred) REFERENCES predmet (id)
  ON UPDATE CASCADE
  ON DELETE CASCADE;

CREATE TABLE prisustvo
(
  id      INT AUTO_INCREMENT
    PRIMARY KEY,
  id_stud INT NULL,
  id_strm INT NULL
)
  ENGINE = InnoDB;

CREATE INDEX prisustvo_student_id_fk
  ON prisustvo (id_stud);

CREATE INDEX prisustvo_stream_id_fk
  ON prisustvo (id_strm);

CREATE TABLE profesor
(
  id        INT AUTO_INCREMENT
    PRIMARY KEY,
  ime       VARCHAR(256) NOT NULL,
  prezime   VARCHAR(256) NOT NULL,
  user_name VARCHAR(256) NOT NULL,
  sifra     VARCHAR(256) NOT NULL,
  CONSTRAINT profesor_user_name_uindex
  UNIQUE (user_name)
)
  ENGINE = InnoDB;

ALTER TABLE predaje
  ADD CONSTRAINT predaje_profesor_id_fk
FOREIGN KEY (id_prof) REFERENCES profesor (id)
  ON UPDATE CASCADE
  ON DELETE CASCADE;

CREATE TABLE racunar
(
  id  INT AUTO_INCREMENT
    PRIMARY KEY,
  kod VARCHAR(256) NOT NULL,
  CONSTRAINT racunar_kod_uindex
  UNIQUE (kod)
)
  ENGINE = InnoDB;

ALTER TABLE koristi
  ADD CONSTRAINT koristi_racunar_id_fk
FOREIGN KEY (id_rac) REFERENCES racunar (id)
  ON UPDATE CASCADE
  ON DELETE CASCADE;

CREATE TABLE stream
(
  id INT AUTO_INCREMENT
    PRIMARY KEY,
  ip VARCHAR(256) NOT NULL,
  CONSTRAINT stream_ip_uindex
  UNIQUE (ip)
)
  ENGINE = InnoDB;

ALTER TABLE predavanje
  ADD CONSTRAINT predavanje_stream_id_fk
FOREIGN KEY (id_strm) REFERENCES stream (id)
  ON UPDATE CASCADE
  ON DELETE CASCADE;

ALTER TABLE prisustvo
  ADD CONSTRAINT prisustvo_stream_id_fk
FOREIGN KEY (id_strm) REFERENCES stream (id)
  ON UPDATE CASCADE
  ON DELETE CASCADE;

CREATE TABLE student
(
  id      INT AUTO_INCREMENT
    PRIMARY KEY,
  ime     VARCHAR(256) NOT NULL,
  prezime VARCHAR(256) NOT NULL,
  indeks  VARCHAR(256) NOT NULL,
  sifra   VARCHAR(256) NOT NULL,
  CONSTRAINT student_indeks_uindex
  UNIQUE (indeks)
)
  ENGINE = InnoDB;

ALTER TABLE koristi
  ADD CONSTRAINT koristi_student_id_fk
FOREIGN KEY (id_stud) REFERENCES student (id)
  ON UPDATE CASCADE
  ON DELETE CASCADE;

ALTER TABLE pohadja
  ADD CONSTRAINT pohadja_student_id_fk
FOREIGN KEY (id_stud) REFERENCES student (id)
  ON UPDATE CASCADE
  ON DELETE CASCADE;

ALTER TABLE prisustvo
  ADD CONSTRAINT prisustvo_student_id_fk
FOREIGN KEY (id_stud) REFERENCES student (id)
  ON UPDATE CASCADE
  ON DELETE CASCADE;


