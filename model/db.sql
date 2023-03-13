CREATE DATABASE colout
    WITH
    OWNER = postgres
    TEMPLATE = template0
    ENCODING = 'UTF8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

COMMENT ON DATABASE colout
    IS 'Test DB for Columbia Outdoor';