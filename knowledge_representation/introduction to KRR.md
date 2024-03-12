- Logical operators
  - ¬ (Not): Represents logical negation.
  - ∧ (And): Represents logical conjunction.
  - ∨ (Or): Represents logical disjunction.
  - → (Implies): Represents the logical implication, indicating a "if ... then ..." relationship.
  - ↔ (If and only if/Iff): Represents a biconditional relationship, indicating "if and only if".

![alt text](table.png)

- Propositional connectives
  - 2 -place(binary): ∧ (conjunction),v(disjunction), → (implication)
  - 1 -place(unary) : ¬ (negation)
  - 0 -place : ⊥ (false,bottom) and T (true,top)
- Satisfiability

  - A propositional formula F is satisfiable if some interpretation(各種可能性) satisfies F
  - a least one interpretation satifty!
  - A set of propositional formulas is satisfiable if some interpretation satisfies all formulas in the set.
  - For example
    1. (p -> (q->p)) => (true->(true-> true)) => true (correct!)
    2. (p -> (p->q)) => (true->(true-> true)) => true (correct!)
    3. (p ->

- Equivalence
  - have the same meaning
  - F ↔ G is a tautology
  - Question
    1. (p ->(q->p)) and (p v ¬p )
       - true -> (false -> true) => true -> true vs true (correct!)
    2. (p ->( p->q)) and p
       - true ->(true -> false) => true -> false => false , false vs true (false, not equivalent!)
    3. (p -> q) and (q -> p)
       - true -> false vs false -> true => false vs true
    4. (p -> q) -> (p ∧ ¬ q ) and ⊥
       - (true -> false) -> (true ∧ true ) => false -> true => true vs false (false, not equivalent!)
    - More example
    - ## Some useful equivalence
