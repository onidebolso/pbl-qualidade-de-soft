# Atividade 2 — Organização da Qualidade na Steam

## 1. Identificação

**Unidade Curricular:** Qualidade de Software

**Metodologia:** Problem-Based Learning (PBL)

**Projeto:** Steam

**Elemento de Competência avaliado:** EC2 — Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

# Tarefa 1 — Diagnóstico da situação

Considerando uma equipe responsável pelo desenvolvimento e manutenção de uma plataforma como a Steam, foram identificados os seguintes problemas organizacionais:

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| Os critérios para considerar uma funcionalidade pronta não estão claramente definidos. | Funcionalidades podem ser disponibilizadas sem atender completamente aos requisitos, aumentando a quantidade de defeitos. |
| A equipe considera que somente o QA é responsável pelos testes e pela qualidade. | Desenvolvedores e demais integrantes podem deixar de identificar problemas antecipadamente, concentrando a qualidade em uma única função. |
| Defeitos encontrados não são registrados e acompanhados de forma adequada. | Problemas podem ser esquecidos, voltar a ocorrer em versões futuras ou permanecer sem uma pessoa responsável pela correção. |

### A qualidade da Steam deve ser responsabilidade exclusiva do profissional de QA?

Não. A qualidade deve ser uma responsabilidade compartilhada entre os diferentes papéis envolvidos no desenvolvimento. O QA possui responsabilidades específicas relacionadas ao planejamento e à execução de testes, mas desenvolvedores, responsáveis pelo produto, liderança e DevOps também influenciam a qualidade. Cada papel deve contribuir dentro de suas responsabilidades.

---

# Tarefa 2 — Papéis e competências

## 1. Product Owner

| Campo | Descrição |
|---|---|
| **Papel** | Product Owner |
| **Responsabilidades relacionadas à qualidade** | Definir e priorizar requisitos; esclarecer critérios de aceitação; validar se as funcionalidades atendem às necessidades dos usuários; priorizar correções de defeitos de acordo com o impacto no produto. |
| **Competências técnicas** | Conhecimento de requisitos, regras de negócio, análise de produto e critérios de aceitação. |
| **Competências comportamentais** | Comunicação, organização, tomada de decisão, negociação e capacidade de entender as necessidades dos usuários. |

## 2. Desenvolvedor

| Campo | Descrição |
|---|---|
| **Papel** | Desenvolvedor |
| **Responsabilidades relacionadas à qualidade** | Implementar funcionalidades conforme os requisitos; realizar testes unitários; corrigir defeitos; revisar código quando aplicável; manter padrões de desenvolvimento. |
| **Competências técnicas** | Programação, testes unitários, controle de versão, depuração e conhecimento de arquitetura e padrões de desenvolvimento. |
| **Competências comportamentais** | Organização, atenção aos detalhes, colaboração, comunicação e resolução de problemas. |

## 3. QA / Analista de Qualidade

| Campo | Descrição |
|---|---|
| **Papel** | QA / Analista de Qualidade |
| **Responsabilidades relacionadas à qualidade** | Planejar testes; elaborar casos de teste; executar testes; registrar defeitos; acompanhar resultados; avaliar riscos e fornecer evidências sobre a qualidade da aplicação. |
| **Competências técnicas** | Técnicas de teste, elaboração de casos de teste, análise de riscos, ferramentas de testes e gerenciamento de defeitos. |
| **Competências comportamentais** | Pensamento crítico, atenção aos detalhes, comunicação, organização e capacidade de questionar requisitos e comportamentos. |

## 4. DevOps

| Campo | Descrição |
|---|---|
| **Papel** | DevOps |
| **Responsabilidades relacionadas à qualidade** | Automatizar processos de integração e entrega; manter ambientes de desenvolvimento e testes; apoiar pipelines de CI/CD; monitorar problemas relacionados à infraestrutura e à disponibilização das versões. |
| **Competências técnicas** | CI/CD, automação, containers, infraestrutura, monitoramento e controle de ambientes. |
| **Competências comportamentais** | Organização, comunicação, colaboração e capacidade de resolver problemas. |

---

# Tarefa 3 — Matriz RACI

Vamos utilizar:

- **PO** = Product Owner
- **DEV** = Desenvolvedor
- **QA** = Analista de Qualidade
- **DO** = DevOps

### Legenda

- **R** — Responsible: executa a atividade.
- **A** — Accountable: responde pelo resultado final ou aprova.
- **C** — Consulted: é consultado.
- **I** — Informed: é informado.

| Atividade | PO | DEV | QA | DevOps |
|---|---:|---:|---:|---:|
| Definir critérios de aceitação | **A/R** | C | C | I |
| Revisar requisitos | **A** | C | C | I |
| Implementar a funcionalidade | A | **R** | C | I |
| Revisar o código | I | **A/R** | C | I |
| Criar testes unitários | I | **A/R** | C | I |
| Planejar e executar testes do sistema | I | C | **A/R** | C |
| Registrar e acompanhar defeitos | I | C | **A/R** | I |
| Priorizar a correção dos defeitos | **A/R** | C | C | I |
| Aprovar a disponibilização da versão | **A** | C | C | **R** |

---

# Práticas recomendadas de QA

## Prática 1 — Critérios de aceitação e Definition of Done

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Definir critérios de aceitação e uma Definition of Done antes da implementação. | Reduz a falta de clareza sobre quando uma funcionalidade pode ser considerada concluída. | PO, DEV e QA |

## Prática 2 — Integração contínua com testes automatizados

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Utilizar CI/CD com execução automatizada de testes durante o processo de integração e entrega. | Ajuda a identificar defeitos mais cedo e reduz o risco de disponibilizar versões com problemas conhecidos. | DEV, QA e DevOps |
