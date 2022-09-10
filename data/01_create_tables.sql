-- public.nota definition

-- Drop table

-- DROP TABLE public.nota;

CREATE TABLE public.nota (
	id serial4 NOT NULL,
	url varchar(255) NULL,
	created_at timestamp NULL DEFAULT now(),
	updated_at timestamp NULL DEFAULT now(),
	CONSTRAINT nota_pkey PRIMARY KEY (id)
);
CREATE INDEX ix_nota_id ON public.nota USING btree (id);
CREATE INDEX ix_nota_url ON public.nota USING btree (url);

-- public.nota_item definition

-- Drop table

-- DROP TABLE nota_item;

CREATE TABLE nota_item (
	id serial4 NOT NULL,
	id_item varchar(255) NULL,
	nota_id int4 NOT NULL,
	description varchar(255) NULL,
	quantity float8 NULL,
	unit varchar(255) NULL,
	unit_value float8 NULL,
	value float8 NULL,
	created_at timestamp NULL DEFAULT now(),
	updated_at timestamp NULL DEFAULT now(),
	CONSTRAINT nota_item_pkey PRIMARY KEY (id)
);
CREATE INDEX ix_nota_item_id ON public.nota_item USING btree (id);
CREATE INDEX ix_nota_item_id_item ON public.nota_item USING btree (id_item);


-- public.nota_item foreign keys

ALTER TABLE public.nota_item ADD CONSTRAINT nota_item_nota_id_fkey FOREIGN KEY (nota_id) REFERENCES nota(id);