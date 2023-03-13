-- ----------------------------
-- Table structure for contractors
-- ----------------------------
DROP TABLE IF EXISTS "public"."contractors";
CREATE TABLE "public"."contractors" (
  "id" serial primary key,
  "business_name" varchar(255) COLLATE "pg_catalog"."default",
  "contact_name" varchar(255) COLLATE "pg_catalog"."default",
  "phone" varchar(255) COLLATE "pg_catalog"."default",
  "addr" varchar(255) COLLATE "pg_catalog"."default",
  "city" varchar(255) COLLATE "pg_catalog"."default",
  "state" varchar(255) COLLATE "pg_catalog"."default",
  "zip" varchar(255) COLLATE "pg_catalog"."default",
  "email" varchar(255) COLLATE "pg_catalog"."default",
  "logo" varchar(255) COLLATE "pg_catalog"."default",
  "license_number" varchar(255) COLLATE "pg_catalog"."default",
  "license_state" varchar(255) COLLATE "pg_catalog"."default",
  "added_date" DATE
)
;

-- ----------------------------
-- Table structure for customers
-- ----------------------------
DROP TABLE IF EXISTS "public"."customers";
CREATE TABLE "public"."customers" (
  "id" int4 NOT NULL,
  "name" varchar(255) COLLATE "pg_catalog"."default",
  "phone" varchar(255) COLLATE "pg_catalog"."default",
  "addr" varchar(255) COLLATE "pg_catalog"."default",
  "city" varchar(255) COLLATE "pg_catalog"."default",
  "state" varchar(255) COLLATE "pg_catalog"."default",
  "zip" varchar(255) COLLATE "pg_catalog"."default",
  "email" varchar(255) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for esitmates
-- ----------------------------
DROP TABLE IF EXISTS "public"."esitmates";
CREATE TABLE "public"."esitmates" (
  "id" int4 NOT NULL,
  "project_id" int4,
  "date" date,
  "location" varchar(255) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for prices
-- ----------------------------
DROP TABLE IF EXISTS "public"."prices";
CREATE TABLE "public"."prices" (
  "id" int4 NOT NULL,
  "contractor_id" int4,
  "project_type_id" int4,
  "price_per_unit" varchar(255) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for project_types
-- ----------------------------
DROP TABLE IF EXISTS "public"."project_types";
CREATE TABLE "public"."project_types" (
  "id" int4 NOT NULL,
  "name" varchar(255) COLLATE "pg_catalog"."default",
  "description" varchar(255) COLLATE "pg_catalog"."default",
  "materials" varchar(255) COLLATE "pg_catalog"."default",
  "units" varchar(255) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for projects
-- ----------------------------
DROP TABLE IF EXISTS "public"."projects";
CREATE TABLE "public"."projects" (
  "id" int4 NOT NULL,
  "contractor_id" int4,
  "customer_id" int4
)
;

-- ----------------------------
-- Table structure for subprojects
-- ----------------------------
DROP TABLE IF EXISTS "public"."subprojects";
CREATE TABLE "public"."subprojects" (
  "id" int4 NOT NULL,
  "name" varchar(255) COLLATE "pg_catalog"."default",
  "project_id" int4,
  "length" float8,
  "width" float8,
  "height" float8,
  "project_type" varchar(255) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Primary Key structure for table contractors
-- ----------------------------
ALTER TABLE "public"."contractors" ADD CONSTRAINT "contractor_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table customers
-- ----------------------------
ALTER TABLE "public"."customers" ADD CONSTRAINT "customers_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table esitmates
-- ----------------------------
ALTER TABLE "public"."esitmates" ADD CONSTRAINT "esitmates_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table prices
-- ----------------------------
ALTER TABLE "public"."prices" ADD CONSTRAINT "prices_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table project_types
-- ----------------------------
ALTER TABLE "public"."project_types" ADD CONSTRAINT "project_types_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table projects
-- ----------------------------
ALTER TABLE "public"."projects" ADD CONSTRAINT "projects_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table subprojects
-- ----------------------------
ALTER TABLE "public"."subprojects" ADD CONSTRAINT "subprojects_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table esitmates
-- ----------------------------
ALTER TABLE "public"."esitmates" ADD CONSTRAINT "project" FOREIGN KEY ("project_id") REFERENCES "public"."projects" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table prices
-- ----------------------------
ALTER TABLE "public"."prices" ADD CONSTRAINT "contractor" FOREIGN KEY ("contractor_id") REFERENCES "public"."contractors" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."prices" ADD CONSTRAINT "project_type" FOREIGN KEY ("project_type_id") REFERENCES "public"."project_types" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table projects
-- ----------------------------
ALTER TABLE "public"."projects" ADD CONSTRAINT "contractor" FOREIGN KEY ("contractor_id") REFERENCES "public"."contractors" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."projects" ADD CONSTRAINT "customer" FOREIGN KEY ("customer_id") REFERENCES "public"."customers" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table subprojects
-- ----------------------------
ALTER TABLE "public"."subprojects" ADD CONSTRAINT "project" FOREIGN KEY ("project_id") REFERENCES "public"."projects" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
