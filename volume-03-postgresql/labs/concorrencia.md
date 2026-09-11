# Laboratório de concorrência

Abra duas sessões no pgAdmin.

## Sessão A
```sql
BEGIN;
UPDATE clientes SET nome = nome WHERE id = 1;
```

Não faça COMMIT ainda.

## Sessão B
Execute uma atualização sobre o mesmo `id` e observe a espera.

Em uma terceira sessão, consulte `pg_stat_activity`.

Finalize com `ROLLBACK` nas sessões de laboratório.
