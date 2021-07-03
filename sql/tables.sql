CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `first_name` char(35) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_name` char(35) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` timestamp NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into users values (1, "Jane", "Smith", NOW(), NOW(), NULL);
insert into users values (2, "John", "Doe", NOW(), NOW(), NULL);