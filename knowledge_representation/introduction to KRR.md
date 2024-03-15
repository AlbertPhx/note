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

- Tautology

  - if every interpretation satisfies F
  - find some interpretations is not satisfiable!
  - Question
    1. (p->q) ->(¬p v q)
    2.
    3.

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
- Entialment

  - all interpretation that satisfies the all formulas in gamma satisfies F also

- Propositional Logic
  - atom : proposition which is true or false
- Conjunctive normal form
  - literal : either an atom p or ¬p
  - clause : OR OR OR
  - CNM : AND AND AND !
  - Question
    - (¬q v p v r) ∧ (¬p v r) ∧ q (O)
    - (¬(q v p) v r) ∧ (¬p v r) ∧ q (X)
    - (¬ v p v r) (O)
  - Any formula can be transformed into CNF Clausify
    - Formula!!!
      - F -> G <=> ¬ F v G
      - ¬(F v G) <=> ¬F ∧ ¬G
      - F v (G ∧ H) <=> (F v G) ∧ (F v H)
      - ¬ (F ∧ G ) <=> ¬ F v ¬ G
      - F <-> G <=> (F -> G) ∧ (G -> F)
    - Example
      - (p v ¬q ) -> r
        <=> ¬(p v ¬q) v r （把箭頭弄掉）
        <=> ( ¬p ∧ ¬¬q ) v r （把它變成 atom，把括號弄掉)
        <=> (¬ p ∧ g ) v r （把或變成且）
        <=> (¬ p v r) ∧ ( g v r)
      - u <-> p ∧ q  
        <=> (u ->(p ∧ q )) ∧ ((p ∧ q->u)) （變成箭頭）
        <=> (¬ u v (p ∧ g)) ∧ (¬ ( p ∧ g) v u)) （把箭頭弄掉）
        <=> (¬u v ( p ∧ g )) ∧ (¬ p v ¬ q v u) （把括號裡頭的變成或）
        <=> (¬u v p) ∧ (¬u v q) ∧ (¬ p v ¬ q v u) (把且改成或)
