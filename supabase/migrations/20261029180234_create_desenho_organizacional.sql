create table public.desenho_projetos (
  id uuid primary key default gen_random_uuid(),
  owner_id uuid not null default auth.uid() references auth.users(id) on delete cascade,
  aberto_em date not null default current_date,
  prazo date,
  processo_sei text,
  subtitulo text,
  estado text not null default 'em_elaboracao' check (estado in ('em_elaboracao','concluida')),
  meta_tipo text not null default 'sem_meta' check (meta_tipo in ('sem_meta','manter','reduzir','aumentar')),
  meta_pontos numeric(12,2) not null default 0 check (meta_pontos >= 0),
  criado_em timestamptz not null default now(),
  atualizado_em timestamptz not null default now()
);

create table public.desenho_cenarios (
  id uuid primary key default gen_random_uuid(),
  projeto_id uuid not null references public.desenho_projetos(id) on delete cascade,
  nome text not null,
  principal boolean not null default false,
  dados jsonb not null default '{}'::jsonb,
  criado_em timestamptz not null default now(),
  atualizado_em timestamptz not null default now(),
  unique (projeto_id, nome)
);

create unique index desenho_cenarios_um_principal on public.desenho_cenarios (projeto_id) where principal;
create index desenho_cenarios_projeto_idx on public.desenho_cenarios (projeto_id);

create table public.desenho_revisoes (
  id bigint generated always as identity primary key,
  cenario_id uuid not null references public.desenho_cenarios(id) on delete cascade,
  versao integer not null check (versao > 0),
  snapshot jsonb not null,
  resumo text,
  criado_por uuid not null default auth.uid() references auth.users(id),
  criado_em timestamptz not null default now(),
  unique (cenario_id, versao)
);

create index desenho_revisoes_cenario_idx on public.desenho_revisoes (cenario_id, versao desc);

create table public.desenho_publicacoes (
  id uuid primary key default gen_random_uuid(),
  projeto_id uuid not null references public.desenho_projetos(id) on delete cascade,
  cenario_id uuid not null references public.desenho_cenarios(id) on delete cascade,
  slug text not null unique check (slug ~ '^[a-z0-9]+(?:-[a-z0-9]+)*$'),
  dados_publicos jsonb not null,
  ativo boolean not null default true,
  publicado_em timestamptz not null default now(),
  atualizado_em timestamptz not null default now()
);

create index desenho_publicacoes_projeto_idx on public.desenho_publicacoes (projeto_id);

alter table public.desenho_projetos enable row level security;
alter table public.desenho_cenarios enable row level security;
alter table public.desenho_revisoes enable row level security;
alter table public.desenho_publicacoes enable row level security;

revoke all on public.desenho_projetos from anon, authenticated;
revoke all on public.desenho_cenarios from anon, authenticated;
revoke all on public.desenho_revisoes from anon, authenticated;
revoke all on public.desenho_publicacoes from anon, authenticated;

grant select, insert, update, delete on public.desenho_projetos to authenticated;
grant select, insert, update, delete on public.desenho_cenarios to authenticated;
grant select, insert, update, delete on public.desenho_revisoes to authenticated;
grant select, insert, update, delete on public.desenho_publicacoes to authenticated;
grant select on public.desenho_publicacoes to anon;
grant usage, select on sequence public.desenho_revisoes_id_seq to authenticated;

create policy desenho_projetos_owner_select on public.desenho_projetos for select to authenticated
  using ((select auth.uid()) = owner_id);
create policy desenho_projetos_owner_insert on public.desenho_projetos for insert to authenticated
  with check ((select auth.uid()) = owner_id);
create policy desenho_projetos_owner_update on public.desenho_projetos for update to authenticated
  using ((select auth.uid()) = owner_id) with check ((select auth.uid()) = owner_id);
create policy desenho_projetos_owner_delete on public.desenho_projetos for delete to authenticated
  using ((select auth.uid()) = owner_id);

create policy desenho_cenarios_owner_select on public.desenho_cenarios for select to authenticated
  using (exists (select 1 from public.desenho_projetos p where p.id = projeto_id and p.owner_id = (select auth.uid())));
create policy desenho_cenarios_owner_insert on public.desenho_cenarios for insert to authenticated
  with check (exists (select 1 from public.desenho_projetos p where p.id = projeto_id and p.owner_id = (select auth.uid())));
create policy desenho_cenarios_owner_update on public.desenho_cenarios for update to authenticated
  using (exists (select 1 from public.desenho_projetos p where p.id = projeto_id and p.owner_id = (select auth.uid())))
  with check (exists (select 1 from public.desenho_projetos p where p.id = projeto_id and p.owner_id = (select auth.uid())));
create policy desenho_cenarios_owner_delete on public.desenho_cenarios for delete to authenticated
  using (exists (select 1 from public.desenho_projetos p where p.id = projeto_id and p.owner_id = (select auth.uid())));

create policy desenho_revisoes_owner_select on public.desenho_revisoes for select to authenticated
  using (exists (
    select 1 from public.desenho_cenarios c join public.desenho_projetos p on p.id = c.projeto_id
    where c.id = cenario_id and p.owner_id = (select auth.uid())
  ));
create policy desenho_revisoes_owner_insert on public.desenho_revisoes for insert to authenticated
  with check (
    criado_por = (select auth.uid()) and exists (
      select 1 from public.desenho_cenarios c join public.desenho_projetos p on p.id = c.projeto_id
      where c.id = cenario_id and p.owner_id = (select auth.uid())
    )
  );

create policy desenho_publicacoes_owner_select on public.desenho_publicacoes for select to authenticated
  using (exists (select 1 from public.desenho_projetos p where p.id = projeto_id and p.owner_id = (select auth.uid())));
create policy desenho_publicacoes_owner_insert on public.desenho_publicacoes for insert to authenticated
  with check (exists (select 1 from public.desenho_projetos p where p.id = projeto_id and p.owner_id = (select auth.uid())));
create policy desenho_publicacoes_owner_update on public.desenho_publicacoes for update to authenticated
  using (exists (select 1 from public.desenho_projetos p where p.id = projeto_id and p.owner_id = (select auth.uid())))
  with check (exists (select 1 from public.desenho_projetos p where p.id = projeto_id and p.owner_id = (select auth.uid())));
create policy desenho_publicacoes_owner_delete on public.desenho_publicacoes for delete to authenticated
  using (exists (select 1 from public.desenho_projetos p where p.id = projeto_id and p.owner_id = (select auth.uid())));
create policy desenho_publicacoes_anon_select on public.desenho_publicacoes for select to anon using (ativo);
