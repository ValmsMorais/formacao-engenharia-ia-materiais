# Orientação de solução

A solução deve:
- abrir uma transação por importação;
- localizar cliente por documento com query parametrizada;
- validar `CASHIN/CASHOUT` e valor positivo;
- inserir rejeição com motivo explícito;
- atualizar contadores da importação;
- confirmar apenas ao final.
