CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` char(35) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_name` char(35) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

insert into users values
(1, "Jane", "Smith", NOW(), NOW(), NULL),
(2, "John", "Doe", NOW(), NOW(), NULL),
(3, "Anne", "Onimus", NOW(), NOW(), NULL);

CREATE TABLE `video_actions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `device` char(35) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `action` char(35) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `date_actioned` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into video_actions values
(NULL, 1, "Windows 10", "start", 100),
(NULL, 2, "OSX 15.4", "start", 200),
(NULL, 1, "iPhone 8s", "start", 250),
(NULL, 1, "Windows 10", "stop", 370),
(NULL, 1, "iPhone 8s", "stop", 410),
(NULL, 2, "OSX 15.4", "stop", 490),
(NULL, 3, "Android 9.1", "start", 700)
;

