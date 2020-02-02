--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: books; Type: TABLE; Schema: public; Owner: archi144
--

CREATE TABLE public.books (
    id integer NOT NULL,
    name text NOT NULL,
    author text NOT NULL,
    type text
);


ALTER TABLE public.books OWNER TO archi144;

--
-- Name: Books_id_seq; Type: SEQUENCE; Schema: public; Owner: archi144
--

CREATE SEQUENCE public."Books_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Books_id_seq" OWNER TO archi144;

--
-- Name: Books_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: archi144
--

ALTER SEQUENCE public."Books_id_seq" OWNED BY public.books.id;


--
-- Name: readers; Type: TABLE; Schema: public; Owner: archi144
--

CREATE TABLE public.readers (
    id integer NOT NULL,
    surname text NOT NULL,
    name text NOT NULL,
    patronymic text,
    studbilet text NOT NULL,
    biletexpiredin date NOT NULL,
    vioaltor boolean
);


ALTER TABLE public.readers OWNER TO archi144;

--
-- Name: Reader_id_seq; Type: SEQUENCE; Schema: public; Owner: archi144
--

CREATE SEQUENCE public."Reader_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Reader_id_seq" OWNER TO archi144;

--
-- Name: Reader_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: archi144
--

ALTER SEQUENCE public."Reader_id_seq" OWNED BY public.readers.id;


--
-- Name: django_reader_books; Type: TABLE; Schema: public; Owner: archi144
--

CREATE TABLE public.django_reader_books (
    id integer NOT NULL,
    name text,
    author text,
    date_return date,
    type text,
    reader_id integer
);


ALTER TABLE public.django_reader_books OWNER TO archi144;

--
-- Name: electronicbook; Type: TABLE; Schema: public; Owner: archi144
--

CREATE TABLE public.electronicbook (
    id integer NOT NULL,
    link text NOT NULL,
    id_book integer
);


ALTER TABLE public.electronicbook OWNER TO archi144;

--
-- Name: paperbook; Type: TABLE; Schema: public; Owner: archi144
--

CREATE TABLE public.paperbook (
    id integer NOT NULL,
    countofvolumes integer NOT NULL,
    id_book integer NOT NULL,
    CONSTRAINT chk_type CHECK ((countofvolumes >= 0))
);


ALTER TABLE public.paperbook OWNER TO archi144;

--
-- Name: paperbook_id_seq; Type: SEQUENCE; Schema: public; Owner: archi144
--

CREATE SEQUENCE public.paperbook_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.paperbook_id_seq OWNER TO archi144;

--
-- Name: paperbook_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: archi144
--

ALTER SEQUENCE public.paperbook_id_seq OWNED BY public.paperbook.id;


--
-- Name: readers_books; Type: TABLE; Schema: public; Owner: archi144
--

CREATE TABLE public.readers_books (
    id_reader integer,
    id_book integer,
    datereturn date NOT NULL
);


ALTER TABLE public.readers_books OWNER TO archi144;

--
-- Name: users; Type: TABLE; Schema: public; Owner: archi144
--

CREATE TABLE public.users (
    id integer NOT NULL,
    login text NOT NULL,
    password text NOT NULL,
    role text
);


ALTER TABLE public.users OWNER TO archi144;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: archi144
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO archi144;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: archi144
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: books id; Type: DEFAULT; Schema: public; Owner: archi144
--

ALTER TABLE ONLY public.books ALTER COLUMN id SET DEFAULT nextval('public."Books_id_seq"'::regclass);


--
-- Name: paperbook id; Type: DEFAULT; Schema: public; Owner: archi144
--

ALTER TABLE ONLY public.paperbook ALTER COLUMN id SET DEFAULT nextval('public.paperbook_id_seq'::regclass);


--
-- Name: readers id; Type: DEFAULT; Schema: public; Owner: archi144
--

ALTER TABLE ONLY public.readers ALTER COLUMN id SET DEFAULT nextval('public."Reader_id_seq"'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: archi144
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: archi144
--

COPY public.books (id, name, author, type) FROM stdin;
3	Книга Марка	Марк	Электронная
4	Книга Дастана	Дастан	Электронная
1	Книга Артура	Артур	Печатная
2	Книга Алексея	Алексей	Печатная
\.


--
-- Data for Name: django_reader_books; Type: TABLE DATA; Schema: public; Owner: archi144
--

COPY public.django_reader_books (id, name, author, date_return, type, reader_id) FROM stdin;
\.


--
-- Data for Name: electronicbook; Type: TABLE DATA; Schema: public; Owner: archi144
--

COPY public.electronicbook (id, link, id_book) FROM stdin;
2	www.dastan.com	4
1	www.mark.com	3
\.


--
-- Data for Name: paperbook; Type: TABLE DATA; Schema: public; Owner: archi144
--

COPY public.paperbook (id, countofvolumes, id_book) FROM stdin;
2	13	2
1	9	1
\.


--
-- Data for Name: readers; Type: TABLE DATA; Schema: public; Owner: archi144
--

COPY public.readers (id, surname, name, patronymic, studbilet, biletexpiredin, vioaltor) FROM stdin;
15	Алексеев	Алексей	Алексеевич	12512515	2021-01-09	f
16	Фолькин	Марк	\N	125125125	2021-02-03	f
14	Мечетин	Артур	Гамлетович	124125125	2021-01-05	f
\.


--
-- Data for Name: readers_books; Type: TABLE DATA; Schema: public; Owner: archi144
--

COPY public.readers_books (id_reader, id_book, datereturn) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: archi144
--

COPY public.users (id, login, password, role) FROM stdin;
1	SysAdmin	SysAdmin	Системный администратор
2	LibAdmin	LibAdmin	Администратор библиотеки
3	LibWorker	LibWorker	Библиотекарь
\.


--
-- Name: Books_id_seq; Type: SEQUENCE SET; Schema: public; Owner: archi144
--

SELECT pg_catalog.setval('public."Books_id_seq"', 1, true);


--
-- Name: Reader_id_seq; Type: SEQUENCE SET; Schema: public; Owner: archi144
--

SELECT pg_catalog.setval('public."Reader_id_seq"', 31, true);


--
-- Name: paperbook_id_seq; Type: SEQUENCE SET; Schema: public; Owner: archi144
--

SELECT pg_catalog.setval('public.paperbook_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: archi144
--

SELECT pg_catalog.setval('public.users_id_seq', 125, true);


--
-- Name: books Books_pkey; Type: CONSTRAINT; Schema: public; Owner: archi144
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT "Books_pkey" PRIMARY KEY (id);


--
-- Name: readers Reader_pkey; Type: CONSTRAINT; Schema: public; Owner: archi144
--

ALTER TABLE ONLY public.readers
    ADD CONSTRAINT "Reader_pkey" PRIMARY KEY (id);


--
-- Name: django_reader_books django_reader_books_pk; Type: CONSTRAINT; Schema: public; Owner: archi144
--

ALTER TABLE ONLY public.django_reader_books
    ADD CONSTRAINT django_reader_books_pk PRIMARY KEY (id);


--
-- Name: electronicbook electonicbook_pk; Type: CONSTRAINT; Schema: public; Owner: archi144
--

ALTER TABLE ONLY public.electronicbook
    ADD CONSTRAINT electonicbook_pk PRIMARY KEY (id);


--
-- Name: paperbook paperbook_pk; Type: CONSTRAINT; Schema: public; Owner: archi144
--

ALTER TABLE ONLY public.paperbook
    ADD CONSTRAINT paperbook_pk PRIMARY KEY (id);


--
-- Name: users users_pk; Type: CONSTRAINT; Schema: public; Owner: archi144
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pk PRIMARY KEY (id);


--
-- Name: django_reader_books_id_uindex; Type: INDEX; Schema: public; Owner: archi144
--

CREATE UNIQUE INDEX django_reader_books_id_uindex ON public.django_reader_books USING btree (id);


--
-- Name: electonicbook_id_book_uindex; Type: INDEX; Schema: public; Owner: archi144
--

CREATE UNIQUE INDEX electonicbook_id_book_uindex ON public.electronicbook USING btree (id_book);


--
-- Name: electonicbook_id_uindex; Type: INDEX; Schema: public; Owner: archi144
--

CREATE UNIQUE INDEX electonicbook_id_uindex ON public.electronicbook USING btree (id);


--
-- Name: electonicbook_link_uindex; Type: INDEX; Schema: public; Owner: archi144
--

CREATE UNIQUE INDEX electonicbook_link_uindex ON public.electronicbook USING btree (link);


--
-- Name: readers_phone_uindex; Type: INDEX; Schema: public; Owner: archi144
--

CREATE UNIQUE INDEX readers_phone_uindex ON public.readers USING btree (studbilet);


--
-- Name: typesbook_id_uindex; Type: INDEX; Schema: public; Owner: archi144
--

CREATE UNIQUE INDEX typesbook_id_uindex ON public.paperbook USING btree (id);


--
-- Name: users_id_uindex; Type: INDEX; Schema: public; Owner: archi144
--

CREATE UNIQUE INDEX users_id_uindex ON public.users USING btree (id);


--
-- Name: electronicbook electonicbook_books_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: archi144
--

ALTER TABLE ONLY public.electronicbook
    ADD CONSTRAINT electonicbook_books_id_fk FOREIGN KEY (id_book) REFERENCES public.books(id) ON DELETE CASCADE;


--
-- Name: paperbook paperbook_books_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: archi144
--

ALTER TABLE ONLY public.paperbook
    ADD CONSTRAINT paperbook_books_id_fk FOREIGN KEY (id_book) REFERENCES public.books(id) ON DELETE CASCADE;


--
-- Name: readers_books readers_books_books_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: archi144
--

ALTER TABLE ONLY public.readers_books
    ADD CONSTRAINT readers_books_books_id_fk FOREIGN KEY (id_book) REFERENCES public.books(id);


--
-- Name: readers_books readers_books_readers_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: archi144
--

ALTER TABLE ONLY public.readers_books
    ADD CONSTRAINT readers_books_readers_id_fk FOREIGN KEY (id_reader) REFERENCES public.readers(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

