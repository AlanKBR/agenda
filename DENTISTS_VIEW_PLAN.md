# Plano de Implementação: Visualização por Dentista (Opção A + U1)

Status: Em andamento
Última atualização: 2025-08-18

Este documento guia a implementação da visualização por dentista com checkboxes à esquerda (estilo Google Calendar), filtrando eventos por dentista e diferenciando-os visualmente. Pode ser usado por qualquer agente para continuar o trabalho em sessões futuras.

## Objetivo
- Listar dentistas a partir de `instance/users.db` (com coluna opcional `cor`).
- Exibir/ocultar eventos por dentista via checkboxes (múltipla seleção).
- Persistir seleção no navegador (localStorage).
- Diferenciar eventos por dentista com borda direita espessa e borda esquerda fina; usar cor padrão quando nula.

## Decisão Arquitetural
- Estratégia A (EventSource único com filtro server-side) + U1 (acesso a `users.db` via sqlite3).
- Backend adiciona `profissional_id` (nullable) em `calendar_event`.
- Endpoint `GET /dentists` lê `users.db` e retorna `{ id, nome, color? }` (aceita `cor` como nome da coluna de cor; enviada como `color`).
- Endpoint `GET /events` aceita `?dentists=1,2,3` e filtra por `profissional_id`.
- Frontend injeta `extraParams` com a seleção e chama `refetchEvents()`.

## Checklist (progresso)
- [ ] Endpoint opcional `GET /dentists/colors` para sugerir paleta consistente (se necessário).
- [ ] Testes básicos (manual ou automatizados) dos filtros.

## Estrutura de Dados
- `CalendarEvent.to_dict()` inclui: `profissional_id`.
- `/dentists` retorna: `[ { id: int, nome: string, color: string|null } ]`.

## UI/UX
- Sidebar fixa (mobile adapta para topo). Cada item: checkbox + bolinha de cor + nome.
- Seleção persistida em `localStorage` (`selectedDentists`).
- Cor padrão quando nula: gerada por paleta baseada no `id` do dentista.
- Sinalização visual: borda direita espessa e borda esquerda fina coloridas por dentista em todas as views; sem iniciais.
 - Aviso de filtro vazio: exibe mensagem quando nenhuma seleção de dentistas e "Todos" desmarcado.
 - Menu de contexto enriquecido: duplicação rápida (+1s, +2s, +1m), seguido por paleta de cores e delete.

## Pendências
- Endpoint opcional de paleta por dentista (`/dentists/colors`) se precisarmos padronizar.
- Testes básicos (manual/automatizados) para filtros e UX principal.

## Como rodar migrações
- Intenção: adicionar colunas necessárias em `calendar_event` e `users`.
- Comando (PowerShell):
  ```powershell
  # calendário
  A:/programa/agenda/venv/Scripts/python.exe A:/programa/agenda/migrate_add_profissional_id.py
  # usuários
  A:/programa/agenda/venv/Scripts/python.exe A:/programa/agenda/migrate_users_add_cor.py
  ```
- Resultado esperado: novas colunas criadas; mensagens de "já existe" se já aplicadas.

## Como testar rapidamente
1) Inicie o app e abra a agenda.
2) Verifique se a sidebar de dentistas aparece com lista e cores.
3) Desmarque/marque dentistas e observe o calendário (deve refazer o fetch e filtrar).
4) Crie um evento (ainda sem selecionar dentista) e confirme que aparece para o filtro "todos" ou quando nenhum filtro aplicado. Após adicionar o seletor de dentista no popover (passo futuro), valide a filtragem específica.

## Notas Técnicas
- `users.db` é acessado via sqlite3 direto para manter simplicidade (U1). Se desejado futuramente, migrar para SQLAlchemy com binds.
- Os nomes de coluna no `users` são detectados dinamicamente. Preferência: `id`, `nome_profissional`/`nome` e `color`/`cor`.
- Se `users.db` inexiste, `/dentists` retorna `[]` e a UI mostra erro.
 - Duplicação: feita no cliente chamando `/add_event` com start/end ajustados; limpa `notes` e fixa `color` para laranja (#f59e42).

## WhatsApp: estratégias de detecção e normalização (proposta)
- Entrada possível: "(11) 91234-5678", "11 1234-5678", "91234-5678", "+55 11 91234-5678", "1234-5678".
- Regras sugeridas:
   1) Extrair todos dígitos do número encontrado (via regex) e ignorar separadores; detectar se começa com 55.
   2) Se possuir 13 dígitos iniciando em 55: já está em E.164 Brasil (55 + DDD 2 dígitos + 9 dígitos). Usar como está.
   3) Se possuir 11 dígitos e não começar com 55: assumir DDD presente (2) + celular (9). Prefixar 55.
   4) Se possuir 10 dígitos: pode ser fixo (sem 9). Ainda assim, WhatsApp pode não existir; prefixar 55. (opção de permitir)
   5) Se possuir 8–9 dígitos: falta DDD. Buscar DDD padrão salvo (ex.: configuração global da clínica) e prefixar.
   6) Se usuário forneceu DDI diferente (ex.: +1, +351), manter como informado e não forçar 55.
- Implementação: adicionar setting opcional `default_ddd` (ex.: 11) e `default_ddi` (ex.: 55). Normalizar no cliente antes de abrir `wa.me` e, opcionalmente, no backend quando salvar/mostrar.
- Fallback: se não for possível normalizar com confiança, exibir diálogo pedindo confirmação do número antes de abrir o WhatsApp.

## Riscos e Mitigações
- Caso `users` não tenha uma coluna de nome, exibiremos o id como rótulo. Mitigar criando uma view ou coluna de nome.
- Se o volume de eventos for alto, o refetch pode custar alguns ms; está OK para a maioria dos cenários.

## Histórico de alterações
- 2025-08-18: Base A+U1 implementada: backend filtros, endpoints e sidebar mínima.
- 2025-08-18: UI ajustada para usar apenas borda direita espessa por dentista (remoção das iniciais/badges e da borda esquerda).
 - 2025-08-18: UI refinada: adicionada borda esquerda fina para reforço visual.



## adicionado pelo usuario mestre
View “Recurso (Dentista)” opcional
Colunas por dentista (Resource Timeline), ideal para visão de equipe; alternável no header.
Imprimir/Exportar
Layout de impressão por dia/semana; exportar ICS dos eventos filtrados.
Templates rápidos
Botões no popover (“Consulta”, “Retorno”, “Procedimento”) pré-preenchendo título/duração/nota.
logs de mudança por usuário