# Atividade 3: Organização da Qualidade na Steam

## 1. Identificação

**Unidade Curricular:** Qualidade de Software
**Metodologia:** Problem-Based Learning (PBL)
**Projeto:** Steam

**Elemento de Competência avaliado:**

**EC2: Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.**

---

# Tarefa 1: Diagnóstico da situação

| Problema identificado                                                                  | Possível consequência para o produto ou para a equipe                                                                               |
| -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Os critérios para considerar uma funcionalidade pronta não estão claramente definidos. | Funcionalidades podem ser disponibilizadas sem atender completamente aos requisitos, aumentando a quantidade de defeitos.           |
| A equipe considera que somente o QA é responsável pelos testes.                        | Os demais integrantes podem deixar de identificar problemas durante o desenvolvimento, concentrando a qualidade em apenas um papel. |
| Defeitos encontrados não são registrados e acompanhados adequadamente.                 | Problemas podem ser esquecidos, permanecer sem correção ou voltar a ocorrer em versões futuras.                                     |

### A qualidade da Steam deve ser responsabilidade exclusiva do profissional de QA?

Não. A qualidade deve ser responsabilidade compartilhada entre os diferentes papéis envolvidos no desenvolvimento. O QA possui responsabilidades específicas relacionadas ao planejamento e execução de testes, mas desenvolvedores, responsáveis pelo produto e DevOps também contribuem para a qualidade do software.

---

# Tarefa 2: Papéis e competências

## Product Owner

| Item                                           | Descrição                                                                                                                                                                                                   |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Papel analisado**                            | Product Owner                                                                                                                                                                                               |
| **Responsabilidades relacionadas à qualidade** | Definir e priorizar requisitos; estabelecer critérios de aceitação; validar se as funcionalidades atendem às necessidades dos usuários; priorizar correções de defeitos de acordo com o impacto no produto. |
| **Competências técnicas**                      | Conhecimento de requisitos, regras de negócio, análise de produto e critérios de aceitação.                                                                                                                 |
| **Competências comportamentais**               | Comunicação, organização, tomada de decisão, negociação e compreensão das necessidades dos usuários.                                                                                                        |

## Desenvolvedor

| Item                                           | Descrição                                                                                                                                                          |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Papel analisado**                            | Desenvolvedor                                                                                                                                                      |
| **Responsabilidades relacionadas à qualidade** | Implementar funcionalidades de acordo com os requisitos; criar e executar testes unitários; corrigir defeitos; revisar código e seguir padrões de desenvolvimento. |
| **Competências técnicas**                      | Programação, testes unitários, controle de versão, depuração e conhecimento de arquitetura e padrões de desenvolvimento.                                           |
| **Competências comportamentais**               | Organização, atenção aos detalhes, colaboração, comunicação e resolução de problemas.                                                                              |

## QA / Analista de Qualidade

| Item                                           | Descrição                                                                                                                                                       |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Papel analisado**                            | QA / Analista de Qualidade                                                                                                                                      |
| **Responsabilidades relacionadas à qualidade** | Planejar testes; elaborar casos de teste; executar testes; registrar e acompanhar defeitos; analisar riscos e fornecer evidências sobre a qualidade do sistema. |
| **Competências técnicas**                      | Técnicas de teste, elaboração de casos de teste, análise de riscos, ferramentas de testes e gerenciamento de defeitos.                                          |
| **Competências comportamentais**               | Pensamento crítico, atenção aos detalhes, comunicação, organização e capacidade de identificar problemas.                                                       |

## DevOps

| Item                                           | Descrição                                                                                                                                                                                                   |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Papel analisado**                            | DevOps                                                                                                                                                                                                      |
| **Responsabilidades relacionadas à qualidade** | Automatizar processos de integração e entrega; manter ambientes de desenvolvimento e testes; apoiar processos de CI/CD; monitorar problemas relacionados à infraestrutura e à disponibilização das versões. |
| **Competências técnicas**                      | CI/CD, automação, containers, infraestrutura, monitoramento e gerenciamento de ambientes.                                                                                                                   |
| **Competências comportamentais**               | Organização, comunicação, colaboração e resolução de problemas.                                                                                                                                             |

---

# Tarefa 3: Matriz de responsabilidades — RACI

### Legenda

* **R — Responsável:** executa a atividade.
* **A — Aprovador:** responde pelo resultado final ou toma a decisão.
* **C — Consultado:** contribui antes da execução ou decisão.
* **I — Informado:** precisa conhecer o resultado.

| Atividade de qualidade                | Product Owner | Desenvolvedor | QA      | DevOps |
| ------------------------------------- | ------------- | ------------- | ------- | ------ |
| Definir critérios de aceitação        | **A/R**       | C             | C       | I      |
| Revisar requisitos                    | **A**         | C             | C       | I      |
| Implementar a funcionalidade          | A             | **R**         | C       | I      |
| Revisar o código                      | I             | **A/R**       | C       | I      |
| Criar testes unitários                | I             | **A/R**       | C       | I      |
| Planejar e executar testes do sistema | I             | C             | **A/R** | C      |
| Registrar e acompanhar defeitos       | I             | C             | **A/R** | I      |
| Priorizar a correção dos defeitos     | **A/R**       | C             | C       | I      |
| Aprovar a disponibilização da versão  | **A**         | C             | C       | **R**  |

---

## Lacuna ou conflito encontrado

Uma possível lacuna identificada é a concentração da aprovação da disponibilização da versão no Product Owner. Embora o DevOps seja responsável pela execução da disponibilização, a decisão final fica concentrada em um único papel. Por isso, é importante que os critérios para aprovação da versão estejam previamente definidos para evitar dúvidas sobre quando uma versão pode ser disponibilizada.

---

## Práticas recomendadas

| Prática recomendada                                       | Problema que ajuda a resolver                                                                                  | Papéis envolvidos                 |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **Definir critérios de aceitação e Definition of Done**   | Reduz a falta de clareza sobre quando uma funcionalidade pode ser considerada concluída e pronta para entrega. | Product Owner, Desenvolvedor e QA |
| **Utilizar integração contínua com testes automatizados** | Ajuda a identificar defeitos mais cedo e reduz o risco de disponibilizar versões com problemas conhecidos.     | Desenvolvedor, QA e DevOps        |

### 1. Critérios de aceitação e Definition of Done

A equipe deve estabelecer critérios objetivos para determinar quando uma funcionalidade está concluída. Esses critérios podem envolver implementação, testes, revisão e atendimento aos requisitos definidos.

### 2. Integração contínua com testes automatizados

A equipe pode utilizar processos de CI/CD para executar testes automaticamente durante a integração das alterações. Dessa forma, problemas podem ser identificados antes que uma nova versão seja disponibilizada aos usuários.
