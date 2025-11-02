(require racket/trace)
;;Your full name: James R Terris

;;Data format: Name, Mother, Father, Date of birth, Date of death.
;;An empty list means Unknown.

;;Maternal branch
(define Mb
'(((Mary Blake) ((Ana Ali) (Theo Blake)) ((17 9 2022) ()))
((Ana Ali) ((Ada West) (Md Ali)) ((4 10 1995) ()))
((Theo Blake) ((Mary Jones) (Tom Blake)) ((9 5 1997) ()))
((Greta Blake) ((Mary Jones) (Tom Blake)) ((16 3 1999) ()))
((Mary Jones) (() ())((12 5 1967) (19 5 2024)))
((Tom Blake) (() ()) ((17 1 1964) ()))
((Ada West) (() ()) ((22 8 1973) ()))
((Md Ali) (() ()) ((14 2 1972) (2 5 2023)))
((Ned Bloom) (() ()) ((23 04 2001)()))
((John Bloom) ((Greta Blake) (Ned Bloom)) ((5 12 2023) ()))))

;,Paternal branch
(define Pb
'(((John Smith) ((Jane Doe) (Fred Smith)) ((1 12 1956) (3 3 2021))) 
((Ana Smith) ((Jane Doe) (Fred Smith)) ((6 10 1958) ()))
((Jane Doe) ((Eve Talis) (John Doe)) ((2 6 1930) (4 12 1992)))
((Fred Smith) ((Lisa Brown) (Tom Smith)) ((17 2 1928) (13 9 2016)))
((Eve Talis) (() ()) ((15 5 1900) (19 7 1978)))
((John Doe) (() ()) ((18 2 1899)(7 7 1970)))
((Lisa Brown) (() ())((31 6 1904) (6 3 1980)))
((Tom Smith) (() ()) ((2 8 1897) (26 11 1987)))
((Alan Doe) ((Eve Talis) (John Doe)) ((8 9 1932) (23 12 2000)))
((Mary Doe) (() (Alan Doe)) ((14 4 1964) ()))))

;;define lst-mb
;;define lst-pb
;;define lst-all

;; C1
(define (lst-mb mb)
  (if (empty? mb) ()
      (cons (caar mb) (lst-mb (cdr mb))))
      )


;; C2
(define (lst-pb pb)
  (if (empty? pb) ()
      (cons (caar pb) (lst-mb (cdr pb))))
      )


;; C3
(define (append-lst list1 list2)
        (cond ((empty? list1) list2)
              ((empty? list2) list1)
              (else (append list1 list2)))
  )


(define (lst-all mb pb)
  (append-lst (lst-mb mb) (lst-pb pb))
  )


;; A1
(define (parents lst)
  (define unfiltered-list (cond ((empty? lst) ())
                                ((and (empty? (caadar lst)) (empty? (car (reverse (cadar lst))))) (parents (cdr lst)))
                                (else (append (cadar lst) (parents (cdr lst))))))
  (filter-list unfiltered-list)
  )


(define (filter-list lst)
  (cond ((empty? lst) ())
        ((empty? (car lst)) (filter-list (cdr lst)))
        ((member (car lst) (cdr lst)) (filter-list (cdr lst)))
        (else (cons (car lst) (filter-list (cdr lst)))))
  )


;; A2
(define (living-members lst)
  (cond ((empty? lst) ())
        ((empty? (cadr (caddar lst))) (cons (cons (caar lst) (append '(born: ) (car(caddar lst)))) (living-members (cdr lst))))
        (else (living-members (cdr lst))))
  )


;; A3
(define (current-age lst)
  (if (empty? lst) ()
      (cons (append (caar lst) (reverse (cons (calculate-members-age (caddar lst) (cadddr(car lst)) (car(reverse(car lst)))) '(age: )))) (current-age (cdr lst))))
  )
      

(define (calculate-members-age day month year)
  (define date '(10 3 2025))
  (cond ((> (cadr date) month) (- (car(reverse date)) year))
        ((and (= (cadr date) month) (>= (car date) day)) (- (car(reverse date)) year))
        (else (- (car(reverse date)) year 1)))
  )
                                            
  
;; A4
(define (same-birthday-month lst month)
  (cond ((empty? lst) ())
        ((= (cadr(reverse(car lst))) month) (cons (caar lst) (same-birthday-month (cdr lst) month)))
        (else (same-birthday-month (cdr lst) month)))
  )


(define (dob lst)
  (if (empty? lst) ()
      (cons (cons (caar lst) (caar(reverse(car lst)))) (dob (cdr lst))))
  )


;; A5
(define (to-string lst)
  (if (empty? lst) ()
      (cons (map symbol->string (car lst)) (to-string (cdr lst))))
  )


(define (to-symbol lst)
  (if (empty? lst) ()
      (cons (map string->symbol (car lst)) (to-symbol (cdr lst))))
  )


(define (sort-by-last lst)
  (to-symbol (sort (to-string lst) (λ (a b) (if (equal? (second a) (second b))
                                                (string<? (first a) (first b))
                                                (string<? (second a)(second b))))))
  )


;; A6
(define (change-name-to-Juan lst old-name new-name)
  (cond ((empty? lst) ())
        ((equal? old-name (caaar lst)) (cons (cons (cons new-name (cdaar lst)) (cdar lst)) (change-name-to-Juan (cdr lst) old-name new-name)))
        (else (cons (car lst) (change-name-to-Juan (cdr lst) old-name new-name)))))


;; B1
(define (children lst)
  (cond ((empty? lst)())
  ((and (empty? (caadar lst)) (empty? (car (cdadar lst)))) (children (cdr lst)))
  (else (cons (caar lst) (children (cdr lst))))
  ))

;; B2
(define (living-members lst)
  (cond ((empty? lst) ())
        ((empty? (cadr (caddar lst))) (cons (cons (caar lst) (append '(born: ) (car(caddar lst)))) (living-members (cdr lst))))
        (else (living-members (cdr lst))))
  )
(define (oldest-living-member lst)
  (car lst))  
 
;; B3
(define (calculate-age birth-lst death-lst)
  (- death-lst birth-lst))
 
(define (average-age-of-death lst ages)
  (cond ((empty? lst) (/ (foldr + 0 ages) (length ages)))
        ((empty? (cadar (reverse (car lst)))) (average-age-of-death (cdr lst) ages))
        (else (average-age-of-death (cdr lst) (cons (calculate-age  (caddr (car(caddar lst))) (caddr (cadr (caddar lst)))) ages)))))

;; B4
(define (birthday-month-same lst month)
  (cond ((empty? lst) ())
        ((= (cadr(reverse(car lst))) month) (cons (caar lst) (same-birthday-month (cdr lst) month)))
        (else (same-birthday-month (cdr lst) month)))
  )

(define (dob lst)
  (if (empty? lst) ()
      (cons (cons (caar lst) (caar(reverse(car lst)))) (dob (cdr lst))))
  )

;; B5
(define (sort-by-first lst)
  (for-each (λ (individual)
              (display (car (car individual)))
              (display " ")) lst)
  )

;; B6
(define (change-name-to-Maria lst old-name new-name)
  (cond ((empty? lst) ())
        ((equal? old-name (caaar lst)) (cons (cons (cons new-name (cdaar lst)) (cdar lst)) (change-name-to-Maria (cdr lst) old-name new-name)))
        (else (cons (car lst) (change-name-to-Maria (cdr lst) old-name new-name)))))

  
;;
;;You should include code to execute each of your functions below.
;C1
;(lst-mb Mb)
;C2
;(lst-pb Pb)
;C3
;(lst-all Mb Pb)
;A1
;(parents Mb)
;A2
;(trace living-members)
;(living-members Mb)
;A3
;(current-age (living-members Mb))
;A4
;(same-birthday-month (append (dob Mb) (dob Pb)) 8)
;A5
;(sort-by-last (lst-all Mb Pb))
;A6
;(trace change-name-to-Juan)
;(change-name-to-Juan (append Mb Pb) 'John 'Juan)
;B1
;(children Pb)
;B2
;(oldest-living-member (living-members Pb))
;B3
;(average-age-of-death Pb '())
;B4
;(birthday-month-same (append (dob Pb)) 2)
;B5
;(sort-by-first Pb)
;B6
;(change-name-to-Maria (append Mb Pb) 'Mary 'Maria)

