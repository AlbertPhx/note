- because of some limitation of propositional logic-> first order logic
- 引入一些 some, younger,all 的概念
- For example

  - JuvDisease (true) -> AffectsChild (true) v AffectsTeenager (true)
  - Child (false) v Teenager (false) -> ¬ Adult (true)
  - JuvArthritis (true) -> JuvDisease (true) ∧ Arthritis (true)
  - Arthritis (true) -> AffectsAdult (true)
  - some intuitive consequence of of our statements
    - Juvenile arthritis does not affect adults => JuvDisease -> ¬ AfffectsAdult
    - Arthritis（關節炎）is not a juvenile disease => Arthritis -> ¬ JuvDisease
    - however,neither of them is entailed
    - 有 bug!
  - because 缺少了 only , some 的概念
  - 舉一個例子~ Every student is younger than some instructor
  - S(andy) : andy is student
  - I(paul) : paul is an instructor
  - Y(andy,paul) :andy is younger than Paul
  - Encoding ∀x(S(x)->(∃y(I(y)∧ Y(x,y))))，不要怕符號， ∀ for all ∃ exist
  - 再來一個例子～ No books are gaseous. Dictionaries are books. Therefore, no dictionaries is gaseous，可以寫成下面那樣
  - ¬ ∃x(B(x) ∧ G(x)) => 沒有一樣東西同時是書本又是 Gas 的 => no books are gaseous
  - ∀x(D(x)-> B(x)) => 所有的字典都是書
  - ¬ ∃x(B(x) ∧ G(x)), ∀x(D(x)-> B(x)) ⊨ (entail) ¬ ∃x(D(x)∧ G(x))
  - 第三個例子 Every child is younger than his monther
  - C(x) : x is a child
  - M(y,x) : y is x's monther
  - ∀x ∀y(y)(C(x)∧ M(y,x)-> Y(x,y))，可以表示成這樣～好棒棒！
  - denote m(x): mother of x, ∀x(C(x)->Y(x,m(x)))，也能表成這樣～ Y 代表 誰比誰年輕的意思

- First-order logic
  - Objects
  - functions : more than, end of
  - relations : red, round, prime etc