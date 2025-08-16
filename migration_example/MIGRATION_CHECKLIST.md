# CHECKLIST DE MIGRAÇÃO - AGENDA ODONTOLÓGICA

## 🔍 FASE 1: ANÁLISE PRÉ-MIGRAÇÃO
- [ ] Mapear tabelas existentes no sistema principal
- [ ] Identificar campos equivalentes (pacientes, usuarios, etc.)
- [ ] Verificar sistema de autenticação atual
- [ ] Analisar estrutura de URLs do sistema principal
- [ ] Definir estratégia de banco (unificado ou separado)

## 🛠️ FASE 2: ADAPTAÇÃO DO CÓDIGO

### Backend
- [ ] Criar Blueprint Flask para a agenda
- [ ] Adaptar queries SQLite para seu ORM/banco
- [ ] Implementar autenticação integrada
- [ ] Ajustar rotas para URL prefix do sistema
- [ ] Testar endpoints individualmente

### Frontend  
- [ ] Mover templates para pasta do sistema principal
- [ ] Adaptar caminhos de static files
- [ ] Integrar com CSS/JS framework do sistema
- [ ] Ajustar layout para match com design atual
- [ ] Testar responsividade

### Database
- [ ] Criar migration para tabela calendar_events
- [ ] Adicionar Foreign Keys para pacientes/usuarios
- [ ] Migrar dados existentes (se houver)
- [ ] Configurar indexes para performance
- [ ] Testar integridade referencial

## 🔧 FASE 3: INTEGRAÇÃO

### Sistema Principal
- [ ] Registrar Blueprint da agenda
- [ ] Configurar rotas no menu principal
- [ ] Implementar permissões de acesso
- [ ] Integrar com sistema de logs
- [ ] Configurar backup dos dados da agenda

### Testes
- [ ] Testar criação de eventos
- [ ] Testar edição/exclusão
- [ ] Testar autocompletar pacientes
- [ ] Testar busca de telefones
- [ ] Testar diferentes tipos de usuário

## 🚀 FASE 4: DEPLOY

### Preparação
- [ ] Documentar processo de migração
- [ ] Criar script de rollback
- [ ] Fazer backup completo
- [ ] Testar em ambiente de staging
- [ ] Treinar usuários finais

### Go-Live
- [ ] Deploy em produção
- [ ] Monitorar logs de erro
- [ ] Validar funcionalidades críticas
- [ ] Coletar feedback dos usuários
- [ ] Otimizar performance se necessário

## ⚠️ PONTOS CRÍTICOS DE ATENÇÃO

### Performance
- [ ] Indexar campos de busca (nome, data)
- [ ] Otimizar queries de autocompletar
- [ ] Implementar cache se necessário
- [ ] Monitorar tempo de resposta

### Segurança
- [ ] Validar permissões por tipo de usuário
- [ ] Sanitizar inputs de formulário  
- [ ] Implementar rate limiting
- [ ] Auditar logs de acesso

### Usabilidade
- [ ] Manter funcionalidades existentes
- [ ] Garantir que navegação seja intuitiva
- [ ] Testar em diferentes browsers
- [ ] Validar em dispositivos móveis

## 📊 MÉTRICAS DE SUCESSO
- [ ] Tempo de carregamento < 2s
- [ ] Zero perda de dados na migração
- [ ] Aceitação > 90% pelos usuários
- [ ] Redução de bugs vs versão anterior
