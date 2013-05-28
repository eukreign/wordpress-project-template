<?php
define('WP_DEFAULT_THEME', '[Project Name]');
define('DB_NAME', '[Project Name]');
define('DB_USER', 'graftonweb');
define('DB_PASSWORD', 'graftonweb');
define('DB_HOST', 'localhost');
define('DB_CHARSET', 'utf8');
define('DB_COLLATE', '');
$table_prefix  = 'wp_';

define('AUTH_KEY',         '[Project Random Key 1]');
define('SECURE_AUTH_KEY',  '[Project Random Key 2]');
define('LOGGED_IN_KEY',    '[Project Random Key 3]');
define('NONCE_KEY',        '[Project Random Key 4]');
define('AUTH_SALT',        '[Project Random Key 5]');
define('SECURE_AUTH_SALT', '[Project Random Key 6]');
define('LOGGED_IN_SALT',   '[Project Random Key 7]');
define('NONCE_SALT',       '[Project Random Key 8]');

define('WPLANG', '');
define('WP_DEBUG', false);

define('WP_SITEURL', 'http://' . $_SERVER['SERVER_NAME'] . '/wordpress');
define('WP_HOME',    'http://' . $_SERVER['SERVER_NAME']);
define('WP_CONTENT_URL', 'http://' . $_SERVER['SERVER_NAME'] . '/wp-content');
define('WP_CONTENT_DIR', dirname(__FILE__) . '/wp-content');

require_once(ABSPATH . 'wp-settings.php');
