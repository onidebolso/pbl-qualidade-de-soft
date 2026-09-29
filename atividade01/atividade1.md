# Atividade 1 — Fundamentos e Características da Qualidade na Steam

## 1. Identificação

**Unidade Curricular:** Qualidade de Software

**Metodologia:** Problem-Based Learning (PBL)

**Projeto:** Steam

**Elemento de Competência avaliado:** EC1 — Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

---

# Tarefa 1 — Fundamentos da qualidade

A Steam é uma plataforma de distribuição digital de jogos, permitindo aos usuários pesquisar, comprar, instalar e gerenciar jogos, além de utilizar recursos como biblioteca, comunidade e avaliações.

### Necessidades identificadas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| **Explícita** | O usuário deve conseguir pesquisar jogos disponíveis na plataforma. | Usuário | O usuário terá dificuldade para encontrar jogos específicos. |
| **Explícita** | O usuário deve conseguir acessar e gerenciar sua biblioteca de jogos. | Usuário | O usuário não conseguirá localizar ou gerenciar adequadamente os jogos que possui. |
| **Implícita** | A pesquisa deve apresentar resultados em tempo adequado para que a navegação seja fluida. | Usuário | A demora pode prejudicar a experiência e dificultar a localização dos jogos. |
| **Implícita** | As informações da conta e da biblioteca devem ser protegidas contra acesso não autorizado. | Usuário e Steam | Pode ocorrer exposição de dados ou acesso indevido à conta e aos jogos do usuário. |

### Justificativa

Um sistema pode implementar todas as funcionalidades explicitamente solicitadas e ainda apresentar baixa qualidade. Por exemplo, a Steam pode possuir uma funcionalidade de pesquisa, mas, se ela apresentar resultados muito lentamente, a necessidade implícita de desempenho adequado não será atendida. Da mesma forma, problemas de segurança podem comprometer a conta do usuário.

---

# Tarefa 2 — Exploração da aplicação

Para essa parte, foi escolhida a funcionalidade de **pesquisa de jogos**, pois permite realizar uma utilização esperada e uma alternativa.

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| Marco Aurélio | Pesquisa de jogos | Foi realizada uma pesquisa por “Portal 2”, um termo válido. Em seguida, foi feita uma busca por “zzzxqv-no-game-987654”, sem correspondência esperada. | Na pesquisa válida, a resposta da busca continha resultados. Na pesquisa sem correspondência, a resposta não continha linhas de resultado. |


# Tarefa 3 — Requisito e característica de qualidade

Para a funcionalidade de pesquisa, foi escolhida a característica **Eficiência de desempenho**, pois permite avaliar o tempo de resposta.

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| Marco Aurélio | A pesquisa de jogos deve apresentar os resultados em tempo adequado após o usuário realizar uma busca, sem causar uma espera excessiva durante a navegação. | Eficiência de desempenho — comportamento temporal | A pesquisa é utilizada para localizar jogos. Para proporcionar uma boa experiência, além de apresentar resultados, a Steam deve apresentá-los sem demora excessiva. O requisito está relacionado principalmente ao tempo de resposta da aplicação. | Realizar várias pesquisas com termos diferentes e medir o tempo entre o envio de cada pesquisa e a apresentação dos resultados; comparar os tempos obtidos. |
