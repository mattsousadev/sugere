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