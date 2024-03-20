- Declarative sentences : we consider whether they're true or not
- Non-declarative sentences : we can't tell they're true or not

- Abductive reasoning : Simplest and most likely explation
- Logical operators (connectives)

  - ¬ (Not): Represents logical negation.
  - ∧ (And): Represents logical conjunction.
  - ∨ (Or): Represents logical disjunction.
  - → (Implies): Represents the logical implication, indicating a "if ... then ..." relationship.
  - ↔ (If and only if/Iff): Represents a biconditional relationship, indicating "if and only if".

- Propositional formula of signature

  - Every atom is a formula
  - Both 0-place connetives are formulas
  - For any binary conective ⊙, if F and G are formulats then (F ⊙ G) is a formula
  - For example

    1.  ⊥ => atom => Propositional formula
    2.  q -> p => don't have () => not Propositional formula
    3.  (¬(q) v r ) => we don't need () for q => not!
    4.  ⊥¬ T = no () => not!

    - 檢查是否有()，但是 atom 不用()

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

- Entialment (蘊含、必然導致)

  - A set Gamma (Γ) of formulas entails (⊨) a formula F ( Γ ⊨ F)
  - all interpretation that satisfies the all formulas in gamma satisfies F also
  - Example
    - {A,B} ⊨ A ∧ B (true)
    - {A,A->B} ⊨ B (true)
    - {A} ⊨ A v B (true)
    - {A} ⊨ A ∧ B (false)
    - ∅ ⊨ B (false)
    - {⊥} ⊨ B (TRUE,因為沒有任何滿足{⊥}的)
    - TL ∧ ¬ T -> JL, TL, ¬JL ⊨ T
    - only interpretation : TL= true, T= true, T = true, J L = false (false -> false => true)
    - false -> false (true) 很重要！
  - check not entail is easlier
  - 前面的必須為 true ，推倒到後面的也為 true
  - 後面的事 logical consequences of Γ

- F is a tautology iff (<->) ¬ unsatisfiable

  - Example : p v ¬ p is a tautology (有一些滿足就好) iff ¬(p v ¬ p) is unsatisfiable (無論怎樣都是 false)

- How are equivalence and entitlement relarted?
  - F is equivalent to G iff
- Propositional Logic
  - atom : proposition which is true or false
- Conjunctive normal form
  - literal : either an atom p or ¬p
  - clause : (A OR B OR C ) 整個就是 clause
  - CNF : AND AND AND ! 把 clause 串起來就變成 CNF
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
        <=> (¬ u v (p ∧ g)) ∧ (¬ ( p ∧ g) v u)（把箭頭弄掉）
        <=> (¬u v ( p ∧ g )) ∧ (¬ p v ¬ q v u) （把括號裡頭的變成或）
        <=> (¬u v p) ∧ (¬u v q) ∧ (¬ p v ¬ q v u) (把且改成或)
- Unit propagation (very important!!!)
  - find interpration for all the atom, go step by step!
  - F <- F|p =(T ∧ (¬T v ¬q)∧ (¬ q v r ) ∧( q v ¬r ))
    <=> ¬ q ∧( ¬q v r) ∧ (¬ ) etc...
  - 消消樂~
  - limitation of unit propagation: what if there is no unit clause?
