--
-- PostgreSQL database dump
--

-- Dumped from database version 14.10
-- Dumped by pg_dump version 14.4 (Ubuntu 14.4-1.pgdg20.04+1)

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
-- Name: participant_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.participant_data (
    participant_id text,
    step_number text,
    "timestamp" timestamp without time zone
);

ALTER TABLE ONLY public.participant_data REPLICA IDENTITY FULL;


ALTER TABLE public.participant_data OWNER TO postgres;

--
-- Data for Name: participant_data; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.participant_data (participant_id, step_number, "timestamp") FROM stdin;
participant_1	1	2024-03-02 12:00:00
participant_2	1	2024-03-02 12:00:00
participant_1	2	2024-03-02 12:30:00
participant_3	2	2024-03-02 12:30:00
participant_4	2	2024-03-02 12:30:00
participant_1	3	2024-03-02 12:45:00
participant_2	2	2024-03-02 12:30:00
participant_1	1	2024-03-02 13:00:00
participant_3	1	2024-03-02 13:00:00
participant_2	4	2024-03-02 13:00:00
participant_1	7	2024-03-02 14:00:00
participant_1	11	2024-03-02 14:30:00
participant_4	1	2024-03-02 14:30:00
participant_1	12	2024-03-02 15:15:00
participant_1	12	2024-03-02 15:15:00
participant_2	13	2024-03-02 15:30:00
participant_3	9	2024-03-02 15:15:00
participant_1	14	2024-03-02 15:15:00
participant_1	15	2024-03-02 16:00:00
\.


--
-- PostgreSQL database dump complete
--

