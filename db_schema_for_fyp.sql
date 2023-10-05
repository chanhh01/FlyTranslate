use flytranslate;

create table users(
	user_id bigint unsigned not null auto_increment,
    username varchar(255) not null,
    email varchar(255) not null,
    pass varchar(255) not null,
    user_role varchar(255) not null,
    primary key(user_id)
);

create table languages(
	lang_id bigint unsigned not null auto_increment,
    lang_name varchar(255) not null,
    lang_code varchar(255) not null,
    lang_code_for_ocr varchar(10) null,
    display_lang_font_dir varchar(255) null,
	primary key(lang_id)
);

create table user_settings(
	setting_id bigint unsigned not null auto_increment,
    user_id bigint unsigned not null,
    source_lang bigint unsigned not null,
    target_lang bigint unsigned not null,
    x1_coord double null default 0,
    y1_coord double null default 0,
    x2_coord double null default 0,
    y2_coord double null default 0,
    full_screen int default 0,
    save_log int default 0,
    text_replacement_bool int default 0,
    minimize_upon_login int default 0,
    foreign key (user_id) references users(user_id) on update cascade,
    foreign key (source_lang) references languages(lang_id) on update cascade,
    foreign key (target_lang) references languages(lang_id) on update cascade,
	primary key(setting_id)
);

create table device_session(
	session_id bigint unsigned not null auto_increment,
    user_id bigint unsigned not null,
    mac_address varchar(255) not null,
    foreign key (user_id) references users(user_id) on update cascade,
	primary key(session_id)
);

create table report_feedback(
	report_id bigint unsigned not null auto_increment,
    user_id bigint unsigned not null,
    title varchar(255) not null,
    content longtext not null,
    archived_or_replied int default 0,
    foreign key (user_id) references users(user_id) on update cascade,
	primary key(report_id)
);

create table faq(
	faq_id bigint unsigned not null auto_increment,
    faq_title varchar(255) not null,
    faq_content longtext not null,
	primary key(faq_id)
);

insert into users (username, email, pass, user_role) values ('admin123', 'admin123@gmail.com', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', 'admin');
insert into user_settings (user_id, source_lang, target_lang, x1_coord, y1_coord, x2_coord, y2_coord, auto_source, full_screen, save_log, text_replacement_bool, translate_on_launch, remember_device)
values (1, 37, 182, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0);
